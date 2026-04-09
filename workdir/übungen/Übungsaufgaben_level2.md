<!-- 
Stil: 
Für Level 2 (Fortgeschritten). 
Schreibstil bleibt locker, motivierend, Schritt-für-Schritt mit Alltagsbezug. 
Exakt wie Level 1 Aufgaben-Aufbau, aber angepasst auf Level 2.
-->

<section style="max-width:700px; margin:0 auto; text-align:center;">
  <h1 style="color:#23366e; font-size:2.5rem; margin-bottom:0.8rem;">
    Übungsaufgaben – Python LEVEL 2 🛠️
  </h1>
  <img 
    src="https://img.icons8.com/ios-filled/100/23366e/source-code.png" 
    width="90" 
    alt="Code Icon" 
    style="margin-bottom:1.4rem; display:block; margin-left:auto; margin-right:auto;"
  />
  <div style="color:#232323; font-size:1.1rem;">
    Willkommen beim nächsten Schritt auf deiner Programmierreise!<br>
    Jetzt wird’s abwechslungsreicher: Du kombinierst Grundwissen zu Bedingungen, Schleifen, Listen, Strings & mehr.<br>
    <br>
    <b style="color:#ac2200;">Fehler sind genauso deine Freunde wie in Stufe 1 – durch’s Ausprobieren kommst du weiter!</b>
    <br><br>
    <span style="color:#23366e;">Teste deinen Code direkt online, z.B. auf
      <a href="https://replit.com/~" style="color:#23366e;">replit.com/~</a> oder
      <a href="https://www.programiz.com/python-programming/online-compiler/" style="color:#23366e;">
        Programiz Online-Compiler</a>.
    </span>
    <br><br>
    <b style="color:#23366e;">Was brauchst du für Level 2?</b><br>
    <ul style="display:inline-block; text-align:left; color:#232323; margin-top:0.4rem;">
      <li>Grundfunktionen: <b>print</b>, <b>input</b>, Variablen</li>
      <li>Erste Erfahrungen mit Bedingungen und Schleifen</li>
      <li>Interesse und Lust, auch an „kniffligeren“ Situationen zu tüfteln</li>
    </ul>
    <span style="color:#23366e;"><b>Disclaimer: </b>Dieses Dokument wurde mit Hilfe von KI erstellt. Die Texte werden noch geprüft und ggf. angepasst.</span>
  </div>
</section>

---

<div class="pagebreak"></div>

# Wie knackst du die Level 2 Aufgaben?

**Gleiche Strategie wie zuvor, jetzt mit bisschen mehr Code-Power:**

1. **Lies die Aufgabe genau:** Was ist gefragt – was ungewohnt?
2. **Erkenne neue Begriffe oder Kniffe:** Googlen & Nachfragen ist erlaubt!
3. **Überleg dir deinen Lösungsweg:** In Alltagssprache oder erstmal als Kommentare.
4. **Code locker drauflos – jeder Versuch zählt!**
5. **Teste, spiel herum, verbessere:** Fehler zeigen, wo du was lernst!
6. **Frag nach Unterstützung, wenn du hängst!**

> **Tipp:** Zu jeder Aufgabe findest du kleine Tipps – lies sie erst, wenn du wirklich nicht weiterkommst. Erst selbst denken, dann Hilfe nutzen: Das bringt dich am meisten weiter!

---

<div class="pagebreak"></div>

# Deine Level 2 Aufgaben – Jetzt wird’s spannend! 🧩

## Aufgabe 1: Mini-Taschenrechner

Schreib ein Programm, das...

- Zwei Zahlen vom User abfragt
- Nach der gewünschten Rechenart fragt: +, -, * oder /
- Das passende Ergebnis ausgibt („Ergebnis: …“)

> 💡 **Tipp:**  
> Nutz `if/elif/else` für die Auswahl der Operation.  
> Teil niemals durch 0 – prüfe das vorher und gib eine freundliche Fehlermeldung aus!

**Beispiel:**  
<pre>
Erste Zahl: <b>12</b>
Zweite Zahl: <b>4</b>
Operation (+, -, *, /): <b>*</b>
Ergebnis: 48
</pre>

---

## Aufgabe 2: Zahlenratespiel

Der Computer denkt sich eine Zahl zwischen 1 und 100 aus – du musst raten!

- Bekomm nach jedem Versuch gesagt, ob dein Tipp zu groß oder zu klein ist.
- Versuchszähler nicht vergessen!
- Gib erst auf, wenn du die richtige Zahl erwischt hast.

> 💡 **Tipp:**  
> `random.randint(1, 100)` hilft dir beim Start (denk an `import random`!).

---

## Aufgabe 3: Listen & Durchschnitt

- Lass mindestens 5 Zahlen der Reihe nach eingeben.
- Leg die Zahlen in einer **Liste** ab.
- Berechne daraus den Durchschnitt – gib alle Zahlen und den Mittelwert aus.

> 💡 **Tipp:**  
> `sum(liste)` und `len(liste)` liefern die nötigen Infos!

---

<div class="pagebreak"></div>

## Aufgabe 4: Palindrom-Checker

- Frag einen Text ab.
- Prüf, ob der – egal ob Groß/Klein, mit/ohne Leerzeichen – ein **Palindrom** ist.
- Zur Erinnerung: Palindrom liest sich rückwärts wie vorwärts (z.B. „Lagerregal“).

> 💡 **Tipp:**  
> Mach alles klein und ohne Leerzeichen:  
> `text.replace(" ", "").lower()`  
> und vergleiche mit der Rückwärts-Version (`[::-1]`)

**Beispiel:**  
<pre>
Text: <b>Rentner</b>
Ergebnis: Palindrom!
</pre>

---

## Aufgabe 5: Wörter & Zeichen zählen

Frage einen beliebigen Satz ab:

- Wie viele Wörter?
- Wie viele Zeichen (ohne Leerzeichen)?

> 💡 **Tipp:**  
> `.split()` hilft für die Wörter,  
> `.replace(" ", "")` für die Zeichenanzahl.

---

## Aufgabe 6: Wörter zählen mit Dictionary

Lass einen längeren Text eingeben, dann:

- Zähle, wie oft jedes Wort (Case egal, keine Satzzeichen!) vorkommt.
- Gib jedes Wort mit Häufigkeit aus.

> 💡 **Tipp:**  
> Alles klein machen (`.lower()`), nach Leerzeichen zerlegen (`.split()`), dann mit `dict` zählen!

**Beispiel:**  
<pre>
Text: <b>Hallo Welt, hallo Welt!</b>
Ausgabe:
hallo: 2
welt: 2
</pre>

---

<div class="pagebreak"></div>

## Bonus: Mini-Adventskalender 🎄

Vom 1. bis 24. Dezember gibt’s jeden Tag eine Überraschung:

- User gibt den Tag ein (1-24)
- Gib zu jedem Tag einen netten Spruch, Emoji o.ä. (Liste oder Dictionary!)
- Nicht vergessen: Prüfen, ob die Zahl gültig ist – sonst eine freundliche Warnung.

> 💡 **Tipp:**  
> Test mal sowas wie `if 1 <= tag <= 24:` und sei kreativ mit den Inhalten für jeden Tag!

---

<span style="color:#232323;"><b>Viel Spaß beim Tüfteln – und dran denken: Jeder Fehler bringt dich weiter!</b></span>

---

<small>
Das sind die Level 2 Aufgaben – Fokus: Python, mehr Kombinieren & Ausprobieren.  
<b>Wenn das strong läuft, dann geht’s direkt zu Level 3 oder entwickle eigene Aufgaben!</b>
</small>
