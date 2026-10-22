# Dashboardin API-sopimus (versio 0.1)

Tila: **ensimmäinen versio katselmoitavaksi, issue #8 / P0-02**. Tämä on suunnitteludokumentti,
ei toteutuslupa. Sopimus koskee versiota 0.1 (simuloidut palvelin- ja säätiedot) ja
määrittelee laajennussäännöt myöhemmille vaiheille. Arvot, jotka on merkitty
**ehdotus**, ovat oletuksia, kunnes käyttäjä vahvistaa tai muuttaa ne.

Koneluettavat tunnisteet ja kenttänimet ovat englanniksi. Käyttäjälle näkyvät
suomenkieliset tekstit määritellään [näkymäluonnoksessa](LAYOUT_SPEC.md); API ei
palauta valmiita suomenkielisiä lauseita.

## 1. Päätökset

| Aihe | Päätös | Tila |
| --- | --- | --- |
| Päivitysväli | Selain hakee tilannekuvan 10 s välein | ehdotus |
| Pyynnön aikakatkaisu | 5 s | ehdotus |
| Vanhenemisraja | Havainto on vanhentunut, kun se on yli 30 s vanha (3 päivitysväliä) | ehdotus |
| Aikaleimat | UTC, ISO 8601, `Z`-pääte, sekunnin tarkkuus | ehdotus |
| Prosenttiarvot | Liukuluku 0–100, ei merkkijono; puuttuva arvo on `null`, ei `0` | ehdotus |
| `load` / kuormakeskiarvot | **Eivät kuulu versioon 0.1.** Voidaan lisätä myöhemmin uutena kenttänä (kohta 7). Vanhan ehdokaskoodin `load` ei ole vaatimus | ehdotus |
| Muisti | Käytetty % = (kokonais − saatavilla oleva) / kokonais. Välimuisti, jonka käyttöjärjestelmä voi vapauttaa, lasketaan vapaaksi | ehdotus |
| Levy | Yksi nimetty "ensisijainen" tiedostojärjestelmä per palvelin (`disk_label`). Erillisiä levyjä ei koskaan keskiarvoisteta hiljaa | ehdotus |
| Sääennuste, tuuli | Eivät kuulu versioon 0.1; vain nykyinen lämpötila ja säätila | ehdotus |

## 2. Päätepisteet

- `GET /health` – prosessin elossaolo. Palauttaa `{"status": "ok"}`. **Ei kerro mitään
  valvottujen kohteiden tilasta.**
- `GET /api/v1/dashboard` – yksi yhtenäinen tilannekuva.

Versiossa 0.1 ei ole kirjoittavia päätepisteitä eikä laitteiden ohjausta.

## 3. Tilannekuvan kentät

### Juuri

| Kenttä | Tyyppi | Pakollinen | Merkitys |
| --- | --- | --- | --- |
| `contract_version` | merkkijono | kyllä | Sopimusversio, esim. `"1.0"` |
| `generated_at` | aikaleima | kyllä | Hetki, jolloin API kokosi tilannekuvan. Kaikki tuoreus lasketaan tätä vasten, ei selaimen kelloa vasten |
| `mode` | `"mock"` \| `"live"` | kyllä | Simuloitu vai oikea data. `mock` on näytettävä käyttäjälle |
| `refresh` | olio | kyllä | `interval_s`, `stale_after_s`; selain käyttää näitä, jos ne ovat annettu |
| `servers` | taulukko | kyllä | Voi olla tyhjä |
| `weather` | olio tai `null` | kyllä | `null` = ei konfiguroitu |
| `sources` | taulukko | kyllä | Lähteiden terveys (kohta 5) |

### Palvelin (`servers[]`)

| Kenttä | Tyyppi | Pakollinen | Merkitys |
| --- | --- | --- | --- |
| `id` | merkkijono | kyllä | Pysyvä tunniste (`a-z0-9-`), ei muutu nimen tai isäntänimen vaihtuessa |
| `name` | merkkijono | kyllä | Näyttönimi |
| `hostname` | merkkijono tai `null` | kyllä | Informatiivinen; ei tunniste |
| `kind` | merkkijono | kyllä | `physical`, `vm`, `container`; tuntematon arvo käsitellään kuin `physical` |
| `parent_id` | merkkijono tai `null` | kyllä | Esim. VM:n isäntä (käyttö vaiheesta 3) |
| `availability` | `online` \| `offline` \| `unknown` | kyllä | Katso totuustaulu (kohta 4) |
| `availability_reason` | merkkijono tai `null` | kyllä | Syy, kun `availability` ≠ `online` |
| `freshness` | `fresh` \| `stale` \| `none` | kyllä | `none` = ei yhtään onnistunutta havaintoa |
| `observed_at` | aikaleima tai `null` | kyllä | Viimeisin **onnistunut** havainto |
| `source_id` | merkkijono | kyllä | Viittaa `sources[].id`-kenttään |
| `cpu_percent` | luku tai `null` | kyllä | Koko isännän CPU-käyttö |
| `memory_percent` | luku tai `null` | kyllä | Katso kohta 1 |
| `disk_percent` | luku tai `null` | kyllä | Ensisijaisen tiedostojärjestelmän käyttö |
| `disk_label` | merkkijono tai `null` | kyllä | Esim. `"/"` tai `"C:"` |

