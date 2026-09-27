# Git-työnkulku ja projektien eteneminen

Tavoite on oppia agenttista ohjelmointia ja rakentaa erillinen ympäristö,
jossa orkestraattori ohjaa workereita. HomeLab Dashboard on myöhempi kohdeprojekti.

## Kaksivaiheinen toimintamalli

1. **HomeLab Dashboardin suunnittelu tässä repositoriossa.** Sovellus suunnitellaan
   mahdollisimman pitkälle valmiiksi: käyttötarpeet, rajaukset, näkymät,
   arkkitehtuuri, tietosopimukset, virhetilanteet, laajennettavuus, tehtävät ja
   hyväksymiskriteerit. Tuotoksina ovat dokumentaatio, koodittomat näkymäluonnokset
   ja issuet. Tässä vaiheessa ei kirjoiteta sovelluskoodia, testikoodia eikä
   ajettavia prototyyppejä. Myöskään vanhaa ehdokaskoodia ei oteta käyttöön.
2. **Orkestraattori ja workerit erillisessä projektissa.** Dashboardin suunnitelman
   hyväksymisen jälkeen käyttäjä siirtyy niiden suunnitteluun ja rakentamiseen.
   Tarkoitus on testata ja harjoitella agenttista koodausta. Dashboardin suunnitellut
   tehtävät toimivat myöhemmin harjoituskohteena käyttäjän erikseen antaman
   Dashboardin toteutusluvan mukaisesti. Orkestraattorin toteutuksesta ja sen
   työvaiheista sovitaan sen omassa projektissa.

Roadmapin vaiheet 0–7 kuvaavat Dashboardin ominaisuuksien etenemistä. Ne eivät ole
nämä kaksi työskentelyvaihetta. Suunnitelman hyväksyminen, dokumentti-PR:n
yhdistäminen tai suunnitteluissuen sulkeminen ei anna Dashboardin toteutuslupaa.

## Milloin Dashboardin suunnittelu on valmis?

Seuraavat ehdot koskevat suunnitelman hyväksymistä. Ne eivät edellytä toimivaa
sovellusta tai ajettuja sovellustestejä. Jokaiselle ehdolle kirjataan katselmoinnissa
todisteeksi dokumentin kohta tai issue sekä mahdolliset jäljellä olevat puutteet.

| Tunnus | Valmistumiskriteeri | Katselmoinnissa tarvittava näyttö |
| --- | --- | --- |
| S1 | Sovelluksen tarkoitus, käyttötavat, tietojen tärkeysjärjestys sekä pakollinen, valinnainen ja pois rajattu sisältö on sovittu. | Vaatimukset kattavat version 0.1 ja myöhemmät roadmapin alueet. Valinnaisilla ominaisuuksilla on valinta tai kirjattu myöhempi päätöstehtävä. |
| S2 | Käyttöliittymän rakenne ja käyttäjälle näkyvä toiminta on määritelty. | Koodittomat näkymäluonnokset, suomenkieliset tekstit sekä normaalin, tyhjän, latautuvan, puutteellisen, virheellisen ja palautuvan näkymän kuvaukset. Kohdemäärän kasvu ja tilan loppuminen on käsitelty. |
| S3 | Tietosisältö, API-sopimus ja tilojen merkitys ovat yksiselitteisiä suunnitellussa laajuudessa. | Dokumentoidut kentät, yksiköt, tunnisteet, ajat, puuttuvat arvot, saatavuus, tuoreus, virheet ja esimerkkivastaukset. Myöhempien lähteiden yhteiset periaatteet ja erikseen varmennettavat kenttävastaavuudet on erotettu. |
| S4 | Arkkitehtuurin vastuut, asetusten periaatteet, käyttöoikeusrajat ja häiriöistä palautuminen on kuvattu. | Tiedonkulku ja osien vastuut ovat selvät, yhteisillä osilla on nimetty tehtävä ja lähdekohtaiset virheet pysyvät erillään. Laitekohtaisia ratkaisuja ei oleteta vahvistetuiksi. |
| S5 | Uusien ominaisuuksien ja valvontakohteiden lisääminen on huomioitu. | Dokumentoitu läpikäynti kolmesta tapauksesta: uusi jo tuetun tyyppinen kohde, uusi tietolähdetyyppi ja uusi näkymäkortti. Jokaisesta kuvataan vaikutukset asetuksiin, tietosopimukseen, taustapalveluun, käyttöliittymään ja testaukseen. |
| S6 | Backlog kattaa sovitun sisällön ja on johdonmukainen. | Jokaisella tehtävällä on lähtötiedot, rajaus, tuotokset, hyväksymiskriteerit ja riippuvuudet. Riippuvuuksissa ei ole kehiä; suunnittelun, toteutuksen ja laiteympäristössä varmennuksen edellytykset erotetaan. Paikallinen luettelo ja GitHub-issuet vastaavat toisiaan. |
| S7 | Hyväksymisen ja testauksen suunnitelma on riittävän konkreettinen. | Tapaustaulukot kuvaavat lähtötilanteen, tapahtuman ja odotetun tuloksen. Sovitut rajat sekä myöhemmin valittavan ympäristön tarkistukset on nimetty. Testien suunnitelma on erotettu myöhemmin kirjoitettavista ja ajettavista testeistä. |
| S8 | Avoimet päätökset ja suunnitelman hyväksyntä on käsitelty. | Nyt ratkaistavissa olevat suunnittelua estävät asiat on ratkaistu. Jokaisella perustellusti siirretyllä päätöksellä on tila, siirron syy, vastuullinen issue, ratkaisuajankohta ja tieto estetyistä tehtävistä. Käyttäjän hyväksyntä kirjataan päivämäärineen ja hyväksytyn suunnitelman version/commitin viitteineen. |

