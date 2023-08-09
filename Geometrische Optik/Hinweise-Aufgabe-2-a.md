# Hinweise für den Versuch Geometrische Optik

## Aufgabe 2: Vermessung eines Zweilinsensystems

### Bestimmung von $H_{1}$, $H_{2}$ und $f$

Wir beschreiben zunächst die Bestimmung von $f$ und der Lagen von $H_{1}$ ($h_{x}$) und $H_{2}$ ($h_{x}'$). 

Da die Lage von $H_{1}$ nicht als bekannt vorausgesetzt werden kann bestimmen wir den Abstand von $G$ relativ zu einem **frei gewählten Bezugspunkt** $X$ (Marker $X$ in Skizze 3), dessen Position auf der optischen Achse wir gleichzeitig als Nullpunkt festlegen. Für die Skizze haben wir $X$ beliebig zwischen $L_{1}$ und $L_{2}$ gewählt. Für den Versuch sollen Sie $X$ exakt zwischen $L_{1}$ und $L_{2}$, in der Mitte des Messingzylinders wählen. Die Abstände von $G$ und $B$ zu $X$ bezeichnen wir als

```math
\begin{equation}
\begin{split}
&G:\quad x\hphantom{^{\prime}} = g+h_{x}, \\
&B:\quad x' = b+h'_{x},
\end{split}
\end{equation}
```

wobei $h_{x}$ ($h'_{x}$) den unbekannten Abstand von $X$ zu $H_{1}$ ($H_{2}$) bezeichnet (siehe Skizze 3). Nach der Linsengleichung besteht zwischen $g$, $b$, $f$ die Beziehung: 

```math
\begin{equation}
\frac{1}{f} = \frac{1}{g} + \frac{1}{b}.
\end{equation}
```

Mit dem Abbildungsmaßstab $\beta$ aus Gleichung (2) lässt sich Gleichung (5) wie folgt umformen: 

```math
\begin{equation}
\begin{split}
&\frac{1}{f} = \frac{1}{g}\left(1+\frac{1}{\beta}\right); \qquad
\frac{1}{f} = \frac{1}{b}\left(\beta+1\vphantom{\frac{1}{\beta}}\right). \\
\end{split}
\end{equation}
```

Unter Verwendung der Gleichungen (4) und (6) lässt sich somit der folgende funktionale Zusammenhang zwischen $x$ ($x'$), $f$ und $h_{x}$ ($h'_{x}$) herstellen: 

```math
\begin{equation}
\begin{split}
&x(f, h_{x}) = f\left(1+\frac{1}{\beta}\right)+h_{x}; \\
&\\
&x'(f, h_{x}') = f\left(\beta+1\vphantom{\frac{1}{\beta}}\right)+h'_{x}; \\
\end{split}
\end{equation}
```

Die Bestimmung von $f$, $h_{x}$ und $h_{x}'$ läuft nun wie folgt ab: 

- Sie variieren den Abstand $x$. Dabei variieren Sie effektiv $g$, während $h_{x}$ durch die feste Wahl von $X$ immer gleich bleibt. Beachten Sie die Lage des Nullpunkts in $X$, $x$ ist demnach mit negativem und $x'$ mit positivem Vorzeichen zu messen.
- Justieren Sie zu jedem gewählten Wert von $x$ den Abstand des Schirms $x'$, so dass $B$ wieder scharf darauf abgebildet wird. Beachten Sie die Unsicherheiten auf $x$ und $x'$.  
- Bestimmen Sie den Abbildungsmaßstab $\beta$ zu jedem Wertepaar aus $x$ und $x'$. Berechnen Sie die Unsicherheiten auf $\beta$ in jedem Punkt aus den Unsicherheiten auf $G$ und $B$, mittels linearer Fehlerfortpflanzung. 

Zwar sind $g$ und $b$ nicht bekannt, $\beta$ kann aber aus $G$ und $B$ bestimmt werden. Trägt man $x(f, h_{x})$ als Funktion von $(1+1/\beta)$ und $x'(f, h'_{x})$ als Funktion von $(\beta+1)$ auf sollte sich jeweils ein linearer Zusammenhang ergeben, aus dem sich $f$ als Steigung und $h_{x}$ ($h'_{x}$) als Achsenabschnitt ablesen lassen. Mit einem geeigneten Modell können Sie $f$, $h_{x}$ und $h_{x}'$ auch **gleichzeitig** anpassen.

Sowohl $h_{x}$ als auch $h_{x}^{\prime}$ können sowohl positive als auch negative Werte annehmen, je nachdem ob sich die entsprechende Hauptebene links oder rechts von $X$ befindet. Aus $h_{x}$ und $h_{x}^{\prime}$ lässt sich der Abstand der Hauptebenen $a=h_{x}'-h_{x}$ bestimmen, der von der Wahl von $X$ unabhängig ist. Sie können $a$ auch direkt in Ihrem Modell implementieren, indem Sie z.B.  $h_{x}'$ als $h_{x}'=a+h_{x}$ ausdrücken. 

# Navigation

 [Main](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Geometrische%20Optik) | Zurück | Weiter
