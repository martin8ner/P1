# Arbeiten in den P1 und P2 Praktika

## Ziele der P1 und P2 Praktika

Ziele der P1 und P2 Praktika sind es Ihnen, den Studierenden, die Möglichkeit zu bieten: 

- Experimente unter Laborbedingungen durchzuführen; 
- Daten mit naturwissenschaftlichem Anspruch zu erheben und weiter zu verarbeiten; 
- physikalische Gesetzmäßigkeiten am Experiment zu überprüfen.  

Sie werden feststellen, dass die durchzuführenden Experimente und die zu  untersuchenden Gesetzmäßigkeiten noch nicht in allen Fällen aus den Vorlesungen bekannt sein werden. Dies lässt sich aufgrund der Organisation des Praktikums, im Rotationsverfahren, nicht vermeiden. Bei einem so breiten Anwendungsgebiet, wie den Grundlagen der Physik, können Sie aber auch nicht davon ausgehen, immer auf bekannten Stoff zu stoßen. Es ist daher auch ein wichtiger Lehrinhalt der P1 und P2 Praktika, dass Sie sich darin üben sich neue Themen und Experimente der Physik *eigenständig* zu erschließen.  

### Durchführung eines Versuchs

Zur **Durchführung** eines Versuchs gehört es, *zielgerichtet* zu experimentieren und Messungen und Teilergebnisse in den Kontext des Experiments *einzuordnen*. Sie sollten also mit einer klaren Vorstellung darüber, was Sie im anstehenden Versuch erwartet, im Praktikum eintreffen und die physikalische Aufgabenstellung vollumfänglich verstanden haben. Dies wird durch die Vorbesprechung zum Versuch sichergestellt. 

### Erhebung der Daten

Zur **Erhebung der Daten** gehört die *systematische*, *reproduzierbare* Aufnahme von Messwerten einschließlich der Einschätzung der damit verbundenen wichtigsten Unsicherheiten. Grundsätzlich gilt in der Physik: **"Keine Messung ohne Einschätzung der damit verbundenen [wichtigsten] Unsicherheiten!"** 

### Das Protokoll

Ein zentraler Bestandteil der Datenerhebung ist das *gewissenhaft*, *vollständig* und *sachlich* geführte **Protokoll der Versuchsdurchführung**, das in die Auswertung des Experiments mündet. Das wissenschaftlich geführte Protokoll setzt voraus, das sich der Durchführende der einzelnen Schritte des Experiments bewusst ist und diese für sich und Außenstehende klar, verständlich und reproduzierbar dokumentiert. Das Protokoll erklärt, *wie* Sie zu einem Messergebnis gekommen sind. Sollte Ihnen bei der Durchführung des Experiments ein Fehler unterlaufen sein, sollte dies aus dem Protokoll nachträglich nachvollziehbar und ggf. in der Einschätzung der Ergebnisse durch Sie und Außenstehende zu berücksichtigen sein. 

Die gewissenhafte Erhebung und Dokumentation Ihrer Daten begründet im wahren Leben Ihren guten Ruf als Wissenschaftler:innen. Ein Fehler in der Durchführung eines Experiments kann zur Entwertung Ihrer Ergebnisse und/oder zur Neuauflage eines –dann verbesserten– Experiments führen. Das gehört bis zu einem gewissen Grad zum Prozess des wissenschaftlichen Erkenntnisgewinns. Mangelhafte *Dokumentation* und daher von außen nicht mehr nachvollziehbare Ergebnisse machen Ihr Experiment von vornherein *unwiederbringlich* unbrauchbar. 

In Zeiten vor der Digitalisierung wurden Protokolle z.B. in Form von Laborbüchern geführt. Für die P1 und P2 Praktika ersetzt das **Jupyter-notebook**, das Sie auf dem Jupyter-server der Fakultät anlegen können das Laborbuch. Sie sollten darin zielgerichtet und für sich und Außenstehende nachvollziehbar 

- die Ziele des Experiments; 
- die Bedingungen der Durchführung; 
- die Messwerte, einschließlich der Einschätzung der Unsicherheiten *aller* aufgezeichneten Daten; 
- die Weiterverarbeitung der Daten und daraus resultierende Teilergebnisse dokumentieren. 

