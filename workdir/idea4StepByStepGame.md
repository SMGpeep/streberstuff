## 🐍 Schritt-für-Schritt-Anleitung: Hangman (Galgenmännchen) mit Dictionary bauen

Du willst selbst ein „Hangman“-Game in Python programmieren? Klasse! Wir machen das gemeinsam – und zwar so, dass Dictionarys ganz wichtig sind und du dabei alles Schritt für Schritt verstehst.

---

### Was ist das Ziel?

Errate ein geheimes Wort – Buchstabe für Buchstabe! Für jeden falschen Tipp wird der Galgen „vollständiger“. Schaffst du es, das Wort zu lösen, bevor das Galgenmännchen „fertig gebaut“ ist?

---

### 1️⃣ Grundgerüst: Wörter & Hinweise ins Dictionary packen

Wir brauchen eine Sammlung an Wörtern, die geraten werden können – und jeweils vielleicht einen kleinen Hinweis dazu.

```python
woerter = {
    "python": "Programmiersprache",
    "katze": "Ein Haustier, das schnurren kann",
    "regen": "Fällt manchmal vom Himmel",
    "auto": "Fährt auf vier Rädern",
    # ... (füge gerne eigene Wörter & Hinweise dazu!)
}
```

---

### 2️⃣ Zufallswort wählen

```python
import random
wort, hinweis = random.choice(list(woerter.items()))
```

---

### 3️⃣ Spielablauf (Basics)

- Zeige dem Spieler das Wort als „____“ (also verdeckt)
- Frage nach einem Buchstaben
- Wenn der Buchstabe im Wort ist: Aufdecken!
- Sonst: Fehler zählen, Galgen „zeichnen“
- Gewonnen? Verloren? Oder nochmal raten!

---

### 4️⃣ Beispiel für eine Spielrunde

```python
geheimwort = wort
geratene_buchstaben = set()
fehler = 0
max_fehler = 7   # z.B. 7 Fehler sind Game Over

while True:
    # Wortanzeige (z.B. _ y t _ _ _)
    anzeige = [b if b in geratene_buchstaben else "_" for b in geheimwort]
    print("Wort:", " ".join(anzeige))
    print(f"Tipp: {hinweis}")
    print(f"Bisher geraten: {', '.join(sorted(geratene_buchstaben))}")
    print(f"Fehler: {fehler}/{max_fehler}")

    buchstabe = input("Nächster Buchstabe: ").lower()
    if not buchstabe or len(buchstabe) != 1 or not buchstabe.isalpha():
        print("Bitte gib genau einen Buchstaben ein!")
        continue
    if buchstabe in geratene_buchstaben:
        print("Den hast du schon probiert!")
        continue

    geratene_buchstaben.add(buchstabe)
    if buchstabe in geheimwort:
        print("Richtig!")
        if all(b in geratene_buchstaben for b in geheimwort):
            print(f"Glückwunsch, das Wort war: {geheimwort}")
            break
    else:
        print("Leider falsch.")
        fehler += 1
        if fehler >= max_fehler:
            print(f"Game over! Das Wort war: {geheimwort}")
            break
```

---

### 5️⃣ Eigene Features & Ideen

- Füge eine Highscore-Liste (mit Dictionary!) hinzu
- Lass Wörter per Zufall, nach Länge, nach Schwierigkeitsgrad wählen
- Baue ein Menü ein: „Neues Wort hinzufügen“, „Hinweise sehen“, „Spiel starten“  
- Speichere neue Wörter dauerhaft (z.B. in einer Datei)  
- Baue ASCII-Art für das „Galgenmännchen“ ein!

---

**Fazit:**  
Mit Dictionarys kannst du Wörter, Hinweise, Highscores, Spielerprofile & Co. super easy verwalten. Trau dich: Teste, ändere, probier rum!

> **Tipp:**  
> Baue zuerst das Grundspiel und dann Schritt für Schritt neue Features ein.  
> Fehler machen gehört dazu – und macht am Ende den Code besser!

---

Viel Spaß beim Coden deines eigenen Hangman-Games! 🚀
