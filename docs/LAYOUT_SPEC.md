# Dashboardin näkymäluonnos (versio 0.1)

Tila: **ensimmäinen versio katselmoitavaksi, issue #9 / P0-03**. Kooditon määrittely: ASCII-luonnokset
ja taulukot, ei toteutuslupa. Perustuu [API-sopimukseen](API_CONTRACT.md) ja vahvistettuihin
valintoihin D15 (passiivinen näyttö), D16 (viat ensin, sitten palvelimet, sitten sää) ja D03
(tärkeät tiedot pysyvät näkyvissä, muut vaihtuvat automaattisesti). Arvot, jotka on merkitty
**ehdotus**, odottavat käyttäjän vahvistusta.

## 1. Lähtökohdat

| Aihe | Määrittely | Tila |
| --- | --- | --- |
| Näyttö | Tavallinen tietokonemonitori; tarkka resoluutio, koko, suunta ja selain avoinna | vahvistettu / avoin |
| Testikoot | 1920×1080 ja 1280×720, vaakasuunta. Eivät ole tunnettua laitteistoa | ehdotus |
| Kieli | Suomi kaikessa näkyvässä tekstissä | vahvistettu |
| Aika | 24 h, aikavyöhyke Europe/Helsinki, muoto `22.10.2026 13:05` | ehdotus |
| Yksiköt | Celsius, prosentit | ehdotus |
| Kiosk | Koko näytön tila käynnistetään selaimen kiosk-asetuksella (käyttöönotto, ei sovellus). Sovelluksen oma koko näytön painike on valinnainen eikä kuulu versioon 0.1 | ehdotus |
| Tekstikoko | Palvelimen nimi ja tila vähintään 24 px, prosenttiarvot vähintään 32 px, pienin teksti (ikä, apuotsikot) vähintään 16 px 1080p-näytöllä. Tarkistus oikealla näytöllä katseluetäisyydeltä | ehdotus |
| Vuorovaikutus | Ei klikattavia elementtejä, ei vierityspalkkeja, ei hiirellä tarvittavia toimintoja | vahvistettu (D15) |

Tila ei saa riippua pelkästä värisävystä: jokaisella tilalla on teksti ja muoto (kuvake/reunus).

## 2. Kokonaisrakenne

```
+--------------------------------------------------------------------------------+
| HomeLab Dashboard      [SIMULOITU DATA]            22.10.2026 13:05   ● Yhteys OK |  Otsikkorivi
+--------------------------------------------------------------------------------+
| ⚠ 2 ongelmaa: NAS – POIS KÄYTÖSTÄ · Media – TUNTEMATON                          |  Yhteenvetokaista
+--------------------------------------------------------------------------------+
| +--------------+ +--------------+ +--------------+            +--------------+ |
| | NAS     ✖    | | Media   ?    | | Pi-hole ✔    |            |  Sää         | |
| | POIS KÄYTÖSTÄ| | TUNTEMATON   | | TOIMII       |            |  6 °C        | |
| | CPU  —       | | CPU  33 %    | | CPU  4 %     |            |  Pilvistä    | |
| | RAM  —       | | RAM  61 %    | | RAM  22 %    |            |  Koti 12:50  | |
| | Levy —       | | Levy 40 %    | | Levy 35 %    |            +--------------+ |
| | pvm 12 s sit.| | vanha 95 s   | | pvm 4 s sit. |                             |
| +--------------+ +--------------+ +--------------+                             |
| +--------------+ +--------------+ +--------------+                             |
| | ... (kierto) | | ...          | | ...          |      Sivu 2/3  ▮▯▯           |
| +--------------+ +--------------+ +--------------+                             |
+--------------------------------------------------------------------------------+
```

Alueet ylhäältä alas, tärkeysjärjestys D16:n mukaan:

1. **Otsikkorivi (aina näkyvissä):** sovelluksen nimi, `SIMULOITU DATA` -merkki kun `mode = mock`,
   kello ja päivämäärä, yhteyden tila.
2. **Yhteenvetokaista (aina näkyvissä):** ongelmien kokonaisuus, tai rauhallinen tila.
3. **Palvelinkortit:** pääsisältö, osa kiinteästi näkyvissä, osa kiertää (kohta 4).
4. **Sääkortti:** oikeassa reunassa, ei koskaan estä palvelinten näyttöä.

## 3. Tilat ja suomenkieliset tekstit

### 3.1 Palvelimen tila

