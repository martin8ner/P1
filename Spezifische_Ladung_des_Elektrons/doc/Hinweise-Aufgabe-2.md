# Hinweise für den Versuch Spezifische Ladung des Elektrons


## Aufgabe 2: Methode von Busch

### Beschreibung der Methode

Die Anordnung für die Bestimmung von $e/m_{e}$ nach dem Verfahren von [Hans Busch](https://de.wikipedia.org/wiki/Hans_Busch_(Physiker)) wird so betrieben, dass $\vec{B}$ **parallel** zu $\vec{E}_{z}$ ausgerichtet ist. Ohne zusätzliche Beschleunigung senkrecht zu $\vec{z}$ erfahren die Elektronen durch $\vec{B}$ also keine Ablenkung und der Elektronenstrahl erscheint als Signal in einem Punkt auf $S$. 

Wir stellen uns zunächst vor, dass eine zeitlich veränderliche, positive Spannung $U_{y}(t),$ mit Werten im Bereich $[0;U_{0}]$ an die Deflektorplatten für die Ablenkung des Elektronenstrahls in (positiver) $y$-Richtung angelegt wird. Diese Spannung führt zu einer Kreisbahn der Elektronen in der $xy$-Ebene senkrecht zu $\vec{z}$. Im Raum bilden die Trajektorien der Elektronen eine Schar von Spiralbahnen oberhalb der $z$-Achse aus. Nachdem die Elektronen die Kreisbahnen in der $xy$-Ebene vollständig durchlaufen haben, treffen sie (**unabhängig von $U_{y}$**) im Punkt $z_{0}$ wieder mit der $z$-Achse zusammen. Der genaue Wert von $z_{0}$ hängt dabei von $U_{z}$ und $B$ ab. Fällt $z_{0}$ mit der Position von $S$ entlang der $z$-Achse zusammen erscheint der Elektronenstrahl wieder als Punkt auf $S$. Für jede andere Positionen in $z\neq n\,z_{0},\hspace{0.05cm}n\in\mathbb{N}$ verlaufen die Trajektorien oberhalb der $z$-Achse. Sie nehmen dabei in einem Punkt $z_{\mathrm{max}}$ auch ihren maximalen Abstand $r_{\mathrm{max}}$ von der $z$-Achse an. Der Betrag von $r_{\mathrm{max}}$ hängt von $U_{y}(t)$ ab, das selbst (als zeitlich veränderliche Spannung) wiederum jeden Wert zwischen 0 und $U_{0}$ annehmen kann. Daher wird, wenn die Position von $S$ entlang der $z$-Achse nicht mit $z_{0}$ zusammenfällt, der Elektronenstrahl dort als Strich sichtbar. Erweitern wir den Wertebereich von $U_{y}$ auf $[-U_{0};U_{0}]$, dann erweitern wir unsere Betrachtungen um eine analoge Schar von Spiralbahnen unterhalb der $z$-Achse, die die $z$-Achse (**wieder unabhängig von $U_{y}$**) in $z_{0}$ berühren. Der Strich, wenn die Position von $S$ entlang der $z$-Achse nicht mit $z_{0}$ zusammenfällt, erweitert sich entsprechend in die negative $y$-Richtung.

In der Anordnung ist die Position von $S$ entlang der $z$-Achse fest vorgegeben. Für ebenfalls feste Werte von $U$ lässt sich $B$ so justieren, dass der Elektronenstrahl auf dem Weg vom verwendeten Deflektorzentrum $d_{i}$ zu $S$ in der $xy$-Ebene genau einen Vollkreis durchläuft und die feste Position von $S$ entlang der $z$-Achse mit $n\,z_{0},\hspace{0.05cm}n\in\mathbb{N}$ zusammenfällt.  

### Berechnung von $e/m_{e}$

Beim hier verwendeten Aufbau müssen Sie den einfachen Zusammenhang für eine als *lang* angenommene Spule aus Gleichung (**(4)** hier), der folgenden empirischen Formel
$$
\begin{equation}
\begin{split}
B(a, I, \ell)&=B_{0}
\left(0,567\left(
\frac{a}{\sqrt{R^{2}+a^{2}}}+
\frac{\ell-a}{\sqrt{R^{2}+(\ell-a)^{2}}}
\right)\right) \\ 
&
\vphantom{
\left(0,567\left(
\frac{a}{\sqrt{R^{2}+a^{2}}}+
\frac{\ell-a}{\sqrt{R^{2}+(\ell-a)^{2}}}
\right)\right)
}
=\kappa\,I \\
\end{split}
\end{equation}
$$
gemäß modifizieren. Dabei ist $a$ der Abstand von $B$ vom Spulenanfang im Eintrittspunkt $E$ auf der $z$-Achse (siehe Abbildung zum Verfahren von Busch hier), $\ell$ die Länge und $R$ der mittlere Radius der Spule; $B_{0}$ ist aus Gleichung (**(4)** hier) zu entnehmen. Einen Vergleich der mit Hilfe von Gleichung **(1)** bestimmten, erwarteten Werte von $B$ mit einer Kalibrationsmessung, für fünf verschiedene Magnetspulenströme $I$ ist in **Abb. 1** gezeigt: 

<img src="../figures/Busch-Magnetfeld.png" width="750" style="zoom:80%;" />

**Abb 1** (Vergleich von $B(a,\hspace{0.05cm}I,\hspace{0.05cm}\ell)$ aus Gleichung **(1)** mit entsprechenden Messwerten bei fünf verschiedenen Spulenströme)

---

Dabei entspricht der $0$-Punkt auf der $x$-Achse der Abbildung dem Punkt $E$; $a$ ist in $\mathrm{mm}$ und $B$ in $\mathrm{mT}$ angegeben. Die Markierungen entsprechen den Messpunkten und die gestrichelten Linien der entsprechenden Erwartung nach Gleichung **(1)**. 

Der Zusammenhang zwischen der Geschwindigkeit der Elektronen in $z$-Richtung und $U_{z}$ an der Oszillographenröhre 
$$
\begin{equation*}
v_{z} = \sqrt{2\,U\,e/m_{\mathrm{e}}}
\end{equation*}
$$
ergibt sich aus Gleichung (**(2)** hier). Für die Kreisbahn der Elektronen in der $xy$-Ebene ergibt sich: 
$$
\begin{equation}
\begin{split}
&e\,v_{e}\hphantom{/}\,\langle B\rangle = m_{e}\frac{v_{e}^{2}}{a_{\mathrm{max}}};\\
&\\
&e/m_{\mathrm{e}}\,\langle B\rangle = \frac{v_{e}}{a_{\mathrm{max}}} = \omega = 2\,\pi\frac{v_{z}}{d_{S}-d_{i}},\\
\end{split}
\end{equation}
$$
wobei $\omega$ der Kreisfrequenz der Bewegung, $d_{S}$ dem Abstand von $S$ und $d_{i}$ dem Abstand des Zentrums des gewählten Deflektorplattenpaars von $E$ entsprechen (siehe obige Abbildung zum Verfahren von Busch hier). Beachten Sie, das $\langle B\rangle$ in Gleichung **(2)** dem gemittelten Magnetfeld 
$$
\begin{equation*}
\langle B\rangle = \frac{1}{d_{S}-d_{i}} \int\limits_{d_{i}}^{d_{S}}B(a, I, N, \ell)\,\mathrm{d}a = K \,I
\end{equation*}
$$
entspricht. Der Integrationsweg ist in **Abb. 2** gezeigt: 

<img src="../figures/BuschMagnetfeld.png" width="750" style="zoom:100%;" />

**Abb 2** (Bestimmung von $\langle B\rangle$ für die Deflektorplatten in Position $d_{2}$)

---

Bei $K$ handelt es sich um einen Geometriefaktor, der vom gewählten Deflektorplattenpaar in $d_{1}$ oder $d_{2}$ abhängt. 

### Hinweise zur Durchführung

#### Aufgabe 2.1: Vorbereitung der Messung

Versorgen Sie die Oszillographenröhre innerhalb des Plexiglaszylinders über das in der obigen Abbildung gezeigte, zugehörige Steuerpult mit allen notwendigen Spannungen. Die Deflektorspannung kann wahlweise mit einem der beiden Paare von Deflektorplatten verbunden werden wobei beide Platten des ungenutzten Paares mit den Kurzschlussbrücken auf Masse gelegt werden müssen. Zur Vorbereitung der Messung gehen Sie wie folgt vor:

- Stellen Sie eine niedrige Beschleunigungsspannung (von z.B. $\approx 300\,\mathrm{V}$) ein. 
- Wählen Sie bei $B=0$ die Deflektorspannung so, dass ein maximal langer Strich auf dem Schirm erscheint. 
- Stellen Sie die Intensität und den Fokus des beobachteten Signals sinnvoll ein. 
- Steigern Sie dann langsam den Magnetspulenstrom und beobachten Sie die resultierende Bildveränderung. Diskutieren Sie deren Zustandekommen in eigenen Worten. 
- Stellen Sie schließlich den Spulenstrom so ein, dass alle Elektronen den Schirm wieder in einem Punkt treffen. Versuchen Sie auch einen höheren Spulenstrom einzustellen, bei dem sich der auf dem Schirm beobachtete Strich erneut zu einem Punkt zusammenzieht.

### Aufgabe 2.2: Bestimmung von $e/m_{\mathrm{e}}$ 

Messen Sie für Beschleunigungsspannungen von $U = 200\,\ldots 700\,\mathrm{V}$ (in Schritten von $50\,\mathrm{V}$) den nötigen Spulenstrom $I$, um auf dem Schirm einen Signalpunkt zu erzeugen. Gehen Sie dabei, für jeden Messpunkt, wie in Aufgabe 2.1 beschrieben vor. Tragen Sie $U$ über $I^{2}$ auf und ermitteln Sie $e/m_{\mathrm{e}}$ aus der Geradensteigung. 

# Navigation

[Main](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Spezifische_Ladung_des_Elektrons) | [Weiter](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Spezifische_Ladung_des_Elektrons/doc/Hinweise-Aufgabe-2-a.md)
