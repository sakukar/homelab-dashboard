# Dashboardin käyttötarpeet ja sisältö

Tila: **osittain vahvistettu suunnitteluluonnos, issue #7 / P0-01**. Tässä määritellään käyttötarpeita
ja sisältöä valmistumiskriteeriä S1 varten. Dokumentti ei ole toteutuslupa eikä
käyttöliittymän lopullinen määrittely. Ehdotukset ja avoimet asiat eivät ole
vahvistettuja päätöksiä.

## Tarkoitus ja vahvistettu lähtökohta

HomeLab Dashboard on jatkuvaan käyttöön tarkoitettu koko näytön tietonäkymä
tavalliselle tietokonenäytölle. Se näyttää kotilaboratorion tilan ja sovittua
lisätietoa suomeksi. Näytön tarkat ominaisuudet ja selain ovat vielä avoinna.

Versio 0.1 näyttää simuloidut palvelin- ja säätiedot. Oikeat valvontakohteet ja
tietolähteet tulevat myöhemmissä roadmapin vaiheissa. Dashboard on erillisen
orkestraattori- ja worker-projektin myöhempi harjoituskohde; näiden agenttien
ohjausnäkymä ei kuulu Dashboardiin.

Vahvistettu vaatimus D14 on laajennettavuus: uusia ominaisuuksia, tietolähteitä ja
valvontakohteita pitää voida lisätä myöhemmin. Nykyinen korttimäärä tai yksittäinen
tietolähde ei saa määritellä koko sovelluksen pysyvää enimmäislaajuutta.

## Käyttötarpeet: ehdotus tarkennettavaksi

| Käyttötilanne | Näytön pitäisi auttaa havaitsemaan | Rajaus |
| --- | --- | --- |
| Tavallinen vilkaisu | Mitkä kohteet ovat toiminnassa ja miltä niiden resurssien käyttö näyttää? | Versiossa 0.1 simuloidut palvelinkortit; oikeat palvelut ja verkko myöhemmin. |
| Kohteen ongelma | Mikä kohde on poissa käytöstä tai minkä tilaa ei tunneta? | Tuntematon tila ei todista kohteen vikaa. Tämä on tilan näyttämistä; varsinainen hälytysjärjestelmä kuuluu vaiheeseen 7. |
| Tiedonkeruun ongelma | Voiko näkyvään tietoon luottaa ja kuinka vanhaa se on? | Dashboardin yhteysvirhe, lähteen virhe ja valvontakohteen tila erotetaan. |
| Yhteyden palautuminen | Ovatko havainnot päivittyneet ja tilat palautuneet ajantasaisiksi? | Näkymän palautuminen ei saa edellyttää käyttäjän tekemää sivun uudelleenlatausta. |
| Kohdemäärän kasvu | Missä ryhmässä uusi kohde näkyy ja miten muut kohteet löytyvät? | Ryhmittely, näkyvä kohdemäärä ja tilan loppumisen käsittely päätetään erikseen. Kohteita ei piiloteta huomaamatta. |
| Lisätiedon katsominen | Mikä säätila on ja mitä muuta erikseen valittua tietoa tarvitaan? | Versiossa 0.1 simuloitu sääkortti. Muut tietokortit eivät kuulu automaattisesti ensimmäiseen versioon. |

## Sisältö ja rajaukset

