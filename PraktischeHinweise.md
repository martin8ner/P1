## Praktische Hinweise zu Durchführung und Auswertung

### Anleitungen zum Versuch

Die jeweils aktuelle Version aller Versuchsanleitungen und die dazugehörigen Daten finden Sie auf dem gitlab-Server des SCC unter den Webadressen: 

* [https://git.scc.kit.edu/etp-lehre/p1-for-students](https://git.scc.kit.edu/etp-lehre/p1-for-students). 

* [https://git.scc.kit.edu/etp-lehre/p2-for-students](https://git.scc.kit.edu/etp-lehre/p2-for-students). 

Wie Sie die Anleitungen vom gitlab-Server des SCC auf Ihre Arbeitsumgebung auf dem Jupyter-server herunterladen und bearbeiten können erfahren Sie aus dem Dokument [Arbeiten auf dem Jupyter-server](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Jupyter-server.md).  

Zur Durchführung und Auswertung des Versuchs können Sie entweder ein neues Jupyter-notebook anlegen, oder Sie öffnen die Anleitung als Jupyter-notebook per Doppelklick in Ihrer Jupyter-Umgebung. 

Im letzteren Fall verwenden Sie einfach die Zellen, mit den Überschriften **"Lösung"**. Sie können den *kursiv*-gestellten Text aus den Zellen löschen. 

Vergessen Sie nicht das Jupyter-notebook bevor Sie den Kontakt zum Server schließen (z.B. mit *Strg+s*) zu speichern. Andernfalls wäre Ihre Arbeit verloren.

### Verarbeitung der aufgenommenen Daten

Wir gehen davon aus, dass Sie in der Regel zu allen aufgenommenen Daten entsprechende Unsicherheiten angeben. Falls dies einmal nicht notwendig sein sollte, weisen wir Sie in der entsprechenden Anleitung explizit darauf hin. Die Abschätzung und Fortpflanzung von Unsicherheiten sollte heutzutage keine Herausforderung mehr für Sie darstellen. Wir verlangen daher zu **jedem** von Ihnen berechneten Ergebnis eine entsprechende Fehlerabschätzung. Hierzu stehen Ihnen mehrere Möglichkeiten zur Verfügung:

#### kafe2

Wir gehen davon aus, dass Studierende mit dem Hauptfach Physik mit dem Programmpaket [kafe2](https://etpwww.etp.kit.edu/~quast/kafe2/htmldoc/) zur Datenauswertung vertraut sind. Auf dem Jupyter-server finden Sie die aktuelle Version des Programmpakets vorinstalliert, dessen Module Sie problemlos mit dem Python-Schlüsselwort `import` in jede Code-Zelle des Jupyter-notebooks importieren können. Eine kurze Einführung finden Sie in der Beschriebung [Verwendung des Programm-Pakets kafe2](to be filled). 

#### PhyPraKit

Für diejenigen unter Ihnen, die [kafe2](https://etpwww.etp.kit.edu/~quast/kafe2/htmldoc/) nicht kennen, oder sich im Umgang damit nicht sicher fühlen, stellt die Fakultät die Modulsammlung [PhyPraKit](https://etpwww.etp.kit.edu/~quast/PhyPraKit/htmldoc/) bereit, aus der Sie voraussichtlich lediglich die Skripte *run_phyFit.py* und ggf. *plotData.py* benötigen werden. Beide Skripte können Sie mit einer verhältnismäßig einfachen Konfigurationsdatei ansteuern. Die Verwendung dieser beiden Skripte und der zugehörigen Konfigurationsdatei erklären wir Ihnen im Dokument [Verwendung der PhyPraKit Module](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/PhyPraKit.md). 

#### Alternative Methoden

Falls Sie alternative Methoden zur Datenauswertung verwenden möchten stellen Sie im Laufe jedes ersten Versuchs im P1 oder P2 sicher, dass die von Ihnen bestimmten Ergebnisse und entsprechenden Unsicherheiten den geforderten Standards der Fakultät entsprechen. Bei Problemen können wir Ihnen für die Verwendung alternativer Methoden zur Datenauswertung leider nur minimale Unterstützung anbieten. Wir werden aber versuchen Ihnen bei Problemen behilflich zu sein.  

### Abgabe des Protokolls

Sie können die fertige Auswertung zur Abgabe ins *pdf*-Format formatieren. Hierzu empfehlen sich derzeit die folgenden Schritte: 

- Exportieren Sie das Jupyter-notebook nach *html*. 
- Laden Sie sich hierzu gegebenenfalls die Bilder, die in das Jupyter-notebook eingebunden werden sollen, vom Jupyter-server auf Ihren lokalen Rechner. Die einzubinden Bilddateien sollten sich dann im gleichen Verzeichnis, wie die exportierte *html*-Datei befinden.
- Sie können die *html*-Datei dann von Ihrem Browser aus z.B. nach *pdf* formatieren. Wenn das *pdf*-Format die Seiten nicht ganz einwandfrei umbricht, ist das für uns *kein Problem*. 
- Laden Sie zur Abgabe sowohl das vollständige Jupyter-notebook (einschließlich der eingebundenen Abbildungen), als auch die entsprechende *pdf*-Version des Jupyter-notebooks auf ILIAS hoch.  

Beachten Sie, dass **das für uns maßgebliche Protokoll** das Jupyter-notebook ist. Die *pdf*-Datei dient lediglich als Dokument in das der/die Tutor:in Kommentare einfügen kann. 

Für uns steht das Experimentieren und die inhaltlich konsistente und vollständige Dokumentation des Versuchsablaufs im Vordergrund! Es ist uns wichtig, dass die Studenten

- den Versuch verstanden und in der vorgegebenen Zeit zielgerichtet durchgeführt haben;
- die zur Verfügung gestellten Apparaturen richtig eingesetzt und ausgelesen haben; 
- sich ein Bild über die mit den aufgenommenen Daten verbundenen Unsicherheiten gemacht haben; 
- alle Daten und Parameter zur Berechnung der (Teil-)Ergebnisse, einschließlich ihrer Unsicherheiten im Protokoll dokumentiert haben. 

Wir gehen davon aus, dass das Protokoll, als Jupyter-notebook, während der Versuchsdurchführung entsteht. Hierzu empfehlen wir die Anleitung/Aufgabenstellung in Jupyter-notebook Format, wie sie für jeden Versuch auf dem gitlab-Server des SCC hinterlet ist als Vorlage zu verwenden. 

Das Protokoll geht durch die folgenden letzten Schritte in die einzureichende Auswertung über: 

- Abschließende Kontrolle und ggf. Aufbereitung aller (Teil-)Ergebnisse. 
-  Reflexion und Diskussion des Versuchsablaufs und der erzielten Ergebnisse. 

Eine strukturierte und organisierte Vorgehensweise bei der Protokollführung, ebenso wie ein sehr gutes, grundlegendes Verständnis für alle den Versuch betreffenden physikalischen Zusammenhänge sind Grundvoraussetzungen, um diese Anforderungen erfüllen zu können.

Wir wünschen im Protokoll jedoch explizit **keine langen Herleitungen** physikalischer Zusammenhänge, die ohnehin aus der Literatur entnehmbar sind. Wir wünschen auch **keine Formatierung in Latex**, die über den in Markdown verwendbaren Satz physikalischer Formeln hinausgeht. Beides ist den Studenten freigestellt. Es geht jedoch weder in die Bewertung der eingereichten Auswertungen noch in das von uns veranschlagte Zeitbudget für die Teilnahme an den P1 und P2 Praktika ein.





Abgabeprozedur und Korrekturen

Bewertung des Versuchs und bewertung des Praktikums