`freshness` lasketaan palvelimella: `fresh`, jos `generated_at − observed_at ≤ stale_after_s`,
`stale`, jos suurempi, ja `none`, jos `observed_at` on `null`.

### Sää (`weather`)

| Kenttä | Tyyppi | Merkitys |
| --- | --- | --- |
| `state` | `ok` \| `unavailable` | `unavailable` = lähde ei vastaa; muut kentät `null` |
| `location_label` | merkkijono | Esim. `"Koti"` |
| `observed_at` | aikaleima tai `null` | |
| `temperature_c` | luku tai `null` | Celsius-asteina |
| `condition` | `clear` \| `partly_cloudy` \| `cloudy` \| `rain` \| `snow` \| `thunder` \| `fog` \| `unknown` | Tuntematon uusi arvo käsitellään kuin `unknown` |

### Lähteen terveys (`sources[]`)

| Kenttä | Tyyppi | Merkitys |
| --- | --- | --- |
| `id` | merkkijono | Esim. `mock-servers`, `mock-weather` |
| `kind` | merkkijono | `servers`, `weather`; myöhemmin `proxmox`, `pfsense`, … |
| `state` | `ok` \| `degraded` \| `failed` \| `disabled` | |
| `error_category` | `null` \| `unreachable` \| `timeout` \| `auth` \| `permission` \| `invalid_response` \| `internal` | Ei sisällä salaisuuksia eikä osoitteita |
| `last_success_at` | aikaleima tai `null` | |

## 4. Tilojen totuustaulu

Tämä erottaa toisistaan kohteen viat, lähteen viat ja vanhan tiedon.

| Tilanne | `availability` | `availability_reason` | `freshness` | Käyttäjälle |
| --- | --- | --- | --- | --- |
| Lähde vastaa, kohde toimii | `online` | `null` | `fresh` | Toimii |
| Lähde vastaa, kohde ei vastaa | `offline` | `host_unreachable` | `fresh` | Pois käytöstä |
| Lähde vastaa, vieras on pysäytetty (vaihe 3) | `offline` | `guest_stopped` | `fresh` | Pois käytöstä (pysäytetty) |
| Lähde ei saanut vastausta (aikakatkaisu, ei yhteyttä) | `unknown` | `source_unreachable` | `fresh` tai `stale` | Tuntematon |
| Lähde hylkäsi tunnistautumisen tai oikeudet | `unknown` | `source_permission` | `fresh` tai `stale` | Tuntematon (lähteen virhe) |
| Kohteesta ei ole koskaan saatu havaintoa | `unknown` | `never_observed` | `none` | Tuntematon |
| Viimeisin onnistunut havainto on liian vanha | viimeisin tunnettu arvo | `null` tai syy | `stale` | **Vanhentunut tieto**; ei esitetä varmana tilana |

Säännöt:

1. Havainnon puuttuminen ei ole `offline`. Vain lähteen positiivinen tieto (kohde ei vastaa,
   vieras pysäytetty) tuottaa `offline`.
2. `freshness: stale` ohittaa visuaalisesti `availability`-arvon: kohdetta ei esitetä
   tilassa "Toimii" ilman vanhentuneen tiedon merkintää.
3. Lähteen vika (`sources[].state = failed`) ei muuta palvelimen `availability`-arvoa
   `offline`-tilaksi.

## 5. Virheet ja osittainen vika

- **Koko API ei vastaa** (verkko, 5xx, aikakatkaisu): selain ei saa JSON-vastausta. Tämä on
  eri asia kuin yksittäisen laitteen vika.