Asennustavan, laiteversioiden ja muun vielä tuntemattoman kohdeympäristön tiedot
voivat jäädä nimettyihin myöhempiin selvitystehtäviin. Niiden puuttuminen ei estä
suunnitelman hyväksymistä, kun vaikutukset ja varmennuksen ehdot on kuvattu.
Ympäristöstä riippumattomia sisältö- tai toimintapäätöksiä ei siirretä vain siksi,
että toteutusta ei ole aloitettu. Ehdotusta ei kirjata vahvistetuksi vaatimukseksi.

**Nykytila:** kaksivaiheinen toimintamalli ja laajennettavuuden tarve on vahvistettu
käyttäjän kanssa. Tämä kirjaus määrittelee valmistumiskriteerit; se ei todista
niiden täyttymistä. Dashboardin suunnitelmaa ei ole vielä hyväksytty valmiiksi,
eikä Dashboardin toteutusta ole valtuutettu. Issue #7 määrittelee toimintamallin ja
hyväksymisehdot; sen valmistuminen ei tarkoita, että esimerkiksi issueiden #8 ja #9
suunnittelutuotokset tai kaikki yllä olevat ehdot olisivat valmiit.

## Sisällöllisen suunnittelun järjestys

1. Sovitaan Dashboardin käyttötarpeet, sisältö ja tietojen tärkeysjärjestys.
2. Määritellään tietojen ja tilojen merkitys sekä API-sopimus (issue #8).
3. Kuvataan näkymät ja niiden toiminta koodittomina luonnoksina (issue #9).
4. Täsmennetään myöhempien ominaisuuksien toiminnalliset tarpeet yksi aihe kerrallaan.
5. Täydennetään arkkitehtuurin, asetusten, laajennettavuuden ja testauksen suunnitelmat.
6. Viimeistellään issueiden rajaukset ja riippuvuudet sekä katselmoidaan ehdot S1–S8.

Tietosopimusta ja näkymäkuvausta tarkennetaan tarvittaessa toistensa havaintojen
perusteella. Myöhempien vaiheiden alustavaa dokumentointia voi tehdä ilman valmista
sovellusta. Tämä ei sulje niiden selvitysissueita, ohita laitekohtaisia tarkistuksia
tai muuta toteutuksen etenemisjärjestystä. Näiden issueiden riippuvuuksien tarkempi
erottelu tehdään backlogia täsmennettäessä. Työ käsitellään edelleen yksi issue kerrallaan.

## Mitä eri Git-vaiheet tarkoittavat?

| Vaihe | Mitä tapahtuu? | Näkyykö muutos GitHubin etusivulla? |
| --- | --- | --- |
| Tiedoston muokkaus | Muutos on palvelimen nykyisessä työhaarassa | Ei |
| Commit | Muutos tallennetaan paikallisen haaran historiaan | Ei |
| Push | Haaran commitit lähetetään GitHubiin | Työhaarassa kyllä; päähaarassa ei |
| Pull request eli PR | Ehdotetaan työhaaran muutoksia kohdehaaraan | Ei vielä |
| Merge päähaaraan | PR:n muutokset yhdistetään `main`-haaraan | Kyllä |

GitHub näyttää oletuksena `main`-haaran. Palvelimen projektihakemisto näyttää
sen haaran tiedostot, joka siellä on valittuna. Tarkista haara ja paikalliset
muutokset komennolla `git status --short --branch`.

## Suunnittelun julkaisu

Alkuperäiset suunnitteludokumentit julkaistiin `agent/issue-7`-haarasta PR:ssä #43,
joka yhdistettiin `main`-haaraan 27.9.2026. Tämä julkaisu ei tarkoittanut koko
suunnitelman hyväksymistä tai toteutuslupaa.

Seuraavat dokumenttimuutokset tehdään yhden issuen työhaarassa ja katselmoidaan
omassa PR:ssä. Agentti ei yhdistä PR:iä tässä projektissa. Muutokset näkyvät
päähaarassa vasta yhdistämisen jälkeen. Muiden koneiden paikalliset päähaarat
päivitetään erikseen sovittuna työvaiheena.

Vanhoja koodi-PR:iä #4, #5 ja #6 ei tarvitse yhdistää dokumenttien saamiseksi
päähaaraan. Ne suljettiin yhdistämättä 27.9.2026. Koodi säilyy niiden haaroissa;
sulkeminen ei poista committeja tai tarkoita alkuperäisten issueiden valmistumista.

## Mitä tapahtuu dokumenttien jälkeen?

- Kun ehdot S1–S8 on katselmoitu ja käyttäjä on hyväksynyt suunnitelman,
  siirrytään kaksivaiheisen toimintamallin toiseen vaiheeseen erillisessä projektissa.
- Dashboardin toteutus odottaa erillistä lupaa. Suunnitteluissue voidaan hyväksyä
  valmiiksi omien tuotostensa perusteella ilman toteutuslupaa.
- Erillisessä orkestraattoriprojektissa suunnitellaan ensin ihmisen, orkestraattorin
  ja workerin vastuut, tehtävän elinkaari, työympäristö ja etenemisen raportointi.
- Teknologiavalinnat, koko toteutuksen issue-jako ja toteutuslupa käsitellään ennen
  koodin kirjoittamista. Työ aloitetaan pienellä, ymmärrettävällä kokeilulla.

Jokaisen työvaiheen alussa kerrotaan tarkoitus ja vaikutukset. Lopuksi kerrotaan
mitä tehtiin, missä haarassa muutokset ovat, onko ne commitoitu ja pushattu,
mikä on PR:n tila, mitä puuttuu ja mikä on seuraava askel.