Am Ende des Praktikumstages mündet das Protokoll in die Auswertung des Versuchs. Die Anleitung in Jupyter-notebook Format sollte Ihnen bei der Erstellung des Protokolls als Vorlage dienen können. Praktische Hinweise zur Arbeit mit dem Jupyter-notebook finden Sie im Abschnitt [Praktische Hinweise zu Durchführung und Auswertung](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/#praktische-hinweise-zu-durchf%C3%BChrung-und-auswertung) in diesem Dokument. 

### Begriffsklärung

#### Versuchsausgang

Niemand erwartet, dass Sie die von Ihnen durchgeführten Versuche bereits am ersten Tag des P1 perfekt dokumentieren können. Es ist einer der Lehrinhalte der P1 und P2 Praktika: Sie sollen anhand gut verstandener physikalischer Prozesse das Experimentieren und die wissenschaftlich-sachliche Einschätzung Ihres Experimentierens *erlernen*. Wir erwarten nicht, dass ein von Ihnen durchgeführtes Experiment zu "publizierbaren" Ergebnissen führt oder nach den Standards physikalischer Publikationen formatiert wurde. Insbesondere erwarten wir nicht, dass Sie mit Ihrem Ergebnis einen existierenden Literaturwert so exakt wie möglich reproduzieren.  

Mit anderen Worten: Die Aussage "Meine Messung stimmt innerhalb von 10% mit dem Literaturwert überein" ist im Allgemeinen für Ihre Messung *irrelevant*. Die Frage, die Sie mit Ihrem Versuch beantworten sollen ist: "Stimmt meine Messung innerhalb der von mir abgeschätzten Unsicherheiten mit meiner erwartung [dem Literaturwert] überein?". 

Dabei ist die adäquate *numerische* Einschätzung der Unsicherheiten der Messung mitunter wichtiger, als der ermittelte Zentralwert.   

#### Einschätzung des eigenen Experimentierens

Auf dem Jupyter-server der Fakultät stehen Ihnen alle nötigen Werkzeuge zur Anwendung von Methoden zur **statistischen Parameterschätzung**, wie sie von der Fakultät empfohlen werden, zur Verfügung. Dadurch sollte sich in vielen Fällen eine, oft nicht auf ihre Anwendbarkeit hin überprüfte "händische" Fehlerabschätzung durch Gaußsche Fehlerfortpflanzung erübrigen. Selbst, wenn Sie sich für die Anwendung Gaußscher Fehlerfortpflanzung entscheiden sollten müssen Sie dies nicht "händisch" mit Hilfe eines Taschenrechners oder einer Excel-Tabelle tun; Sie können eine einfache Funktion in Python-Code direkt in Ihr Versuchsprotokoll in Jupyter-notebook integrieren. Falls Ihnen dabei ein Fehler unterlaufen sollte, ist dies mit der Funktion, als Bestandteil des Protokolls nachvollziehbar und zu jeder Zeit korrigierbar. Der [Vorversuch Datenverarbeitung](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Vorversuch) des P1 bietet Ihnen die Möglichkeit Ihr Wissen und Ihre Erfahrung auf diesem Gebiet in Vorbereitung auf das P1 aufzufrischen und/oder zu vertiefen. 

Als Physiker:innen müssen Sie in die Situation hineinwachsen, dass Sie selbstverständlich die Unsicherheiten von Ihnen weiterverarbeiteter Daten bewusst abfragen und ggf. ein- oder abschätzen. Sie sollten *nach Möglichkeit* keinen Messwert oder Parameter ohne entsprechende *quantitative* Abschätzung seiner Unsicherheiten weiterverarbeiten. Die Einschätzung von Unsicherheiten gehört zu Ihrem Handwerk als Wissenschaftler:innen. In einer numerischen Parameterschätzung erhalten Sie *verlässliche* Konfidenzintervalle für die von Ihnen bestimmten Messgrößen aus der angewandten Anpassung (dem *fit*).

## Ein Praktikumstag im P1 oder P2

Ein Praktikumstag im P1 oder P2 verläuft von **13:00 – 19:00**. Wir gehen davon aus, dass Sie sich vor Versuchsantritt mit den grundlegenden Fragestellungen des aktuellen Versuchs vertraut gemacht haben, und dass Sie den Versuch der Vorwoche abgeschlossen und ausgewertet haben. Unter diesen Voraussetzung sollte Ihr Tag im P1 oder P2 wie folgt aussehen: 

### Nachbesprechung des vorangegangenen Versuchs

Von **13:00 – 13:30** besprechen Sie die Durchführung und Auswertung des vorangegangenen Versuchs *im Team* und *persönlich* bei dem/der entsprechenden Tutor:in. Dabei vertreten Sie vor dem/der Tutor:in Ihre Ergebnisse und klären, ob noch Änderungen an der Auswertung vorzunehmen sind. Sie können diese Besprechung, je nach Absprache mit dem/der Tutor:in auch schon vorher, zu jedem Zeitpunkt nach Abschluss Ihrer Auswertung durchführen. Wir wünschen uns jedoch, dass diese Besprechung *im Team* und *persönlich* erfolgt. Eine Besprechung online oder per E-Mail sollte die Ausnahme bilden. Sie finden den/die Tutor:in in den Räumlichkeiten des vorangegangen Versuchs. Dieser Teil entfällt bei der Durchführung des ersten Versuchs im Praktikum.

### Vorbesprechung des aktuellen Versuchs

Von **13:30 – 14:00** besprechen Sie Ziel und Durchführung Ihres aktuellen Versuchs mit dem/der entsprechenden Tutor:in. Im Rahmen dieser Vorbesprechung klären Sie ab, 

- ob Sie die physikalische Fragestellung oder den zu untersuchenden physikalischen Sachverhalt ausreichend verstanden haben; 
- ob Sie Ziel und Strategie zur Durchführung des Versuchs verstanden haben;  
- ob Sie die für die Versuchsdurchführung notwendigen Gerätschaften identifizieren und sachgerecht bedienen können. 

Diese Besprechung sollten Sie nicht als Prüfung verstehen. Natürlich wollen wir wissen, ob Sie wissen worum es in den nächsten 5,5 Stunden für Sie gehen soll. Sollte dies nicht der Fall sein, können Sie aus dem Versuchstag nichts lernen. Vorrangiges Ziel der Vorbesprechung ist es aber, Sie in die Position zu versetzen, dass Sie mit einer klaren Idee den Versuch weitestgehend *selbstständig* durchführen können. Bei anspruchsvollen Versuchen und gerade zu Beginn des P1 kann dies eine schwere Aufgabe sein. Sie haben nach der Vorbesprechung 3,5 Stunden Zeit, diese Aufgabe in Ihrem Sinne bestmöglich zu lösen. Der/Die Tutor:in ist dazu da, Ihnen dabei zu helfen. 

### Versuchsdurchführung

Von **14:00 – 17:30** haben Sie Zeit den aktuellen Versuch durchzuführen. Der/Die Tutor:in sollte über die gesamte Zeitspanne zur Beantwortung von Fragen zu Ihrer Verfügung stehen. Manche Versuchsaufbauten müssen aus Sicherheitsgründen vor Inbetriebnahme von dem/der Tutor:in abgenommen werden. Bemühen Sie sich den Versuch *als Team* so *selbstständig* wie möglich durchzuführen, aber stellen Sie gemeinsam mit dem/der Tutor:in sicher, dass Ihre Durchführung zielgerichtet ist und erzielte Zwischenergebnisse im Zusammenhang des gesamten Versuchs für Sie Sinn ergeben. Hierfür empfehlen wir Ihnen dringend Teilauswertungen in Jupyter-notebook durchzufüren. Versuchen Sie nach Ihren Möglichkeiten die Qualität der aufgenommenen Daten sicherzustellen. Falls Sie vor 17:30 mit der Durchführung der Versuchs fertig sein sollten, können Sie bereits mit der Auswertung beginnen. 

### Einführung in den nächsten Versuch durch Kommiliton:innen

Von **17:30 – 18:00** nutzen Sie die Zeit sich mit dem nächsten Versuch persönlich vertraut zu machen: Teilen Sie sich hierzu in zwei Gruppen A und B auf. Gruppe A verbleibt zunächst beim aktuellen Versuch. Gruppe B sucht den Raum des nächsten Versuchs auf und lässt sich von Gruppe A des dortigen Versuchs 15 min lang erklären, worum es bei diesem Versuch geht und wie er ablaufen wird. Gruppe A sollte nach 3,5 Stunden des Experimentierens in der Lage sein, den Kommiliton:innen aus Gruppe B erklären zu können, was sie im aktuellen Versuch gemacht haben. Der/Die entsprechende Tutor:in unterstützt Sie dabei gegebenenfalls. Nach 15 min kehrt Gruppe B zu ihrem aktuellen Versuch zurück und die Gruppen A und B tauschen ihre Rollen. 

### Abschluss des aktuellen Versuchs

Von **18:00 – 19:00** haben Sie die Möglichkeit verbleibende Messungen des aktuellen Versuchs abzuschließen. Sie führen damit Ihr Protokoll zu einem wohldefinierten Abschluss. Der Praktikumstag endet aus organisatorischen Gründen pünktlich um 19:00, selbst, wenn Sie den Versuch noch nicht vollständig durchgeführt haben sollten. Geben Sie in einem solchen Fall in Ihrem Protokoll an, woran es lag, dass Sie nicht rechtzeitig fertig geworden sind. Sprechen Sie Ihre Messungen und Zwischenergebnisse nochmal abschließend mit dem/der Tutor:in durch, bevor Sie gehen. 

### Auswertung 

Die Auswertung des Versuchs erfolgt auf Grundlage Ihres Protokolls vorzugsweise in Jupyter-notebook. Zu Ihrer Orientierung bzgl. des Umfangs gehen Sie davon aus, dass Sie **nicht mehr als 2 Stunden** für die verbleibende Auswertung des aktuellen Versuchs benötigen sollten. Beachten Sie, dass das vorrangige Ziel der Auswertung ist, Ihre Messung und die erzielten Ergebnisse mit einer sinnvollen persönlichen Einschätzung einschließlich entsprechender *quantifizierter* Unsicherheiten für Sie und Außenstehende verständlich zu dokumentieren. Ihr Protokoll und die entsprechende Auswertung sollten *übersichtlich*, *nachvollziehbar* und *vollständig* sein. Wir verlangen explizit **keine** Formatierung in Latex. 

Die Abgabe erfolgt über das Hochladen, sowohl des Jupyter-notebooks als auch einer *pdf*-Version des Jupyter-notebooks ins ILIAS-System.    

## Einordnung des Praktikums und ECTS-Regelung

Das P1 und P2 entsprechen in der Bewertung des damit verbundenen Arbeitsaufwands jeweils **6 ECTS-Punkten**. Es handelt sich dabei um rund 1/5 Ihrer Arbeit für das Physikstudium im jeweils laufenden Semester. Diese Leistung erbringen Sie konzentriert auf 10 Wochen des Semesters. Sie sollten diese Zeit für die Praktika bei der Gestaltung Ihres Semesterplans dringend einplanen. 

Die Praktika der Physik bieten Ihnen die Möglichkeit zu Experimentieren, physikalische Gesetzmäßigkeiten experimentell nachzuvollziehen, physikalische Sachverhalte, die aus einer Vorlesung nicht immer intuitiv und klar sind, am Experiment nachzuvollziehen und sich in der Aufzeichnung und Weiterverarbeitung von Messdaten mit wissenschaftlichem Anspruch auszubilden. Dies ist ein essentieller Bestandteil jedes Physikstudiums und damit Ihrer Ausbildung zum wissenschaftlichen Arbeiten. 

Bei der Berechnung der ECTS-Punkte für die Praktika legen wir das folgende Modell zugrunde: 

- **4–6 Stunden Versuchsvorbereitung**, in denen Sie sicher stellen, dass Sie nach Ihrer eigenen Einschätzung optimal auf den nächsten Versuch vorbereitet sind.
- **6 Stunden Versuchsdurchführung**.
- **2–4 Stunden Versuchsnachbereitung** (inklusive potentieller Neueinreichungen nach der Nachbesprechung mit dem/der Tutor:in).      

Damit ergeben sich bis zu **160 Stunden** Arbeitsaufwand im laufenden Semester. 

Beachten Sie bei der Beurteilung des Arbeitsaufwands, dass die Praktika aus studienorganisatorischen Gründen, bereits nach 10 Wochen und somit  deutlich vor dem offiziellen Ende der Vorlesungszeit des Semesters enden. Dies räumt Ihnen die Möglichkeit ein sich gegen Ende der Vorlesungszeit angemessen auf anstehende Abschlussprüfungen vorzubereiten. Der Preis hierfür ist, dass sich der Arbeitsaufwand während des laufenden Praktiums entsprechend erhöht.

## Praktische Hinweise zu Durchführung und Auswertung

### Anleitungen zum Versuch

Die jeweils aktuelle Version aller Versuchsanleitungen und die dazugehörigen Daten finden Sie auf dem gitlab-Server des SCC unter den Webadressen: 

* [https://git.scc.kit.edu/etp-lehre/p1-for-students](https://git.scc.kit.edu/etp-lehre/p1-for-students). 

* [https://git.scc.kit.edu/etp-lehre/p2-for-students](https://git.scc.kit.edu/etp-lehre/p2-for-students). 

Wie Sie die Anleitungen vom gitlab-Server des SCC auf Ihre Arbeitsumgebung auf dem Jupyter-server herunterladen und bearbeiten können erfahren Sie aus dem Dokument [Arbeiten auf dem Jupyter-server](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Jupyter-server.md).  

Zur Durchführung und Auswertung des Versuchs können Sie entweder ein neues Jupyter-notebook starten, oder Sie öffnen die Anleitung als Jupyter-notebook per Doppelklick in Ihrer Jupyter-Umgebung. 

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