| API-tila | Teksti | Kuvake / reunus | Huomio |
| --- | --- | --- | --- |
| `online` + `fresh` | TOIMII | ✔ vihreä, ohut reunus | Vähiten korostettu |
| `offline` | POIS KÄYTÖSTÄ | ✖ punainen, paksu reunus | `guest_stopped`: lisäteksti "pysäytetty" |
| `unknown` | TUNTEMATON | ? keltainen, katkoviivareunus | `source_*`-syy: lisäteksti "lähteen virhe" |
| mikä tahansa + `stale` | VANHA TIETO | ⏱ harmaa, katkoviivareunus | Aiempaa tilaa ei näytetä varmana; kerrotaan ikä |
| `unknown` + `never_observed` | EI HAVAINTOA | ? harmaa | |

### 3.2 Mittarit

- CPU, RAM ja Levy näytetään nimilapulla, prosenttiarvolla ja palkilla. Levyn nimilappuun
  lisätään `disk_label`, esim. "Levy /".
- `null` näytetään tekstillä "ei tietoa" ja tyhjällä palkilla. Arvoa **0 %** ei koskaan
  näytetä tyhjän tilalle.
- Korkea käyttö korostetaan värillä ja tekstillä "KORKEA" arvon vieressä, kun arvo ≥ 90 %
  (ehdotus; ei hälytyskynnys, ks. PRODUCT_SCOPE.md).
- Jokaisessa kortissa näkyy havainnon ikä: "päivitetty 12 s sitten"; yli 30 s: "vanha 95 s".

### 3.3 Yhteenvetokaista

| Tilanne | Teksti |
| --- | --- |
| Ei ongelmia | "Kaikki N kohdetta toimii" |
| Ongelmia | "⚠ K ongelmaa: <nimi> – <tila> · <nimi> – <tila>"; näytetään enintään 3 nimeä, loput "+M muuta" |
| Pelkkiä vanhentuneita | "Tieto on vanhentunut K kohteen osalta" |
| Lähde epäonnistunut | "Lähde ei vastaa: <lähde>" lisätään kaistalle |
| Ei kohteita | "Ei valvottavia kohteita" |

Kaista lasketaan **koko** kohdelistasta, ei vain näkyvistä korteista. Näin yksikään vika ei jää
huomaamatta, vaikka sen kortti ei ole kierron kohdalla.

### 3.4 Yhteys

| Tilanne | Otsikkorivin teksti |
| --- | --- |
| Päivitykset onnistuvat | ● Yhteys OK |
| Viimeisin haku epäonnistui | ⚠ Yhteys katkennut – viimeisin päivitys 42 s sitten |
| Yhteys palautuu | ● Yhteys OK (korostus 5 s, ei käyttäjän toimia) |

Katkon aikana viimeisin kelvollinen tilannekuva pysyy näkyvissä, mutta kaikki kortit näytetään
vanhentuneina (`VANHA TIETO`) 30 s kuluttua viimeisestä onnistuneesta hausta.

## 4. Kohdemäärän kasvu ja kierto (D03)

Ehdotus (ei vahvistettu): ruudukossa on kuusi korttipaikkaa (3 × 2) sekä 1080p- että 720p-näytöllä.
Paikkamäärä ei ole sovelluksen kohdemäärän yläraja.

Säännöt:

1. Kohteet lajitellaan vakavuuden mukaan: `offline`, sitten `unknown`/`stale`, sitten `online`;
   saman luokan sisällä nimen mukaan.
2. **Kiinteät paikat:** vikaantuneet kohteet saavat kiinteät paikat ensimmäisistä paikoista,
   enintään neljä. Ne eivät kierrä.
3. **Kiertävät paikat:** loput paikat (vähintään kaksi) kiertävät läpi jäljellä olevat kohteet
   sivuina. Jos vikoja on yli neljä, ylimääräiset viat tulevat ensin kiertoon.
4. Kiertoväli 15 s (ehdotus). Sivuindikaattori "Sivu 2/3" ja edistymispalkki näkyvät aina,
   kun sivuja on enemmän kuin yksi.
5. Jos kaikki kohteet mahtuvat kuuteen paikkaan, kiertoa ei ole eikä indikaattoria.
6. Kierto ei piilota kohdetta: jokainen kohde näkyy vähintään yhden kiertojakson aikana, ja
   viat näkyvät aina yhteenvetokaistalla.
7. Kun kohteen tila muuttuu viaksi kesken kierron, kortti siirtyy kiinteälle paikalle
   seuraavassa päivityksessä (≤ 10 s).

Jos vikoja on enemmän kuin neljä, käyttäjä näkee silti kaikkien määrän yhteenvetokaistalta.

## 5. Näkymätilat

