# Hinweise für den Versuch Spezifische Ladung des Elektrons


## Aufgabe 1: Fadenstrahlrohr [1/2]

### Elektronenstrahl im homogenen Magnetfeld

In einem homogenen Magnetfeld der Stärke $\vec{B}$ wird der Elektronenstrahl senkrecht zu seiner Bewegungsrichtung durch die [Lorentzkraft](https://de.wikipedia.org/wiki/Lorentzkraft) abgelenkt, wie in **Skizze 1** dargestellt:

<img src="../figures/LadungMagnetfeld.png" width="500" style="zoom:100%;" />

**Skizze 1** (Bahn des Elektrons im Magnetfeld)

---

Für den Fall  $\vec{v}_{e}\perp\vec{B}$ gilt: 
$$
e\,B\,v = m_{\mathrm{e}}\,\frac{v_{\mathrm{e}}^{2}}{r}, \qquad \frac{e}{m_{\mathrm{e}}}= \frac{v_{\mathrm{e}}}{B\,r},
$$
wobei $B=|\vec{B}|$, $v_{\mathrm{e}}$ der Geschwindigkeit der Elektronen und $r$ dem Radius des Strahls entsprechen. Aus der am Fadenstrahlrohr anliegenden Beschleunigungsspannung $U$ lässt sich $v_{\mathrm{e}}$ wie folgt bestimmen:
$$
e\,U = \frac{m\,v_{\mathrm{e}}^{2}}{2}, \qquad v_{\mathrm{e}} = \sqrt{2\,U\,\frac{e}{m_{\mathrm{e}}}}.
$$
Aus den Gleichungen **(1)** und **(2)** ergibt sich daraus der Zusammenhang
$$
\frac{8\,U}{B^{2}} = \frac{e}{m_{\mathrm{e}}}\,\frac{1}{d^{2}},
$$
aus dem sich $e/m_{\mathrm{e}}$ als Steigung einer Ursprungsgeraden bestimmen lässt, wenn man auf der $x$-Achse $1/d^{2}$ und auf der $y$-Achse $8\hspace{0.05cm}U/B^{2}$ aufträgt. Dabei bezeichnet $d$ den Durchmesser der Kreisbahn.

### Magnetfeld einer langen Spule

Das Magnetfeld einer langen Spule lässt sich mit Hilfe des [Ampèreschen Gesetzes](https://de.wikipedia.org/wiki/Amp%C3%A8resches_Gesetz#Magnetfeld_der_Spule) leicht berechnen: 
$$
\begin{equation}
B(I, N, \ell) = \mu_{0}\,\frac{N\,I}{\ell},
\end{equation}
$$
wobei $\mu_{0}$ der [magnetischen Feldkonstanten](https://de.wikipedia.org/wiki/Magnetische_Feldkonstante), $I$ dem Strom durch die Spule, $N$ der Anzahl der Windungen und $\ell$ der Länge der Spule entsprechen. Die Berechnung erfolgt über den [Satz von Stokes](https://de.wikipedia.org/wiki/Satz_von_Stokes), wie in **Skizze 2** angedeutet: 

<img src="../figures/Stokes.png" width="500" style="zoom:100%;" />

**Skizze 2** (Integrationspfad zur Anwendung des Satzes von Stokes)

---

Im Inneren der langen Spule $\vec{B}$ parallel zur Symmetrieachse der Spule. Außerhalb fällt $\vec{B}$ sehr schnell ab. Schließt man den Integrationpfad $\mathcal{C}$ in einem Bogen, der sich weit genug von der Spule entfernt befindet kann dort $\vec{B}=0$ angenommen werden. Daraus folgt: 
$$
\begin{equation*}
\oint\limits_{\mathcal{C}}\vec{B}\cdot\mathrm{d}\vec{s} = B\,\ell = \mu_{0}\,N\,I
\end{equation*}
$$

### Magnetfeld im Inneren zweier Helmholtzspulen

Unter der Bedingung, das der Abstand zwischen zwei [Helmholtz-Spulen](https://de.wikipedia.org/wiki/Helmholtz-Spule) $H_{1}$ und $H_{2}$ dem Radius $R$ der Spulen entspricht ist davon auszugehen, dass die [Stärke des Magnetfelds $B(r)$ auf der radialen Symmetrieachse des Spulenpaares](https://de.wikipedia.org/wiki/Helmholtz-Spule#Berechnung_der_magnetischen_Flussdichte) besonders homogen ist. Dabei bezeichnet $r$ den radialen Abstand von der Symmetrieachse der Spulen. 

In diesem Fall erwartet man nach dem [Gesetz von Biot-Savart](https://de.wikipedia.org/wiki/Biot-Savart-Gesetz) die Feldstärke
$$
\begin{equation}
B(r=0) = \frac{8}{\sqrt{125}}\,\frac{\mu_{0}\,N\,I}{R},
\end{equation}
$$
wobei $I$ dem Strom durch das Spulenpaar und $N$ der Anzahl der Windungen pro Spule entsprechen. Dieser Formel liegt die Annahme zugrunde, dass beide Spulen in allen in Gleichung **(2)** auftauchenden Parametern baugleich sind.

### Hall-Effekt

Wird ein stromdurchflossenes ausgedehntes Leiterstück senkrecht zum Stromfluss $\vec{j}$ von einem Magnetfeld $\vec{B}$ durchsetzt kommt es durch die Wirkung der Lorentzkraft im Leiter zur Ladungstrennung, wie in **Skizze 3** dargestellt: 

<img src="../figures/HallEffekt.png" width="500" style="zoom:100%;" />

**Skizze 2** (Mikroskopisches Modell des Hall-Effekts)

---

Durch die getrennten Ladungen baut sich eine Spannung $U_{\mathrm{H}}$, die Hall-Spannung senkrecht zu $\vec{j}$ auf für die im Gleichgewichtszustand gilt: 
$$
\begin{equation*}
\begin{split}
&e\,v_{e}\,B = e\,E_{\mathrm{H}};
&\\
&\\
&E_{\mathrm{H}}=\frac{U_{\mathrm{H}}}{d}; \qquad v_{e}=\frac{I}{A\,n_{e}};\qquad A=d\,b \\
&\\
&\\
&U_{H} = \frac{I\,B}{b\,n_{e}}
\end{split}
\end{equation*}
$$
 wobei $B=\vec{B}$, $n_{e}$ der Ladungsträgerdichte im Leiter und $b$ der Breite des Leiterstücks entsprechen, es gilt also $U_{\mathrm{H}}\propto B$. 

### Hinweise zur Durchführung

### Aufgabe 1.1: Magnetfeld im Fadenstrahlrohr

Das Magnetfeld $\vec{B}$ des Fadenstrahlrohrs wird durch zwei im Plexiglaskasten verbaute stromdurchflossene [Helmholtz-Spulen](https://de.wikipedia.org/wiki/Helmholtz-Spule) $H_{1}$ und $H_{2}$ erzeugt. Da der Raum zwischen $H_{1}$ und $H_{2}$ für eine Messung unzugänglich ist schätzen Sie $\vec{B}$ wie folgt ab:

- Bauen Sie symmetrisch zu $H_{1}$ und $H_{2}$, vor dem Plexiglaskasten eine baugleiche dritte Helmholtz-Spule $H_{3}$ und eine mit Bohrungen versehene Holzplatte $M$ mit Millimeter-Skala auf, so dass sich $M$ in der Mittelebene zwischen $H_{2}$ und $H_{3}$ befindet. Dies ist i.a. durch die feste Konstruktion vor dem Plexiglaskasten bereits der Fall. Achten Sie dennoch auf den Abstand zwischen $H_{2}$ und $H_{3}$, der dem Radius der Spulen entsprechend sollte!
- Schließen Sie $H_{2}$ und $H_{3}$ an die Stromversorgung an. Die Anordnung gleicht somit in ihrer Geometrie der Anordnung von $H_{1}$ und $H_{2}$. 
- In den Bohrungen von $M$ können Sie die [Hall-Sonde](https://de.wikipedia.org/wiki/Hall-Effekt) befestigen. Messen Sie die Hall-Spannung $U_{\mathrm{H}}$ an den vorgesehenen Stellen für die Spulenströme $1,0\hspace{0.05cm}\mathrm{A}$, $1,5\hspace{0.05cm}\mathrm{A}$ und $2,0\hspace{0.05cm}\mathrm{A}$. Nutzen Sie hierzu alle zu Verfügung stehenden Bohrungen.
- Der angezeigte Wert von $U_{\mathrm{H}}$ hängt von der Temperatur der Hall-Sonde ab. Achten Sie daher während des Betriebs darauf, dass die Sonde nicht allzu starken Temperaturänderungen ausgesetzt ist. Lassen Sie die Sonde z.B. nicht allzu lange eingeschaltet.

Kalibrieren Sie daraufhin die Hall-Sonde mit Hilfe von Gleichung **(4)**. Gehen Sie dabei wie folgt vor: 

- Messen Sie etwa **10 Wertepaare** aus $U_{\mathrm{H}}$ und dem Strom $I$ durch die lange Spule, die Ihnen zur Kalibration der Hall-Sonde zur Verfügung steht.  
- Aus der Stromstärke $I$ können Sie mit Hilfe von Gleichung **(4)** $B=|\vec{B}|$ berechnen. Bestimmen Sie aus den aufgezeichneten Datenpunkten eine Eichgerade $B(U_{\mathrm{H}})$. 
- Mit Hilfe dieser Eichgeraden können Sie die in Aufgabe 1.1 bestimmten Werte von $U_{\mathrm{H}}$ in magnetische Feldstärken $B(U_{\mathrm{H}})$ übersetzen. 

Die Kalibration erfolgt **nach der eigentlichen Ausmessung** des Magnetfeldes mit der Hall-Sonde, damit Sie wissen, welcher Wertebereich von $U_{\mathrm{H}}$ für die Kalibration von Relevanz ist.  

### Aufgabe 1.2: Durchmesser der Elektronenkreisbahnen im Fadenstrahlrohr

Messen Sie den Durchmesser $d=2\,r$ der Kreisbahn des Elektronenstrahls im Fadenstrahlrohr. 

<img src="../figures/FadenstrahlrohrSchaltung.png" width="750" style="zoom:100%;" />

**Skizze 3** (Schaltplan zur Verkabelung des Fadenstrahlrohrs)

---

Gehen Sie dabei wir folgt vor:

- Bauen Sie die Spule $H_{3}$ ab und schließen Sie das Fadenstrahlrohr, wie in **Skizze 3** angegeben an. 
- Benutzen Sie an den vorgesehenen Stellen die vorhandenen Sicherheitskabel. Sie benötigen nur die grau markierten Spannungsanschlüsse.

- Versuchen Sie den [Parallaxenfehler](https://de.wikipedia.org/wiki/Parallaxenfehler) bei der Bestimmung von $d$ mit Hilfe der Schiebemarker vor, und des Spiegels hinter dem Fadenstrahlrohr zu minimieren. 
- Achten Sie darauf, dass das Fadenstrahlrohr so in der Halterung orientiert ist, dass sich Kreisbahnen und keine Spiralen ergeben.
- Stellen Sie die Ergebnisse beider Messreihen in einem geeigneten gemeinsamen Koordinatensystem dar und bestimmen Sie daraus den Wert von $e/m_{\mathrm{e}}$.


# Navigation

[Main](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Spezifische_Ladung_des_Elektrons) | [Weiter](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Spezifische_Ladung_des_Elektrons/doc/Hinweise-Aufgabe-1-a.md)
