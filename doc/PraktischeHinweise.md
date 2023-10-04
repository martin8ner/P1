# Praktische Hinweise zur Durchführung und Auswertung der Versuche

## Versuchsanleitung und Durchführung

Die jeweils aktuelle Version aller Versuchsanleitungen und die dazugehörigen Daten finden Sie auf dem gitlab-Server des SCC unter den folgenden Webadressen: 

* **Für das P1**: [https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main). 

* **Für das P2**: [https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students. 

Zu jedem Versuch erhalten Sie eine grundlegende Vorstellung des Versuchs, Hinweise zur physikalischen Einordnung, mit denen Sie den entsprechenden Versuch durchführen können und einen Durchführungsteil im Jupyter-notebook-Format. Wie Sie die Anleitungen vom gitlab-Server des SCC auf Ihre Arbeitsumgebung auf dem Jupyter-Server herunterladen und bearbeiten können erfahren Sie aus dem Dokument [Arbeiten auf dem Jupyter-Server](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/doc/JupyterServer.md).  

Zur Durchführung und Auswertung des Versuchs öffnen Sie die Durchführung (mit dem Titel des Versuchs und der Endung **.ipynb*) als Jupyter-notebook per Doppelklick in Ihrer Arbeitsumgebung auf dem Jupyter-Server. 

Verwenden Sie die Zellen, mit den Überschriften **"Lösung"**. Sie können den *kursiv*-gestellten Text aus den Zellen löschen. Als Anhalt, sollten Sie i.a. 

- eine Markdown-Zelle verwenden, in der Sie kurz beschreiben, was Sie als nächstes vorhaben und entsprechend aufgenommene Daten in Textform dokumentieren; 
- gefolgt von einer Code-Zelle, in der Sie die Daten geeignet darstellen oder weiterverarbeiten, um ein physikalisch relevantes Ergebnis zu produzieren; 
- gefolgt von einer Markdown-Zelle, in der Sie das erzielte Ergebnis, wieder in Textform, dokumentieren und entsprechend diskutieren. 

Vergessen Sie nicht das Jupyter-notebook bevor Sie den Kontakt zum Server schließen (z.B. mit *Strg+s*) zu speichern. Andernfalls wäre Ihre Arbeit verloren.

## Verarbeitung der aufgenommenen Daten

Wir gehen davon aus, dass Sie in der Regel zu allen aufgenommenen Daten oder angenommenen Parametern entsprechende Unsicherheiten angeben. Falls dies einmal nicht notwendig sein sollte, weisen wir Sie in der entsprechenden Anleitung ausdrücklich darauf hin. Falls es eine Quelle gibt, aus der Sie diese Unsicherheiten beziehen können, zitieren Sie diese. Falls nicht, schätzen Sie entsprechende Unsicherheiten nach bestem Wissen und Gewissen selbst ab. Die Abschätzung und Fortpflanzung von Unsicherheiten sollte heutzutage keine Herausforderung mehr für Sie darstellen. Wir verlangen daher **zu jedem von Ihnen berechneten Ergebnis die Abschätzung der entsprechenden Unsicherheiten**. Hierzu stehen Ihnen mehrere Möglichkeiten zur Verfügung:

### kafe2

Wir gehen davon aus, dass Studierende im Hauptfach Physik mit dem Programmpaket [kafe2](https://etpwww.etp.kit.edu/~quast/kafe2/htmldoc/) zur Datenauswertung vertraut sind. Auf dem Jupyter-Server finden Sie die aktuelle Version des Programmpakets vorinstalliert, dessen Module Sie problemlos mit dem Python-Schlüsselwort `import` in jede Code-Zelle des Jupyter-notebooks importieren können. Eine knappe Einführung finden Sie im Dokument [Verwendung des Programmpakets kafe2](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/doc/kafe2.md). 

### PhyPraKit

Für diejenigen unter Ihnen, die [kafe2](https://etpwww.etp.kit.edu/~quast/kafe2/htmldoc/) nicht kennen, oder sich im Umgang damit nicht sicher fühlen, stellt die Fakultät die Modulsammlung [PhyPraKit](https://etpwww.etp.kit.edu/~quast/PhyPraKit/htmldoc/) bereit, aus der Sie voraussichtlich lediglich die Skripte *run_phyFit.py* (zur Parameterschätzung) und ggf. *plotData.py* (für die Darstellung von Datenreihen) benötigen werden. Beide Skripte können Sie mit einer verhältnismäßig einfachen Konfigurationsdatei ansteuern. Die Verwendung dieser beiden Skripte und der zugehörigen Konfigurationsdatei erklären wir Ihnen im Dokument [Verwendung der PhyPraKit Module](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/doc/PhyPraKit.md?ref_type=heads). 

### Fehlerfortpflanzung in Python

Die Softwarepakte kafe2 und PhyPraKit schließen die Verwendung Gaußscher Fehlerfortpflanzung nicht aus. Diese müssen Sie jedoch nicht mehr mühsam mit dem Taschenrechner oder aus einer Excel-Tabelle extrahieren. Es empfiehlt sich eine geeignete Python-Funktion direkt in eine Code-Zelle Ihres Jupyter-notebook Protokolls zu integrieren. Damit lässt sich die Fehlerfortpflanzung auf beliebig viele Messwerte und Parameter skalieren und es ist für Sie und Ihre:n Tutor:in deutlich transparenter eventuelle Fehler oder unzulässige Annahmen bei der Fehlerfortpflanzung zu erkennen, einzuschätzen und ggf. zu korrigieren.  

### Alternative Methoden

Falls Sie alternative Methoden (wie Excel oder Origin) zur Datenauswertung verwenden möchten stellen Sie im Laufe jedes ersten Versuchs im P1- oder P2-Praktikum sicher, dass die von Ihnen bestimmten Ergebnisse und entsprechenden Unsicherheiten den Anforderungen der Fakultät entsprechen. Bei Problemen können wir Ihnen für die Verwendung alternativer Methoden zur Datenauswertung **leider nur minimale Unterstützung** anbieten. Wir werden aber versuchen Ihnen bei Problemen behilflich zu sein.  

## Versuchsauswertung

### Anspruch

Für uns steht das **Experimentieren und die inhaltlich konsistente und vollständige Dokumentation des Versuchsablaufs im Vordergrund!** Es ist uns wichtig, dass Sie

- den Versuch verstanden und in der vorgegebenen Zeit zielgerichtet durchgeführt haben;
- die zur Verfügung gestellten Apparaturen richtig eingesetzt und ausgelesen haben; 
- sich ein Bild über die mit den aufgenommenen Daten verbundenen Unsicherheiten gemacht haben; 
- alle Daten und Parameter zur Berechnung der (Teil-)Ergebnisse, einschließlich ihrer Unsicherheiten im Protokoll **(auch für Außenstehende) nachvollziehbar dokumentiert** haben. 

Wir gehen davon aus, dass das Protokoll, als Jupyter-notebook, während der Versuchsdurchführung entsteht. Hierzu sollten Sie die Durchführung im Jupyter-notebook-Format als Vorlage verwenden. Es bietet sich an die Durchführung während der Vorbereitung auf den Versuch bereits mit allen Informationen, die Sie für die Durchführung des Versuchs als notwendig erachten, oder mit vorbereiteten Tabellen-, Text- oder Code-Fragmenten zu versehen, die Sie während der Versuchsdurchführung dann nur noch modifizieren oder vervollständigen müssen. 

Beachten Sie, dass im Jupyter-notebook für die Durchführung des Versuchs weder Raum für die Einleitung des Versuchs noch für eventuelle Herleitungen vorgesehen ist. Beide Aspekte sind durch die Anleitung auf dem SCC gitlab-Server bereits hinreichend abgedeckt. Wir gehen selbstverständlich davon aus, dass Sie den Versuch vorbereitet und verstanden haben. Dies Sicherzustellen ist Bestandteil der Abfrage vor Versuchsbeginn.  

Das Protokoll geht durch die folgenden letzten Schritte in die **einzureichende Auswertung** über: 

- Abschließende Kontrolle und ggf. Aufbereitung aller (Teil-)Ergebnisse. Bringen Sie dabei das Protokoll in eine **allgemein verständliche und lesbare Form**. Sie studieren Physik und nicht Germanistik, es ist für uns aber nicht akzeptabel, wenn Ihr Protokoll vor Rechtschreibfehlern strotzt, oder Sätze nicht nach den Regeln der deutschen Sprache abgeschlossen werden. Dies fällt unter den Punkt der allgemeinen Verständlichkeit!
-  Reflexion und Diskussion des Versuchsablaufs und der erzielten Ergebnisse. 

**Eine strukturierte und organisierte Vorgehensweise bei der Protokollführung, ebenso wie ein sehr gutes, grundlegendes Verständnis für alle den Versuch betreffenden physikalischen Zusammenhänge sind Grundvoraussetzungen, um diese Anforderungen erfüllen zu können.**

Wir wünschen im Protokoll ausdrücklich **keine langen Herleitungen** physikalischer Zusammenhänge, die ohnehin aus der Literatur, oder den Hinweisen zu den Versuchen entnehmbar sind. Wir wünschen auch **keine Formatierung in Latex**, die über den in Markdown verwendbaren Satz physikalischer Formeln hinausgeht. Beides ist Ihnen freigestellt. Es geht jedoch weder in die Bewertung der eingereichten Auswertungen noch in das von uns veranschlagte Zeitbudget für den Arbeitsaufwand für die erfolgreiche Teilnahme an den P1- und P2-Praktika ein.

Die organisierte und strukturierte Dokumentation Ihrer Versuchsdurchführung ist nicht an ein Dokumentenformat gebunden. Es ist insbesondere bei dem Arbeiten mit Jupyter-notebook nicht Aufgabe der Tutor:innen (Teil-)Ergebnisse Ihres Protokolls in Code-Zellen des Jupyter-notebooks zusammen zu suchen. Wir gehen davon aus, dass Sie erzielte (Teil-)Ergebnisse z.B. im Anschluss an Code-Zellen in einer Markdown-Zelle klar kennzeichnen, zusammenfassen und diskutieren.

Im Zuge der Umstellung von Latex- auf Jupyter-notebook-Protokolle haben wir zuweilen die Kritik gehört, dass die Protokoll im Latex-Satz "professioneller" und "schöner" aussahen. Beachten Sie hierzu den folgenden Grundsatz: Es ist der *Inhalt*, der das professionelle Auftreten eines:r Physiker:in ausmacht und nicht die Form. Zäumen Sie daher das Pferd nicht von hinten auf, zuerst kommt der Inhalt, danach kommt die Form. Sie werden im weiteren Verlauf Ihres Studiums noch genug Gelegenheiten haben, sich mit dem Satz von Latex-Dokumenten vertraut zu machen. 

### Bevorzugtes Dokumentenformat

Wir erwarten die Rückgabe der Versuchsauswertungen durch *fristgerechten upload*  der ausgefüllten Versuchs-Durchführung, **im Jupyter-notebook-Format, exportiert nach *pdf***, auf das ILIAS-System. In dieses Dokument kann Ihr:e Tutor:in elektronisch kommentieren. Es ist obligatorisch.

Zum Export des Jupyter-notebooks nach *pdf* achten Sie auf unsere Hinweise zum [Arbeiten auf dem Jupyter-server](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/doc/JupyterServer.md). 

Ausnahmen von dieser Regel sind zulässig. Beachten Sie jedoch, dass Sie **in jedem Fall eine Version Ihres Protokolls in *pdf*-Format** auf dem ILIAS-System hinterlegen müssen, damit Ihr Versuch die Chance hat anerkannt zu werden. 

### Beispiel eines Protokolls/einer Auswertung

Wir veröffentlichen ein Beispiel dafür, wie eine Auswertung im Jupyter-notebook-Format (exportiert nach *pdf*) aussehen könnte, nach dem ersten Versuchstag des P1, als Musterlösung zum [Vorversuch Datenauswertung](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Vorversuch) auf dem gitlab-Server des SCC. Dieses Beispiel können Sie als Vorlage für alle weiteren Versuchsauswertungen verwenden. 

### Bewertung

Ihr:e Tutor:in wird die von Ihnen eingereichte Versuchsauswertung im *pdf*-Format durchsehen und entsprechend kommentieren. Wir sehen dabei die folgenden **Kategorien von Kommentaren** vor: 

- **Beanstandungen**: Hierbei handelt es sich z.B. um inhaltliche Fehler; Unzulänglichkeiten, die Ihr Protokoll/Ihre Auswertung nicht nachvollziehbar oder unverständlich machen; nicht gekennzeichnete oder näher dokumentierte, fehlende Aufgabenteile oder; fehlende Einschätzungen oder Unsicherheiten der (Teil-)Ergebnisse. Dabei geht es uns v.a. um inhaltliche Beanstandungen, die von substantieller Natur für das Verständnis des Versuchs und die sachliche Einschätzung Ihrer Arbeit und Ihrer Ergebnisse sind. Beachten Sie, dass es für uns in erster Linie unerheblich ist, wie genau oder ungenau Sie mit Ihrer Messung eine gegebene Erwartung getroffen haben. Wichtig ist die Einschätzung innerhalb der von Ihnen während des Versuchs veranschlagten Unsicherheiten. Selbst wenn Sie im Rahmen dieser Unsicherheiten, nach Ihrem Dafürhalten, mit Ihrem Ergebnis "weit von Ihrer Erwartung abweichen" sollten kann dies für uns immer noch in Ordnung sein kann, wenn Sie Ihre Messung ernsthaft und sorgfältig auf den Prüfstand stellen, reflektieren und diskutieren.   
- **Anmerkungen**: Hierbei handelt es sich um alle weiteren Kommentare zu Ihrer Auswertung. Als Studenten der Physik sollten Sie den Anspruch haben eine semantisch, grammatikalisch und orthographisch einwandfreie Auswertung abzugeben! Ihre physikalische Argumentation sollte, nach Einschätzung Ihre:r Tutor:in korrekt sein. Vielleicht ist Ihr:e Tutor:in geneigt Ihnen den ein oder anderen Tipp an die Hand zu geben, wie Sie Ihre Messung oder Auswertung noch besser hätten durchführen können.  

**Beanstandungen sollten Sie auf jeden Fall korrigieren** und die korrigierte Auswertung (als Version $\mathrm{v2}$) erneut auf das ILIAS-System hochladen. Hierzu steht Ihnen die Versionierung von *uploads* auf ILIAS zur Verfügung. Wir empfehlen Ihnen dabei auch auf die Anmerkungen Ihr:er Tutor:in einzugehen. 

Die Bewertung der Auswertung erfolgt **spätestens 14 reguläre Studientage (d.h. zwei Versuchstage während des laufenden Betriebs) nach Versuchsdurchführung**, per Eintrag ins Praktikumsbuch, wie folgt:

- **-**: Auswertung mit (verbliebenen) Beanstandungen.
- **0**: Auswertung ohne Beanstandung.
- **+**: Bemerkenswert gute Auswertung ohne Beanstandungen. 

Anmerkungen gehen im Allgemeinen nicht und wenn doch, dann nur in groben Fällen und nach Rücksprache des/der Tutor:in mit den Dozenten des Praktikums, in die Bewertung der Auswertung ein. Die Bewertung soll den gesamten Versuch von der Durchführung bis zur Auswertung wiedergeben. Deshalb ist es notwendig, dass Ihr:e Tutor:in zeitnah nach Abschluss der Versuchsdurchführung zu einer Beurteilung Ihrer Versuchsdurchführung und Auswertung gelangen kann. 

### Zeitlicher Ablauf

Für die Rückgabe der Auswertung sehen wir den folgenden zeitlichen Ablauf vor: 

- Am Ende jedes Versuchstags besprechen Sie Ihre Ergebnisse mit Ihrem:er Tutor:in und **laden Ihr Protokoll als Version $\mathrm{v0}$ ins ILIAS-System hoch.** Dieser Vorgang gilt als Nachweis dafür, dass Sie den Versuch durchgeführt haben. Sie haben von diesem Zeiptunk an mindestens 6 reguläre Studientage Zeit Ihr Protokoll zur Abgabe aufzubereiten, über den Versuchsablauf zu reflektieren und die erzielten Ergebnisse abschließend zu diskutieren. 
- Wenn Sie denken, dass Ihr Protokoll zur Abgabe bereit ist laden Sie es als Version $\mathrm{v1}$ auf das ILIAS-System hoch. Hierzu steht Ihnen die Versionierung von *uploads* auf ILIAS zur Verfügung. Die im ILIAS-System hinterlegte Version $\mathrm{v1}$ Ihres Protokolls gilt als Ihre Versuchsauswertung. **Tun Sie dies bis 12:00 Uhr, am Tag vor dem nächsten Versuchstag!** Ihr:e Tutor:in wird Ihr Protokoll zu dieser Zeit aus dem ILIAS-System runterladen, durchsehen, kommentieren und die kommentierte Version Ihrer Auswertung wieder auf das ILIAS-System hochladen. Eventuelle Beanstandungen können Sie am kommenden Praktikumstag mit Ihrem:r Tutor:in durchsprechen. 
- Suchen Sie den/die Tutor:in des ausgewerteten Versuchs zwischen **15:30 – 16:00 am nächsten Praktikumstag** auf, um Ihre Durchführung und Auswertung des vorangegangenen Versuchs nochmal mit ihm/ihr zu besprechen. Gibt es zu diesem Zeitpunkt keine Beanstandungen mehr zu Ihrer Versuchsauswertung gilt die Auswertung als testiert mit dem Vermerk "**0**" (oder "**+**") im Praktikumsbuch. Liegen noch Beanstandungen vor haben Sie mindestens 6 weitere reguläre Studientage, d.h. wiederum **bis 12:00 Uhr, am Tag vor dem dann nächsten Versuchstag** Zeit diese zu beheben. Laden Sie innerhalb dieser Frist die entsprechend korrigierte Version Ihrer Auswertung als Version $\mathrm{v2}$ auf das ILIAS-System hoch. Hierzu steht Ihnen die Versionierung von *uploads* auf ILIAS zur Verfügung. 
- Falls es zu Beanstandungen kam, wird Ihr:e Tutor:in, vor Beginn des kommenden Prakitkumstags, die von Ihnen hinterlegte Version $\mathrm{v2}$ Ihrer Auswertung auf dem ILIAS-System nur noch auf die Behebung der besprochenen Beanstandungen hin kontrollieren. Ihre Auswertung wird daraufhin **ohne weitere Besprechung testiert**. Ihr:e Tutor:in wird die testierte Version $\mathrm{v2}$ Ihrer Auswertung zu Dokumentationszwecken erneut auf das ILIAS-System hochladen. Liegen zu diesem Zeitpunkt immer noch Beanstandungen vor wird dies im Praktikumsbuch mit einem "**-**" vermerkt. 
- Sollte in der Woche nach dem Versuchstag ein **Feier- oder Ferientag** vorliegen verlängert sich die jeweilige Bearbeitungszeit entsprechend bis zum nächsten regulären Praktikumstag.      

Nach Ablauf des Praktikums müssen Sie **für jeden Versuch eine Auswertung** (d.h. ein Protokoll mindestens in der Version $\mathrm{v1}$) auf dem ILIAS-System hinterlegt haben. Ansonsten gilt der entsprechende Versuch als "nicht durchgeführt" und muss ggf. nochmal von Ihnen durchgeführt werden. Dies liegt im Ermessen der Dozenten des Praktikums. 

Weiterhin dürfen nach Ablauf des Praktikums **nicht mehr als zwei Auswertung mit dem Vermerk "**-**" im Praktikumsbuch** vorliegen. Je nach Beanstandung müssen Sie die Auswertungen entsprechend überarbeiten oder entsprechende Versuche oder Versuchsteile während der Nachholtermine, nach Ablauf des Praktikums, erneut Durchführen. Auch dies liegt im Ermessen der Dozenten des Praktikums. 

Sie studieren nicht BWL, sondern Physik. Bei allem Hang zur Ökonomie ist es für uns nicht akzeptabel, wenn Sie zu den letzten Versuchen im Semester, soweit Sie es sich leisten können mögen, keine Auswertungen mehr abgeben. Wir stellen als Minimalanforderung, den *upload* einer Auswertung als Version $\mathrm{v1}$ Ihres Protokolls, die nicht mit der Version $\mathrm{v0}$ identisch ist.    

### FAQ zum zeitlichen Ablauf der Versuchsauswertung und der Bewertung

**Wie soll ich ein Protokoll in Jupyter-notebook führen?** – Verwenden Sie am besten die Durchführung (mit dem Titel des durchzuführenden Versuchs und der Endung **.iypnb*) als Vorlage. Bearbeiten Sie diese am besten in der Vorbereitung auf die Versuchsdurchführung, so dass Sie Werte ggf. nur noch eintragen und gleich weiterverarbeiten können. Für die prompte Weiterverarbeitung von Daten (z.B. zum Zweck der Fehlerfortpflanzung) bieten sich Code-Zellen an. Sie sollten unbedingt jedes (Teil-)Ergebnis in einer anschließenden Markdown-Zelle klar kennzeichnen, zusammenfassen und diskutieren. Nach dem Export ins *pdf*-Format sollte Ihr Protokoll vollständig und "von oben bis unten" flüssig und klar verständlich lesbar sein. Stellen Sie vor dem Export ins *pdf*-Format sicher, dass alle Zellen Ihres Jupyter-notebooks ausgeführt sind. Ein Beispiel für eine Auswertung in Jupyter-notebook erhalten Sie als Musterlösung des [Vorversuchs Datenverarbeitung](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Vorversuch) nach dem ersten Versuchstag des P1. 

**Wann laden wir die "vorläufige" Version $\mathrm{v0}$ unseres Protokolls auf ILIAS hoch?** – Direkt nach Beendigung des Praktikumstages (zwischen 18:00 –19:00 Uhr). Gehen Sie es am besten vorher nochmal kurz mit Ihrem:r Tutor:in durch das Protokoll und die erzielten Zwischenergebnisse durch.

**Wozu laden wir überhaupt eine Version $\mathrm{v0}$ unseres Protokolls auf ILIAS hoch?** – Sie tun dies zum Nachweis, dass Sie den Versuch durchgeführt haben. 

**Wieviel Zeit haben wir, um die Versuchsauswertung nach dem Versuchstag als Version $\mathrm{v1}$ auf ILIAS hochzuladen?** – Sie haben bis *12:00 Uhr, am Tag vor dem nächsten Versuchstag* Zeit Ihr Protokoll aufzubereiten und als Version $\mathrm{v1}$ auf ILIAS hochzuladen. Dabei sollte es sich um mindestens 6 reguläre Studientage (einschließlich Wochenenden) handeln. 

**Wie sollen wir die Protokolle beim upload auf ILIAS benennen und kennzeichnen?** – Verwenden Sie für jede Version den Namen der entsprechenden Versuchsdurchführung, nach dem Export ins *pdf*-Format. Für die entsprechende Versionierung verwenden Sie die Möglichkeit zur Versionierung im ILAS-System. 

**Was müssen wir nach dem *upload* der Version $\mathrm{v0}$ denn überhaupt noch an unserem Protokoll tun, um es als Version $\mathrm{v1}$ auf ILIAS hochzuladen?** – Wir gehen davon aus, dass Sie das Protokoll, dass Sie während des Versuchs aufgenommen haben nochmal in Hinblick auf Lesbarkeit und  Vollständigkeit überarbeiten. Überprüfen Sie Zwischenergebnisse und schließen Sie das Protokoll mit wohldefinierten Endergebnissen ab. Stellen Sie die aufgezeichneten Daten ggf. geeignet dar, versehen Sie alle Zwischen- und Endergebnisse mit Unsicherheiten und reflektieren und diskutieren Sie den Versuchsablauf und Ihre Ergebnisse. Dies sollte nicht mehr als 4 Stunden ihrer Zeit in Anspruch nehmen. Wir empfehlen dies zeitnah nach Beendigung des Versuchs zu tun, damit Sie die Durchführung des Versuchs noch in Ihrer Erinnerung präsent haben.

**Was passiert, wenn wir die Version $\mathrm{v1}$ des Protokolls zu spät auf ILIAS hochgeladen haben?** – In diesem Fall können Sie nicht mehr erwarten, dass Ihr:e Tutor:in Ihr Protokoll bereits am folgenden Versuchstag gelesen und mit Anmerkungen versehen haben werden. Die Besprechung kann in einem solchen Fall wenig(er) zielgerichtet erfolgen. Sie sollten eine solche Situation unbedingt vermeiden.  

**Wie erfahren wir von den Anmerkungen oder Beanstandungen unseres:r Tutor:in?** – Ihr:e Tutor:in werden **jeweils einen Tag vor jedem Praktikumstag** das ILIAS-System überprüfen. Wenn er/sie eine entsprechende Version Ihres Protokolls  vorfindet, wird er/sie diese Version des Protokolls durchlesen und daraufhin zeitnah eine neue, kommentierte Version in *pdf*-Format auf ILIAS hochladen. Anmerkungen erfolgen direkt im Text, Beanstandungen werden im entsprechenden Sichtfenster auf dem Deckblatt explizit vermerkt. Bei der Besprechung Ihrer Auswertung mit Ihrem:r Tutor:in können Sie die Beanstandungen gemeinsam diskutieren und ggf. weiteren Handlungsbedarf abklären. 

**Der nächste Praktikumstag ist ein Feiertag – wann müssen wir das Protokoll auf ILIAS hochladen?** – Ist der nächste Praktikumstag eine Feier- oder Ferientag verschiebt sich die gesamte Abgabe und -besprechung des Protokolls bis zum entsprechend nächsten regulären Praktikumstag. Die Abgabe, als *upload* auf ILIAS muss in diesem Fall fristgerecht um 12:00 Uhr am Vortag des nächsten Praktikumstages erfolgen. Dies gilt sowohl für die Erstabgabe, als auch für die Bearbeitung eventueller Beanstandungen. 

**Was macht unser:e Turor:in mit der Version $\mathrm{v2}$ des Protokolls und wie erfahren wir, wie das Protokoll testiert wurde?** – Ihr:e Tutor:in wird **jeweils einen Tag vor jedem Praktikumstag** das ILIAS-System überprüfen. Wenn er/sie eine entsprechende Version Ihres Protokolls  vorfindet, wird er/sie diese Version des Protokolls nur noch auf die Bearbeitung der diskutierten Beanstandungen hin überprüfen und daraufhin wieder zeitnah eine neue, kommentierte Version in *pdf*-Format auf ILIAS hochladen. Diese Version beinhaltet das Testat. 

**Wir haben die Version $\mathrm{v1}$ unseres Protokolls schon vor der Abgabefrist auf ILIAS hochgeladen. Kann unser:e Tutor:in das Protokoll nicht schon früher durchlesen und kommentieren?** – Das hängt von Ihrem:r Tutor:in ab. Weder die Praktikumsleitung noch Sie können verlangen, dass die Tutor:innen in ständiger Bereitschaft sind ILIAS auf hochgeladene Protokolle hin zu überprüfen. Wir bitten dafür um Ihr Verständnis.  

**Was passiert, wenn wir ein "-" für unsere Auswertung bekommen?** – Sie können sich zwei Auswertungen mit nicht aufgelösten Beanstandungen (d.h. mit dem Vermerk "-") leisten. Falls für Sie mehr als zwei Protokolle mit ausstehenden Beanstandungen vorliegen, müssen Sie die entsprechenden Beanstandungen (ggf. zu einem Nachholtermin, nach Beendigung des regulären Praktikumsbetriebs) beheben. Versuche, die Sie ohne Beanstandungen absolviert haben bleiben Ihnen im System erhalten. Sie müssen Sie also nicht nochmal durchführen.  

**Auf Grundlage des Jupyter-notebook können wir nicht zusammenarbeiten! Warum können wir nicht z.B. [Overleaf](https://de.overleaf.com/) verwenden?** – Wir wünschen uns, dass Sie die Vorbereitung, Durchführung und Auswertung der Versuche, als Team, gemeinsam, am gleichen Ort bestreiten. Wir wünschen uns explizit den für ein erfolgreiches Studium unerlässlichen, persönlichen Austausch. Außerdem sollten Sie den größten Teil des Versuchs und der Auswertung ohnehin bereits während des Praktikumstags absolvieren können. Die Verwendung von Jupyter-notebook stellt gegenüber der Verwendung von Overleaf also keinen gravierenden Nachteil dar. Die Verwendung von Werkzeugen, wie Overleaf ist Ihnen freigestellt. Sie geht jedoch nicht in das von uns veranschlagte Zeitbudget für den Arbeitsaufwand für die erfolgreiche Teilnahme an den P1- und P2-Praktika ein.

## Bewertung des Praktikums

Wir weisen ausdrücklich darauf hin, dass das P1 und P2 **nur als bestanden gewertet wird. Eine Bewertung darüber hinaus wird nicht erteilt.** 

Das die von Ihnen durchgeführten Versuche mit dem Vermerk "**0**" bewertet werden stellt die Regel dar. **Es ist für das Bestehen der Kurse *irrelevant*, wie viele der von Ihnen durchgeführten Versuche mit einem "+" bewertet wurden.** Es handelt sich dabei um ein rein internes Beurteilungssystem der P1- und P2-Praktika und um entsprechendes positives Feedback für Sie. 

Da Sie die Versuche i.a. zu zweit durchführen ist eine faire Beurteilung einzelner Personen auf Grundlage der getroffenen Vermerke im Praktikumsbuch nicht möglich. 

In seltenen Fällen kommt es vor, dass Stipendiaten Beurteilungen ihrer Leistungen zum Nachweis bei entsprechenden Stiftungen benötigen. **Eine solche Beurteilung erfolgt persönlich durch einen Dozenten des Praktikums, der Sie während des Praktiumsverlaufs begleitet und/oder Sie noch einmal zu einem Gespräch einlädt. Melden Sie einen solchen Fall unbedingt vor Beginn des Praktikums beim entsprechenden Dozenten an.** Im Nachhinein kann eine solche Beurteilung nicht mehr vorgenommen werden.

# Navigation

[Zurück zu P1-Praktikum](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students)
