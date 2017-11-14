# Ergänzende Beispielrechnungen
Dieses Repositorium enthält Beispielrechnungen als Ergänzung zur Dissertation mit dem Titel
"Regelungstheoretische Analyse- und Entwurfsansätze für unteraktuierte mechanische Systeme" von C. Knoll,
siehe [Volltext](http://www.qucosa.de/recherche/frontdoor/?tx_slubopus4frontend%5bid%5d=urn:nbn:de:bsz:14-qucosa-209765)
<br>
<br>
Die Beispielrechnungen sind als IPython-Notebook in der Programmiersprache `Python` (Version 2.7.x)
implementiert und haben folgende Abhängigkeiten:


* Wissenschaftliche Standardpakete
  * numpy, scipy, sympy, matplotlib
  * Am besten über einen Paket-Manager zu installieren

* [`symbtools`](https://github.com/cknoll/rst_symbtools)
  * `core`-Modul: Grundlegende Funktionalität zum symbolischen Rechnen in der Regelungstheorie
    * Lie-Ableitungen, Rangprüfung, Zeitableitung von Symbolen, ...
  * `modeltools`-Modul
    * Aufstellen der Bewegungsgleichungen eines mechanischen Systems und Transformation
    in verschiedene Darstellungen
  * `noncommutativetools`
    * Funktionalität zum Rechnen mit Polynommatrizen über Schiefpolynomen,
    z.B. Rechtsverschiebung des Operators d/dt, Ansatzbasierte Bestimmung einer
    unimodularen Inversen


* [`pycartan`](https://github.com/cknoll/pycartan)
  * Funktionalität zum Rechnen mit Differentialformen, die auf geeigneten Jet-Bündeln definiert sind.



* [`PyTrajectory`](https://github.com/TUD-RST/pytrajectory)
  * Softwarepaket zur Trajektorienplanung auf Basis der Lösung eines Randwertproblems


* [`displaytools`](https://github.com/cknoll/displaytools)
 * IPython-Erweiterung, welche die speziellen Kommentare `##`, `##:` einführt um
 das Ergebnis einer Zuweisung anzeigen zu lassen.


### Liste der Beispiele:
Im Folgenden sind alle Beispiel-Notebooks aufgelistet und über den Webdienst http://nbviewer.jupyter.org
verlinkt. Dieser Dienst greift auf die Dateien dieses Repositoriums zu und stellt sie passend dar (schneller und besser als github selbst).

 * Zweigelenkmainipulator mit passivem zweiten Gelenk, ohne Schwerkraft. Verwendet in Beispielen: 2.4, 2.11, 4.33.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/zweigelenk_manipulator.ipynb

 * Translatorisches mechanisches System mit drei Freiheitsgraden. Verwendet in Beispiel: 2.15.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/nicht_kollokierte_partielle_linearisierung_nach_spong.ipynb

 * Wagen-Pendel-System (Untersuchung der Integrierbarkeit des flachen Ausgangs des Variationssystems). Verwendet in Beispielen: 4.10, 4.40, 4.41, 4.54.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/wagen_pendel_nichtflachheit.ipynb

 * Zwei elastisch gekoppelte Körper und ein aktuiertes Pendel (Untersuchung der statischen EZ-Linearisierbarkeit). Verwendet in Beispielen: 4.11, 4.13, 4.20.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/zwei_elast_gekoppelte_wagen_pendel.ipynb

 * Akademisches Beispiel zum Unterschied zwischen unimodularer und F-unimodularer Vervollständigung. Verwendet in Beispiel: 4.16.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/f-unimodularitaet.ipynb

 * Acrobot (Zweigelenkmainipulator mit passivem erstem Gelenk) unter Einfluss der Schwerkraft. Verwendet in Beispiel: 4.34.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/acrobot_steuerbarkeit.ipynb
 * Zweifachpendel mit vollständig aktuiertem verschieblichem Aufhängepunkt. Verwendet in Beispiel: 4.46.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/zweifachpendel_nq2_np2_ruled_manif.ipynb

 * Mechanismus aus zwei translatorisch aktuierten Körpern und zwei Pendeln. Verwendet in Beispiel: 4.47.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/planar_verschieb_masse_pendel_akt_masse_pendel.ipynb

 * Akademisches Beispiel (Nachweis der Nichtflachheit für ein Eingrößensystem). Verwendet in Beispiel: 4.53.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/nichtflachheit_akademisches_bsp_m1.ipynb

 * Ebenes einachsiges Fahrzeug (Untersuchung der Integrierbarkeit des fl. Ausgangs des Variationssystems). Verwendet in Beispielen: 4.57, 4.61.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/einachsiges_fz_unimod_ergaenzung_und_notwendige_integrabilitaetsbedingung.ipynb

 * Planar verschiebliches Pendel mit Zusatzmasse (Untersuchung der Integrierbarkeit des flachen Ausgangs des Variationssystems). Verwendet in Beispielen: 4.58, 4.62.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/planar_verschiebl_pendel_elast_masse_int.ipynb

 * (Konfigurations-)Flachheit eines linearen translatorischen Systems. Verwendet in Beispiel: 4.74.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/visko-elastisch-transl_np1_nq1.ipynb

 * (Konfigurations-)Flachheit des linearisierten Modells des einachsigen Fahrzeugs. Verwendet in Beispiel: 4.75.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/einachsiges_fz_konfflache_ausgaenge_linearisiert.ipynb

 * Wagen mit rutschender Last (Steuerbarkeitsanalyse und Trajektorienberechnung). Verwendet in Beispiel: 5.3.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/wagen_mit_rutschender_last.ipynb

 * Mechanismus aus zwei translatorisch aktuierten Körpern und zwei Pendeln: Trajektorienplanung durch RWA-Lösung. Verwendet in den Beispielen: 5.8, 5.10.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/planar_verschieb_masse_pendel_akt_masse_pendel_rwa.ipynb

 * Acrobot: Trajektorienplanung durch RWA-Lösung. Verwendet in Beispiel: 5.10.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/acrobot_rwa.ipynb

 * Wagen-Pendel-System (Trajektorienplanung mittels Zeitumkehrsymmetrie). Verwendet in Beispiel: 5.19.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/wagen_pendel_zus.ipynb

 * Erzeugung einer Dauerschwingung das Wagen-Pendel-System. Verwendet in Beispiel: 6.7.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/wagen_pendel_grenzzyklus.ipynb

 * Überprüfung der Anwendung der äußeren Ableitung auf eine Polynommatrix. Verwendet in Beispiel: A.24.
   * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/polynommatrix-1-form.ipynb

 * PVTOL: Koordinatentransformation (Aufspaltung in passive und aktive Koordinaten). Verwendet in Beispielen: B.3, B.4.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/senkrechtstarter_pvtol_koordinatentransformation.ipynb

 * Einachsiges ebenes Fahrzeug: Nichtexistenz der BI-NF nach [OS01, Abschnitt 3.7]. Verwendet in Beispiel: B.5.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/einachsiges_fz_nichtexistenz_bi_nf_nach_Olfati-Saber.ipynb

 *  Numerische Rangbestimmung. Verwendet in Beispielen: B.8, B.9.
  * http://nbviewer.ipython.org/github/cknoll/beispiele/blob/master/numerische_rangbestimmung.ipynb



