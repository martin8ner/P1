# Hinweise für den Versuch Vierpole und Leitungen

## Einordnung und Leitungsgleichungen

### Signalübertragung in Leitungen

Signale können über leitungsgebundene oder drahtlose Medien übertragen werden. Bei den leitungsgebundenen Medien unterscheidet man zudem zwischen Wellen- und Stromleitern. Wellenleiter basieren auf einem Leiter, wie beim [Hohlleiter](https://de.wikipedia.org/wiki/Hohlleiter), oder gar keinem Leiter, wie beim [Lichtwellenleiter](https://de.wikipedia.org/wiki/Lichtwellenleiter). Die Signalübertragung erfolgt in diesem Fall über die Leitung elektromagnetischer Wellen, Messgrößen sind die elektrische und die magnetische Feldstärke; die Beschreibung erfolgt über die [Maxwell-Gleichungen](https://de.wikipedia.org/wiki/Maxwell-Gleichungen). 

In diesem Versuch beschäftigen wir uns mit der stromleitungsgebundenen Signalübertragung. Stromleiter basieren auf mindestens zwei getrennten Leitern, einem Hin- und einem Rückleiter, wie in **Skizze 1** dargestellt: 

<img src="../figures/Leitungen.png" width="900" style="zoom:100%;" />

**Skizze 1** (Ersatzschaltbild einer (links) idealen und (rechts) realen Leitung)

---

Die Signalübertragung erfolgt in Form von Strömen und Spannungen. Die Leitung besteht aus einem gut leitenden Material, wie Kupfer oder Aluminium und idealerweise fällt über die Leitung *keine* Spannung ab. In der Realität besitzen sowohl Hin-, als auch Rückleiter einem Widerstand. Beispiele für stromleitungsgebundene Signalüberstragung sind:

- Die Leitungen, mit denen Sie die Schaltungen im Praktikum stecken.
- Das Koaxialkabel, dessen Eigenschaften Sie in diesem Versuch u.a. untersuchen werden. 
- Telegraphen und [transatlantische Telefonkabel](https://de.wikipedia.org/wiki/Transatlantisches_Telefonkabel).
- Die Kupfer [Doppelader](https://de.wikipedia.org/wiki/Doppelader) zur Übertragung von Telefon- und DSL-Signalen.
- Leitungen auf Platinen, z.B. in Computern. 

Je nach der Länge der Leitung und der Periode oder Frequenz der übertragenen Signale unterscheidet man drei Regime zur Beschreibung des Signalübertragungsprozesses:

- Im Falle von Gleichstrom genügt die Beschreibung mit Hilfe des [spezifischen Widerstands](https://de.wikipedia.org/wiki/Spezifischer_Widerstand), Querschnitts und der Länge, als primäre Eigenschaften der Leitung. 
- Im Fall von Wechselspannung, oder bei der Übertragung getakteter Signale erweist es sich als notwendig [Kapazitäten](https://de.wikipedia.org/wiki/Elektrische_Kapazit%C3%A4t) und [Induktivitäten](https://de.wikipedia.org/wiki/Induktivit%C3%A4t) der Leitung zu berücksichtigen. In diesem Fall erfolgt die Beschreibung der Signalübertragung durch die **Leitungsgleichung**. Die ist der Fall bei harmonischen Signalen deren Wellenlänge ($\lambda$) wesentlich kleiner als die Länge der Leitung ($L$) ist, und bei getakteten Signalen, deren Pulsdauer wesentlich kleiner, als die Signallaufzeit ist.  

In einem modernen Computer erfolgt die Signalübertragung mit einer Taktzahl im $3\,\mathrm{GHz}$-Bereich. In einem Kupferkabel breitet sich das elektrische Signal mit einer Geschwindigkeit von $0,7-0,9\,c$ aus. Auf Längenskalen einer Platine ($\mathcal{O}(10\,\mathrm{cm})$) ist die Anwendung der Leitungsgleichung zur adäquaten Beschreibung  der Signalübertragung also bereits notwendig.   

### Ersatzschaltbild der Leitung

Die Beschreibung einer homogenen Leitung erfolgt über ein infinitesimal kleines Leitungsstück dessen Eigenschaften in ein Ersatzschaltbild, wie in **Skizze 2** gezeigt übertragen werden. 

<img src="../figures/Leitungsschaltbild.png" width="900" style="zoom:100%;" />

**Skizze 2** (Ersatzschaltbild eines infinitesimalen realen Leitungsstücks)

---

Eine reale Leitung besitzt einen endlichen Widerstand proportional zur Länge der Leitung, der daher zweckmäßig differenziell als $R'\,\mathrm{d}z$ ausgedrückt wird. Durch den Stromfluss tritt zwischen Hin- und Rückleiter ein magnetischer Fluss $\mathrm{d}\phi$ auf, die Leitung besitzt also auch eine Induktivität $L'\,\mathrm{d}z$, die ebenfalls proportional zur Länge der Leitung ist. Ähnliches gilt für die Kapazität $C'\,\mathrm{d}z$ aufgrund der getrennten Ladungen in Hin- und Rückleiter. Schließlich ist die Isolation zwischen Hin- und Rückleiter nur endlich groß, was durch den (Isolation-)[Leitwert](https://de.wikipedia.org/wiki/Elektrischer_Leitwert) $G'\,\mathrm{d}z$ ausgedrückt wird. Die gestrichenen Größen bezeichnet man als:
$$
\begin{equation*}
\begin{split}
R' = \frac{\mathrm{d}R}{\mathrm{d}z}\qquad&:\text{ Widerstandsbelag;}\\
L' = \frac{\mathrm{d}L}{\mathrm{d}z}\qquad&:\text{ Induktivitätsbelag;}\\
C' = \frac{\mathrm{d}C}{\mathrm{d}z}\qquad&:\text{ Kapazitätsbelag;}\\
G' = \frac{\mathrm{d}G}{\mathrm{d}z}\qquad&:\text{ Leitwertsbelag;}\\\end{split}
\end{equation*}
$$
und als **primäre Leitungsparameter**. Sind diese Parameter für eine endliche Leitung bekannt kann das Verhalten der Leitung bei allen Frequenzen exakt beschrieben werden. 

Beim Ersatzschaltbild aus **Skizze 2** handelt es sich um eine spezielle Form eines **Vierpols**, der i.a. zwei Pole zum Anlegen eines Eingangssignals, sowie zwei Pole, an denen ein Ausgangssignal abgegriffen werden kann, aufweist. Der Begriff Vierpol stammt aus dem Jahre 1921 und wurde durch den Ingenieur [Franz Breisig](https://de.wikipedia.org/wiki/Franz_Breisig) geprägt. 

### Leitungsgleichungen

Um die Leitungsgleichungen abzuleiten wenden wir die [Kirchhoffschen Regeln](https://de.wikipedia.org/wiki/Kirchhoffsche_Regeln) auf das Ersatzschaltbild aus **Skizze 2**, so wie in **Skizze 3** dargestellt an:

<img src="../figures/Leitungsgleichungen.png" width="900" style="zoom:100%;" />

**Skizze 3** (Ableitung der Leitungsgleichungen)

---

Zunächst folgen wir der durch den blauen Pfeil angedeuteten *Masche* und erhalten:
$$
\begin{equation*}
\begin{split}
&U(z) = R'\,\mathrm{d}z\,I(z) + L'\,\mathrm{d}z\frac{\mathrm{d}I}{\mathrm{d}t} + U(z+\mathrm{d}z); \\
&\\
&\frac{\mathrm{d}U}{\mathrm{d}z}(z) = -R'\,I(z) - L'\frac{\mathrm{d}I}{\mathrm{d}t}(z)
\end{split}
\end{equation*}
$$
Den Strom bestimmen wir aus dem rot eingekreisten *Knoten* und erhalten:
$$
\begin{equation*}
\begin{split}
&I(z) = G'\,\mathrm{d}z\,U(z+\mathrm{d}z) + C'\,\mathrm{d}z\frac{\mathrm{d}U}{\mathrm{d}t}(z+\mathrm{d}z) + I(z+\mathrm{d}z); \\
&\\
&\frac{\mathrm{d}I}{\mathrm{d}z}(z) = -G'\,U(z) - C'\frac{\mathrm{d}U}{\mathrm{d}t}(z)
\end{split}
\end{equation*}
$$
Daraus ergeben sich zusammenfassend die **Leitungsgleichungen**:
$$
\begin{equation}
\begin{split}
&\frac{\partial U}{\partial z}(z) = -R'\,I(z) - L'\frac{\partial I}{\partial t}(z) \\
&\\
&\frac{\partial I}{\partial z}(z) = -G'\,U(z) - C'\frac{\partial U}{\partial t}(z)
\end{split}
\label{eq:Leitungsgleichungen}
\end{equation}
$$
Es handelt sich dabei um zwei gekoppelte partielle Differentialgleichungen erster Ordnung. Gekoppelt, weil in der Differentialgleichung zur Bestimmung der Spannung $U$ die Stromstärke $I$ vorkommt und umgekehrt.  

### Harmonischer Zeitverlauf

Wir lösen die Gleichungen ($\ref{eq:Leitungsgleichungen}$) für einen harmonischen Zeitverlauf, wir machen also z.B. den folgenden Ansatz für $U(z)$:
$$
\begin{equation*}
U(z, t) = U(z)\,e^{-i\,\omega\,t}
\end{equation*}
$$
Daraus ergibt sich: 
$$
\begin{equation}
\begin{split}
&\frac{\mathrm{d} U}{\mathrm{d} z}(z) = -\left(R' + i\,\omega\,L'\right)\,I(z) \\
&\\
&\frac{\mathrm{d} I}{\mathrm{d} z}(z) = -\left(G' + i\,\omega\,C'\right)\,U(z).
\end{split}
\label{eq:Leitungsgleichungen_harm}
\end{equation}
$$
Durch Differentiation der oberen Gleichung aus den Gleichungen ($\ref{eq:Leitungsgleichungen_harm}$) und einsetzen der unteren Gleichung lässt sich das Gleichungssystem entkoppeln und man erhält eine harmonische Schwingungsgleichung der Form: 
$$
\begin{equation*}
\begin{split}
&\frac{\mathrm{d}^{2}U}{\mathrm{d}z^{2}} = -\left(R' + i\,\omega\,L'\right)\,\frac{\mathrm{d}I}{\mathrm{d}z} \\
&\hphantom{\frac{\mathrm{d}^{2}U}{\mathrm{d}z^{2}}} = \hphantom{-}\underbrace{\left(R' + i\,\omega\,L'\right)\,\left(G' + i\,\omega\,C'\right)}\,U(z). \\
&\hspace{4.5cm}\equiv\rho \\
\end{split}
\end{equation*}
$$
Die für die Ausbreitung einer harmonischen Signals in einer Leitung relevanten Größen
$$
\begin{equation}
\begin{split}
&\rho = \alpha + i\beta = \left(R' + i\,\omega\,L'\right)\,\left(G' + i\,\omega\,C'\right)\\
&\\
&\rho\quad:\text{ Ausbreitungskonstante}\\
&\alpha\quad:\text{ D\"ampfungskonstante}\\
&\beta\quad:\text{ Phasenkonstante}\\
\end{split}
\end{equation}
$$
werden als **sekundäre Leitungsparameter** bezeichnet. Die Dämpfungskonstante beschreibt die Dämpfung des Signals in Ausbreitungsrichtung; die Phasenkonstante die Phasenverschiebung des Signals in Ausbreitungsrichtung. 



# Navigation

[Main](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Geometrische_Optik) | [Weiter](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische_Optik/doc/Hinweise-Aufgabe-1-a.md)
