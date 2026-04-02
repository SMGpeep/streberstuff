# todo: anpassen!
    => ein html draus machen, gifs einbinden / visualisieren, etc.

## 🐍 Schritt für Schritt: Dein erstes Hangman-Spiel (Galgenmännchen)

Möchtest du dein erstes Hangman-Game in Python programmieren? Super Idee!  
In dieser Anleitung erkläre ich jeden Schritt extra anfängerfreundlich – damit du alles nachvollziehen kannst, auch wenn du gerade erst mit Python startest.  
Wir benutzen ein Dictionary, also ein besonderes Wörterbuch in Python, mit dem du die Worte und Hinweise speichern kannst.

---

### Was ist Hangman?

Beim Hangman-Spiel überlegt sich der Computer ein geheimes Wort.  
Du versuchst, dieses Wort Buchstabe für Buchstabe zu erraten. Immer wenn du einen falschen Buchstaben rätst, wird ein Teil vom Galgenmännchen „gemalt“. Schaffst du es, das Wort zu raten, bevor das Männchen fertig „hängt“?

---

### 1️⃣ Wörter und Hinweise als Dictionary speichern

Ein Dictionary (auf Deutsch: Wörterbuch) ist in Python ein Behälter für „Schlüssel-Wert“-Paare.  
Hier speichern wir unsere Wörter als Schlüssel und kleine Tipps als Werte.

Das sieht so aus:

```python
# Wörterbuch: Wort -> Hinweis
woerter = {
    "python": "Das ist eine Programmiersprache.",
    "katze": "Ein Haustier, das schnurren kann.",
    "regen": "Fällt manchmal vom Himmel (und macht nass).",
    "auto": "Fährt auf vier Rädern – meistens schnell!",
    # Hier kannst du auch eigene Wörter & Hinweise dazu eintragen :-)
}
```
*Du kannst später noch mehr Wörter/Tipp-Paare eintragen, oder die vorhandenen anpassen.*

---

### 2️⃣ Zufällig ein Wort auswählen

Wir wollen, dass jedes Mal ein anderes Wort drankommt.  
Mit der `random`-Bibliothek kann man ganz einfach ein zufälliges Wort (und den dazugehörigen Hinweis) aus unserem Dictionary ziehen:

```python
import random

# Aus dem Dictionary eine beliebige (Wort, Hinweis)-Kombination auswählen
wort, hinweis = random.choice(list(woerter.items()))
```
*Der Computer wählt so ein beliebiges Wort + Tipp für dich.*

---

### 3️⃣ Wie läuft das Spiel?

- Das Wort bleibt geheim – es wird als lauter Unterstriche angezeigt („_ _ _ _“).
- Du gibst einen Buchstaben ein.
- Ist der Buchstabe im Wort, wird er aufgedeckt.
- Ist er nicht drin, zählst du 1 Fehler mehr.
- Wenn du zu viele Fehler machst, verlierst du.
- Wenn du alle Buchstaben errätst, hast du gewonnen.

---

### 4️⃣ Beispiel: Eine ganze Spielrunde

Hier ist ein einfacher Beispielcode, wie eine Runde aussehen kann.  
Kommentarzeilen (`# ...`) erklären alles Schritt für Schritt. Lies sie in Ruhe durch!

```python
geheimwort = wort  # Das Wort, das erraten werden muss
geratene_buchstaben = set()   # Hier speichern wir, was du schon geraten hast
fehler = 0      # So viele Fehler hast du gemacht
max_fehler = 7  # Nach 7 Fehlern ist leider Schluss

while True:
    # So sieht das Wort für dich aus: erratene Buchstaben werden gezeigt
    anzeige = [buchstabe if buchstabe in geratene_buchstaben else "_" for buchstabe in geheimwort]
    print("Wort:", " ".join(anzeige))
    print(f"Tipp: {hinweis}")
    print(f"Bisher geraten: {', '.join(sorted(geratene_buchstaben))}")
    print(f"Fehler: {fehler}/{max_fehler}")

    # Jetzt fragt der Computer dich nach dem nächsten Buchstaben
    buchstabe = input("Bitte gib einen Buchstaben ein: ").lower()
    
    # Prüfe, ob die Eingabe gültig ist (nur EIN Buchstabe, kein Zahl/leerzeichen)
    if not buchstabe or len(buchstabe) != 1 or not buchstabe.isalpha():
        print("Achtung: Bitte genau einen Buchstaben eingeben!")
        continue

    if buchstabe in geratene_buchstaben:
        print("Den Buchstaben hast du schon versucht.")
        continue

    # Füge den neuen Buchstaben zu den geratenen hinzu
    geratene_buchstaben.add(buchstabe)

    if buchstabe in geheimwort:
        print("Richtig geraten!")
        # Sind jetzt alle Buchstaben entdeckt?
        if all(b in geratene_buchstaben for b in geheimwort):
            print(f"Glückwunsch! Das Wort war: {geheimwort}")
            break   # Das Spiel ist geschafft!
    else:
        print("Leider falsch.")
        fehler += 1
        if fehler >= max_fehler:
            print(f"Game over! Das Wort war: {geheimwort}")
            break   # Leider verloren, Spiel zu Ende
```

---

### 5️⃣ Was könntest du noch ausprobieren?

- **Highscore-Liste:** Wer schafft das Wort mit den wenigsten Fehlern? Das geht auch mit einem Dictionary!
- **Mehr Auswahl:** Lasse den User entscheiden, ob er ein leichtes oder ein langes Wort spielen will.
- **Eigenes Menü:** Baue eine Auswahl – „Neues Wort hinzufügen“, „Tipp sehen“, „Spiel starten“ usw.
- **Wörter speichern:** Speichere eigene Wörter dauerhaft in einer Datei, damit sie beim nächsten Mal wieder da sind.
- **Grafik:** Zeige ein kleines „ASCII-Bild“ vom Galgenmännchen für jeden Fehler an.

---

**Merke:**  
Mit Dictionaries kannst du in Python ganz einfach Wörter, Hinweise, Punktstände und vieles mehr verwalten.  
Probier’ Sachen aus! Es ist vollkommen okay, Fehler zu machen – so lernt man am meisten.

> **Tipp:**  
> Bau erstmal das Grundspiel – wenn das läuft, kannst du es immer weiter verbessern.  
> Wenn etwas nicht klappt, frag gerne nach! Wir sind ja hier zum Lernen.

---

Viel Spaß beim Basteln und Programmieren deines eigenen Hangman-Games! 🚀
Falls du Hilfe brauchst: Frag einfach deinen Tutor 😉
