# Hinweise für den Versuch Kreisel

## Aufgabe 1: Physik starrer Körper [1/2]

### Von Winkelgeschwindigkeit bis Trägheitstensor

Zur Beschreibung der Dynamik des Massepunkts in der Mechanik verwenden wir die physikalischen Größen Geschwindigkeit $\vec{v}$, Impuls $\vec{p}$ und Kraft $\vec{F}$. Mit dem Kreisel betrachten wir einen ausgedehnten, starren Körper, in Rotation, zu dessen Beschreibung wir zu $\vec{v}$, $\vec{p}$ und $\vec{F}$ äquivalente Größen heranziehen:  

- Das Äquivalent zu $\vec{v}$ ist die **Winkelgeschwindigkeit** $\vec{\omega}$; 
- das Äquivalent zu $\vec{p}$ ist der **Drehimpuls** $\vec{L}$; und 
- das Äquivalent zu $\vec{F}$ ist das **Drehmoment** $\vec{M}$.  

Für ein gegebenes Massenelement $\delta m$ wird der Zusammenhang dieser Größen zueinander durch das äußere Produkt ([Kreuzprodukt](https://de.wikipedia.org/wiki/Kreuzprodukt)) "$\times$" mit dem Ortsvektor $\vec{r}$ des Massenelements hergestellt: 
$$
\begin{equation*}
\vec{v} = \vec{r}\times \vec{\omega}; \qquad
\vec{L} = \vec{r}\times \vec{p}; \qquad
\vec{M} = \vec{r}\times \vec{F}. \\
\end{equation*}
$$
Ein Zusammenhang zwischen $\vec{L}$ und $\vec{\omega}$ ergibt sich aus
$$
\begin{equation}
\vec{L} = \vec{r}\times\vec{p} = \delta m\left(\vec{r}\times\vec{v}\right) = \delta m\left(\vec{r}\times\left(\vec{r}\times\vec{\omega}\right)\right).
\end{equation}
$$
Um das doppelte Kreuzprodukt in Gleichung **(1)** weiter zu verstehen, können wir auf eine Regel aus der [analytischen Geometrie](https://de.wikipedia.org/wiki/Analytische_Geometrie) (die sog. "bac-cab"-Regel) zurückgreifen:
$$
\begin{equation*}
\vec{a}\times\vec{b}\times\vec{c} = \big(\vec{b}\cdot\vec{a}\big)\,\vec{c} - \big(\vec{c}\cdot\vec{a}\big)\,\vec{b}
\end{equation*}
$$
Das Kreuzprodukt $\vec{b}\times\vec{c}$ kann durch einen Vektor $\vec{\kappa}$ beschrieben werden, der senkrecht auf die aus $\vec{b}$ und $\vec{c}$ aufgespannte Ebene steht. Das erneute Kreuzprodukt $\vec{a}\times\vec{\kappa}$ führt auf einen Vektor, der wiederum in diese Ebene fällt. Als Konsequenz kann dieser Vektor als eine Linearkombination aus $\vec{b}$ und $\vec{c}$ geschrieben werden. Die Linearkombination ergibt sich aus den vorangestellten [Skalarprodukten](https://de.wikipedia.org/wiki/Skalarprodukt). 

Anwendung auf Gleichung **(1)** führt auf: 
$$
\begin{equation}
\begin{split}
&\vec{L} = \delta m\left(r^{2}\vec{\omega} - \big(\vec{\omega}\cdot\vec{r}\big)\vec{r}\right)\\
&\\
&L_{i} = \underbrace{\delta m\left(r^{2}\delta_{ij} - r_{i}r_{j}\right)}\omega_{j}.\\
&\hphantom{L_{i} = \delta m\,r^{2}\,\,}\equiv \Theta_{ij}\\
\end{split}
\end{equation}
$$
In der zweiten Zeile von Gleichung **(2)** haben wir die Vektoren komponentenweise ausgeschrieben, wobei $i$ und $j$ jeweils unabhängigen Indizes entsprechen. Die komponentenweise Darstellung von Gleichung **(2)** zeigt, dass sich die Komponenten $L_{i}$ durch die lineare Abbildung
$$
\begin{equation*}
L_{i} = \Theta_{ij}\,\omega_{j}
\end{equation*}
$$
aus den Komponenten $\omega_{j}$ ergeben. Dabei kann, je nach Struktur von $\Theta_{ij}$ **jede Komponente** von $\vec{\omega}$ zum Wert jeder Komponente von $\vec{L}$ beitragen. Die Größe
$$
\begin{equation*}
\boldsymbol{\Theta} \equiv \left(\Theta_{ij}\right)
\end{equation*}
$$
bezeichnen wir als [Trägheitstensor](https://de.wikipedia.org/wiki/Tr%C3%A4gheitstensor). Aufgrund seines Transformationsverhaltens unter Drehungen im Raum handelt es sich um einen Tensor 2. Stufe. Konkret als Matrix ausgeschrieben hat $\boldsymbol{\Theta}$ die Form: 
$$
\begin{equation}
\boldsymbol{\Theta} = \delta m
\left(
\begin{array}{ccc}
r^{2}-x^{2} & x\,y & x\,z \\
y\,x & r^{2}-y^{2} & y\,z \\
z\,x & z\,y & r^{2}-z^{2} \\
\end{array}
\right)
\end{equation}
$$

### Bestimmung von $\vec{L}$ aus $\vec{\omega}$ als Eigenwertproblem  

Bei Gleichung **(2)** handelt es sich um ein gekoppeltes [lineares Gleichungssystem](https://de.wikipedia.org/wiki/Lineares_Gleichungssystem) der Form
$$
\begin{equation}
\left(
\begin{array}{c}
L_{x} \\
L_{y} \\
L_{z} \\
\end{array}
\right)
=
\left(
\begin{array}{ccc}
\Theta_{xx} & \Theta_{xy} & \Theta_{xz} \\
\Theta_{yx} & \Theta_{yy} & \Theta_{yz} \\
\Theta_{zx} & \Theta_{zy} & \Theta_{zz} \\
\end{array}
\right)
\cdot
\left(
\begin{array}{c}
\omega_{x} \\
\omega_{y} \\
\omega_{z} \\
\end{array}
\right)
\end{equation}
$$
für das $\boldsymbol{\Theta}$ einer linearen Abbildung von $\mathbb{R}^{3}\to\mathbb{R}^{3}$ in der Darstellung einer $3\times3$-Matrix entspricht. In bestimmten Fällen kann ein solches Gleichungssystem, durch geeignete Transformationen 
$$
\begin{equation*}
\boldsymbol{\widetilde{\Theta}} = \bold{U}^{-1}\cdot\boldsymbol{\Theta}\cdot\bold{U}
\end{equation*}
$$
entkoppelt werden, so dass $\boldsymbol{\widetilde{\Theta}}$ die Form einer [Diagonalmatrix](https://de.wikipedia.org/wiki/Diagonalmatrix) annimmt. Die Suche nach solchen Abbildungen $\bold{U}$ bezeichnet man als [Eigenwertproblem](https://de.wikipedia.org/wiki/Eigenwerte_und_Eigenvektoren). Die Matrix $\bold{U}$ führt die Basisvektoren des Vektors 
$$
\begin{equation*}
\vec{\tilde{\omega}} = \bold{U}\cdot\vec{\omega}
\end{equation*}
$$
bis auf die Multiplikation mit dem Eigenwert $\theta_{i}$ in sich selbst über. Die Transformation $\bold{U}$ entspricht also einem Wechsel in eine Einheitsbasis, die durch $\boldsymbol{\widetilde{\Theta}}$ in sich selbst abgebildet wird. 

Wie Sie sich selbst aus Gleichung **(3)** überzeugen können besitzt der Trägheitstensor die Eigenschaft **symmetrisch** zu sein, was für die Lösung des Eigenwertproblems weitreichende Konsequenzen hat: 

- Für symmetrische Abbildung ist das Eigenwertproblem **immer lösbar**. Unter den Eigenwerten kann jedoch [Entartung](https://de.wikipedia.org/wiki/Eigenwerte_und_Eigenvektoren#Berechnung_der_Eigenwerte) vorliegen. 
- Die Eigenwerte sind **immer reell**.
- Die durch die zugehörigen Eigenvektoren aufgespannten Unterräume stehen **immer senkrecht aufeinander**.

Die Matrizen $\bold{U}$ zur Diagonalisierung von $\boldsymbol{\Theta}$ sind Rotationsmatrizen $\bold{R}$ mit der definierenden Eigenschaft: 
$$
\begin{equation*}
\bold{R}^{-1} = \bold{R}^{\intercal}.
\end{equation*}
$$
In diesem Fall hat die Lösung des Eigenwertproblems also eine **anschauliche geometrische Bedeutung**: 

Es ist die Drehung von einem allgemeinen in ein spezielles Bezugssystem, in dem die Eigenvektoren des Problems parallel zu den [Hauptträgheitsachsen](https://de.wikipedia.org/wiki/Haupttr%C3%A4gheitsachse) des starren Körpers verlaufen. Diese Achsen sind durch die Form und Massenbelegung des Körpers vorgegeben. 

Das Eigenwertproblem erhält aufgrund dieser Besonderheiten den eigenen Namen [Hauptachsentransformation](https://de.wikipedia.org/wiki/Hauptachsentransformation). Nach Hauptachsentransformation hat Gleichung **(4)** die einfache Form: 
$$
\begin{equation}
\left(
\begin{array}{c}
L_{x} \\L_{y} \\L_{z} \\
\end{array}
\right)
=
\left(
\begin{array}{ccc}
\theta_{x} & 0 & 0 \\
0 & \theta_{y} & 0 \\
0 & 0 & \theta_{z}\\
\end{array}
\right)
\cdot
\left(
\begin{array}{c}
\omega_{x} \\
\omega_{y} \\
\omega_{z} \\
\end{array}
\right),
\end{equation}
$$
oder in Komponentenschreibweise
$$
\begin{equation*}
L_{i} = \theta_{i}\,\delta_{ij}\,\omega_{j}.
\end{equation*}
$$

### Bestimmung eines beliebigen Trägheitsmoments aus dem Trägheitstensor

Es macht nur Sinn von einem Trägheitsmoment $\theta_{\hat{n}}$ eines starren Körpers bezüglich einer Achse $\hat{n}$ zu sprechen, um die der Körper rotiert. Beim Trägheitstensor $\boldsymbol{\Theta}$ handelt es sich um eine lineare Abbildung von $\vec{\omega}$ auf $\vec{L}$, die i.a. als $3\times3$-Matrix dargestellt wird. Beim Trägheitsmoment $\theta_{\hat{n}}$ handelt es sich um eine Zahl.  Aus $\boldsymbol{\Theta}$ erhät man $\theta_{\hat{n}}$ aus der beidseitigen Multiplikation von $\boldsymbol{\Theta}$ mit $\hat{n}$:
$$
\begin{equation*}
\begin{split}
\theta &= \delta m \, n_{i}\left(r^{2}\delta_{ij}-r_{i}r_{j}\right)n_{j} \\
&\\
&=\delta m\,\left(r^{2}n_{i}^{2} - \big(n_{i}\, r_{i}\big)\big(n_{j}\,r_{j}\big)\right) \\
&\\
&=\delta m\,\left(r^{2}\hat{n}^{2} - \big(\hat{n}\cdot\vec{r}\big)^{2}\right) \\
&\\
&=\delta m\,\left(r^{2} - \big(\hat{n}\cdot\vec{r}\big)^{2}\right) \\
\end{split}
\end{equation*}
$$
Auch dieses Ergebnis hat eine anschauliche Bedeutung, wie in **Skizze 1** dargestellt:

<img src="../figures/Trägheitsmoment.png" width="900" style="zoom:100%;" />

**Skizze 1** (Anschauliche Bedeutung des Trägheitsmoments $\theta_{\hat{n}}$)

---

Das Trägheitsmoment $\theta_{\hat{n}}$ jedes Massenelements $\delta m$ eines starren Körpers berechnet sich aus dessen Abstand $\vec{r}_{\perp}$ senkrecht zu $\hat{n}$.

# Navigation

[Main](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Geometrische_Optik) | [Weiter](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische_Optik/doc/Hinweise-Aufgabe-1-a.md)
