<!DOCTYPE html>
<html lang="de">
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
        .weiter-btn {
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
        .weiter-btn:hover {
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
            Hangman (Galgenmännchen) ist ein beliebtes Wortratespiel. Ziel ist es, Buchstaben zu raten, um ein verstecktes Wort zu finden.
            In diesem Projekt programmieren wir Schritt für Schritt unser eigenes Hangman-Spiel in Python.
        </p>
        <button class="weiter-btn" onclick="zeigeKapitel(2)">Weiter zu Kapitel 2</button>
    </section>
    <!-- Kapitel 2 -->
    <section class="kapitel" id="kapitel2">
        <h2>Kapitel 2: Das Grundgerüst</h2>
        <p>
            Erstelle eine neue Python-Datei, z.B. <code>hangman.py</code>.<br>
            Schreibe als allererstes folgenden Code, um das Spiel zu starten:
        </p>
        <pre>
            print("Willkommen bei Hangman!")
        </pre>
        <p>
            <b>Aufgabe:</b> Führe dein Skript aus und überprüfe, ob die Begrüßung erscheint.
        </p>
        <button class="weiter-btn" onclick="zeigeKapitel(3)">Weiter zu Kapitel 3</button>
    </section>

    <!-- Kapitel 3 -->
    <section class="kapitel" id="kapitel3">
        <h2>Kapitel 3: Ein Wort auswählen</h2>
        <p>
            Jetzt brauchst du ein Wort, das erraten werden soll. Lege ein kleines Wörter-Array an, aus dem zufällig ein Wort gewählt wird.<br>
            Beispiel:
        </p>
        <pre>
import random

woerter = ["python", "hangman", "programmieren"]
wort = random.choice(woerter)
        </pre>
        <p>
            <b>Aufgabe:</b> Gib das gewählte Wort mit <code>print(wort)</code> zur Kontrolle aus.
        </p>
        <button class="weiter-btn" onclick="zeigeKapitel(4)">Weiter zu Kapitel 4</button>
    </section>

    <!-- Kapitel 4 -->
    <section class="kapitel" id="kapitel4">
        <h2>Kapitel 4: Das Spielgerüst und erste Benutzereingabe</h2>
        <p>
            Nun bauen wir die Spiel-Logik schrittweise auf. 
            Frage mit <code>input()</code> einen Buchstaben vom Spieler ab und gib ihn danach aus.
        </p>
        <pre>
buchstabe = input("Gib einen Buchstaben ein: ")
print("Du hast gewählt:", buchstabe)
        </pre>
        <p>
            <b>Aufgabe:</b> Integriere diesen Code und führe das Programm aus.
        </p>
        <button class="weiter-btn" onclick="zeigeKapitel(5)">Weiter zu Kapitel 5</button>
    </section>

    <!-- Kapitel 5 (Beispiel; weitere Kapitel können genauso hinzugefügt werden) -->
    <section class="kapitel" id="kapitel5">
        <h2>Kapitel 5: Nächste Schritte</h2>
        <p>
            Super! Von hier aus kannst du das Spiel um folgende Aspekte erweitern:
            <ul>
                <li>Vergleiche den geratenen Buchstaben mit dem gesuchten Wort</li>
                <li>Zeige den aktuellen Stand des Wortes (_ y _ h _ o _)</li>
                <li>Zähle die Fehlversuche</li>
                <li>Beende das Spiel bei Gewinn oder Verlust</li>
            </ul>
            <i>Konkrete Teilaufgaben dazu folgen noch in den nächsten Kapiteln.</i>
        </p>
        <button class="weiter-btn" onclick="zeigeKapitel(1)">Zurück zum Anfang</button>
    </section>

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
    </script>
</body>
</html>