# Das große Dictionary-Projekt – Dein persönliches Wörterbuch

import os

def lade_woerterbuch(dateiname):
    woerterbuch = {}
    if os.path.exists(dateiname):
        try:
            with open(dateiname, "r", encoding="utf-8") as f:
                for zeile in f:
                    parts = zeile.strip().split("::")
                    if len(parts) == 2:
                        wort, bedeutungen = parts
                        woerterbuch[wort] = bedeutungen.split('|')
        except Exception as e:
            print("Fehler beim Laden:", e)
    return woerterbuch

def speichere_woerterbuch(woerterbuch, dateiname):
    try:    
        with open(dateiname, "w", encoding="utf-8") as f:
            for wort, bedeutungen in woerterbuch.items():
                f.write(f"{wort}::{'|'.join(bedeutungen)}\n")
    except Exception as e:
        print("Fehler beim Speichern:", e)

def wort_hinzufuegen(woerterbuch):
    wort = input("Deutsches Wort: ").strip()
    if not wort:
        print("Bitte gib ein Wort ein!")
        return
    if wort in woerterbuch:
        print(f'"{wort}" gibt es schon.')
        weitere = input("Weitere Bedeutung hinzufügen? (j/n): ")
        if weitere.lower() != 'j':
            return
    bedeutungen = input("Englische Bedeutung(en) (Komma getrennt): ")
    bedeutungsliste = [b.strip() for b in bedeutungen.split(",") if b.strip()]
    if wort in woerterbuch:
        woerterbuch[wort].extend(bedeutungsliste)
        woerterbuch[wort] = list(set(woerterbuch[wort]))  # Duplikate vermeiden
    else:
        woerterbuch[wort] = bedeutungsliste
    print(f'"{wort}" wurde gespeichert!')

def bedeutung_abfragen(woerterbuch):
    wort = input("Wort zum Nachschlagen: ").strip()
    if wort in woerterbuch:
        print(f'Bedeutungen von "{wort}": {", ".join(woerterbuch[wort])}')
    else:
        print(f'"{wort}" wurde nicht gefunden.')

def wort_entfernen(woerterbuch):
    wort = input("Welches Wort möchtest du löschen?: ").strip()
    if wort in woerterbuch:
        del woerterbuch[wort]
        print(f'"{wort}" wurde entfernt.')
    else:
        print(f'"{wort}" nicht gefunden.')

def alles_anzeigen(woerterbuch):
    if not woerterbuch:
        print("Das Wörterbuch ist leer.")
        return
    print("--- Wörterbuch ---")
    for wort, bedeutungen in woerterbuch.items():
        print(f'{wort}: {", ".join(bedeutungen)}')

def menu():
    dateiname = "woerterbuch.txt"
    woerterbuch = lade_woerterbuch(dateiname)
    while True:
        print("\n--- Mein Wörterbuch ---")
        print("1. Neues Wort hinzufügen")
        print("2. Übersetzung(en) ansehen")
        print("3. Wort löschen")
        print("4. Alles anzeigen")
        print("5. Beenden")
        wahl = input("Aktion (1-5): ")
        if wahl == "1":
            wort_hinzufuegen(woerterbuch)
            speichere_woerterbuch(woerterbuch, dateiname)
        elif wahl == "2":
            bedeutung_abfragen(woerterbuch)
        elif wahl == "3":
            wort_entfernen(woerterbuch)
            speichere_woerterbuch(woerterbuch, dateiname)
        elif wahl == "4":
            alles_anzeigen(woerterbuch)
        elif wahl == "5":
            print("Tschüss 👋")
            break
        else:
            print("Ungültige Auswahl, bitte 1-5 eingeben.")

if __name__ == "__main__":
    menu()