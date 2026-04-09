<style>
@media print {
  .pagebreak { page-break-before: always; }
}
</style>
<section style="max-width:700px; margin:0 auto; text-align:center;">
  <h1 style="color:#23366e; font-size:2.5rem; margin-bottom:0.8rem;">
    Das Große Dictionary-Projekt
  </h1>
  <img 
    src="https://img.icons8.com/ios-filled/100/23366e/source-code.png" 
    width="90" 
    alt="Code Icon" 
    style="margin-bottom:1.4rem; display:block; margin-left:auto; margin-right:auto;"
  />
  <div style="color:#222; font-size:1.1rem;">
    <br>
    In diesem Projekt baust du dir Schritt für Schritt dein eigenes Wörterbuch-Programm in Python.<br>
    <br>
    Mit deinem Dictionary kannst du nicht nur Wörter übersetzen, sondern das Programm auch beliebig erweitern – zum Beispiel zu einem kleinen Vokabeltrainer.<br>
    <br>
    Ziel ist es, dass du dir hiermit die Handhabung mit Dictionaries näher bringst und besser veranschaulichen kannst.  
    Wie du das Menü gestaltest oder welche zusätzlichen Funktionen du einbaust, bleibt ganz dir überlassen. <br>
    Viel Spaß beim Programmieren und Experimentieren!
    <br>
  </div>
</section>

---
<div class="pagebreak"></div>

# Aufgabenstellung:

Schreib ein Programm, das ein eigenes Wörterbuch („Dictionary“) in Python verwaltet.  
So könnte deine Mission aussehen:

1. **Start:** Beim Programmstart ist das Wörterbuch leer oder enthält ein paar Beispiel-Einträge.
2. **Menü:** Der User kann aus mehreren Aktionen wählen:  
   - **Neues Wort hinzufügen** (z.B. deutsches Wort + englische Übersetzung)
   - **Bedeutung abfragen** (User gibt ein Wort ein, das Programm sucht die Übersetzung)
   - **Wort entfernen**
   - **Gesamte Liste anzeigen**
   - **Programm beenden**
3. **Fehler abfangen:**  
   - Rückmeldung, wenn Wörter nicht gefunden werden!
   - Keine Abstürze, auch bei „falschen“ Eingaben.
4. **Persistenz:** 
   - Speicher das Dictionary in einer .txt Datei ab
   - Überleg dir wie du es abspeicherst, damit du es leicht wieder auslesen kannst.
   - Beim Start soll die txt Datei geladen werden (sofern sie existiert!)
5. **Extratipp:**  
   - Speichere nicht nur einzelne Übersetzungen, sondern zum Beispiel Listen von Synonymen oder viele Bedeutungen pro Wort.
   - Optional: Baue das Dictionary zu einem kleinen Vokabeltrainer aus (zufällige Abfrage)!
> 💡 **Tipp:**  
> Nutze eine **while-Schleife** für das Menü.  
> Lass den User immer wieder entscheiden, was als Nächstes passieren soll.  
> Denk daran: Dictionaries sind perfekt, um schnellen Zugriff auf die Daten zu bekommen!

**Beispiel:**

<pre>
--- Mein Wörterbuch ---
1. Neues Wort hinzufügen
2. Übersetzung ansehen
3. Wort löschen
4. Alles anzeigen
5. Beenden
Aktion (1-5): <b>1</b>
Deutsches Wort: <b>Haus</b>
Englische Übersetzung: <b>house</b>
<b>"Haus" wurde gespeichert!</b>
</pre>



> Viel Spaß beim tüfteln – spiel ruhig mit verschiedenen Datenstrukturen herum und experimentiere, was noch alles mit Dictionaries geht!
