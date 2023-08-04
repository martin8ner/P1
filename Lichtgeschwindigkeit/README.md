<img src="/home/rwolf/Data/Vorlesungen/2022/2022-WS-P1/p1-for-students/Lichtgeschwindigkeit/figures/Logo_KIT.svg" style="zoom:15%;float:right;" />

# Fakultät für Physik

## Physikalisches Praktikum P1 für Studierende der Physik

Versuch P1-43, 44, 45 (Stand: November 2022)

[Raum F1-12](http://www-ekp.physik.uni-karlsruhe.de/~simonis/praktikum/layoutobjekte/Lageplan_P1.png)



# Lichtgeschwindigkeit



## Motivation

Die erste Person, die auf die Endlichkeit der Lichtgeschwindigkeit $c$ hinwies, war der dänische Astronom [Ole Rømer](https://de.wikipedia.org/wiki/Ole_R%C3%B8mer), der 1676 die Umlaufzeit des Jupytermondes [Io](https://de.wikipedia.org/wiki/Liste_der_Jupitermonde) vermaß. Abhängig von der Jahreszeit, in der er seine Beobachtungen machte stellte Rømer systematische Unterschiede in der Periode von Io fest, was er damit erklärte, dass die Ausbreitung des Lichtes nicht augenblicklich erfolgen kann. Rømers Messung der Lichtgeschwindigkeit wurde erst akzeptiert, als sie 1729 von [James Bradley](https://de.wikipedia.org/wiki/James_Bradley) bestätigt wurde. Im 19. Jahrhundert, führten Albert Michelson und Edward Morley das berühmte [Michelson-Morley-Experiment](https://de.wikipedia.org/wiki/Michelson-Morley-Experiment) durch. Ziel dieses Versuchs war der Nachweis der Existenz des [Äthers](https://de.wikipedia.org/wiki/Äther_(Physik)), eines postulierten Mediums in dem sich Lichtwellen ausbreiten, und dass den gesamten Raum gleichmäßig ausfüllt. **Dieser Versuch schlug fehl!** Stattdessen führte er zum Schluss, dass die Geschwindigkeit mit der sich das Licht im Vakuum ausbreitet fest und unveränderlich sein muss. 

Heute sind wir in der Lage die astronomischen Laborsysteme der Vergangenheit in den Praktikumsraum F1-12 zu bringen, um diese sehr wichtige Naturkonstante im Praktikum nachzumessen. Sie werden $c$ nach zwei verschiedenen Methoden bestimmen: Zum einen nach der [Drehspiegelmethode](https://de.wikipedia.org/wiki/Drehspiegelmethode) von Foucault und Michelson. Hierbei handelt es sich um eine historische Messung, die erstmals 1850/51 durchgeführt wurde. Sie werden diese Messung als Demonstrationsversuch, gemeinsam mit Ihren Kommiliton:innen und Ihrem:r Tutor:in, durchführen und auswerten. Zum anderen messen Sie $c$ mit Hilfe der Phasenverschiebung modulierter Lichtsignale (Phasenvergleichsmethode). Man kann $c$ nicht einfach mit einer Stoppuhr messen. Beide Methoden zur Messung von $c$ beruhen auf raffinierten Techniken, ohne die die jeweilige Messung nicht möglich wäre: Bei der Drehspiegelmethode ist es der Aufbau als abbildendes optisches System, bei der Phasenvergleichsmethode ist es die geschickte Modulation des Lichtstrahls zur Messung kurzer Zeitabstände.

## Lernziele

Wir listen im Folgenden die wichtigsten **Lernziele** auf, die wir Ihnen mit dem Versuch **Lichtgeschwindigkeit** vermitteln möchten: 

- Sie lernen zwei raffinierte, experimentelle Techniken zur Bestimmung einer schwierig zu messenden Größe kennen. 
- Um sich auf die Versuche vorzubereiten leiten Sie alle nötigen Zusammenhänge her und vergegenwärtigen sich die Größenordnung der zu messenden Effekte.
- Sie lernen feste Phasenbeziehungen aus der Wellenmechanik als wichtiges Werkzeug zur Messung kurzer Zeitdifferenzen kennen und wenden es in einem leicht abgewandelten Zusammenhang zur Messung des Brechungsindex optisch dichter Medien an. 
- Sie wenden das Erlernte an, um den Brechungsindex optische dichter Medien mit handelsüblichen Gebrauchsgegenständen zu bestimmen.  

## Versuchsaufbau

Der Versuch umfasst zwei unterschiedliche Aufbauten zur Messung der Lichtgeschwindigkeit. Im Folgenden sind die wichtigsten Informationen der verwendeten Aufbauten kurz zusammengefasst. Für ihre Auswertung wichtige technische Details finden Sie in der Datei Datenblatt.md. Die angegebenen Größen sind zudem in [*python*](https://www.python.org/)-Modulen im Verzeichnis [*params*](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Lichtgeschwindigkeit/params) auf dem SCC Gitlab Server hinterlegt. 

### Drehspiegelmethode

<img src="/home/rwolf/Data/Vorlesungen/2022/2022-WS-P1/p1-for-students/Lichtgeschwindigkeit/figures/Drehspiegelmethode.png" style="zoom:60%;" />

Das Licht eines Lasers wird auf einen Drehspiegel gerichtet und von dort auf ein System aus einem Umlenk- und einem Endspiegel reflektiert. Der Strahlengang verläuft vom Laser zum Endspiegel und wieder zurück. Vor dem Laser befindet sich ein um $45^{\circ}$ zur Strahlachse gedrehter, halbdurchlässiger Spiegel als Strahlteiler, der einen Teil des reflektierten Lichts auf einen Schirm mit Ableseskala und Mikroskop umlenkt. Die Skala wird mit Hilfe eines USB-Mikroskops auf einem Bildschirm angezeigt (siehe Bild unten links in der zugehörigen [Skizze](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Lichtgeschwindigkeit/figures/Drehspiegelmethode.png)). Zwischen Dreh- und Umlenkspiegel befindet sich eine Linse zur Verringerung der Divergenz des Lichtstrahls der auf den Endspiegel abgebildet wird. Im Zeitfenster $\Delta t$ zwischen seinem ersten und zweiten Auftreffen auf den Drehspiegel hat ein angenommenes Lichtpaket, nach den Angaben der obigen Skizze, die Wegstrecke $2\,(a+b)$ zurückgelegt. Der Drehspiegel hat sich in dieser Zeit um den Winkel $\Delta\alpha$ weiter gedreht. Dadurch erscheint der auf den Schirm gelenkte Lichtstrahl im Vergleich zum Fall des ruhenden Drehspiegels versetzt. Der Versatz hängt von der Geschwindigkeit des Lichtpakets $c$ und der Frequenz $\nu$ ab, mit der sich der Drehspiegels dreht. Die Brennweite der Linse, sowie die festen Abstände zwischen dem Laser und den jeweiligen Spiegeln sind in der zugehörigen [Skizze](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Lichtgeschwindigkeit/figures/Drehspiegelmethode.png) angegeben. 

#### Wichtige Hinweise zu diesem Versuchsaufbau

- Die Strahlung des verwendeten Lasers der [Klasse 2](https://de.wikipedia.org/wiki/Laser#Laserklassen) ist **gefährlich für Ihre Augen!** Sie sind daher angehalten während des Versuchs eine der ausgelegten Laserschutzbrillen tragen. Beachten Sie unsere [Hinweise zum sicheren Umgang mit Lasern](https://labs.physik.kit.edu/163.php?tab=%5B313%5D#tabpanel-313).
- Diese Messung führen Sie, als **Demonstrationsversuch**, mit Ihren Kommiliton:innen und Ihrem:r Tutor:in gemeinsam durch. 

### Phasenvergleichsmethode

<img src="/home/rwolf/Data/Vorlesungen/2022/2022-WS-P1/p1-for-students/Lichtgeschwindigkeit/figures/Phasenvergleichsmethode.png" style="zoom:60%;" />

Diese Methode zur Messung der Lichtgeschwindigkeit basiert auf der Messung der Phasenverschiebung $\Delta\varphi$ zwischen einem Empfänger- und einem Referenzsignal. Aus $\Delta\varphi$ lässt sich bei gegebener Kreisfrequenz $\omega$ des Referenzsignals eine Zeitdifferenz $\Delta t$ bestimmen und bei bekanntem Abstand $\ell$ zwischen Sender und Empfänger so die Lichtgeschwindigkeit berechnen. Eine monochromatische Lichtquelle (Sender) ist beweglich auf eine $\approx2\,\mathrm{m}$ lange Führungsschiene montiert. Ihr Licht wird mit Hilfe einer Sammellinse auf eine feststehende Photodiode (Empfänger) abgebildet. Ein $60\,\mathrm{MHz}$-Frequenzgenerator erzeugt ein Referenzsignal, mit dem die Intensität der Leuchtdiode des Senders moduliert wird. Die Lichtgeschwindigkeit ergibt sich aus der Phasenverschiebung $\Delta\varphi$ zwischen dem Empfänger- und Referenzsignal als Funktion des Abstandes zwischen Sender und Empfänger. 