- **API-laajuinen virhe**: HTTP 500/503 ja runko

  ```json
  { "error": { "code": "internal_error", "message": "Tilannekuvan muodostus epäonnistui." } }
  ```

  `code` on vakaa konetunniste (`internal_error`, `unavailable`); `message` on vain
  diagnostiikkaa varten, ja käyttöliittymä näyttää oman suomenkielisen tekstinsä `code`-arvon
  perusteella. Vastaus ei sisällä salaisuuksia, osoitteita tai pinojälkiä.
- **Yksittäisen lähteen vika**: HTTP 200 ja käyttökelpoinen tilannekuva, jossa vika näkyy
  `sources[]`- ja palvelimien `availability_reason`-kentissä.
- Epäkelpo vastausrunko ei korvaa aiempaa kelvollista tilannekuvaa (selaimen puoli, ks.
  [PROJECT_PLAN.md](PROJECT_PLAN.md) kohta 5).

## 6. Esimerkkivastaukset

Esimerkeissä `generated_at` on `2026-10-22T10:00:00Z`.

### 6.1 Kaikki kunnossa

```json
{
  "contract_version": "1.0",
  "generated_at": "2026-10-22T10:00:00Z",
  "mode": "mock",
  "refresh": { "interval_s": 10, "stale_after_s": 30 },
  "servers": [
    {
      "id": "nas", "name": "NAS", "hostname": "nas.example.invalid", "kind": "physical",
      "parent_id": null, "availability": "online", "availability_reason": null,
      "freshness": "fresh", "observed_at": "2026-10-22T09:59:56Z", "source_id": "mock-servers",
      "cpu_percent": 12.5, "memory_percent": 48.0, "disk_percent": 71.2, "disk_label": "/"
    },
    {
      "id": "media", "name": "Media", "hostname": "media.example.invalid", "kind": "vm",
      "parent_id": null, "availability": "online", "availability_reason": null,
      "freshness": "fresh", "observed_at": "2026-10-22T09:59:56Z", "source_id": "mock-servers",
      "cpu_percent": 33.0, "memory_percent": 61.4, "disk_percent": 40.0, "disk_label": "/"
    }
  ],
  "weather": {
    "state": "ok", "location_label": "Koti", "observed_at": "2026-10-22T09:50:00Z",
    "temperature_c": 6.4, "condition": "cloudy"
  },
  "sources": [
    { "id": "mock-servers", "kind": "servers", "state": "ok", "error_category": null, "last_success_at": "2026-10-22T09:59:56Z" },
    { "id": "mock-weather", "kind": "weather", "state": "ok", "error_category": null, "last_success_at": "2026-10-22T09:50:00Z" }
  ]
}
```

### 6.2 Tyhjä kohdelista

```json
{
  "contract_version": "1.0", "generated_at": "2026-10-22T10:00:00Z", "mode": "mock",
  "refresh": { "interval_s": 10, "stale_after_s": 30 },
  "servers": [], "weather": null,
  "sources": [
    { "id": "mock-servers", "kind": "servers", "state": "ok", "error_category": null, "last_success_at": "2026-10-22T09:59:56Z" }
  ]
}
```

### 6.3 Osittainen vika: yksi kohde pois, yksi lähteen virhe

`nas` ei vastaa (`offline`, lähde toimii). `media` on `unknown`, koska lähde ei vastannut.

```json
{
  "contract_version": "1.0", "generated_at": "2026-10-22T10:00:00Z", "mode": "mock",
  "refresh": { "interval_s": 10, "stale_after_s": 30 },
  "servers": [
    {
      "id": "nas", "name": "NAS", "hostname": null, "kind": "physical",
      "parent_id": null, "availability": "offline", "availability_reason": "host_unreachable",
      "freshness": "fresh", "observed_at": "2026-10-22T09:59:56Z", "source_id": "mock-servers",
      "cpu_percent": null, "memory_percent": null, "disk_percent": null, "disk_label": null
    },
    {
      "id": "media", "name": "Media", "hostname": null, "kind": "vm",
      "parent_id": null, "availability": "unknown", "availability_reason": "source_unreachable",
      "freshness": "stale", "observed_at": "2026-10-22T09:58:10Z", "source_id": "mock-servers-b",
      "cpu_percent": 33.0, "memory_percent": 61.4, "disk_percent": 40.0, "disk_label": "/"
    }
  ],
  "weather": { "state": "ok", "location_label": "Koti", "observed_at": "2026-10-22T09:50:00Z", "temperature_c": 6.4, "condition": "cloudy" },
  "sources": [
    { "id": "mock-servers", "kind": "servers", "state": "ok", "error_category": null, "last_success_at": "2026-10-22T09:59:56Z" },
    { "id": "mock-servers-b", "kind": "servers", "state": "failed", "error_category": "timeout", "last_success_at": "2026-10-22T09:58:10Z" }
  ]
}
```