| Tila | Mitä käyttäjä näkee |
| --- | --- |
| Ensilataus | Koko alue: "Ladataan tietoja…" ja vaimeat korttirungot; otsikkorivi ja kello näkyvät heti |
| Normaali | Kohdat 2–4 |
| Tyhjä kohdelista | Yhteenvetokaista: "Ei valvottavia kohteita"; korttialueella ohjeteksti "Kohteita ei ole vielä määritelty"; sääkortti näkyy |
| Yksi kohde | Yksi kortti vasemmassa yläkulmassa samalla koolla kuin muissakin; ei venytetä koko ruudulle |
| Kuusi kohdetta | Täysi ruudukko, ei kiertoa |
| Yli kuusi kohdetta | Kohdan 4 mukainen kierto |
| Osittainen data | Kohteet, joilta puuttuu arvo, näyttävät "ei tietoa"; muut näytetään normaalisti |
| Lähteen osittainen vika | Vaikuttavat kortit `TUNTEMATON`, yhteenvetokaistalla "Lähde ei vastaa: <lähde>" |
| Vanhentunut tieto | Kortit `VANHA TIETO` ja ikä, ei vihreää "toimii"-esitystä |
| API-laajuinen vika (ensilatauksessa) | Koko alueella: "Tietoja ei saatu. Yritetään uudelleen…" ja seuraavan yrityksen aika |
| API-laajuinen vika (myöhemmin) | Viimeisin tilannekuva pysyy näkyvissä; yhteys-tila 3.4 |
| Palautuminen | Tuore tilannekuva korvaa vanhan; virheilmoitus poistuu; käyttäjän ei tarvitse ladata sivua uudelleen |
| Sää puuttuu (`null`) | Sääkortti piilotetaan tai näyttää "Sää ei ole käytössä"; palvelinruudukko saa tilan |
| Sää ei saatavilla (`unavailable`) | Sääkortti: "Säätietoa ei saatu"; palvelimet eivät muutu |
| Simuloitu data | `SIMULOITU DATA` -merkki otsikkorivillä aina, kun `mode = mock` |

## 6. Pitkät nimet ja puuttuvat kentät

- Palvelimen nimi: yksi rivi, katkaistaan lopusta tekstillä `…`; koko nimi ei ole saatavilla
  ilman vuorovaikutusta, joten nimet pidetään konfiguraatiossa enintään 24 merkin pituisina
  (ehdotus).
- Isäntänimi (`hostname`) näytetään pienellä toisella rivillä vain, jos se mahtuu; muuten ei.
- Puuttuva `hostname` ei jätä aukkoa vaan kortin korkeus pysyy samana.
- Sää: pitkä paikannimi katkaistaan samoin.

## 7. Sääkortti

Sisältö: lämpötila (`6 °C`), säätila tekstinä (selkeää, puolipilvistä, pilvistä, sadetta,
lumisadetta, ukkosta, sumua, "Ei tiedossa" tuntemattomalle), paikka ja havaintoaika.
Ennusteet ja tuuli eivät kuulu versioon 0.1. Säätilan kuvake on lisätieto, ei ainoa tieto.

## 8. Läpikäynti: API-esimerkit ja näkymät

| API-esimerkki ([API_CONTRACT.md](API_CONTRACT.md) kohta 6) | Näkymä |
| --- | --- |
| 6.1 Kaikki kunnossa | Yhteenvetokaista "Kaikki 2 kohdetta toimii"; kaksi korttia TOIMII; sää näkyy; simuloitu data -merkki |
| 6.2 Tyhjä | Kohdan 5 tyhjä tila; sää piilotettu (`weather: null`) |
| 6.3 Osittainen vika | NAS: POIS KÄYTÖSTÄ (kiinteä); Media: VANHA TIETO / lähteen virhe; kaista "2 ongelmaa" ja "Lähde ei vastaa: mock-servers-b" |
| 6.4 Puuttuvat mittaukset | Kortti TOIMII, RAM ja Levy "ei tietoa" |
| 6.5 Vanhentunut | Kortti VANHA TIETO "vanha 95 s"; ei vihreää |
| 6.6 Epäonnistunut lähde | Kortti EI HAVAINTOA; sää "Säätietoa ei saatu"; kaista "Lähde ei vastaa" |
| 6.7 API-laajuinen virhe | Ensilatauksessa virhetila; muuten yhteys-tila 3.4 |

## 9. Tarkistettavat asiat (käyttäjän päätökset)

1. Korttipaikkojen määrä (ehdotus 6) ja kiertoväli (ehdotus 15 s).
2. Kiinteiden vikapaikkojen enimmäismäärä (ehdotus 4 / 6).
3. Tilojen suomenkieliset sanat: TOIMII / POIS KÄYTÖSTÄ / TUNTEMATON / VANHA TIETO.
4. Näytetäänkö kello ja päivämäärä (ehdotus kyllä).
5. Varsinainen näyttö, resoluutio ja katseluetäisyys; tekstikoot tarkistetaan sillä.
6. Sijoitus: sääkortti oikealla vai alhaalla.

Näihin vastattuaan luonnoksesta voidaan tehdä lopullinen katselmointiversio.
