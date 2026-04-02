<!-- 
Kommentar: 
Schreibstil Inspiration von „Crashkurs Programmieren“:
- Locker und zugänglich, direkte Ansprache („du“)
- Viele Erklärboxen/Hinweise in Farbe, oft als Tipp
- Viele Analogien, Alltagsbezug („wie Radfahren“, „Lego“)
- Ermutigend, freundlich, Fehler ganz normalisierten
- Schritt-für-Schritt und keine Angst vor Google etc.
- Fachbegriffe immer einfach erklärt oder einfach erwähnt, Mut zum Ausprobieren/mal schief machen.
- Struktur klar (Aufzählungen, Beispielboxen, Trennstriche und Seitenumbrüche)
In Zukunft bitte genau diesen Tonfall und Aufbau für Anleitungen und Aufgaben übernehmen.
-->

<style>
@media print {
  .pagebreak { page-break-before: always; }
}
</style>
<section style="max-width:700px; margin:0 auto; text-align:center;">
  <h1 style="color:#1a237e; font-size:2.5rem; margin-bottom:0.8rem;">
    Übungsaufgaben – Python LEVEL 3: EXPERTE 🧠✨
  </h1>
  <img 
    src="https://img.icons8.com/ios-filled/100/1a237e/source-code.png" 
    width="90" 
    alt="Code Icon" 
    style="margin-bottom:1.4rem; display:block; margin-left:auto; margin-right:auto;"
  />
  <div style="color:#232323; font-size:1.1rem;">
    Willkommen beim <b style="color:#1a237e;">Level 3: EXPERTEN-Modus</b> deiner Python-Quest!<br>
    Hier geht’s ans Eingemachte – aber keine Panik: <b style="color:#ad1457;">Jede Herausforderung ist auch eine Einladung zum Knobeln, Ausprobieren und Überraschtwerden.</b><br>
    <br>
    <span style="color:#ad1457;">Was erwartet dich?</span><br>
    Aufgaben, bei denen sogar Fortgeschrittene ins Grübeln kommen – perfekt, um neue Denkwege, Fehler, kreative Lösungen und ein bisschen Googeln zu genießen.<br>
    <br>
    <b style="color:#1a237e;">Dein Spielfeld ist offen:</b> Interpretier die Aufgaben, bau eigene Extras ein, oder probier’s einfach anders als gewohnt! Fehler? Sind willkommene Gäste 😎<br>
    <br>
    <span style="color:#ad1457;">Tipp zum Durchstarten:</span>
    Ob auf deinem Rechner oder online (z.B. <a href="https://replit.com/~" style="color:#1a237e;">replit.com/~</a>), Hauptsache, du kannst sofort loslegen.<br>
    <br>
    <span style="color:#ad1457;"><b>Hinweis:</b> Dieses Dokument wurde mit Unterstützung von KI erstellt und wird regelmäßig auf Praxistauglichkeit geprüft.</span>
  </div>
</section>

---

<div class="pagebreak"></div>

# Deine Level 3 Aufgaben – EXPERTENZONE 🚀

---

## Aufgabe 1: Primzahlgenerator – Turbo-Version

Schreib ein Programm, das <strong>alle Primzahlen</strong> bis zu einer selbst gewählten (vom User eingegebenen) Zahl findet und sauber ausgibt.

> <span style="color:#ad1457;">💡 Tipp:</span>
> • Probier’s effizient: Das „Sieb des Eratosthenes“ ist ein heißer Kandidat!  
> • Fang bei falschen Eingaben freundlich auf – auch „0“ oder Quatsch bitte nett abfangen.  
> • Beispiel: Bei <code>20</code> ⇒ <b>2, 3, 5, 7, 11, 13, 17, 19</b>

---

## Aufgabe 2: Anagramm-Alarm

Frage mehrere Wörter ab und prüfe, ob sie Anagramme voneinander sind.

> <span style="color:#ad1457;">💡 Tipp:</span>
> • „Anagramme“ = gleiche Buchstaben, andere Reihenfolge (z.B. „liste“ <span style="color:#ad1457;">⇄</span> „leits“)  
> • Nutze Listen, <b>sort()</b>, String-Methoden und clevere Vergleiche!