### 6.4 Puuttuvat mittaukset

Kohde vastaa (`online`), mutta levy- ja muistiarvoa ei saatu. Puuttuva arvo on `null`, ei `0`.

```json
{
  "id": "nas", "name": "NAS", "hostname": null, "kind": "physical", "parent_id": null,
  "availability": "online", "availability_reason": null, "freshness": "fresh",
  "observed_at": "2026-10-22T09:59:56Z", "source_id": "mock-servers",
  "cpu_percent": 12.5, "memory_percent": null, "disk_percent": null, "disk_label": null
}
```

### 6.5 Vanhentunut havainto

Viimeisin havainto on 95 s vanha, joten `freshness` on `stale`. Aiempi tila `online`
säilyy arvona, mutta sitä ei esitetä varmana.

```json
{
  "id": "nas", "name": "NAS", "hostname": null, "kind": "physical", "parent_id": null,
  "availability": "online", "availability_reason": null, "freshness": "stale",
  "observed_at": "2026-10-22T09:58:25Z", "source_id": "mock-servers",
  "cpu_percent": 12.5, "memory_percent": 48.0, "disk_percent": 71.2, "disk_label": "/"
}
```

### 6.6 Epäonnistunut lähde ilman aiempia havaintoja

```json
{
  "contract_version": "1.0", "generated_at": "2026-10-22T10:00:00Z", "mode": "mock",
  "refresh": { "interval_s": 10, "stale_after_s": 30 },
  "servers": [
    {
      "id": "nas", "name": "NAS", "hostname": null, "kind": "physical", "parent_id": null,
      "availability": "unknown", "availability_reason": "never_observed", "freshness": "none",
      "observed_at": null, "source_id": "mock-servers",
      "cpu_percent": null, "memory_percent": null, "disk_percent": null, "disk_label": null
    }
  ],
  "weather": { "state": "unavailable", "location_label": "Koti", "observed_at": null, "temperature_c": null, "condition": "unknown" },
  "sources": [
    { "id": "mock-servers", "kind": "servers", "state": "failed", "error_category": "unreachable", "last_success_at": null },
    { "id": "mock-weather", "kind": "weather", "state": "failed", "error_category": "timeout", "last_success_at": null }
  ]
}
```

### 6.7 API-laajuinen virhe

HTTP 503:

```json
{ "error": { "code": "unavailable", "message": "Tilannekuva ei ole saatavilla." } }
```

## 7. Yhteensopivat laajennukset

1. **Uusi kenttä** (esim. `load_average`, `disks[]`) lisätään valinnaisena. Asiakas ohittaa
   tuntemattomat kentät. Pakollisen kentän lisäys on rikkova muutos.
2. **Uusi enum-arvo** (`kind`, `condition`, `availability_reason`, `error_category`) ei ole
   rikkova muutos. Asiakas käsittelee tuntemattoman arvon turvalliseen oletukseen
   (`unknown`/`physical`), eikä kaadu.
3. **Uusi osio** (esim. `network`, `cameras`) lisätään uutena ylätason avaimena. Se ei muuta
   olemassa olevien osioiden merkitystä, ja sen lähde raportoi omana `sources[]`-rivinä.
4. **Uusi valvontakohde jo tuettua tyyppiä** ei muuta sopimusta: se on uusi `servers[]`-rivi.
5. **Rikkova muutos** (kentän poisto, merkityksen muutos, yksikön muutos) vaatii uuden polun
   `/api/v2/…`; vanhaa versiota tuetaan siirtymäajan.
6. `contract_version` kasvattaa pienempää numeroa yhteensopivissa ja suurempaa rikkovissa
   muutoksissa.

## 8. Tarkistettavat asiat

- Käyttäjä vahvistaa tai muuttaa kohdan 1 ehdotukset (10/5/30 s, muistin ja levyn määritelmät,
  `load`-kentän pois jättäminen).
- Mock-tilan skenaarioiden (healthy, one-down, unknown, empty, partial, stale, high usage,
  failure ja recovery) vastaavuus tämän dokumentin esimerkkeihin tarkistetaan issuessa #10.
- Aiempi ehdokaskoodi (PR #6) ei ole sopimuksen lähtökohta. Sen poikkeamat: ei vakaata
  `id`-kenttää, ei havaintoaikaa, `load`-merkitys epäselvä.
- Kolmen laajennusskenaarion läpikäynti (S5) tehdään erikseen.
