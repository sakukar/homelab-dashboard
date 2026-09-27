# Git-työnkulku ja projektien eteneminen

Tavoite on oppia agenttista ohjelmointia ja rakentaa erillinen ympäristö,
jossa orkestraattori ohjaa workereita. HomeLab Dashboard on myöhempi kohdeprojekti.

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

1. Suunnitteludokumentit on erotettu omaan `agent/issue-7`-haaraan, jonka pohjana
   on `main`. Dokumentti-PR liittyy issueen #7.
2. Avaa dokumentti-PR:n **Files changed** ja tarkista sisältö.
3. Kun sisältö sopii, yhdistä PR GitHubissa **Merge pull request** -toiminnolla.
   Agentti ei yhdistä PR:iä tässä projektissa.
4. Yhdistämisen jälkeen README ja suunnitelmat näkyvät repositorion päähaarassa.
5. Päivitetään palvelimen paikallinen päähaara erikseen sovittuna työvaiheena,
   jotta palvelimen ja GitHubin oletusnäkymä vastaavat toisiaan.

Vanhoja koodi-PR:iä #4, #5 ja #6 ei tarvitse yhdistää dokumenttien saamiseksi
päähaaraan. Ne suljettiin yhdistämättä 27.9.2026. Koodi säilyy niiden haaroissa;
sulkeminen ei poista committeja tai tarkoita alkuperäisten issueiden valmistumista.

## Mitä tapahtuu dokumenttien jälkeen?

- Dashboardin issuet pysyvät suunnittelutilassa ja sen toteutus odottaa.
- Erillisessä orkestraattoriprojektissa suunnitellaan ensin ihmisen, orkestraattorin
  ja workerin vastuut, tehtävän elinkaari, työympäristö ja etenemisen raportointi.
- Teknologiavalinnat, koko toteutuksen issue-jako ja toteutuslupa käsitellään ennen
  koodin kirjoittamista. Työ aloitetaan pienellä, ymmärrettävällä kokeilulla.

Jokaisen työvaiheen alussa kerrotaan tarkoitus ja vaikutukset. Lopuksi kerrotaan
mitä tehtiin, missä haarassa muutokset ovat, onko ne commitoitu ja pushattu,
mikä on PR:n tila, mitä puuttuu ja mikä on seuraava askel.
