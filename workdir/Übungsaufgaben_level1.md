<style>
@media print {
  .pagebreak { page-break-before: always; }
}
</style>
<section style="max-width:700px; margin:0 auto; text-align:center;">
  <h1 style="color:#23366e; font-size:2.5rem; margin-bottom:0.8rem;">
    Übungsaufgaben – Python LEVEL 1 🚀
  </h1>
  <img 
    src="https://img.icons8.com/ios-filled/100/23366e/source-code.png" 
    width="90" 
    alt="Code Icon" 
    style="margin-bottom:1.4rem; display:block; margin-left:auto; margin-right:auto;"
  />
  <div style="color:#222; font-size:1.1rem;">
    Willkommen bei deinen ersten richtigen Coding-Aufgaben!<br>
    Jetzt heißt es: selbst ran an die Tasten und das Gelernte ausprobieren.<br>
    <br>
    <b style="color:#ac2200;">Fehler sind deine Freunde – mit jedem Probieren wirst du besser!</b>
    <br><br>
    <span style="color:#23366e;">Kein Stress: Jeder fängt mal klein an, auch beim Programmieren.</span>
    <br><br>
    <b style="color:#ac2200;">Was brauchst du für Level 1?</b><br>
    <ul style="display:inline-block; text-align:left; color:#222; margin-top:0.4rem;">
      <li>Einfache Grundfunktionen: <b>print</b>, <b>input</b>, ein bisschen mit Variablen spielen</li>
      <li>Neugier, Lust zum Ausprobieren und keine Angst vor Fehlern!</li>
      <li>Kein spezielles Vorwissen nötig – Google hilft auch Profis</li>
      <li>Am besten: Einfach Code ausprobieren – z.B. auf
        <a href="https://replit.com/~" style="color:#23366e;">replit.com/~</a>
        oder
        <a href="https://www.programiz.com/python-programming/online-compiler/" style="color:#23366e;">
          Programiz Online-Compiler</a>
      </li>
    </ul>
      <span style="color:#23366e;"><b>Disclaimer: </b>Dieses Dokument wurde mit Hilfe von KI erstellt. Die Texte werden noch geprüft und ggf. angepasst.</span>
  </div>
</section>

---
<div class="pagebreak"></div>

## Wie meisterst du die Level 1 Aufgaben?

**Locker bleiben! Hier ein Starthilfe-Leitfaden für deine ersten Python-Problemlösungen:**

1. **Lies die Aufgabe genau:** Was musst du rausfinden/lösen?
2. **Markiere dir Schlüsselwörter:** Sagt dir alles was? Sonst: kurz nachschlagen!
3. **Überlege in Alltagssprache:** Was soll passieren – Schritt für Schritt!
4. **Einfach starten!** Jeder Anfang zählt, egal wie klein.
5. **Teste, staune, verbessere:** Fehler zeigen dir, wo du üben kannst.
6. **Fragen stellen/Googeln ist erlaubt und sogar schlau!**

> **Tipp:** Kleine Schritte sind top! Niemand muss perfekte Lösungen am Stück tippen. Jeder Versuch bringt dich weiter.

---

<div class="pagebreak"></div>

# Deine Level 1 Aufgaben – Werde Programmierheld:in 🤓

---

## Aufgabe 1: Dein erstes „Hallo Welt“ – Klassiker!

Easy:  
Schreib ein kleines Programm, das einfach nur <strong>Hallo Welt!</strong> ausgibt.

> <span style="color:#1a5d19;">💡 Tipp:</span>  
> Es gibt in Python ein „Zauberwort“ fürs Anzeigen auf dem Bildschirm – das kann man einfach mal probieren oder suchen!

---

## Aufgabe 2: Begrüßung in Großbuchstaben

Frag nach dem Namen der Nutzerin/des Nutzers und begrüße sie/ihn – ABER: Die Begrüßung soll in Großbuchstaben erscheinen.

**Beispiel:**  
<pre>
Wie heißt du? <b>Alex</b>
HALLO, ALEX!
</pre>

> <span style="color:#1a5d19;">💡 Tipp:</span>  
> Eingaben abfragen? In Python geht das mit einer Funktion.<br>
> Für Großbuchstaben gibt’s eine Trick-Methode für „Text“-Variablen.  
> Trau dich, rumzuprobieren oder kurz nachzulesen!

---

## Aufgabe 3: Altersrechner mit Jahresfrage

Erfrage das Geburtsjahr und berechne das Alter.<br>
Zusatz: „Hast du dieses Jahr schon Geburtstag gehabt?“ Wenn nein, ein Jahr abziehen!<br>
Gib dann das Alter freundlich aus.

**Beispiel:**  
<pre>
In welchem Jahr bist du geboren? <b>2009</b>
Hast du dieses Jahr schon Geburtstag gehabt? (ja/nein) <b>ja</b>
Du bist 14 Jahre alt!
</pre>

> <span style="color:#1a5d19;">💡 Tipp:</span>  
> Das aktuelle Jahr finden? Dafür gibt es z.B. das „datetime“-Modul.  
> Einfach mal: python aktuelles jahr googeln!

---

<div class="pagebreak"></div>

## Aufgabe 4: Rechner-Programm für Einsteiger

1. Frage zwei Zahlen ab  
2. Frage nach der Rechenart (+, -, *, /)  
3. Zeige das Ergebnis  
4. Aber: Wenn du durch Null teilen willst – geb eine freundliche Fehlermeldung!

**Beispiel:**  
<pre>
Erste Zahl: <b>9</b>
Zweite Zahl: <b>3</b>
Was möchtest du machen? (+, -, *, /): <b>*</b>
Ergebnis: 27
</pre>

> <span style="color:#1a5d19;">💡 Tipp:</span>  
> Mit <b>if/elif/else</b> kannst du prüfen, was gerechnet werden soll.<br>
> Division durch Null? Wenn du das vorher prüfst, macht dein Programm keine komischen Fehler!
> Einfach ausprobieren und Schritt für Schritt vorgehen.

---

## Aufgabe 5: Immer wieder weiter? – Die Schleifenfrage

Dein Programm soll wiederholt fragen:  
<code>Möchtest du noch eine Aufgabe machen? (ja/nein)</code>  
Solange „ja“ kommt: „Los geht’s, weiter!“  
Bei „nein“: „Alles klar, bis zum nächsten Mal!“  
Andere Antworten: „Bitte nur 'ja' oder 'nein' eingeben.“

**Beispiel:**  
<pre>
Möchtest du noch eine Aufgabe machen? (ja/nein): <b>vielleicht</b>
Bitte nur 'ja' oder 'nein' eingeben.
Möchtest du noch eine Aufgabe machen? (ja/nein): <b>ja</b>
Los geht's, weiter!
Möchtest du noch eine Aufgabe machen? (ja/nein): <b>nein</b>
Alles klar, bis zum nächsten Mal!
</pre>

> <span style="color:#1a5d19;">💡 Tipp:</span>  
> Mit einer hübschen <b>while</b>-Schleife plus <b>if</b>-Abfrage klappt das bestens.<br>
> Denk Schritt für Schritt – erst wenn du den Ablauf im Kopf hast, wird’s im Code ganz easy.

---

<span style="color:#23366e;"><b>Viel Spaß beim Ausprobieren – trau dich und leg los!</b></span>

---

<small>
Level 1 ist dein Sprungbrett – es geht ums Machen, nicht ums Perfektsein.<br>
Im nächsten Level warten weitere Herausforderungen und Tricks – aber jetzt zählt nur eins: Loslegen, Spaß haben, wachsen!
</small>

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