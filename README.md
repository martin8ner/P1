# Arbeiten in den P1 und P2 Praktika

## Ziele der P1 und P2 Praktika

Ziele der P1 und P2 Praktika sind es den Studierenden die Möglichkeit zu bieten: 

- Experimente unter Laborbedingungen durchzuführen; 
- Daten mit naturwissenschaftlichem Anspruch zu erheben und weiterzuverarbeiten; 
- physikalische Gesetzmäßigkeiten am Experiment zu überprüfen.  

### Durchführung

Zur **Durchführung** gehört es, *zielgerichtet* zu experimentieren und Messungen und Teilergebnisse in den Kontext des Experiments *einzuordnen*. Sie sollten also mit einer klaren Vorstellung darüber, was Sie im anstehenden Versuch erwartet im Praktikum eintreffen und die physikalische Aufgabenstellung vollumfänglich verstanden haben. Dies wird durch die Vorbesprechung zum Versuch sichergestellt. 

### Datenerhebung

Zur **Datenerhebung** gehört die *systematische*, *reproduzierbare* Aufnahme von Messwerten einschließlich der Einschätzung der damit verbundenen wichtigsten Unsicherheiten. Grundsätzlich gilt in der Physik: "Keine Messung ohne Einschätzung der damit verbundenen [wichtigsten] Unsicherheiten!" 

### Protokoll

Ein zentraler Bestandteil der Datenerhebung ist das *gewissenhaft*, *vollständig* und *sachlich* geführte **Protokoll der Versuchsdurchführung**, das in die Auswertung des Experiments mündet. Das wissenschaftlich geführte Protokoll setzt voraus, das sich der Durchführende der einzelnen Schritte des Experiments bewusst ist und diese für sich und Außenstehende klar, verständlich und reproduzierbar dokumentiert. Das Protokoll erklärt, *wie* Sie zu einem Messergebnis gekommen sind. Sollte Ihnen bei der Durchführung des Experiments ein Fehler unterlaufen sein sollte dies aus dem Protokoll nachträglich nachvollziehbar und ggf. in der Einschätzung der Ergebnisse durch Sie und Außenstehende zu berücksichtigen sein. 

Die gewissenhafte Erhebung und Dokumentation Ihrer Daten begründet im wahren Leben Ihren guten Ruf als Wissenschaftler. Ein Fehler in der Durchführung eines Experiments kann zwar zur Invalidierung der Ergebnisse und/oder zur Neuauflage eines –dann verbesserten– Experiments führen. Ein mangelhaft dokumentiertes Experiment und daher von außen nicht mehr nachvollziehbare Ergebnisse invalidieren die vorgestellten Ergebnisse jedoch *sofort* und *unwiederbringlich*. 

In Zeiten vor der Digitalisierung wurden Protokolle z.B. in Form von Laborbüchern geführt. Für die P1 und P2 Praktika ersetzt das **Jupyter-notebook**, das Sie auf dem Jupyter-server der Fakultät anlegen können das Laborbuch. Sie sollten darin zielgerichtet und für sich und Außenstehende nachvollziehbar 

- die Ziele des Experiments; 
- die Bedingungen der Durchführung; 
- die Messwerte, einschließlich der Einschätzung der Unsicherheiten *aller* aufgezeichneten Daten; 
- die Weiterverarbeitung der Daten und daraus resultierende Teilergebnisse dokumentieren. 

Am Ende des Praktikumstages mündet das Protokoll in die Auswertung des Versuchs. 

### Begriffsklärung

#### Versuchsausgang

Wir erwarten nicht, dass Sie dieses Vorgehen bereits mit dem ersten Versuch des P1 perfekt beherrschen. Sie sollen es vielmehr im Laufe der P1 und P2 Praktika erlernen. 

Sie sollen im P1 und P2 anhand gut verstandener physikalischer Prozesse das Experimentieren und die wissenschaftlich-sachliche Einschätzung Ihres Experimentierens *erlernen*. Wir erwarten nicht, dass ein von Ihnen durchgeführtes Experiment zu "publizierbaren" Ergebnissen führt. Insbesondere erwarten wir nicht, dass Sie mit Ihrem Ergebnis einen existierenden Literaturwert so exakt wie möglich reproduzieren.  

