# Arbeiten auf dem Jupyter-server

## Zugang zum Jupyter-server

Zugang zum Jupyter-server erhalten Sie über die Webadresse: [https://jupytermachine.etp.kit.edu/](https://jupytermachine.etp.kit.edu/). Als Login verwenden Sie Ihren Studierenden-Account am KIT. Wählen Sie, wenn Sie danach gefragt werden, die Option **Python** aus und starten Sie den Server. 

Falls der Zugang zum Server nicht für Sie freigeschaltet sein sollte, können Sie die Freischaltung [hier](https://comp.physik.kit.edu/Account/) veranlassen. Stellen Sie bitte **vor Praktikumsbeginn** sicher, dass Sie einen gültigen Account haben und sich entsprechend auf dem Jupyter-server einlogen können. 

## Einrichten eines Versuchs

Nach dem Start sollten Sie ein zweigeteiltes Fenster in Ihrer Jupyter-Umgebung vorfinden, wie im folgenden Bild gezeigt: 

<img src="/home/rwolf/Data/Vorlesungen/2022/2022-WS-P1/p1-for-students/figures/JupyterAccount.png" alt="figures" style="zoom:100%;" />

Auf der linken Seite befindet sich ein Navigationsfenster mit der Verzeichnisstruktur Ihrer Jupyter-Umgebung, rechts daneben befindet sich ein Fenster (der sog. *Launcher*), in dem Sie auswählen können, welche Art von Notebook Sie öffnen möchten. Sie können, wenn Sie möchten, die Option **Notebook** und **Python 3** (das erste Icon oben links im *Launcher*) anwählen. Das rechte Fenster der Jupyter-Umgebung kann mehrere Register enthalten.  

Die jeweils aktuelle Version aller Versuchsanleitungen und die dazugehörigen Daten finden Sie auf dem gitlab-Server des SCC unter den Webadressen: 

* [https://git.scc.kit.edu/etp-lehre/p1-for-students](https://git.scc.kit.edu/etp-lehre/p1-for-students). 

* [https://git.scc.kit.edu/etp-lehre/p2-for-students](https://git.scc.kit.edu/etp-lehre/p2-for-students). 

Das folgende Bild gibt Ihnen eine Vorstellung, wie die Webseite des gitlab-Servers des SCC in etwa aussieht. Beachten Sie, dass dieses Bild nicht den aktuellen Zustand des Servers widerspiegeln muss.  

![SCC-gitlab](/home/rwolf/Data/Vorlesungen/2022/2022-WS-P1/p1-for-students/figures/scc_gitlab.png)

Um das Repository des Versuchs, den Sie auf dem Jupyter-server bearbeiten wollen, in Ihre Jupyter-Umgebung zu laden, gehen Sie z.B. wie folgt vor: 

- Gehen Sie im Menü Ihrer Jupyter-Umgebung auf das Verzeichnis **Git** und wählen Sie die Option **Clone a Repository** aus. 
- In einem neuen Fenster werden Sie daraufhin aufgefordert die URI-Adresse für das Repository anzugeben, das Sie klonen möchten. Diese finden Sie im [SCC Gitlab Repository](https://git.scc.kit.edu/etp-lehre/p1-for-students) (hier verlinkt für das P1). Wir geben im Folgenden ein Beispiel für den [Vorversuch Datenverarbeitung](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Vorversuch) des P1.
- Öffnen Sie das SCC Gitlab Repository des [Vorversuchs Datenverarbeitung](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Vorversuch) des P1 z.B. in einem neuen Reiter Ihres Browsers und klicken Sie den Knopf mit der Aufschrift **Clone** (blauer Knopf, rechts im obigen Bild). Wählen Sie aus dem sich öffnenden Untermenü die Option **Clone with HTTPS** aus. Die entsprechende Webadresse wird in die Zwischenablage Ihres Computers geladen.
- Wechseln Sie in Ihrem Browser wieder in den Reiter mit Ihrer Jupyter-Umgebung und geben Sie die Webadresse für das zu klonende SCC-gitlab Repository an. 
- Sie werden daraufhin nochmal gebeten sich dem SCC-gitlab Server gegenüber zu identifizieren. Verwenden Sie hierzu erneut Ihren Studierenden-Account am KIT. 

Nach erfolgreicher Durchführung sollten Sie, dem obigen Beispiel des Repository für den Vorversuch Datenverarbeitung des P1 folgend, eine Verzeichnis-Struktur **p1-for-students/Vorversuch** in Ihrer Jupyter-Umgebung vorfinden. Im Verzeichnis **Vorversuch** können Sie die Durchführung und Auswertung des Versuchs beginnen. Für jeden weiteren Versuch des P1 (oder P2) wäre das Vorgehen den obigen Beschreibungen entsprechend.

## Arbeiten mit dem Jupyter-notebook

Das Jupyter-notebook wird in Zellen bearbeitet. Es kann sich dabei um **Textzellen** (z.B. in Markdown) oder um **Code-Zellen** handeln, in die Sie direkt Python-Code eingeben können. Eine kurze Einführung in Jupyter-notebook können Sie [hier](https://www-ekp.physik.uni-karlsruhe.de/~quast/jupyter/jupyterTutorial.html) finden. Ein Jupyter-cheat sheet finden Sie z.B. [hier](https://www.edureka.co/blog/wp-content/uploads/2018/10/Jupyter_Notebook_CheatSheet_Edureka.pdf). Für die Durchführung der Versuche des P1 (oder P2) können die folgenden Jupyter-*features* von Bedeutung/Nutzen für Sie sein: 

- *Esc+m*: Wechsele Zellenmodus zu Markdown

- *Esc-y*: Wechsele Zellenmodus zu Code (d.h. Python)

- Befindet sich eine Zelle im Code-Modus können Sie direkt Kommandos in Python eingeben. Das folgende Beispiel importiert die Variable $l$ aus der Datei [*parameters_task_3.py*](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Vorversuch/params/parameters_task_3.py) aus dem *params*-Verzeichnis ihrer Jupyter-Umgebung für den Vorversuch Datenverarbeitung des P1 und gibt den Wert der Variablen auf dem Bildschirm aus, sobald Sie die Zelle ausführen. 

  ```python
  from params.parameters_task_3 import l
  print(l)
  ```

- *Strg+Enter*: Ausführen einer (Code-)Zelle.

- Sie sollten außerdem wissen, dass Sie jede in der Verzeichnisstruktur Ihrer Jupyter-Umgebung befindliche Datei per Doppelklick im rechten Fenster der Umgebung öffnen, bearbeiten und nach der Bearbeitung abspeichern können. 

- Möchten Sie ein Python-Skript aus Ihrer Jupyter-Umgebung direkt aus dem Jupyter-notebook ausführen, tun Sie dies in einer Code-Zelle mit dem  [Magic command](https://ipython.readthedocs.io/en/stable/interactive/magics.html) **%run**. Im Folgenden ist z.B. gezeigt, wie man das Skript *run_phyFit.py* aus dem *tools*-Verzeichnis Ihrer Jupyter-Umgebung direkt aus einer Code-Zelle eines Jupyter-notebooks (hier mit der Option `–-help`) aufrufen kann: 

  ```python
  %run ./tools/run_phyFit.py --help
  ```

- Es empfiehlt sich alle angegebenen Skripte zunächst, wie oben demonstriert mit der Option `--help` aufzurufen (beachten Sie die zwei Minuszeichen). Zum einen erfahren Sie, ob sich das entsprechende Skript grundsätzlich fehlerfrei aufrufen lässt. Zum anderen erfahren Sie, wie und mit welchen weiteren Konfigurationsparametern Sie das jeweilige Skript aufrufen können. Zum Beispiel können Sie mit den folgenden weiteren Parametern das Bild der konfigurierten Anpassung direkt im Arbeitsverzeichnis Ihrer Jupyter-Umgebung in *png*-Format abspeichern:

  ```python
  %run ./tools/run_phyFit.py -s -f png yaml/data.yaml
  ```

  Dabei steht die Option *-s* (beachten Sie das einfache Minuszeichen) für "save", also Abspeichern und die Option *-f png* für das Datenformat *png*.   

