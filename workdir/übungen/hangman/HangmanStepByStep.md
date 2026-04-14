<!DOCTYPE html>
<html lang="de">
<script>
    function zeigeKapitel(nummer) {
        // Alle Kapitel ausblenden
        var kapitel = document.querySelectorAll('.kapitel');
        kapitel.forEach(k => k.classList.remove('aktiv'));
        // Das gewünschte Kapitel einblenden
        var aktuelles = document.getElementById('kapitel' + nummer);
        if (aktuelles) {
            aktuelles.classList.add('aktiv');
            aktuelles.scrollIntoView({ behavior: "smooth" });
        }
    }
    function zeigeCode() {
        // Ersetze gesamten Body-Inhalt durch die Code-Seite
        document.body.innerHTML = `
            <h1>Hier ist der fertige Hangman-Code!</h1>
            <p>
            Du kannst diesen Code in eine <code>hangman.py</code> Datei kopieren und starten.<br>
            Versuche aber trotzdem, die Schritte vorher selbst zu lösen ;-)
            </p>
            <pre style="background:#212529;color:#f8f8f2;padding:20px;border-radius:6px;overflow:auto;font-size:1rem">
import random
woerter = {
    "python": "Programmiersprache",
    "katze": "Ein Haustier, das schnurren kann",
    "regen": "Fällt manchmal vom Himmel",
    "auto": "Fährt auf vier Rädern",
    # ... (füge gerne eigene Wörter & Hinweise dazu!)
}
wort, hinweis = random.choice(list(woerter.items()))
geheimwort = wort
geratene_buchstaben = set()
fehler = 0
max_fehler = 7   # z.B. 7 Fehler sind Game Over
galgen = [
    """
       ------
       |    |
       |    
       |   
       |    
       |   
    --------
    """,
    """
       ------
       |    |
       |    O
       |   
       |    
       |   
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |    
       |   
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |    
       |   
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |    
       |   
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |   
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |   
    --------
    """
]
while True:
    # Wortanzeige (z.B. _ y t _ _ _)
    anzeige = [b if b in geratene_buchstaben else "_" for b in geheimwort]
    print("Wort:", " ".join(anzeige))
    print(f"Tipp: {hinweis}")
    print(f"Bisher geraten: {', '.join(sorted(geratene_buchstaben))}")
    print(galgen[min(fehler, len(galgen)-1)])
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
            </pre>
            <button class="weiter-btn" onclick="window.location.reload()">Zurück zum Schritt-für-Schritt Guide</button>
        `;
    }
</script>
<head>
    <meta charset="UTF-8">
    <title>Python Side-Projekt: Hangman Schritt für Schritt</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            background-color: #f8f9fa;
            color: #222;
            line-height: 1.7;
        }
        .kapitel {
            border: 1px solid #ebebeb;
            box-shadow: 2px 2px 8px #e7e7e7;
            background: #fff;
            padding: 30px;
            margin-bottom: 35px;
            border-radius: 7px;
        }
        .weiter-btn, .cheater-btn {
            display: block;
            margin: 25px auto 0 auto;
            padding: 10px 30px;
            font-size: 1rem;
            background-color: #71b380;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background 0.2s;
        }
        .weiter-btn:hover, .cheater-btn:hover {
            background-color: #599c6b;
        }
        h2 {
            margin-top: 0;
        }
        .kapitel {
            display: none;
        }
        .kapitel.aktiv {
            display: block;
        }
    </style>
</head>
<body>
    <h1>Side-Projekt: Hangman Schritt für Schritt mit Python</h1>
    <p style="font-style:italic;">Optionales Übungsprojekt – Arbeiten Sie Kapitel für Kapitel und bauen Sie Ihr eigenes Hangman-Spiel!</p>
    <!-- Kapitel 1 -->
    <section class="kapitel aktiv" id="kapitel1">
        <h2>Kapitel 1: Was ist Hangman?</h2>
        <p>
           Hangman (auch "Galgenmännchen") ist ein sehr simples Wörterratespiel, um die Zeit ~im Unterricht~ zu vertreiben.
           In den nachfolgenden Kapiteln werden wir eine Version davon in python umsetzen.
            <br>
           Disclaimer: Es gibt viele Wege etwas zu implementieren, hier geht es allein darum den Prozess näher kennenzulernen. 
           <br>
        </p>
        <button class="weiter-btn" onclick="zeigeKapitel(2)">Weiter zu Kapitel 2</button>
    </section>
    <!-- Kapitel 2 -->
    <section class="kapitel" id="kapitel2">
        <h2>Kapitel 2: Das Grundgerüst</h2>
        <p>
            Nachdem wir keine Ahnung haben, was wir alles benötigen, fangen wir klein an:
            Wir erstellen eine neue Python-Datei, z.B. <code>hangman.py</code>.<br>
            Dann printen wir, um sicher zustellen, dass die Datei auch ausführbar ist:
        </p>
        <pre>
            print("Willkommen bei Hangman!")
        </pre>
        <p>
            <b>Aufgabe:</b> Erstellen, schreiben, prüfen.
        </p>
        <button class="weiter-btn" onclick="zeigeKapitel(3)">Weiter zu Kapitel 3</button>
    </section>
    <!-- Kapitel 3 -->
    <section class="kapitel" id="kapitel3">
        <h2>Kapitel 3: Was braucht das Spiel eigentlich?</h2>
        <p>
            Nachdem wir Wörter erraten wollen, brauchen wir eine Liste an Wörtern, aus der ein Wort zufällig ausgewählt wird:
        </p>
        <pre>