**Mit anderen Worten:** Die Aussage "Meine Messung stimmt innerhalb von 10% mit dem Literaturwert überein" ist im Allgemeinen für Ihre Messung *irrelevant*. Die Frage, die Sie mit Ihrem Versuch zu beantworten haben ist: "Stimmt meine Messung innerhalb der von mir abgeschätzten Unsicherheiten mit dem Literaturwert überein?". 

Dabei ist die adäquate *numerische* Einschätzung der Unsicherheiten der Messung mitunter wichtiger, als der ermittelte Zentralwert.   

#### Einschätzung des eigenen Experimentierens

Auf dem Jupyter-server der Fakultät stehen Ihnen alle nötigen Werkzeuge zur Anwendung von Methoden zur statistischen Parameterschätzung, wie sie von der Fakultät empfohlen werden, zur Verfügung. Dadurch sollte sich in vielen Fällen eine, oft nicht auf ihre Anwendbarkeit hin überprüfte "händische" Fehlerabschätzung durch Gaußsche Fehlerfortpflanzung erübrigen. Der [P1 Vorversuch](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Vorversuch) Datenanalyse bietet Ihnen die Möglichkeit Ihr Wissen und Ihre Erfahrung auf diesem Gebiet in Vorbereitung auf das P1 zu vertiefen und aufzufrischen. 

Als Physiker müssen Sie in die Situation hineinwachsen, dass Sie selbstverständlich die Unsicherheiten von Ihnen weiterverarbeiteter Daten bewusst abfragen und ggf. einschätzen. Sie sollten *nach Möglichkeit* keinen Messwert oder Parameter ohne entsprechende *quantitative* Abschätzung seiner Unsicherheiten weiterverarbeiten. Die Einschätzung von Unsicherheiten gehört zu Ihrem Handwerk als Wissenschaftler. In einer numerischen Parameterschätzung erhalten Sie verlässliche Konfidenzintervalle für die von Ihnen bestimmten Messgrößen aus der angewandten Anpassung (dem *fit*). Im Zweifel können Sie Unsicherheiten mithilfe der Sktiptsprache *python* systematisch und für jeden aufgezeichneten und weiterverarbeiteten Messwert fortpflanzen. 

## Ein Praktikumstag im P1 oder P2

Ein Praktikumstag im P1 oder P2 verläuft von **13:00 – 19:00**. Wir gehen davon aus, dass Sie sich vor Versuchsantritt mit den grundlegenden Fragestellungen des aktuellen Versuchs vertraut gemacht haben, und dass Sie den Versuch der Vorwoche abgeschlossen und ausgewertet haben. Unter diesen Voraussetzung sollte Ihr Tag im P1 oder P2 wie folgt aussehen: 

### Nachbesprechung des vorangegangenen Versuchs

Von **13:00 – 13:30** besprechen Sie Durchführung und Auswertung des vorangegangenen Versuchs *im Team* und *persönlich* bei dem/der entsprechenden Tutor:in. Dabei vertreten Sie vor dem/der Tutor:in Ihre Ergebnisse und klären, ob noch Änderungen an der Auswertung vorzunehmen sind. Sie können diese Besprechung, je nach Absprache mit dem/der Tutor:in auch schon vorher zu jedem Zeitpunkt nach Abschluss Ihrer Auswertung durchführen. Wir wünschen uns jedoch, dass diese Besprechung *im Team* und *persönlich* erfolgt. Eine Besprechung online oder per E-Mail sollte die Ausnahme bilden. Sie finden den/die Tutor:in in den Räumlichkeiten des vorangegangen Versuchs.

### Vorbesprechung des aktuellen Versuchs

Von **13:30 – 14:00** besprechen Sie Ziel und Durchführung Ihres aktuellen Versuchs mit dem/der entsprechenden Tutor:in. Im Rahmen dieser Vorbesprechung klären Sie ab, 

- ob Sie die physikalische Fragestellung oder den zu untersuchenden physikalischen Sachverhalt ausreichend verstanden haben; 
- ob Sie Ziel und Strategie zur Durchführung des Versuchs verstanden haben;  
- ob Sie die für die Versuchsdurchführung notwendigen Gerätschaften identifizieren und sachgerecht bedienen können. 

