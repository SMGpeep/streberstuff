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