import random

woerter = ["python", "hangman", "guenther"]
wort = random.choice(woerter)
        </pre>
        <p>
            <b>Aufgabe:</b> Gib das gewählte Wort mit <code>print(wort)</code> zur Kontrolle aus.
        </p>
        <button class="weiter-btn" onclick="zeigeKapitel(4)">Weiter zu Kapitel 4</button>
    </section>
    <!-- Kapitel 4 -->
    <section class="kapitel" id="kapitel4">
        <h2>Kapitel 4: "GameLoop"</h2>
        <p>
            Unsere Vorbereitungen sind erstmal abgeschlossen.
            Jetzt bauen wir eine <code>while()</code> Schleife, in der Unsere Game logik sich befindet.
            Innerhalb dieser Schleife wollen wir jz den Nutzer nach seinen Eingaben/Guesses fragen:
        </p>
        <pre>
buchstabe = input("Gib einen Buchstaben ein: ")
print("Du hast gewählt:", buchstabe)
        </pre>
        <p>
            <b>Aufgabe:</b> Integriere diesen Code in eine Schleife und führe das Programm aus.
        </p>
        <button class="weiter-btn" onclick="zeigeKapitel(5)">Weiter zu Kapitel 5</button>
    </section>
    <!-- Kapitel 5 (Beispiel; weitere Kapitel können genauso hinzugefügt werden) -->
    <section class="kapitel" id="kapitel5">
        <h2>Kapitel 5: Ist der Buchstabe richtig?</h2>
        <p>
            Jetzt die "logik". Ist der Guess richtig?
            Was passiert, wenn er richtig ist?
            Was, wenn er falsch ist?<br>
            <b>Aufgabe:</b> Prüfe ob der Buchstabe im Wort vorhanden ist.
        </p>
        <button class="weiter-btn" onclick="zeigeKapitel(6)">Weiter zu Kapitel 6</button>
    </section>
    <section class="kapitel" id="kapitel6">
        <h2>Kapitel 6: Fehlversuche zählen</h2>
        <p>
            Oh nurr, der Guess war falsch.<br>
            I guess dann zähl ich <code>fehlversuche = fehlversuche +1</code> 
            <b>Aufgabe:</b> Füge eine Variable hinzu, die die Anzahl der Fehler mitzählt, und erhöhe sie, wenn ein Buchstabe nicht im Wort ist.
        </p>
        <button class="weiter-btn" onclick="zeigeKapitel(7)">Weiter zu Kapitel 7</button>
    </section>
    <section class="kapitel" id="kapitel7">
        <h2>Kapitel 7: Gewinn oder Verlust erkennen</h2>
        <p>
            Das Spiel soll beendet werden, wenn entweder alle Buchstaben erraten wurden, oder die Maximale Anzahl an Fehlern überschritten wurden.
            Die einzige Frage hier ist, wie soll das Spiel beendet werden.<br>
            Ist es ein <code>while gameNotOver():</code>
            oder ein: <code>while true: if gameOver():break</code>
            <b>Aufgabe:</b>Ergänze eine Abfrage, die prüft ob das Spiel vorbei ist & gib eine entsprechende Nachricht aus.
        </p>
        <button class="weiter-btn" onclick="zeigeKapitel(8)">Weiter zu Kapitel 8</button>
    </section>
    <section class="kapitel" id="kapitel8">
        <h2>Kapitel 8: Gestalten wir es schöner </h2>
        <p>
            Theoretisch!
            Ist das Spiel jetzt spielbar.
            Allerdings fehlt uns noch der Charme des Galgenmännchens.
            Wir wollen wissen, wie viele Stellen das Wort hat, bspw: _ _ _ _ _
            Und sobald wir ein "P" erraten, geben wir es auch aus:   P _ _ _ _
            <b>
            Das der pseudocode:
            <code>Für jeden Buchstaben im string: wenn buchstabe nicht erraten: buchstabe = '_'</code> 
            <b>Aufgabe:</b> Programmiere eine Ausgabe, die alle bisher korrekt geratenen Buchstaben zeigt, alle anderen als Unterstrich.
        </p>
        <button class="weiter-btn" onclick="zeigeKapitel(9)">Weiter</button>
    </section>
  </section>
    <section class="kapitel" id="kapitel9">
        <h2>Kapitel 9: Gestalten wir es NOCH schöner </h2>
        <p>
            Herzlichen Glückwunsch!
            Das Spiel läuft.
            Wir können allerdings noch einen oben drauf setzen, indem wir eine kleine Hangman "animation" dazu bauen.
            Hint: Wir brauchen eine Liste an Frames
            <!-- hangman.gif einbinden-->
            <b>
            <b>Aufgabe:</b> Zeig das Galgenmännchen an & lass es mit steigender Fehlerzahl weiter hängen :().
        </p>
        <button class="weiter-btn" onclick="zeigeKapitel(1)">Zurück zum Anfang</button>
        <button class="cheater-btn" onclick="zeigeCode()"> Ich will cheaten :(</button>
    </section>
  
</body>
</html>