Diese Besprechung sollten Sie nicht als Prüfung verstehen. Natürlich wollen wir wissen, ob Sie wissen worum es in den nächsten 5,5 Stunden für Sie gehen soll. Sollte dies nicht der Fall ist, können Sie aus dem Versuchstag nichts lernen. Vorrangiges Ziel der Vorbesprechung ist es aber, Sie in die Position zu versetzen, dass Sie mit einer klaren Idee den Versuch weitestgehend *selbstständig* durchführen können. Das sollte Ihr Anspruch an sich selbst sein. Bei anspruchsvollen Versuchen und gerade zu Beginn des P1 kann dies eine schwere Aufgabe sein. Sie haben nach der Vorbesprechung 4,5 Stunden Zeit, diese Aufgabe in Ihrem Sinne bestmöglich zu lösen. Der/Die Tutor:in ist dazu da, Ihnen dabei zu helfen. 

### Versuchsdurchführung

Von **14:00 – 17:30** haben Sie Zeit den aktuellen Versuch durchzuführen. Der/Die Tutor:in sollte über die gesamte Zeitspanne zur Beantwortung von Fragen zu Ihrer Verfügung stehen. Manche Versuchsaufbauten müssen aus Sicherheitsgründen vor Inbetriebnahme von dem/der Tutor:in abgenommen werden. Bemühen Sie sich den Versuch *als Team* so *selbstständig* wie möglich durchzuführen, aber stellen Sie gemeinsam mit dem/der Tutor:in sicher, dass Ihre Durchführung zielgerichtet ist und erzielte Zwischenergebnisse im Zusammenhang des gesamten Versuchs für Sie Sinn ergeben. Hierfür empfehlen wir Ihnen dringend Teilauswertungen in Jupyter-notebook durchzufüren. Falls Sie vor 17:30 mit der Durchführung der Versuchs fertig sein sollten können Sie bereits mit der Auswertung beginnen. 

### Einführung in den nächsten Versuch durch Kommilitonen

Von **17:30 – 18:00** nutzen Sie die Zeit sich mit dem nächsten Versuch persönlich vertraut zu machen: Teilen Sie sich hierzu ein zwei Gruppen A und B auf. Gruppe A verbleibt zunächst beim aktuellen Versuch. Gruppe B sucht den Raum des nächsten Versuchs auf und lässt sich von Gruppe A des dortigen Versuchs 15 min lang erklären, worum es bei diesem Versuch geht und wie er ablaufen wird. Gruppe A sollte nach 4,5 Stunden des Experimentierens in der Lage sein, den Kommilitonen aus Gruppe B erklären zu können, was sie im aktuellen Versuch gemacht haben. Der/Dir entsprechende Tutor:in unterstützt Sie dabei gegebenenfalls. Nach 15 min kehrt Gruppe B zu ihrem aktuellen Versuch zurück und die Gruppen A und B tauschen sich durch. 

### Abschluss des aktuellen Versuchs

Von **18:00 – 19:00** haben Sie die Möglichkeit verbleibende Messungen des aktuellen Versuchs abzuschließen. Sie führen damit Ihr Protokoll zu einem wohldefinierten Abschluss. Der Praktikumstag endet aus organisatorischen Gründen um Punkt 19:00, selbst, wenn Sie den Versuch noch nicht vollständig durchgeführt haben sollten. Geben Sie in einem solchen Fall in Ihrem Protokoll an, woran es lag, dass Sie nicht rechtzeitig fertig geworden sind. Sprechen Sie Ihre Messungen und Zwischenergebnisse nochmal abschließend mit dem/der Tutor:in durch bevor Sie gehen. 

### Auswertung 

Die Auswertung des Versuchs erfolgt auf Grundlage Ihres Protokolls vorzugsweise in Jupyter-notebook. Sie sollten als Anhalt **nicht mehr als 2 Stunden** für die Auswertung des aktuellen Versuchs benötigen. Beachten Sie, dass das vorrangige Ziel der Auswertung ist, Ihre Messung und die erzielten Ergebnisse mit einer sinnvollen persönlichen Einschätzung einschließlich entsprechender *quantifizierter* Unsicherheiten für Sie und Außenstehende zu dokumentieren. Ihr Protokoll und die entsprechende Auswertung sollten *übersichtlich*, *nachvollziehbar* und *vollständig* sein. Wir verlangen explizit nicht den Satz in Latex. 

Die Abgabe erfolgt über das Hochladen, sowohl des Jupyter-notebooks als auch einer pdf-Version des Jupyter-notebooks ins ILIAS System.    

### Einordnung des P1 oder P2 und ETCS Regelung

