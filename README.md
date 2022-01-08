## Vorlage Bachelorarbeit HTW Berlin - Fachbereich 2

Es handelt sich hierbei um eine inoffizielle LaTeX Vorlage für die Bachelorarbeit an der HTW Berlin für den Fachbereich 2, speziell Studiengang Ingenieur-Informatik. Die Vorlage wurde nach den Vorgaben aus dem Modul "Wissenschaftliches Arbeiten" erstellt. Ich hafte für keine formalen Fehler oder sonstige Fehler!

### Bevor kompiliert wird:

  - In den Einstellungen vom LaTeX Editor muss `XeLatex` als Compiler eingestellt werden.
  - Der Baubefehl `--shell-escape` wird gebraucht: https://texwelt.de/fragen/10341/wie-aktiviere-ich-shell-escape-in-meinem-editor
  - Die Bibliographie wird von `Bibtex` mit `Biber` als Backend gemanaged. Das muss evtl. auch im Editor eingestellt werden.

### Projektstruktur

Ordner `abb` ist für Bilder da (Bilder müssen mit `abb/[bildname]` eingebunden werden)
Ordner `code` kann für Codeausschnitte benutzt werden(noch nicht in Benutzung)
Ordner `pages` ist für alle .tex Inhaltsdateien da

Datei `ref.bib` ist das BibTex Literaturverzeichnis
Datei `abk.tex` ist für die Abkürzungen da (acronym package)
Datei `symb.tex` ist für Symbole da
Datei `vars.tex` ist für LaTeX Command Definitionen da, u.a. auch einfach Variablen

Die Hauptdatei heißt `main.tex`.

Das Python Script `creator.py` ist zum Erzeugen eines vordefinierten LaTeX Codes für Bilder und Codeausschnitte da. Wenn du dich nicht mit Python auskennst dann ist es unwichtig :) Ist eh nur ne kleine Automatisierung.