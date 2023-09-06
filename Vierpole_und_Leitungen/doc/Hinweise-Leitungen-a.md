# Hinweise für den Versuch Vierpole und Leitungen

## Einordnung und Leitungsgleichungen

### Das $\pi$-Glied

Im folgenden betrachten wir einen idealen Vierpol, ohne ohmsche Widerstände, für den wir die Leitungskapazität ($C$) symmetrsich rechts und links von der Leitungsimpedanz ($L$), wie in **Skizze 4** dargestellt, aufteilen: 

<img src="../figures/PiGlied.png" width="900" style="zoom:100%;" />

**Skizze 4** (Schaltbild eines idealen Vierpols mit symmetrisch aufgeteilter Kapazität ($C$) rechts und links der Lastimpedanz ($L$) ($\pi$-Glied))

---

Das rechte Ende der Leitung wird mit einer Lastimpedanz $Z_{\mathrm{A}}=U_{1}/I_{1}$ kurzgeschlossen. Für die Impedanzen der Leitung gilt in diesem Fall: 
$$
\begin{equation}
\begin{split}
&Z_{\mathrm{L}} = i\,\omega\,L; \\
&Z_{\mathrm{C}} = \frac{2}{i\,\omega\,C}; \\
\end{split}
\end{equation}
$$
Aus den [Kirchhoffschen Regeln](https://de.wikipedia.org/wiki/Kirchhoffsche_Regeln) ergibt sich für diese Schaltung:
$$
\begin{equation*}
I_{0} = \frac{U_{0}}{Z_{\mathrm{C}}}+I_{\mathrm{L}}
\end{equation*}
$$
(aus dem Knoten links der Induktivität), 
$$
\begin{equation*}
I_{\mathrm{L}} = \frac{U_{1}}{Z_{\mathrm{C}}}+I_{1}
\end{equation*}
$$
(aus dem Knoten rechts der Induktivität) und
$$
\begin{equation*}
U_{0} = Z_{\mathrm{L}}\,I_{\mathrm{L}}+U_{1} 
\end{equation*}
$$
(aus der Schleife um $Z_{\mathrm{A}}$). Durch Einsetzen lässt sich damit der Zusammenhang zwischen dem Eingangssignal ($U_{0}$ und $I_{0}$) und dem Ausgangsignal ($U_{1}$ und $I_{1}$) herstellen: 
$$
\begin{equation}
\begin{split}
U_{0} &= Z_{\mathrm{L}}\left(\frac{U_{1}}{Z_{\mathrm{C}}}+I_{1}\right)+U_{1} \\
&= \left(\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}+1\right)U_{1}+Z_{\mathrm{L}}\,I_{1};\\
&\\
&\\
I_{0} &= \left(\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}+1\right)I_{\mathrm{L}} + \frac{U_{1}}{Z_{\mathrm{C}}} = \left(\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}+1\right)\left(\frac{U_{1}}{Z_{\mathrm{C}}}+I_{1}\right) + \frac{U_{1}}{Z_{\mathrm{C}}}\\
&=\frac{1}{Z_{\mathrm{C}}}\left(\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}+2\right)U_{1} + \left(\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}+1\right)I_{1}.\\

\end{split}
\end{equation}
$$
Die Impedanz $Z_{\mathrm{E}}$ am Signaleingang hängt also von der Lastimpedanz $Z_{\mathrm{A}}$ am Signalausgang ab. Greift man das Ausgangssignal mit einer **charakteristischen Impedanz**
$$
\begin{equation}
Z_{0}=\frac{\sqrt{\frac{L}{C}}}{\sqrt{1-\left(\frac{\omega}{\omega_{0}}\right)^{2}}} \qquad \text{mit:}\quad\omega_{0}=\frac{2}{\sqrt{L\,C}}
\end{equation}
$$
ab, die dem **Wellenwiderstand** der Vierpolschaltung entspricht gilt $Z_{\mathrm{E}}=Z_{\mathrm{A}}=Z_{0}$, d.h. Eingangs- und Ausgangsimpedanz nehmen den gleichen Wert, nämlich den des Wellenwiderstands an. 

Unter Verwendung von $Z_{0}$ lassen sich die Gleichungen (**2**) wie folgt umformen: 
$$
\begin{equation}
\begin{split}
U_{0} &= \left(\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}+1\right)U_{1}+Z_{\mathrm{L}}\,I_{1};\\
&\\
&\\
I_{0} &=\frac{Z_{\mathrm{L}}}{Z_{0}^{2}}\,U_{1} + \left(\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}+1\right)I_{1}.\\

