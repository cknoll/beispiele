Dieses Repositorium enthält Beispielrechnungen als Ergänzung zur Dissertation mit dem Titel
"Regelungstheoretische Analyse- und Entwurfsansätze für unteraktuierte mechanische Systeme" von C. Knoll.
<br>
<br>
Die Beispielrechnungen sind als IPython-Notebook in der Programmiersprache `Python` (Version 2.7.x)
implementiert und haben folgende Abhängigkeiten:

* Wissenschaftliche Standardpakete
  * numpy, scipy, sympy, matplotlib
  * Am besten über einen Paket-Manager zu installieren
 
* [`symbtools`](https://github.com/cknoll/rst_symbtools) 
  * `core`-Modul: Grundlegende Funktionalität zum symbolischen Rechnen in der Regelungtheorie
    * Lie-Ableitungen, Rangprüfung, Zeitableitung von Symbolen, ...
  * `modeltools`-Modul
    * Aufstellen der Bewegungsgleichungen eines mechandischen Systems und Transformation
    in verschiedene Darstellungen
  * `noncommutativetools`
    * Funktionalität zum Rechnen mit Polynommatrizen über Schiefpolynomen,
    z.B. Rechtsverschiebung des Operators d/dt, Ansatzbasierte bestimmung einer
    unimodularen Inversen
   

* [`pycartan`](https://github.com/cknoll/pycartan)
  * Funktionalität zum Rechnenen mit Differentialformen, die auf geeigneten Jet-Büdneln definiert sind.

  

* [`PyTrajectory`](https://github.com/TUD-RST/pytrajectory)
  * Softwarepaket zur Trajektorienplanung auf Basis der Lösung eines Randwertproblems
  
    
* [`displaytools`](https://github.com/cknoll/displaytools)
 * IPython-Erweiterung, welche die speziellen Kommentare `##`, `##:` einführt um
 das Ergebnis einer Zuweisung anzeigen zu lassen.