---

## Aufgabe 3: Palindrom-Sätze auf Profi-Niveau

Frag einen Satz ab (egal ob mit Leerzeichen oder Satzzeichen). Teste, ob er – nach Kleinbuchstaben-Konvertierung & Weglassen aller Nicht-Buchstaben – ein Palindrom ist!

> <span style="color:#ad1457;">💡 Tipp:</span>
> • Beispiel: „Eine Horde bedrohe nie!“ ⇒ Palindrom  
> • <code>import re</code> hilft, mit <b>re</b>-Methoden alles Unnötige auszublenden  
> • Erst alles bereinigen, dann prüfen

---

## Aufgabe 4: Wörter zählen – Extra scharf

Lass einen längeren Text eingeben und zähle, wie oft jedes unterschiedliche Wort vorkommt (Groß/Kleinschreibung egal!).

> <span style="color:#ad1457;">💡 Tipp:</span>
> • Satzzeichen vorher entfernen  
> • Nutze ein <b>dict</b> oder <b>collections.Counter</b> als Zähl-Schatztruhe  
> • Beispiel: „Hallo Welt, hallo Erde!“ → hallo:2, welt:1, erde:1

---

<div class="pagebreak"></div>

## Aufgabe 5: Erfinde dein eigenes Zahlenspiel!

Überlege dir ein eigenes kleines Zahlenrätsel (wie „FizzBuzz“, „3-6-9-Spiel“ o.ä.).  
Schreib vor dem Code <b>als Kommentar kurz, wie dein Spiel funktioniert</b>.</br>
Dann setz es um!

> <span style="color:#ad1457;">💡 Tipp:</span>
> • Misch Bedingungen, sei kreativ!  
> • Eine erklärende Mini-Beschreibung (als Kommentar am Start!)  
> • Klarer Aufbau, ordentlich kommentieren

---

## Aufgabe 6: Sudoku-Checker (Kompakt-Modus)

Schreibe ein Programm, das prüft, ob eine gegebene Sudoku-Lösung (z.B. 4x4 oder 9x9) korrekt ist.<br>
Die Lösung wird als Liste von Listen eingegeben – überprüfe komplette Zeilen, Spalten UND Blöcke.

> <span style="color:#ad1457;">💡 Tipp:</span>
> • 4x4: Zahlen 1–4, 9x9: 1–9 – jede muss pro Zeile, Spalte, Block genau einmal auftauchen  
> • <b>set</b>s helfen dir bei der Prüfung!  
> • Denk an die Blocklogik (bei 4x4: 2x2-Blöcke).

---

## Aufgabe 7: Datei auslesen – Top 10 Wörter

Schreibe ein Programm, das eine Textdatei einliest, die 10 häufigsten Wörter findet und samt Anzahl ausgibt.<br>
Stichwort: Datei auslesen, Wörter zählen, nach Häufigkeit sortieren.

> <span style="color:#ad1457;">💡 Tipp:</span>
> • <code>open()</code> + <code>read()</code> = dein Einstieg  
> • <code>collections.Counter</code> oder <code>dict</code> zählt flott  
> • Satzzeichen vorher raus!

---

## Aufgabe 8: Die magische Zahl – Rätsellust

Der Computer denkt sich eine „magische Zahl“ zwischen 1 und 100 aus.<br>
Du darfst raten: Nach jedem Versuch bekommst du ein Feedback („zu groß“, „zu klein“, „geschafft!“).  
Am Ende siehst du, wie viele Versuche du brauchtest.

> <span style="color:#ad1457;">💡 Tipp:</span>
> • <code>random.randint(1, 100)</code> zaubert dir die Aufgabe  
> • <b>while</b>-Schleife: Bleib hartnäckig!  
> • Versuchszählt hilft dir vergleichen :)

---

<span style="color:#1a237e;"><b>Viel Spaß mit den Level 3 Challenges – mutig testen, kombinieren, eigene Extras probieren … und bitte Fehler feiern! 🤓🎉</b></span>

---

<small>
Diese Level 3 Aufgaben sind für echte Python-Fans – aber:  
<b>Neue Ideen? Coole Kniffe? Fügt sie gern hinzu oder mailt sie weiter!</b>
</small>