| Sisältö | Nykyinen asema | Käyttäjälle näkyvä tarkoitus | Jatkosuunnittelun omistaja |
| --- | --- | --- | --- |
| Palvelimen tunniste/nimi ja saatavuus | Vahvistettu versioon 0.1 simuloituna | Kohteen tunnistaminen ja sen tilan ymmärtäminen | #8 tietosisältö, #9 esitystapa |
| CPU-, RAM- ja levyn käyttö | Vahvistettu versioon 0.1 simuloituna | Resurssien käytön yleiskuva; tuntematon arvo erotetaan nollasta | #8 yksiköt ja merkitykset, #9 esitystapa |
| Tiedon tuoreus, puuttuminen ja yhteysvirheet | Version 0.1 suunnitelmassa | Käyttäjä erottaa ajantasaisen havainnon vanhasta tai puuttuvasta tiedosta | #8 tilasäännöt, #9 näkyvät tekstit ja tilat |
| Sääkortti ja simuloidun datan merkintä | Vahvistettu versioon 0.1 | Sään lisätieto sekä selvä tieto siitä, ettei näkymä vielä valvo oikeita kohteita | #8 ja #9; oikean sääpalvelun valinta #33 |
| Oikeat palvelimet ja tärkeät palvelut | Myöhempi roadmapin vaihe 2 | Isäntien ja erikseen valittujen palvelujen tila | #19 lähteet ja kohteet, #22 palvelut |
| Proxmox-isännät ja vieraat | Myöhempi roadmapin vaihe 3 | Isäntien, virtuaalikoneiden ja konttien väliset suhteet ja tila | #24 |
| pfSense, WAN, varayhteys ja VPN | Myöhempi roadmapin vaihe 4 | Verkkoyhteyksien ja käytössä olevan yhteysreitin tila | #27 |
| MikroTik-laitteet ja liittymät | Myöhempi roadmapin vaihe 5 | Valittujen paikallisverkon laitteiden ja liittymien tila | #30 |
| Oikea sää ja kameranäkymä | Myöhempi roadmapin vaihe 6; tarkka sisältö avoin | Valitun sijainnin sää ja sovittu kamerakuva | #33; lähde, kuvaustapa ja kameramäärä päätetään myöhemmin |
| Muu kodin tietokortti | Valinnainen, ei vielä valittu | Käyttäjän erikseen nimeämä tarve | #33 määrittelee; #36 toteutetaan myöhemmin vain, jos sisältö valitaan |
| Historia ja hälytykset | Myöhempi roadmapin vaihe 7 | Aikaisemman tilanteen ja sovittujen poikkeamien tarkastelu | #37; säilytys, rajat, kuittaus ja käyttötapa avoinna |
| Ulkoiset ilmoitukset | Vahvistamaton lisätoive | Mahdollinen ilmoitus Dashboardin ulkopuolelle | #37 käsittelee tarpeen; valinta vaatii oman erikseen suunniteltavan toteutusissuen |

Roadmapin myöhempi ominaisuus on suunniteltua sisältöä, ei vielä yksityiskohtaisesti
hyväksytty ratkaisu. Kuormituksen lisämittarit kuten `load` ja kuormakeskiarvot
eivät saa tulla pakolliseksi näkymäsisällöksi vanhan ehdokaskoodin perusteella;
niiden tarve ja merkitys täsmennetään issuessa #8.

Dashboardin nykyiseen laajuuteen eivät kuulu infrastruktuurin ohjaus, virtuaalikoneiden
käynnistys tai sammutus, palomuurin tai reitityksen muuttaminen, kameran ohjaus,
automaattinen korjaaminen, kameratallennus tai yleinen lisäosakauppa.

## Vahvistetut käyttötapaa koskevat valinnat

Käyttäjä vahvisti seuraavat valinnat keskustelussa 27.9.2026. Vahvistus koskee
näitä kolmea valintaa, ei koko tämän dokumentin hyväksymistä tai toteutuslupaa.

| Päätös | Vahvistettu valinta | Vielä suunniteltava yksityiskohta |
| --- | --- | --- |
| D15: käyttötapa | Pääosin passiivinen tilannenäyttö; tärkeä tieto näkyy ilman klikkauksia. | Mahdollisten lisätietonäkymien tarve ratkaistaan erikseen; niiden käyttö ei saa olla edellytys tärkeän nykytilan näkemiselle. |
| D16: tietojen tärkeysjärjestys | Viat ja yhteysongelmat ensin, sitten palvelinten tila ja kuormitus, lopuksi sää. | Muiden myöhemmin valittavien tietokorttien keskinäinen järjestys sekä yhtäaikaisten ongelmien esitystapa. |
| D03: tilan loppuminen | Tärkeimmät tiedot pysyvät näkyvissä, muut vaihtuvat automaattisesti. | Pysyvästi näkyvät tiedot, ryhmittely, vaihtoväli, kierron järjestys ja näkyvä korttimäärä määritellään issuessa #9. Aiempi kuuden kortin määrä on edelleen ehdotus. |

