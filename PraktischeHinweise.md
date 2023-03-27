# Praktische Hinweise zur Durchführung und Auswertung der Versuche

## Versuchsanleitung

Die jeweils aktuelle Version aller Versuchsanleitungen und die dazugehörigen Daten finden Sie auf dem gitlab-Server des SCC unter den folgenden Webadressen: 

* **Für das P1**: [https://git.scc.kit.edu/etp-lehre/p1-for-students](https://git.scc.kit.edu/etp-lehre/p1-for-students). 

* **Für das P2**: [https://git.scc.kit.edu/etp-lehre/p2-for-students](https://git.scc.kit.edu/etp-lehre/p2-for-students). 

Wie Sie die Anleitungen vom gitlab-Server des SCC auf Ihre Arbeitsumgebung auf dem Jupyter-server herunterladen und bearbeiten können erfahren Sie aus dem Dokument [Arbeiten auf dem Jupyter-server](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Jupyter-server.md).  

Zur Durchführung und Auswertung des Versuchs können Sie entweder ein neues Jupyter-notebook anlegen, oder Sie öffnen die Anleitung als Jupyter-notebook per Doppelklick in Ihrer Jupyter-Umgebung. 

Im letzteren Fall verwenden Sie einfach die Zellen, mit den Überschriften **"Lösung"**. Sie können den *kursiv*-gestellten Text aus den Zellen löschen. 

Vergessen Sie nicht das Jupyter-notebook bevor Sie den Kontakt zum Server schließen (z.B. mit *Strg+s*) zu speichern. Andernfalls wäre Ihre Arbeit verloren.

## Verarbeitung der aufgenommenen Daten

Wir gehen davon aus, dass Sie in der Regel zu allen aufgenommenen Daten oder angenommenen Parametern entsprechende Unsicherheiten angeben. Falls dies einmal nicht notwendig sein sollte, weisen wir Sie in der entsprechenden Anleitung ausdrücklich darauf hin. Die Abschätzung und Fortpflanzung von Unsicherheiten sollte heutzutage keine Herausforderung mehr für Sie darstellen. Wir verlangen daher **zu jedem von Ihnen berechneten Ergebnis die Abschätzung der entsprechenden Unsicherheiten**. Hierzu stehen Ihnen mehrere Möglichkeiten zur Verfügung:

### kafe2

Wir gehen davon aus, dass Studierende im Hauptfach Physik mit dem Programmpaket [kafe2](https://etpwww.etp.kit.edu/~quast/kafe2/htmldoc/) zur Datenauswertung vertraut sind. Auf dem Jupyter-server finden Sie die aktuelle Version des Programmpakets vorinstalliert, dessen Module Sie problemlos mit dem Python-Schlüsselwort `import` in jede Code-Zelle des Jupyter-notebooks importieren können. Eine kurze Einführung finden Sie im Dokument [Verwendung des Programmpakets kafe2](to be filled). 

### PhyPraKit

Für diejenigen unter Ihnen, die [kafe2](https://etpwww.etp.kit.edu/~quast/kafe2/htmldoc/) nicht kennen, oder sich im Umgang damit nicht sicher fühlen, stellt die Fakultät die Modulsammlung [PhyPraKit](https://etpwww.etp.kit.edu/~quast/PhyPraKit/htmldoc/) bereit, aus der Sie voraussichtlich lediglich die Skripte *run_phyFit.py* (zur Parameterschätzung) und ggf. *plotData.py* (für die Darstellung von Datenreihen) benötigen werden. Beide Skripte können Sie mit einer verhältnismäßig einfachen Konfigurationsdatei ansteuern. Die Verwendung dieser beiden Skripte und der zugehörigen Konfigurationsdatei erklären wir Ihnen im Dokument [Verwendung der PhyPraKit Module](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/PhyPraKit.md). 

### Fehlerfortpflanzung in Python

Die Softwarepakte *kafe2* und *PhyPraKit* schließen die Verwendung Gausßscher Fehlerfortpflanzung nicht aus. Diese müssen Sie jedoch nicht mehr mühsam mit dem Taschenrechner oder aus einer Excel-Tabelle extrahieren. Es empfiehlt sich eine geeignete Python-Funktion direkt in einer Code-Zelle Ihres Jupyter-notebook Protokolls zu integrieren. Damit lässt sich die Fehlerfortpflanzung auf beliebig viele Messwerte und Parameter skalieren und es ist für Sie und Ihre:n Tutor:in deutlich transparenter eventuelle Fehler oder unzulässige Annahmen bei der Fehlerfortpflanzung zu erkennen, einzuschätzen und ggf. zu korrigieren.  

### Alternative Methoden

Falls Sie alternative Methoden (wie Excel oder Origin) zur Datenauswertung verwenden möchten stellen Sie im Laufe jedes ersten Versuchs im P1 oder P2 sicher, dass die von Ihnen bestimmten Ergebnisse und entsprechenden Unsicherheiten den Anforderungen der Fakultät entsprechen. Bei Problemen können wir Ihnen für die Verwendung alternativer Methoden zur Datenauswertung **leider nur minimale Unterstützung** anbieten. Wir werden aber versuchen Ihnen bei Problemen behilflich zu sein.  

## Versuchsauswertung

### Anspruch

Für uns steht das Experimentieren und die inhaltlich konsistente und vollständige Dokumentation des Versuchsablaufs im Vordergrund! Es ist uns wichtig, dass Sie

- den Versuch verstanden und in der vorgegebenen Zeit zielgerichtet durchgeführt haben;
- die zur Verfügung gestellten Apparaturen richtig eingesetzt und ausgelesen haben; 
- sich ein Bild über die mit den aufgenommenen Daten verbundenen Unsicherheiten gemacht haben; 
- alle Daten und Parameter zur Berechnung der (Teil-)Ergebnisse, einschließlich ihrer Unsicherheiten im Protokoll nachvollziehbar dokumentiert haben. 

Wir gehen davon aus, dass das Protokoll, als Jupyter-notebook, während der Versuchsdurchführung entsteht. Hierzu empfehlen wir die Anleitung im Jupyter-notebook-Format als Vorlage zu verwenden. 

Das Protokoll geht durch die folgenden letzten Schritte in die einzureichende Auswertung über: 

- Abschließende Kontrolle und ggf. Aufbereitung aller (Teil-)Ergebnisse. Bringen Sie dabei das Protokoll in eine allgemein verständliche und lesbare Form.
-  Reflexion und Diskussion des Versuchsablaufs und der erzielten Ergebnisse. 

Eine strukturierte und organisierte Vorgehensweise bei der Protokollführung, ebenso wie ein sehr gutes, grundlegendes Verständnis für alle den Versuch betreffenden physikalischen Zusammenhänge sind Grundvoraussetzungen, um diese Anforderungen erfüllen zu können.

Wir wünschen im Protokoll jedoch ausdrücklich **keine langen Herleitungen** physikalischer Zusammenhänge, die ohnehin aus der Literatur entnehmbar sind. Wir wünschen auch **keine Formatierung in Latex**, die über den in Markdown verwendbaren Satz physikalischer Formeln hinausgeht. Beides ist Ihnen freigestellt. Es geht jedoch weder in die Bewertung der eingereichten Auswertungen noch in das von uns veranschlagte Zeitbudget für den Arbeitsaufwand für die erfolgreiche Teilnahme an den P1 und P2 Praktika ein.

### Bevorzugtes Dokumentenformat

Wir erwarten die Rückgabe der Versuchsauswertungen durch *fristgerechten upload* auf das ILIAS-System in den folgenden Formaten:

- **Jupyter-notebook exportiert nach *pdf***: in dieses Dokument kann Ihr:e Tutor:in elektronisch kommentieren.
- **Jupyter-notebook** (original). Achten Sie dabei ggf. darauf, dass Sie das vollständige Jupyter-notebook einschließlich aller eingebundenen Abbildungen hochladen.

Ausnahmen von dieser Regel sind zulässig. Beachten Sie jedoch, dass Sie in jedem Fall eine Version Ihres Protokolls in *pdf*-Format auf dem ILIAS-System hinterlegen müssen, damit Ihr Versuch die Chance hat anerkannt zu werden. 

Um Jupyter-notebook nach *pdf* zu formatieren empfehlen sich derzeit die folgenden Schritte: 

- Exportieren Sie das Jupyter-notebook ins *html*-Format. 
- Laden Sie sich hierzu gegebenenfalls die Bilder, die in das Jupyter-notebook eingebunden werden sollen, vom Jupyter-server auf Ihren lokalen Rechner. Die einzubindenden Bilddateien sollten sich dann im gleichen Verzeichnis, wie die exportierte *html*-Datei befinden.
- Sie können die *html*-Datei dann von Ihrem Browser aus z.B. nach *pdf* formatieren. Wenn das *pdf*-Format die Seiten nicht einwandfrei umbricht, ist das für uns *kein Problem*.   

### Bewertung

Ihr:e Tutor:in wird die von Ihnen eingereichte Versuchsauswertung im *pdf*-Format durchsehen und entsprechend kommentieren. Wir sehen dabei die folgenden Kategorien von Kommentaren vor: 

- **Beanstandungen**: Hierbei handelt es sich z.B. um inhaltliche Fehler; Unzulänglichkeiten, die Ihr Protokoll/Ihre Auswertung nicht nachvollziehbar oder unverständlich machen; nicht gekennzeichnete oder näher dokumentierte fehlende Aufgabenteile oder; fehlende Einschätzungen oder Unsicherheiten der (Teil-)Ergebnisse. Dabei geht es uns v.a. um inhaltliche Beanstandungen, die von substantieller Natur für das Verständnis des Versuchs und die sachliche Einschätzung Ihrer Arbeit und Ihrer Ergebnisse sind. Beachten Sie, dass es für uns in erster Linie unerheblich ist, wie genau oder ungenau Sie mit Ihrer Messung eine gegebene Erwartung getroffen haben. Wichtig ist die Einschätzung innerhalb der von Ihnen während des Versuchs eingeschätzten Unsicherheiten. Selbst wenn Sie im Rahmen dieser Unsicherheiten, nach Ihrem Dafürhalten, mit Ihrem Ergebnis "weit von Ihrer Erwartung abweichen" sollten kann dies für uns immer noch in Ordnung sein kann, wenn Sie Ihre Messung ernsthaft und sorgfältig auf den Prüfstand stellen, reflektieren und diskutieren.   
- **Anmerkungen**: Hierbei handelt es sich um alle weiteren Kommentare zu Ihrer Auswertung. Sie sollten den Anspruch haben eine semantisch, grammatikalisch und orthographisch einwandfreie Auswertung abzugeben. Ihre physikalische Argumentation sollte, nach Einschätzung Ihre:r Tutor:in korrekt sein. Vielleicht ist Ihr:e Tutor:in geneigt Ihnen den ein oder anderen Tipp an die Hand zu geben, wie Sie Ihre Messung oder Auswertung besser noch hätten durchführen können.  

**Beanstandungen sollten Sie auf jeden Fall korrigieren** und die korrigierte Auswertung (als Version $\mathrm{v2}$) erneut auf das ILIAS-System hochladen. Wir empfehlen Ihnen dabei auch auf die Anmerkungen Ihr:er Tutor:in einzugehen. 

Die Bewertung der Auswertung erfolgt **spätestens 14 reguläre Studientage (d.h. während des laufenden Betriebs zwei Versuchstage) nach Versuchsdurchführung**, per Eintrag ins Praktikumsbuch, wie folgt:

- **-**: Auswertung mit Beanstandungen.
- **0**: Auswertung ohne Beanstandung.
- **+**: Bemerkenswert gute Auswertung ohne Beanstandungen. 

Anmerkungen gehen im Allgemeinen nicht und wenn doch, dann nur in groben Fällen und nach Rücksprache des/der Tutor:in mit den Dozenten des Praktikums, in die Bewertung der Auswertung ein. Die Bewertung soll den gesamten Versuch von der Durchführung bis zur Auswertung wiedergeben. Deshalb ist es notwendig, dass Ihr:e Tutor:in zeitnah nach Abschluss der Versuchsdurchführung zu einer Beurteilung des Versuchs gelangen kann. 

### Zeitlicher Ablauf

Für die Rückgabe der Auswertung sehen wir den folgenden zeitlichen Ablauf vor: 

- $T_{0}$: Am Ende jedes Versuchstags besprechen Sie Ihre Ergebnisse mit Ihr:er Tutor:in und laden Ihr Protokoll als Version $\mathrm{v0}$ ins ILIAS-System hoch. Dieser Vorgang gilt gleichzeitig als Nachweis dafür, dass Sie den Versuch durchgeführt haben. Sie haben von diesem Zeiptunk an **7 reguläre Studientage (d.h. während des laufenden Betriebs bis zum nächsten Versuchstag) Zeit** Ihr Protokoll zur Abgabe aufzubereiten, über den Versuchsablauf zu reflektieren und die erzielten Ergebnisse abschließend zu diskutieren. Wenn Sie denken, dass Ihre Versuchsauswertung zur Abgabe bereit ist können Sie sie jederzeit als Version $\mathrm{v1}$ und auf das ILIAS-System hochladen und Ihre:n Tutor:in mit der Bitte um einen Termin zur Nachbesprechung kontaktieren. Die im ILIAS-System hinterlegte Version $\mathrm{v1}$ Ihres Protokolls gilt als Ihre Versuchsauswertung. Falls Ihr:e Tutor:in bereits vor Ablauf dieser Frist Beanstandungen zu Ihrer Auswertung anzeigen sollte können Sie diese beliebig oft überarbeiten und erneut (als Version $\mathrm{v1}$) auf das ILIAS-System hochladen.   
- $T_{1}$: Spätestens am nächsten Versuchstag (d.h. 7 reguläre Studientage nach Versuchsdurchführung) sollten Sie die Version $\mathrm{v1}$ Ihres Protokolls als Versuchsauswertung auf das ILIAS-System hochgeladen haben. Gibt es zu diesem Zeitpunkt keine Beanstandungen zu Ihrer Versuchsauswertung gilt die Auswertung als testiert mit dem Vermerk "**0**" oder "**+**". Liegen noch Beanstandungen vor haben Sie weitere **7 reguläre Studientage (d.h. während des laufenden Betriebs wiederum bis zum nächsten Versuchstag) Zeit** diese in Absprache mit Ihr:er Tutor:in zu beheben. Laden Sie innerhalb dieser Frist die entsprechend korrigierte Version Ihrer Auswertung als Version $\mathrm{v2}$ auf das ILIAS-System hoch. Wie zuvor können Sie dies zu jedem Zeitpunkt innerhalb dieser Zeitspanne tun, sich entsprechendes Feedback Ihre:r Tutor:in einholen, Ihre Auswertung beliebig oft überarbeiten und erneut (als Version $\mathrm{v2}$) auf das ILIAS-System hochladen.  
- $T_{2}$: Am wiederum nächsten Versuchstag (d.h. 14 reguläre Studientage nach Versuchsdurchführung) wird Ihre Auswertung, wie Sie im ILIAS-System hinterlegt ist, ohne weiteren Hinweis testiert. Liegen zu diesem Zeitpunkt noch Beanstandungen vor wird dies im Praktikumsbuch mit einem "**-**" vermerkt.    

Nach Ablauf des Praktikums müssen Sie **für jeden Versuch eine Auswertung** (d.h. ein Protokoll in der Version $\mathrm{v1}$) auf dem ILIAS-System hinterlegt haben. Ansonsten gilt der Versuch als "nicht durchgeführt" und muss ggf. nochmal von Ihnen durchgeführt werden. Dies liegt im Ermessen der Dozenten des Praktikums. 

Weiterhin dürfen Sie sich nach Ablauf des Praktikums **nicht mehr als zwei Auswertung mit dem Vermerk "**-**" im Praktikumsbuch** leisten. Je nach Beanstandung müssen Sie die Auswertungen entsprechend überarbeiten oder entsprechende Versuche während der Nachholtermine nach Ablauf des Praktikums erneut Durchführen. Auch dies liegt im Ermessen der Dozenten des Praktikums.  

## Bewertung des Praktikums

Wir weisen ausdrücklich darauf hin, dass das P1 und P2 **nur als bestanden gewertet** wird. Eine Bewertung darüber hinaus wird nicht erteilt. 

Das die von Ihnen durchgeführten Versuche mit dem Vermerk "**0**" bewertet werden stellt die Regel dar. Es ist für das Bestehen der Kurse *irrelevant*, wie viele der von Ihnen durchgeführten Versuche mit einem "**+**" bewertet wurden. Es handelt sich dabei um ein rein internes Beurteilungssystem der P1 und P2 Praktika und um entsprechendes positives Feedback für Sie. 

Da Sie die Versuche i.a. zu zweit durchführen ist eine faire Beurteilung einzelner Personen auf Grundlage der getroffenen Vermerke im Praktikumsbuch nicht möglich. 

In seltenen Fällen kommt es vor, dass Stipendiaten Beurteilungen ihrer Leistungen zum Nachweis bei den entsprechenden Stiftungen benötigen. Eine solche Beurteilung erfolgt dann persönlich durch einen Dozenten des Praktikums, der Sie während des Praktiumsverlaufs begleitet und/oder Sie noch einmal zu einem Gespräch einlädt. Melden Sie einen solchen Fall unbedingt **vor Beginn des Praktikums** beim entsprechenden Dozenten an. Im Nachhinein kann eine solche Beurteilung nicht mehr vorgenommen werden.

