<img src="./figures/Logo_KIT.svg" style="zoom:15%;float:right;" />

# Fakultät für Physik

## Physikalisches Praktikum P1 für Studierende der Physik

Versuch P1-43, 44, 45 (Stand: November 2022)

[Raum F1-12](http://www-ekp.physik.uni-karlsruhe.de/~simonis/praktikum/layoutobjekte/Lageplan_P1.png)



# Lichtgeschwindigkeit



## Motivation

Die erste Person, die auf die Endlichkeit der Lichtgeschwindigkeit hinwies, war der dänische Astronom [Ole Rømer](https://de.wikipedia.org/wiki/Ole_R%C3%B8mer), der 1676 die Umlaufzeit des Jupytermondes [Io](https://de.wikipedia.org/wiki/Liste_der_Jupitermonde) vermaß. Abhängig von der Jahreszeit, in der er seine Beobachtungen machte stellte Rømer systematische Unterschiede in der Periode von Io fest, was er damit erklärte, dass die Ausbreitung des Lichtes nicht augenblicklich erfolgen kann. Rømers Messung der Lichtgeschwindigkeit wurde erst akzeptiert, als sie 1729 von [James Bradley](https://de.wikipedia.org/wiki/James_Bradley) bestätigt wurde. Im 19. Jahrhundert, führten Albert Michelson und Edward Morley das berühmte [Michelson-Morley-Experiment](https://de.wikipedia.org/wiki/Michelson-Morley-Experiment) durch. Ziel dieses Versuchs war der Nachweis der Existenz des [Äthers](https://de.wikipedia.org/wiki/Äther_(Physik)), eines postulierten Mediums in dem sich Lichtwellen ausbreiten und dass den gesamten Raum gleichmäßig ausfüllt. Dieser Versuch schlug fehl. Stattdessen führte er zu dem Schluss, dass die Geschwindigkeit mit der sich das Licht im Vakuum ausbreitet fest und unveränderlich sein muss. 

Heute sind wir in der Lage die astronomischen Laborsysteme der Vergangenheit in den Praktikumsraum F1-12 zu bringen, um diese sehr wichtige Naturkonstante im Praktikum nachzumessen. Wir messen die Lichtgeschwindigkeit bei diesem Versuch nach zwei verschiedenen Verfahren: Zum einen nach der [Drehspiegelmethode](https://de.wikipedia.org/wiki/Drehspiegelmethode) von Foucault und Michelson. Hierbei handelt es sich um eine historische Messung, die erstmals 1850/51 durchgeführt wurde. Zum anderen nach einer Phasenvergleichsmethode.

## Anmerkungen zum Versuch Lichtgeschwindigkeit

Wir listen im Folgenden die wichtigsten **Lernziele** auf, die wir Ihnen mit dem Versuch **Lichtgeschwindigkeit** vermitteln möchten: 

- Sie lernen beide Methoden zur Messung der Lichtgeschwindigkeit kennen. 
- Sie vergegenwärtigen sich die subtilen Unterschiede beider Messungen. Machen Sie sich z.B. klar, welche Geschwindigkeit Sie mit dem jeweiligen Verfahren messen, die Gruppen- oder die Phasengeschwindigkeit. Erwarten Sie unterschiedliche Ergebnisse für die Messungen nach dem einen oder anderen Verfahren?
- Sie lernen die Größenordnung der zur Messung herangezogenen Effekte im Vorfeld abzuschätzen, so dass Sie mit einer gut informierten Erwartung an jede Aufgabe herangehen können.
- Aufgrund der hohen Geschwindigkeit des Lichts sind die erwarteten Effekte klein. Sie lernen intelligente, experimentelle Techniken kennen, um diese Effekte trotzdem sicht- und für die Messung im Praktikum nutzbar zu machen. 
- In Ihrer Auswertung sollten Sie die experimentellen, technischen Grenzen und die Quellen der dominanten Unsicherheiten beider Messverfahren sorgfältig diskutieren und beide Verfahren in dieser Hinsicht kritisch miteinander vergleichen.  

## Versuchsaufbau

Der Versuch umfasst zwei unterschiedliche Aufbauten zur Messung der Lichtgeschwindigkeit. Im Folgenden sind die wichtigsten Informationen der verwendeten Aufbauten kurz zusammengefasst. Die angegebenen Größen sind zudem in python-Modulen im Verzeichnis *params* auf dem SCC Gitlab hinterlegt. 

### Drehspiegelmethode

<img src="./figures/Drehspiegelmethode.png" style="zoom:60%;" />

Das Licht eines Lasers ist auf einen Drehspiegel gerichtet und wird von dort auf ein System aus einem Umlenk- und einem Endspiegel reflektiert. Der Drehspiegel kann in einem Frequenzbereich bis $450\,\mathrm{Hz}$ betrieben werden. Der Strahlengang verläuft vom Laser zum Endspiegel und wieder zurück. Vor dem Laser befindet sich ein um $45^{\circ}$ zur Strahlachse gedrehter, halbdurchlässiger Spiegel als Strahlteiler, der einen Teil des reflektierten Lichts auf einen Schirm mit Ableseskala umlenkt. Die Skala wird mit Hilfe eines USB-Mikroskops auf einem Bildschirm angezeigt (siehe Bild unten links in der zugehörigen Skizze). Zwischen Dreh- und Unlenkspiegel befindet sich eine Linse zur Verringerung der Divergenz des Lichtstrahls mit dem der Laser auf den Endspiegel abgebildet wird. Im Zeitfenster $\Delta t$ zwischen seinem ersten und zweiten Auftreffen auf den Drehspiegel hat ein angenommenes Lichtpaket, nach den Angaben der obigen Skizze, die Wegstrecke $2\,(a+b)$ zurückgelegt. Der Drehspiegel hat sich in dieser Zeit um den Winkel $\Delta\alpha$ weiter gedreht. Dadurch erscheint der auf den Schirm gelenkte Lichtstrahl im Vergleich zum ruhenden Drehspiegel versetzt. Der Versatz hängt von der Geschwindigkeit des Lichtpakets und der Winkelgeschwindigkeit des Drehspiegels ab. Die Brennweite der Linse, sowie die festen Abstände zwischen dem Laser und den jeweiligen Spiegeln sind in der zugehörigen Skizze angegeben. 

Weitere technische Daten sind im Folgenden angegeben:  

- Als **Lichtquelle** dient ein [Klasse 2](https://de.wikipedia.org/wiki/Laser#Laserklassen) He-Ne-Laser mit einer Strahlleistung etwa $1\,\mathrm{mW}$, einem Strahldurchmesser $\approx0,8\,\mathrm{mm}$ und einer Strahldivergenz von $1\,\mathrm{mrad}$.
- Der **Drehspiegel** ist $1\,\mathrm{cm}$ breit, $2\,\mathrm{cm}$ hoch und zweiseitig spiegelnd beschichtet. Er wird mit einem Regeltransformator betrieben, der eine maximale Frequenz von  $\approx450\,\mathrm{U/s}$ erlaubt. Ein Frequenzzähler erlaubt die Bestimmung der eingestellten Frequenz. Zur unabhängigen Kalibration in einem Punkt steht eine Stimmgabel für den Kammerton "A" bei $440\,\mathrm{Hz}$ mit Resonanzkasten und Anschlaghammer zur Verfügung.
- Beim **Umlenk- und Endspiegel** handelt es sich jeweils um einen [Planspiegel](https://de.wikipedia.org/wiki/Planspiegel) mit einem Radius von $r>100\,\mathrm{m}$ und einem Durchmesser $d=11,5\,\mathrm{cm}$. 
- Die **Sammellinse** im Strahlengang hat eine Brennweite von $f=5\,\mathrm{m}$ und einen Durchmesser von $d=11,5\,\mathrm{cm}$.  
- Die Aufbauten um **Schirm und USB-Mikroskop** sind mit einem halbdurchlässigen Spiegel, einer weiteren Sammellinse (mit Brennweite $f=10\,\mathrm{cm}$ und Durchmesser $d=3,8\,\mathrm{cm}$), einem Glasmaßstab mit $\mathrm{mm}$-Teilung vor einer Mattglasscheibe und einem Filterglas ausgestattet.

### Phasenvergleichsmethode

<img src="./figures/Phasenvergleichsmethode.png" style="zoom:60%;" />

Eine monochromatische Lichtquelle (im Folgenden auch "Sender" genannt) ist mittels einer $\approx2\,\mathrm{m}$ langen Führungsschiene beweglich montiert. Ihr Licht wird mit Hilfe einer Sammellinse auf die feststehende Empfängerdiode abgebildet. Ein $60\,\mathrm{MHz}$-Frequenzgenerator steuert den Sender und liefert ein Referenzsignal. Die Lichtgeschwindigkeit ergibt sich aus der abstandsabhängigen Phasenverschiebung $\Delta\varphi$ zwischen Empfänger und Referenzsignal. Um $\Delta\varphi$ deutlich sichtbar zu machen werden beide Signale jeweils mit einem Signal der Frequenz $59,9\,\mathrm{MHz}$ multiplikativ gemischt. Mittels eines Tiefpassfilters werden die hochfrequenten Anteile des gemischten Signals unterdrückt und die niederfrequenten Anteile auf einem einfachen computergestützten Oszilloskop, als Funktion der Zeit dargestellt. Die Phasenbeziehung zwischen Empfänger- und Referenzsignal bleibt dabei erhalten. Beachten Sie hierzu Anmerkung 2.1

Weitere technische Daten sind im Folgenden angegeben:  

- **Hauptnetzgerät** (siehe weißer Kasten auf den Bildern unten rechts, orangefarbener Kasten auf dem Bild oben rechts in der zugehörigen Skizze) mit einem $60$ und einem $59,9\,\mathrm{MHz}$-Frequenzgenerator, mit entsprechenden Mischstufen zur multiplikativen Mischung des Empfänger- und Referenzsignals. Im Hauptnetzgerät befindet sich eine **Photodiode** ($\approx13\,\mathrm{mm}$ hinter der Frontplatte des Geräts), als Empfänger. Das Gerät hat zwei Ausgänge für das Oszilloskop und einen Ausgang zum Betrieb der Sender-Lichtquelle. 
- Eine **Sammellinse** (mit Brennweite $f=20\,\mathrm{cm}$ und Durchmesser $d=3,8\,\mathrm{cm}$ dient zur Fokussierung des Lichts auf die Photodiode.
- Die **Lichtquelle** des Senders ist eine rote Leuchtdiode in einem Gehäuse (siehe Bild unten links in der zugehörigen Skizze). Das Gehäuse ist justierbar und mit einer verschiebbaren [Kondensorlinse](https://de.wikipedia.org/wiki/Kondensor) versehen.

- Beim **Oszilloskop** handelt es sich um ein computergestütztes Picoscope mit der Möglichkeit des [Zweikanal-](https://de.wikipedia.org/wiki/Oszilloskop#Mehrkanalbetrieb) und des X/Y-Betriebs. Die Ausgabe auf den Monitor kann man auf dem Bild oben rechts in der zugehörigen Skizze sehen.

- Zudem stehen die folgenden Materialen für die Durchführung des Versuchs zur Verfügung: ein mit Wasser gefülltes Rohr mit Endfenstern (Innenlänge $994\,\mathrm{mm}$, Glasdicke $2\times3\,\mathrm{mm}$, einfach vorhanden); zwei Plexiglaszylinder (Länge $8\,\mathrm{cm}$ und $30\,\mathrm{cm}$), mit polierten Stirnflächen und Ständer (einfach vorhanden); Laserentfernungsmesser (Typ: [Bosch DLE40](https://www.laserentfernungsmesser-test.de/tests/bosch-dle-40-blau-laserentfernungsmesser-test/), Messgenauigkeit $\pm1,5\,\mathrm{mm}$); verschiedene [Küvetten](https://de.wikipedia.org/wiki/K%C3%BCvette) (Grundfläche: $100\,\mathrm{mm} \times 50\,\mathrm{mm}$) für Wasser und Silikonöl.

## Anmerkungen zu den Versuchen

- Die Apparatur für die Messung der Lichtgeschwindigkeit nach der Drehspiegelmethode (Aufgabe 1) ist nur einfach vorhanden. Diese Messung muss daher nacheinander von den Gruppen durchgeführt werden.
- Besprechen Sie die Methoden zur Auswertung direkt mit dem Betreuer.

## Aufgabe 1: Drehspiegelmethode

### Aufgabe 1.1: Vorbereitung

Diskutieren Sie das Messverfahren, sowie Aufbau und Eigenschaften des konkreten Strahlengangs basierend auf den oben gemachten Angaben zum Versuchsaufbau. Ihre Diskussion sollte die folgenden Punkte und Fragen berücksichtigen: 

- Welche Aufgabe erfüllt die Linse? 
- Wo sollten Sie die Linse im Strahlengang positionieren, damit sie den Ausgang des Lasers auf den Endspiegel abbildet? Verwenden Sie dazu die [Linsengleichung](https://de.wikipedia.org/wiki/Linsengleichung) und machen Sie sich klar, wie Sie die Gegenstands- und Bildweite jeweils aus den oben gemachten Angaben berechnen können. 
- Wieso ruht der beobachtete Leuchtfleck während der Messung auf der Skala, obwohl sich der Spiegel kontinuierlich dreht? 
- Leiten Sie die Formel zur Berechnung der Lichtgeschwindigkeit für den konkreten Fall her und schätzen Sie die Größe des erwarteten Versatzes relativ zum ruhenden Drehspiegel ab. 

Bei den Berechnungen handelt es sich um wichtige Vorbereitungen für die Durchführung des Versuchs.

### Aufgabe 1.2: Justierung der Apparatur und Messung

**Vollziehen Sie für sich die Justierung der Apparatur nach**. Gehen Sie dabei entlang des Strahlengangs, wie folgt, vor: 

- *Laser – Drehspiegel*: Der horizontal ausgesandte Laserstrahl sollte den ruhenden Drehspiegel mittig treffen und horizontal wieder verlassen. 
- *Drehspiegel – Umlenkspiegel*: Richten Sie den Drehspiegelwinkel so aus, dass der reflektierte Strahl (noch ohne Linse) auf die Mitte des Umlenkspiegels fällt. Decken Sie hierzu den Endspiegel ab.
- *Umlenkspiegel – Endspiegel*: Richten Sie den Umlenkspiegel so aus, dass der Strahl auf die Mitte des Endspiegels fällt. 
- *Linse*: Richten Sie die Linse gemäß Ihren Berechnungen aus Aufgabe 1.1 aus. 
- *Endspiegel – Umlenkspiegel*: Richten Sie den Endspiegel so aus, dass der Strahl in sich reflektiert wird (beachten Sie die Lichtflecke auf dem Umlenkspiegel). 
- *Kontrolle und Feinjustierung*: Stellen Sie durch Feinabstimmung sicher, dass der zurückkehrende Strahl den Drehspiegel und die Laseraustrittsöffnung trifft. 
- *Schirm und USB-Mikroskop*: Positionieren Sie das USB-Mikroskop hinter dem Schirm mit der Skala. Laser und Skala sind gleich weit vom Strahlteiler entfernt. 
- *Frequenzmessung am Drehspiegel*: Positionieren Sie den Phototransistor für die Messung der Rotationsfrequenz des Drehspiegels.

Beachten Sie hierzu Anmerkung 1.2. 

**Messung der Lichtgeschwindigkeit**. Tragen Sie den Ort des beobachteten Lichtpunkts als Funktion der Rotationsfrequenz des Drehspiegels auf und bestimmen Sie aus dem in Aufgabe 1.1 bestimmten funktionalen Zusammenhang den Wert $c$ der Lichtgeschwindigkeit. Zur Kalibration des Frequenzzählers in einem Punkt stellen Sie die Rotationsfrequenz des Drehspiegels von $440\,\mathrm{Hz}$ anhand der auftretenden Schwebung zwischen dem Motorengeräusch des Drehspiegels und dem Stimmgabelton für den Kammerton "A" ein und vergleichen Sie den erhaltenen Wert mit der elektronischen Frequenzanzeige. Diskutieren Sie systematische und statistische Unsicherheiten bei der Bestimmung von $c$ und bestimmen Sie die Unsicherheit $\Delta c$ auf den bestimmten Wert.

## Anmerkungen zu Aufgabe 1

### Anmerkung 1.1 – **Achtung**

Die Strahlung des verwendeten Lasers ([Klasse 2](https://de.wikipedia.org/wiki/Laser#Laserklassen)) ist, wenn Sie direkt in den Strahl hinein blicken **gefährlich für Ihre Augen!** Dies ist insbesondere der Fall, da Sie mit Spiegeln arbeiten. Bei ruhendem (oder sehr langsam rotierendem) Spiegel müssen Sie daher zu Ihrem eigenen Schutz eine der ausgelegten Schutzbrillen tragen.

### Anmerkung 1.2  

Optische Apparaturen sind sehr sensibel. Eine grundsätzliche Neujustierung kann mehrere Stunden dauern. Während des P1 sollten Sie die Justierung nach Möglichkeit also so belassen, wie Sie sie vorfinden. 

## Lösung:

*Sie können Ihre Lösung/Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.*

## Aufgabe 2: Phasenvergleichsmethode

Diese Methode zur Messung der Lichtgeschwindigkeit basiert auf der Messung der Phasenverschiebung $\Delta\varphi$ zwischen dem Empfänger- und Referenzsignal. Aus $\Delta\varphi$ lässt sich bei gegebener Kreisfrequenz $\omega$ des Referenzsignals eine Zeitdifferenz $\Delta t$ bestimmen und bei bekanntem Abstand $\ell$ zwischen Sender und Empfänger so die Lichtgeschwindigkeit berechnen.   

### Aufgabe 2.1: Vorbereitung

Beantworten Sie zur Vorbereitung auf den Versuch die folgenden Fragen: 

- Welche Größenordnung sollte die Frequenz $\nu$ der Lichtwelle haben, damit Sie zwischen Empfänger- und Referenzsignal eine Phasendifferenz von $\Delta\varphi=0,2\,\pi$, d.h. einem $1/10$ der Periodendauer, auflösen können? 
- Welche Ablenkgeschwindigkeit $v_{\mathrm{Osz.}}$ sollte ein Oszilloskop entlang der Zeitachse haben, damit eine solche Phasenverschiebung zu einer wahrnehmbaren Verschiebung z.B. von $\Delta d=5\,\mathrm{mm}$ führt? Vergleichen Sie Ihre Abschätzung mit der Ablenkgeschwindigkeit $v_{\mathrm{Osz.}}\lesssim 10\,\mathrm{cm/\mu s}$ eines einfachen Oszilloskops. Welche Schlussfolgerung ziehen Sie daraus? Beachten Sie hierzu Anmerkung 2.1.

### Aufgabe 2.2: Justierung der Apparatur

Überprüfen Sie die Verbindungskabel anhand des Anschlussschemas auf der Frontplatte des Hauptnetzgeräts. Richten Sie mit Hilfe der Justierschrauben zur Zentrierung der Leuchtdiode des Senders und des verschiebbaren Kondensors am Lichtsendergehäuse einen möglichst parallelen Strahl vom Sender in Richtung des Empfängers ein. Stellen Sie die Sammellinse vor der Photodiode des Empfängers so auf, dass die Photodiode optimal ausgeleuchtet wird. Beachten Sie hier zu Anmerkung 2.2. 

### Aufgabe 2.3: Lichtgeschwindigkeit und Brechungsindex

Absolvieren Sie das folgende Messprogramm: 

#### Aufgabe 2.3.1

Überprüfen und notieren Sie mit dem Oszilloskop die Differenzfrequenz $(\omega-\omega')$. Dabei entspricht $\omega=2\,\pi\cdot60\,\mathrm{MHz}$ der Kreisfrequenz des für die Messung verwendeten Referenzsignals und $\omega' = 2\,\pi\cdot59,9\,\mathrm{MHz}$ der Kreisfrequenz des beigemischten Signals zum Zweck der Amplitudenmodulation. Beachten Sie hierzu Anmerkung 2.1. Für eine zuverlässige Frequenzmessung benötigt das Oszilloskop mehrere vollständige Wellenzüge im Anzeigebereich.

#### Aufgabe 2.3.2

Messen Sie die zeitliche Differenz $\Delta t$ zwischen Sender und Empfänger als Funktion von deren Abstand $\ell$ aus der Phasenverschiebung $\Delta\varphi$ zwischen Empfänger- und Referenzsignal. Beachten Sie den Zeitdehnungsfaktor aus Gleichung (4) in Anmerkung 2.1. Entnehmen Sie der Auftragung die Lichtgeschwindigkeit $c$ in Luft mit entsprechender Unsicherheit $\Delta c$ und diskutieren Sie die Quellen der dominanten Unsicherheiten.

#### Aufgabe 2.3.3

Bestimmen Sie den Brechungsindex $n_{\mathrm{H_{2}O}}$von Wasser aus der Messung der Laufzeitdifferenz, wenn $1\,\mathrm{m}$ Lichtweg in Luft durch $1\,\mathrm{m}$ Lichtweg in Wasser ersetzt wird.

Bestimmen Sie analog den Brechungsindex $n_{\mathrm{Plex}}$ von Plexiglas mit Hilfe der $8$ und $30\,\mathrm{cm}$ langen Plexiglaszylinder.

#### Aufgabe 2.3.4

Bestimmen Sie die Lichtgeschwindigkeit in Luft durch Messung von $\lambda /2$ mit Hilfe von [Lissajous-Figuren](https://de.wikipedia.org/wiki/Lissajous-Figur) im X/Y-Betrieb des Oszilloskops. Da Sie fast die gesamte zur Verfügung stehende Strecke der Führungsschiene benötigen, müssen Sie bei minimalem Abstand die Phase am Betriebsgerät geeignet einstellen.

## Anmerkungen zu Aufgabe 2

### Anmerkung 2.1 – Messbereichserweiterung des Oszilloskops

Mit der Zeitauflösung eines einfachen Oszilloskops ist die beabsichtigte Messung nicht ohne weiteres möglich. Hier zeigen wir Ihnen, wie Sie die Messung trotzdem mit den im Praktikum zur Verfügung stehenden Mitteln durchführen können: 

 Hierzu nutzen wir eines der [Additionstheoreme](https://de.wikipedia.org/wiki/Formelsammlung_Trigonometrie#Produkte_der_Winkelfunktionen) der Kosinus-Funktion: 
$$
\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta,
$$
woraus sich der folgende Zusammenhang leicht ableiten lässt: 
$$
\cos\alpha\cos\beta = \frac{1}{2}\Bigl(\cos(\alpha+\beta)+\cos(\alpha-\beta)\Bigr).
$$
Wir wählen zur Beschreibung des funktionalen Zusammenhangs des Referenzsignals oder des Signals am Empfänger eine Kosinusfunktion $\cos(\omega\,t+\varphi)$, wobei $\omega$ der Kreisfrequenz und $\varphi$ einer freien Phase entsprechen. Wir modulieren (mit Hilfe der Mischstufen des Hauptnetzgeräts) die Amplituden der Signale an den Eingängen des Oszilloskops für das Empfänger- und Referenzsignal multiplikativ mit der gleichen, geringfügig kleineren Frequenz $\omega'\lesssim\omega$ , woraus sich für das Signal auf dem Oszilloskop der folgende funktionale Zusammenhang ergibt: 
$$
\cos(\omega\,t+\varphi)\cos(\omega'\,t) = \frac{1}{2}\Bigl(\cos((\omega+\omega')\,t+\varphi) + \cos((\omega-\omega')\,t+\varphi)\Bigr).
$$
Wir interessieren uns für den zweiten Term in der Klammer auf der rechten Seite von Gleichung (3), der den Verlauf $\cos((\omega-\omega')\,t+\varphi)$ aufweist. Der hochfrequente Term $\cos((\omega+\omega')\,t+\varphi)$ wird durch einen Tiefpassfilter unterdrückt. 

Die Phase $\varphi$ wird unverändert vom unmodulierten Eingangssignal der Form $\cos(\omega\,t+\varphi)$ auf den Term $\cos((\omega-\omega')\,t+\varphi)$ übertragen, so dass auch die feste Phasenbeziehung zwischen Empfänger- und Referenzsignal erhalten bleibt. Eine Phasendifferenz $\Delta\varphi_{\mathrm{Ein.}}$ im unmodulierten Eingangssignal entspricht so der gleichen Phasendifferenz $\Delta\varphi_{\mathrm{Osz.}}$ in der Darstellung auf dem Oszilloskop.  Der Verlauf auf der Zeitachse des Oszilloskops erscheint konsistent um den Faktor  
$$
\Delta t_{\mathrm{Osz.}} = \frac{\omega}{\omega-\omega'}\,\Delta t_{\mathrm{Ein.}}
$$
gedehnt, wobei $\Delta t_{\mathrm{Osz.}}$ dem auf dem Oszilloskop dargestellten Zeitfenster (mit dem Verlauf $\cos((\omega-\omega')\,t+\varphi)$) und $\Delta t_{\mathrm{Ein.}}$ dem Zeitfenster des Eingangssignals (mit dem Verlauf $\cos(\omega\,t+\varphi)$) entsprechen. Durch den gedehnten Maßstab können auch sehr kurze Zeitdifferenzen im Eingangssignal aufgelöst werden. Es handelt sich dabei also effektiv um eine "Messbereichserweiterung" des Oszilloskops hin zu kürzeren Zeitabständen.

### Anmerkung 2.2

Zur erfolgreichen Durchführung dieses Versuchs achten Sie auf die sorgfältige Justierung der Apparatur insbesondere bei großen Abständen von Sender und Empfänger. Stellen Sie sicher, dass das Lichtsignal des Senders auch bei maximalem Abstand zwischen Sender und Empfänger noch erkannt wird. Das Empfängersignal sollte bei jedem Abstand zwischen Sender und Empfänger ausreichend groß sein. Die Amplitude am Empfänger sollte bei allen Entfernungen $\pm2\,\mathrm{V}$ jedoch nicht überschreiten, weil die internen Mischerstufen der Elektronik sonst übersteuern und dabei die Phasenlage verfälschen.

### Anmerkung 2.3

Für Aufgabe 2.3 sollte die Anfangsphasenlage per Stellknopf vernünftig gewählt werden. 

## Lösung:

*Sie können Ihre Lösung/Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.*

## Aufgabe 3: Laserentfernungsmesser

Heute benutzt fast jeder Handwerker oder Architekt einen handelsüblichen Laserentfernungsmesser um z.B. den Abstand zweier Wandflächen eines Neubaus zu vermessen. Wir wollen zum Abschluss dieses Versuchs viel einfacher als in Aufgabe 2 mit einem solchen Gerät die Brechungsindizes verschiedener Medien bestimmen. Stellen Sie dazu die bereitstehenden Küvetten jeweils einmal längs und einmal quer in den Strahlengang zwischen dem Entfernungsmesser und einem beliebigen Reflektor. Berechnen Sie aus den vom Gerät „falsch“ angezeigten Entfernungen den jeweiligen Brechungsindex. Bei intelligenter Durchführung können Sie die Messung so mit minimalen zusätzlichen Informationen erhalten. 

## Lösung:

*Sie können Ihre Lösung/Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.*