Vikojen korostaminen ei vielä valitse hälytyskynnyksiä, ilmoituskanavia
tai kuittauspainikkeita. Ne pysyvät vaiheen 7 päätöksinä. Tässä valitaan tiedon
tärkeysjärjestys, ei lisätä hälytysjärjestelmää versioon 0.1.

## Valintojen vaikutukset jatkosuunnitteluun

Seuraavat tapaukset ovat ehdotuksia myöhempien tietosopimus- ja
käyttöliittymämäärittelyjen tarkistamiseen. Tarkat tilasäännöt ja tekstit sovitaan
issueissa #8 ja #9; tässä ei vielä päätetä niiden toteutusta.

| Tilanne | Tarkistettava käyttäjän kannalta |
| --- | --- |
| Kaikki näkyvät kohteet toimivat | Palvelinten tila ja resurssit sekä sää ovat ymmärrettävissä ilman klikkauksia. Simuloitu tila on selvästi tunnistettavissa. |
| Vuorossa näkymätön kohde vikaantuu | Käyttäjä havaitsee ongelman odottamatta koko vaihtokiertoa. Tarkka pysyvä esitystapa ja havaintoviive määritellään erikseen. |
| Useita kohteita vikaantuu samalla kertaa | Näkyvä tieto kertoo ongelmien kokonaisuudesta eikä anna yhden näkyvän kohteen perusteella virheellistä kuvaa muista. Tarkka yhteenveto ja järjestys jäävät suunniteltaviksi. |
| Dashboardin päivitysyhteys katkeaa | Käyttäjä näkee tiedon ajantasaisuusongelman; vanhoja tiloja ei esitetä varmoina nykytiloina. |
| Kohdemäärä ylittää kerralla näkyvän määrän | Tärkeimmät tiedot pysyvät näkyvissä. Muut kohteet tulevat automaattisesti nähtäviksi, eikä yksikään jää kierron ulkopuolelle huomaamatta. |
| Sää tai muu lisätieto puuttuu | Palvelinten ja yhteysongelmien esitys säilyy ymmärrettävänä. |

## Vielä tarkennettava sisältö

- Näytön ensisijaiset käyttäjät ja katseluetäisyys; ei oleteta muita käyttäjäryhmiä.
- Mitkä nimetyt kohteet tai kohderyhmät ovat käyttäjälle tärkeimpiä. Varsinaiset
  osoitteet, tunnukset ja laiteversiot kuuluvat myöhempään ympäristöselvitykseen.
- Palvelinten ryhmittelyn ja järjestyksen peruste sekä version 0.1 näkyvä korttimäärä.
- Kellon ja päivämäärän tarve sekä yksikkö- ja aikamuotovalinnat D02:n mukaisesti.
- Myöhempien kameran, historian ja muiden lisätietojen tarkka käyttötarve ja tilantarve.

## Tämän suunnitteluvaiheen valmistuminen

Käyttötarpeiden ja sisällön osuus on valmis katselmoitavaksi, kun nyt käsiteltävät
valinnat on kirjattu vastauksineen, käyttötapaukset ja sisällön rajaus on käyty
käyttäjän kanssa läpi ja avoimet asiat on osoitettu oikeisiin jatkotehtäviin.
Tämä luonnos ei vielä täytä koko S1-kriteeriä eikä sulje issueta #7.

Seuraava suunnittelutehtävä on tietojen ja tilojen merkityksen täsmentäminen
issuessa #8 sovittujen käyttötarpeiden pohjalta. Lopulliset näkymäluonnokset ja
tilan loppumisen yksityiskohdat kuuluvat issueen #9.