Das P1 und P2 entsprechen in der Bewertung des damit verbundenen Arbeitsaufwands jeweils **6 ETCS Punkten**. Es handelt sich dabei um einen signifikanten Anteil Ihrer Arbeit für das Physikstudium im laufenden Semester. Sie sollten diese Zeit für die Praktika bei der Gestaltung Ihres Semesterplans dringend einräumen. Die Praktika der Physik bieten Ihnen die Möglichkeit zu Experimentieren, physikalische Gesetzmäßigkeiten experimentell nachzuvollziehen, physikalische Sachverhalte, die aus einer Vorlesung nicht immer intuitiv und klar sind am Experiment nachzuvollziehen und sich in der Aufzeichnung und Weiterverarbeitung von Messdaten mit wissenschaftlichem Anspruch auszubilden. Dies ist ein essentieller Bestandteil jedes Physikstudiums und damit Ihrer Ausbildung zum wissenschaftlichen Arbeiten. 

Bei der Anrechnung von ETCS Punkten legen wir das folgende Modell zugrunde: 

- **4–6 Stunden Versuchsvorbereitung**, in denen Sie sicher stellen, dass Sie nach Ihrer eigenen Einschätzung optimal auf den nächsten Versuch vorbereitet sind.
- **6 Stunden Versuchsdurchführung**.
- **2–4 Stunden Versuchsnachbereitung** (inklusive potentieller Neueinreichungen nach der Nachbesprechung mit dem/der Tutor:in).      

Damit ergeben sich **168 Stunden** Arbeitsaufwand im laufenden Semester. 

Beachten Sie bei der Beurteilung des Arbeitsaufwandes, dass die Praktika aus studienorganisatorischen Gründen deutlich vor dem offiziellen Ende der Vorlesungszeit des Semesters enden, was Ihnen die Möglichkeit einräumt sich gegen Ende der Vorlesungszeit angemessen auf anstehende Abschlussprüfungen vorzubereiten. Dadurch erhöht sich der Arbeitsaufwand während des laufenden Praktiums entsprechend. 

# Arbeiten auf dem Jupyter-server