\end{split}
\end{equation}
$$
Hierzu bietet es sich an $Z_{0}$ zunächst, unter Verwendung der Gleichungen (**1**), nach $Z_{\mathrm{L}}$ und $Z_{\mathrm{C}}$ auszudrücken:
$$
\begin{equation*}
\begin{split}
&Z_{0}=\frac{\sqrt{\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}Z_{\mathrm{L}}\,Z_{\mathrm{C}}}}{\sqrt{2+\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}}\\
\end{split}
\end{equation*}
$$
In Matrixschreibweise gehen die Gleichungen (**5**) in die folgende Form 
$$
\begin{equation}
\begin{split}
&\left(\begin{array}{c}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}U_{0}\\\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}Z_{0}\,I_{0}\end{array}\right) = 
\left(\begin{array}{cc}\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}+1 & \frac{Z_{\mathrm{L}}}{Z_{0}}\\ \frac{Z_{\mathrm{L}}}{Z_{0}} & \frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}+1\end{array}\right)\cdot 
\left(\begin{array}{c}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}U_{1}\\\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}Z_{0}\,I_{1}\end{array}\right)\\
&\\
&\left(\begin{array}{c}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}U_{1}\\\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}Z_{0}\,I_{1}\end{array}\right) = 
\left(\begin{array}{cc}\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}+1 & -\frac{Z_{\mathrm{L}}}{Z_{0}}\\ -\frac{Z_{\mathrm{L}}}{Z_{0}} & \frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}+1\end{array}\right)\cdot 
\left(\begin{array}{c}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}U_{0}\\\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}Z_{0}\,I_{0}\end{array}\right)\\
\end{split}
\end{equation}
$$
über, in der die Matrix 
$$
\begin{equation*}
\begin{split}
&\mathcal{T} = \left(\begin{array}{cc}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}\hphantom{-}\cosh\gamma & \vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}-\sinh\gamma\\ -\sinh\gamma & \hphantom{-}\cosh\gamma\end{array}\right)\\
&\\
&\text{mit:}\\
&\\
&\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}+1\equiv\cosh\gamma;\qquad
\frac{Z_{\mathrm{L}}}{Z_{0}}\equiv\sinh\gamma\\
\end{split}
\end{equation*}
$$
den Übergang
$$
\begin{equation*}
\left(\begin{array}{c}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}U_{0}\\\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}Z_{0}\,I_{0}\end{array}\right) \longrightarrow 
\left(\begin{array}{c}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}U_{1}\\\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}Z_{0}\,I_{1}\end{array}\right).
\end{equation*}
$$
beschreibt. Die komplexwertige Größe $\gamma=\alpha+i\,\beta$ kann mit der **Ausbreitungskonstanten** identifiziert werden.

Für $\omega\to\omega_{0}$ nimmt die Übergangsmatrix die Form
$$
\begin{equation*}
\left(\begin{array}{cc}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}\hphantom{-}\cosh\gamma & \vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}-\sinh\gamma\\ -\sinh\gamma & \hphantom{-}\cosh\gamma\end{array}\right)
%\longrightarrow 
\xrightarrow{\omega\to\omega_{0}}
\left(\begin{array}{cc}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}-1 & \hphantom{-}0 \\ \hphantom{-}0 & -1\end{array}\right),
\end{equation*}
$$
an, die Ausgangsgrößen weisen gegenüber den Eingangsgrößen also eine Phasenverschiebung um $\pi$ auf, welshalb die hier betrachtete Schaltung auch als $\pi$-Glied bezeichnet wird.  

### Ideale Drosselkette

Der Übergang vom Vierpol zur (idealen) Drosselkette erfolgt durch $n$-facher Hintereinanderschaltung von $\pi$-Gliedern, wie in **Skizze 5** dargestellt: 

<img src="../figures/Drosselkette.png" width="900" style="zoom:100%;" />

**Skizze 5** (Schaltbild einer idealen Drosselkette, bestehend aus $n$ $\pi$-Gliedern)

---

Der Transfer
$$
\begin{equation*}
\left(\begin{array}{c}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}U_{0}\\\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}Z_{0}\,I_{0}\end{array}\right) \longrightarrow 
\left(\begin{array}{c}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}U_{n}\\\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}Z_{0}\,I_{n}\end{array}\right).
\end{equation*}
$$
erfolgt durch mehrfache Multiplikation mit $\mathcal{T}$:
$$
\begin{equation*}
\left(\begin{array}{c}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}U_{n}\\\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}Z_{0}\,I_{n}\end{array}\right) = \mathcal{T}^{n}\cdot
\left(\begin{array}{c}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}U_{0}\\\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}Z_{0}\,I_{0}\end{array}\right) = 
\left(\begin{array}{cc}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}\hphantom{-}\cosh(n\gamma) & \vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}-\sinh(n\gamma)\\ -\sinh(n\gamma) & \hphantom{-}\cosh(n\gamma)\end{array}\right)
\cdot
\left(\begin{array}{c}\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}U_{0}\\\vphantom{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}}Z_{0}\,I_{0}\end{array}\right)
\end{equation*}
$$
 Als Spannungsübertragung ergibt sich also
$$
\begin{equation*}
\frac{U_{n}}{U_{0}} = \cosh(n\gamma)-Z_{0}\frac{I_{0}}{U_{0}}\sinh(n\gamma)
\end{equation*}
$$
und für den Spezialfall $Z_{\mathrm{E}}=Z_{\mathrm{A}}=Z_{0}$
$$
\begin{equation*}
\begin{split}
\frac{U_{n}}{U_{0}} &= \cosh(n\gamma)-\sinh(n\gamma) \\
&= e^{-n\gamma} = e^{-n\alpha}e^{-i\,n\beta}
\end{split}
\end{equation*}
$$
Für eine harmonische Schwingung am Eingang ergibt sich daraus:
$$
\begin{equation*}
\begin{split}
&U_{0}(t) = \hat{U}_{0}e^{i\,\omega t};\\
&\\
&U_{n}(t) = \hat{U}_{0}e^{-n\alpha}e^{i\,\left(\omega t-n\beta\right)}\\
\end{split}
\end{equation*}
$$
$n\alpha$ ist also als **Dämpfungskonstante** und $n\beta$ als **Phasenkonstante** der Drosselkette aus $n$ $\pi$-Giedern zu erkennen. 

# Navigation

[Main](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Vierpole_und_Leitungen) | [Weiter](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Vierpole_und_Leitungen/doc/Hinweise-Leitungen-a.md)
