# Hinweise für den Versuch Datenverarbeitung am Beispiel des Pendles

## Hinweise zur Durchführung

- Bei so großen Datenmengen ist eine manuelle Weiterverarbeitung der Daten unmöglich. Verwenden Sie dazu die Programmiersprache [python](https://www.python.org/). Sie können python direkt in Programmierzellen des Jupyter-notebook einbinden. Eine Kurzanleitung zu Verwendung von Jupyter-notebook auf dem Jupyter-server der Fakutät finden Sie in der Datei [Jupyter-server.md](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/doc/Jupyter-server.md). 

- Wir empfehlen weiterhin das Programmpaket [kafe2](https://philfitters.github.io/kafe2/), das Sie aus der Vorlesung *Computergestützte Datenanalyse* (CgDa) kennen oder —wenn Sie mit der Verwendung von kafe2 noch nicht allzu vertraut sein sollten— die Modulsammlung [PhyPraKit](https://readthedocs.org/projects/phyprakit/) zur Anpassung an die Daten und zur Visualisierung. Es handelt sich um **die einzigen Programmpakete die Ihnen erlauben (ohne Expertenkonfiguration) die verlangten Anpassungen, allen Anforderungen gemäß, durchzuführen.** 

- Beachten Sie, dass wir für Modellanpassungen an Daten in der Physik i.a. ein Maß für die Güte der Anpassung ([*goodness of fit*, GoF](https://en.wikipedia.org/wiki/Goodness_of_fit)) verlangen, und dass die Anpassung nicht nur einen Zentralwert, sondern auch ein verlässliches [Konfidenzintervall](https://de.wikipedia.org/wiki/Konfidenzintervall) zurückgeben muss. Beides ist weder für die Standardbibliotheken von [scipy](https://scipy.org/) noch für [Origin](https://de.wikipedia.org/wiki/Origin_(Software)) der Fall. Zur Visualisierung können Sie alternativ auch [matplotlib](https://matplotlib.org/) verwenden. 

- Sowohl kafe2, als auch PhyPraKit sind bereits auf dem Jupyter-server der Fakultät vorinstalliert und können *out-of-the-box* verwendet werden. Eine Kurzanleitung zur Verwendung von kafe2 finden Sie in der Datei [kafe2.md](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/doc/kafe2.md). Eine Kurzanleitung zur Verwendung der Modulsammlung PhyPraKit finden Sie in der Datei [PhyPraKit.md](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/doc/PhyPraKit.md). Darüber hinaus stehen Ihnen beide Programmpakete überall [offen und frei](https://de.wikipedia.org/wiki/Open_Source) zur Verfügung. 

- Die Daten, wie sie original aus dem Smartphone ausgelesen wurden finden Sie in der Datei 

  ```shell
  data_raw.csv
  ```

  vor. Die Anwendung phyphox hat die Beschleunigungssensoren des Smartphones mit einer festen [Abtastrate](https://de.wikipedia.org/wiki/Abtastung_(Signalverarbeitung)) (engl. *sampling rate*) von $100\,\mathrm{Hz}$ ausgelesen. Um die Eigenschaften der Schwingung für uns ausreichend gut erfassen zu können haben wir $5\,\mathrm{min}$ lang gemessen. Sie können sich schnell klarmachen welche Datenmenge dabei aufgelaufen ist. Die Periode der Schwingung haben wir während des Versuchs zu $\text{1–2}\,\mathrm{s}$ abgeschätzt. Wir haben daher als ersten Schritt zur Aufbereitung der Daten die Signalrate um den Faktor 10 reduziert, indem wir nur jede 10. Zeile der csv-Datei ausgelesen haben. Man bezeichnet diese Vorgehensweise als *down sampling*.  Den so prozessierten Datensatz finden Sie in der Datei

  ```shell
  data_down_sampled.csv,
  ```

  die Sie für alle weiteren Versuchsteile nutzen sollten. Sie kennen das Vorgehen des *down sampling* aus der Vorlesung *Computergestützte Datenauswertung* CgDa. Zusätzlich haben wir die ersten und letzten Sekunden des Experiments aus den Betrachtungen ausgeschlossen: 

  - In den ersten Sekunden unterlag die Messung Störungen des Anstoßes, die mit zunehmender Zeit abklingen. 
  - In den letzten Sekunden war die Schwingung durch Unregelmäßigkeiten in der Keillage des ausschwingenden Pendels gestört.  

- Beachten Sie, dass die Skripte *plotData.py* und *run_phyFit.py* aus der PhyPraKit Modusammlung die Eingangs- und Konfigurationsdaten nicht im csv-Format sondern in der Struktursprache [yaml](https://de.wikipedia.org/wiki/YAML)  erwarten. Die Notwendigkeit Daten um zu formatieren ist ein häufiges Problem in der Datenverarbeitung. Sie können zur Umformatierung das Skript *cvs2yaml.py* verwenden.