Zugang zum Jupyter-server erhalten Sie über die Webadresse: [https://jupytermachine.etp.kit.edu/](https://jupytermachine.etp.kit.edu/). Als Login verwenden Sie Ihren Studenten Account am KIT. Wählen Sie, wenn Sie danach gefragt werden die Option **Python** aus und starten Sie den Server. 

Falls der Zugang zum Server nicht für Sie freigeschaltet sein sollte können Sie die Freischaltung [hier](https://comp.physik.kit.edu/Account/) veranlassen. Stellen Sie bitte **vor Praktikumsbeginn** sicher, dass Sie einen gültigen Account haben und sich entsprechend auf dem Jupyter-server einlogen können. 

Nach dem Start sollten Sie ein zweigeteiltes Fenster in Ihrer Jupyter-Umgebung vorfinden, wie im folgenden Bild gezeigt: 

<img src="./figures/JupyterAccount.png" alt="figures" style="zoom:100%;" />

Auf der linken Seite befindet sich ein Navigationsfenster mit der Verzeichnisstruktur Ihrer Jupyter-Umgebung, rechts daneben befindet sich ein Fenster (der sog. *Launcher*) in dem Sie auswählen können, welche Art von Notebook Sie öffnen möchten. Sie können, wenn Sie möchten, die Option **Notebook** und  **Phython 3** (das erste Icon oben links im *Launcher*) anwählen. Das rechte Fenster der Jupyter-Umgebung kann mehrere Register enthalten.  

Die aktuellste Version aller Versuchsanleitungen und der dazugehörigen Daten finden Sie auf dem gitlab-Server des SCC unter der Webadresse: [https://git.scc.kit.edu/etp-lehre/p1-for-students](https://git.scc.kit.edu/etp-lehre/p1-for-students). Das folgende Bild gibt Ihnen einen Vorstellung, wie die Webseite des gitlab-Servers des SCC in etwa aussieht. Beachten Sie, dass dieses Bild nicht den aktuellen Zustand des Servers wiederspiegeln muss.  

![SCC-gitlab](./figures/scc_gitlab.png)

Um das Repository des Versuchs, den Sie auf dem Jupyter-server bearbeiten wollen in Ihre Jupyter-Umgebung zu laden, gehen Sie z.B. wie folgt vor: 

- Gehen Sie im Menü Ihrer Jupyter-Umgebung auf das Verzeichnis **Git** und wählen Sie die Option **Clone a Repository** aus. 
- In einem neuen Fenster werden Sie daraufhin aufgefordert die URI-Adresse für das Repository anzugeben, das Sie klonen möchten. Diese finden Sie im [SCC Gitlab Repository](https://git.scc.kit.edu/etp-lehre/p1-for-students). Wir geben im Folgenden ein Beispiel für den P1 Vorversuch.
- Öffnen Sie das SCC Gitlab Repository des [P1 Vorversuchs](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Vorversuch) z.B. in einem neuen Reiter Ihres Browsers und klicken Sie den Knopf **Clone** (blauer Knopf, rechts im obigen Bild). Wählen Sie aus dem sich öffnenden Untermenü die Option **Clone with HTTPS** aus. Die entsprechende Webadresse wird in den Arbeitsspeicher Ihres Computers geladen.
- Wechseln Sie in Ihrem Browser wieder in den Reiter mit Ihrer Jupyter-Umgebung und geben Sie die Webadresse für das zu klonende SCC Gitlab Repository an. 
- Sie werden daraufhin nochmal gebeten sich dem SCC Gitlab Server gegenüber zu identifizieren. Verwenden Sie hierzu erneut Ihren KIT Account. 

Nach erfolgreicher Durchführung sollten Sie, dem obigen Beispiel des Repository für den P1 Vorversuch folgend, eine Verzeichnis-Struktur **p1-for-students/Vorversuch** in Ihrer Jupyter-Umgebung vorfinden. Im Verzeichnis **Vorversuch** können Sie die Durchführung und Auswertung des Versuchs beginnen. Für jeden weiteren Versuch des P1 wäre das Vorgehen den obigen Beschreibungen entsprechend.

# Arbeiten mit dem Jupyter-notebook

Das Jupyter-notebook wird in Zellen bearbeitet. Es kann sich dabei um **Textzellen** (z.B. in Markdown) oder um **Code-Zellen** handeln, in die Sie direkt Python-Code eingeben können. Eine kurze Einführung in Jupyter-notebook können Sie [hier](https://www-ekp.physik.uni-karlsruhe.de/~quast/jupyter/jupyterTutorial.html) finden. Ein Jupyter-cheat sheet finden Sie z.B. [hier](https://www.edureka.co/blog/wp-content/uploads/2018/10/Jupyter_Notebook_CheatSheet_Edureka.pdf). Für die Durchführung der Versuche des P1 können die folgenden Jupyter-*features* von Bedeutung/Nutzen für Sie sein: 

- *Esc+m*: Wechsele Zellenmodus zu Markdown

- *Esc-y*: Wechsele Zellenmodus zu Code (d.h. Python)

- Befindet sich eine Zelle im Code-Modus können Sie direkt Kommandos in Python eingeben. Das folgende Beispiel importiert die Variable $l$ aus der Datei [*parameters_task_3.py*](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Vorversuch/params/parameters_task_3.py) aus dem *params*-Verzeichnis ihrer Jupyter-Umgebung für den P1 Vorversuch und gibt den Wert der Variablen auf dem Bildschirm aus, sobald Sie die Zelle ausführen. 

  ```python
  from params.parameters_task_3 import l
  print(l)
  ```

- *Strg+Enter*: Ausführen einer Zelle.

- Sie sollten außerdem wissen, dass Sie jede der in der Verzeichnisstruktur Ihrer Jupyter-Umgebung befindlichen Dateien per Doppelklick im rechten Fenster der Umgebung öffnen, bearbeiten und nach der Bearbeitung abspeichern können. 

- Möchten Sie ein Skript aus Ihrer Jupyter-Umgebung direkt aus dem Jupyter-notebook ausführen tun Sie dies in einer Code-Zelle mit dem  [Magic command](https://ipython.readthedocs.io/en/stable/interactive/magics.html) **%run**. Im Folgenden ist z.B. gezeigt, wie man das Skript *run_phyFit.py* aus dem *tools*-Verzeichnis Ihrer Jupyter-Umgebung direkt aus einer Code-Zelle eines Jupyter-notebooks aufrufen kann: 

  ```python
  %run ./tools/run_phyFit.py --help
  ```

- Es empfiehlt sich alle angegebenen Skripte zunächst, wie oben demonstriert mit der Option *–help* aufzurufen (beachten Sie die zwei Minuszeichen). Zum einen erfahren Sie, ob sich das entsprechende Skript grundsätzlich fehlerfrei aufrufen lässt. Zum anderen erfahren Sie, wie und mit welchen weiteren Konfigurationsparametern Sie das jeweilige Skript aufrufen können. Zum Beispiel können Sie mit den folgenden weiteren Parametern das Bild der konfigurierten Anpassung direkt im Arbeitsverzeichnis Ihrer Jupyter-Umgebung in *png*-Format abspeichern:

  ```python
  %run ./tools/run_phyFit.py -s -f png yaml/data.yaml
  ```
  
  Dabei steht die Option *-s* (beachten sie das einfach Minuszeichen) für "save", also Abspeichern und die Option *-f png* für das Datenformat *png*.   

# Parameteranpassung mit dem Skript  *run_phyFit.py*

Es empfiehlt sich, bevor Sie mit der Auswertung der Versuche beginnen, sich mit der Nutzung des Skripts *run_phyFit.py* und der Struktur der notwendigen *yaml*-Datei ein wenig vertraut zu machen. Im Folgenden ist die Durchführung einer Anpassung an einen Beispieldatensatz, bestehend aus 14 freigewählten Datenpunkten, mit Hilfe der Datei [*yaml/data.yml*](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Vorversuch/yaml/data.yaml) (hier verlinkt aus dem P1 Vorversuch) gezeigt: 

Die wichtigsten Strukturelemente der *yaml*-Datei sind in den folgenden Kommentarzeilen kurz erklärt: 

```yaml
# Das ist eine Kommentarzeile schreiben Sie so viele Kommentare in Ihre yaml-Dateien, wie sie möchten! 

# Hier geben Sie den Titel des plots an, der nach der Anpassung des Modells and die Daten angezeigt werden wird.
title: "Beispiel aus Datei 'data.yaml'"
# Hier geben Sie den Titel auf der x-Achse an.
x_label: 'x-Werte'
# Hier geben Sie den titel auf der y-Achse an.
y_label: 'y-Werte'
# Dieses Label wird in der Legende angezeigt. 
label: Zufallsdaten
# Dieses sind die Werte der Beispieldaten auf der x-Achse.
x_data: [0., 0.2, 0.4, 0.6, 0.8, 1., 1.2, 1.4, 1.6, 1.8, 2., 2.2, 2.4, 2.6]
# Dieses hier sind die Unsicherheiten der Werte auf der x-Achse. Geben Sie nur eine einzige Zahl an, gilt diese als Unsicherheit für alle Werte. Dies wird die Verwendung in diesem Versuch sein. 
x_errors: [0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.055,0.06,0.065,0.07,0.075]
# Dieses sind die Werte der Beispieldaten auf der y-Achse.  
y_data: [ 1.149, 0.712, 0.803, 0.464, 0.398, 0.355, 0.148,
          0.328, 0.181, 0.140, 0.0651, 0.005, -0.005, 0.116 ]
# Hier sehen Sie nur einen Eintrag für die Unsicherheiten der Werte auf der y-Achse. Das entspricht der Verwendung in diesem Versuch.
y_errors: 0.07
# Dieses ist ein Namenslabel für das Modell, das Sie an die Daten anpassen möchten.
model_label: 'Exponential'
# Dieses ist die Modell-Funktion, die Sie an die Daten anpassen möchten. Beachten Sie das "|"-Symbol nach dem yaml-Schlüsselwort "model_function". Danach folgt die definition der Funktion in Python. Sie können alle vor-installerten Bibliotheken, wie z.B. Numpy (np) verwenden. 
model_function: |
    def exp_model(x, A=1., x0=1.):
      return A*np.exp(-x/x0)
```

Wenn Sie das Skript mit der Konfigurationsdatei *yaml/data.yaml* aus einer Code-Zelle eines Jupyter-notebook in Ihrer Jupyter-Umgebung ausführen, sollten Sie das folgende Bild erhalten: 

```python
%run ./tools/run_phyFit.py yaml/data.yaml
```

![](figures/xyData_and_Model.png)

Das Modell einer Exponentialfunktion mit den Parametern $A$ und $x_{0}$ wurde an die Datenpunkte angepasst.

Sie sollten die angepassten Parameter $A$ und $x_{0}$ der Modellfunktion, das Datenlabel, das Label der Modellfunktion und die Achsenbeschriftungen mit den entsprechenden Schlüsselworten in der *yaml*-Datei identifizieren können. 

## Ein paar Tipps für Anfänger auf diesem Gebiet: 

- *yaml* ist eine Struktursprache, die aus Paaren von beliebigen "Schlüsselworten" und "Werten" (d.h. *key-value* Paaren) besteht. Diese sind grundsätzlich durch einen Doppelpunkt voneinander getrennt. 
- Die Schlüsselworte, die wir in der oben gezeigten Datei verwenden haben nichts mit der Sprache *yaml* an sich zu tun. Die Sprache ist nur das Medium, um das Skript *run_phyFit.py* zu konfigurieren. Es handelt sich um **Schlüsselworte, die das Skript erwartet**. 
- Sie können keine Anpassung einer Funktion an Daten durchführen, wenn Sie dem Skript die Daten nicht als Werte zu den Schlüsselworten *x_data* und *y_data* bekannt machen. Ebenso erwartet das Skript Werte für die Unsicherheiten auf die Datenpunkte, die man mit den Schlüsselworten *x_errors* und *y_errors* übergibt, und eine anzupassende Modellfunktion. Diese einfachen Anforderungen erklären die Schlüsselworte, für die Sie in der *yaml*-Datei Werte zur Verfügung stellen sollten.
- Halten Sie sich exakt an die Syntax der Schlüsselworte. Die Worte *x-data*, *x_Data* oder *x_data* sind **nicht identisch**. Beachten Sie Groß- und Kleinschreibung!
- Wenn Sie für einen Wert (einfache oder doppelte) Anführungsstriche öffnen, müssen Sie diese auch mit gleichartigen Anführungsstrichen wieder schließen. Das sind klassische Tippfehler bei Programmieranfängern. 

Sie werden sehen, dass Sie den Bogen mit etwas Übung ganz gut raus bekommen werden. Falls Sie im Laufe der Versuche mit Ihren eigenen *yaml*-Dateien mal nicht klarkommen sollten vergleichen Sie sie mit der Beispieldatei oder jeder anderen funktionierenden *yaml*-Datei aus Ihrem wachsenden Fundus, bis Sie den Unterschied gefunden haben. Bei anhaltenden Problemen wendne sie sich an Ihre Tutor:innen oder die Dozenten des Praktikums. Wir helfen Ihnen jederzeit gerne weiter.  

**Anm.:** Mit der gleichen *yaml*-Datei können Sie das Skript *plotData.py* ausführen.  

# Durchführung und Auswertung

 Zur Durchführung und Auswertung des Versuchs können Sie entweder ein neues Jupyter-notebook starten (siehe Abschnitt "Arbeiten auf dem Jupyter-server"), oder Sie öffnen die Anleitung als Jupyter-notebook per Doppelklick in Ihrer Jupyter-Umgebung. 

Im letzteren Fall verwenden Sie einfach die Zellen, mit den Überschriften **"Lösung"**. Sie können den *kursiv*-gestellten Text aus den Zellen löschen. 

Vergessen Sie nicht das Jupyter-notebook bevor Sie den Kontakt zum Server schließen (z.B. mit *Strg+s*) zu speichern. Andernfalls wäre Ihre Arbeit verloren.

Sie können die fertige Auswertung zur Abgabe nach pdf formatieren. Hierzu empfehlen sich derzeit die folgenden Schritte: 

- Exportieren Sie das Jupyter-notebook nach *html*. 
- Laden Sie sich hierzu gegebenenfalls die Bilder, die in das Jupyter-notebook eingebunden werden sollen, vom Jupyter-server auf Ihren lokalen Rechner. Die einzubinden Bilddateien sollten sich dann im gleichen Verzeichnis, wie die exportierte *html*-Datei befinden.
- Sie können die *html*-Datei dann von Ihrem Browser aus z.B. nach *pdf* formatieren. Wenn das *pdf*-Format die Seiten nicht ganz einwandfrei umbricht, ist das für uns *kein Problem*. 
- Laden Sie zur Abgabe sowohl das vollständige Jupyter-notebook (einschließlich der eingebundenen Abbildungen), als auch die entsprechende pdf-Version des Jupyter-notebooks auf ILIAS hoch.  

