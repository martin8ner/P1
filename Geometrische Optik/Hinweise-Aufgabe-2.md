# Hinweise für den Versuch Geometrische Optik

## Aufgabe 2: Vermessung eines Zweilinsensystems

### Strahlengang eines Zweilinsensystems

Mit Hilfe des in Skizze 3 eingezeichneten Strahlengangs kann ein System aus zwei Linsen $L_{1}$ und $L_{2}$ (mit den Brennweiten $f_{1}$ und $f_{2}$) wie eine einzige dicke Linse $L$ mit den Hauptebenen $H_{1}$ und $H_{2}$ und der Brennweite $f$ behandelt werden. Alle relevanten Variablenbezeichnungen können Skizze 3 entnommen werden.

<img src="./figures/AbbeVerfahren.png" width="900" style="zoom:100%;" />

**Skizze 3** (Strahlengang eines Zweilinsensystems)

Für $f$ gilt die Formel von [Allvar Gullstrand](https://de.wikipedia.org/wiki/Allvar_Gullstrand) (auch als Gullstrand-Formel bezeichnet): 

```math
\begin{equation}
\frac{1}{f} = \frac{1}{f_{1}} + \frac{1}{f_{2}} - \frac{d}{f_{1}f_{2}},
\end{equation}
```

wobei $d$ der Abstand zwischen $L_{1}$ und $L_{2}$ (gemessen von den jeweiligen Scheiteln von $L_{1}$ und $L_{2}$) ist. 

Die Konstruktion erfolgt dabei wie folgt: 

- Strahl 1 verläuft, parallel zur optischen Achse, von $G$ bis $H_{1}$ (obere durchgezogene Linie).

- Strahl 2 verläuft von $G$, durch den linken Brennpunkt von $L$, bis $H_{1}$ (untere durchgezogene Linie). 

- Von $H_{1}$ nach $H_{2}$ werden beide Strahlen parallel verschoben (gestrichelte Linien zwischen $H_{1}$ und $H_{2}$).

- Von $H_{2}$ aus wird Strahl 1 durch den rechten Brennpunkt von $L$ und Strahl 2 parallel zur optischen Achse verlängert. Dort, wo die Strahlen 1 und 2 sich treffen entsteht $B$.  

- Für den Abbildungsmaßstab gilt die Beziehung: 
  
  ```math
  \begin{equation}
  \beta = \frac{B}{G} = \frac{b}{g}
  \end{equation}
  ```

Dies entspricht der Konstruktion eines Bildes $B$ für eine einzelne, dicke Linse mit der Brennweite $f$.  

Sind $f_{1}$ und $f_{2}$ bekannt lassen sich die Lagen von $H_{1}$ und $H_{2}$ aus 

```math
\begin{equation}
h_{1} = -\frac{f\,d}{f_{1}}; \quad h_{2}=\frac{f\,d}{f_{2}}
\end{equation}
```

berechnen, wobei $h_{1}$ und $h_{2}$ von den Scheiteln der Linsen aus zu messen sind. 

Für diesen Versuch sind $f_{1}$ und $f_{2}$ und damit auch die Lagen von $H_{1}$ und $H_{2}$ zunächst unbekannt. Die Größen $f$, $f_{1}$, $f_{2}$, sowie die Lagen von $H_{1}$ und $H_{2}$ lassen sich jedoch mit Hilfe des [Abbe-Verfahrens](https://de.wikipedia.org/wiki/Abbe-Verfahren) ermitteln.

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

### Bestimmung von $f_{1}$ und $f_{2}$

Wir gehen im Folgenden davon aus, dass Sie $X$ exakt zwischen den $L_{1}$ und $L_{2}$ gewählt haben. In diesem Fall liegen die Scheitelpunkte der Linsen bei $\pm d/2$ und Sie können $f_{1}$ und $f_{2}$ aus Gleichung ($\ref{eq:Hauptebenen}$), wie folgt bestimmen:
$$
\begin{equation}
\begin{split}
-\frac{d}{2}-h_{x} = h_{1} = -\frac{f\,d}{f_{1}}\qquad &\longrightarrow \qquad h_{x} = \hphantom{-}\frac{f\,d}{f_{1}}-\frac{d}{2};\\
\frac{d}{2}-h_{x}' = h_{2} = \hphantom{-}\frac{f\,d}{f_{2}} \qquad &\longrightarrow \qquad h_{x}' =  -\frac{f\,d}{f_{2}} + \frac{d}{2}. \\
\end{split}
\end{equation}
$$
Wenn Sie $h_{x}$ und $h_{x}'$ in Ihrem Modell aus Gleichung ($\ref{eq:Modell}$) entsprechend entsetzen 
$$
\begin{equation}
\begin{split}
&x(f, h_{x}) = f\left(1+\frac{1}{\beta}\right)+d\left(\frac{f}{f_{1}}-\frac{1}{2}\right); \\
&\\
&x'(f, h_{x}') = f\left(\beta+1\vphantom{\frac{1}{\beta}}\right)-d\left(\frac{f}{f_{2}}- \frac{1}{2}\right), \\
\end{split}
\label{eq:Modell_f1f2}
\end{equation}
$$
können Sie aus der Anpassung $f_{1}$ und $f_{2}$  direkt bestimmen. Sie können hierzu $f$ ggf. auf den zuvor ermittelten Wert fixieren. Die Variation von $f$, ebenso wie die Variation von $d$, innerhalb der zuvor bestimmten Grenzen, können Sie als systematische Variation quantifizieren. 

Alternativ können Sie $f_{1}$ und $f_{2}$ direkt aus Gleichung ($\ref{eq:Gullstrand}$) bestimmen, indem Sie $f$ für verschiedene Werte von $d$ bestimmen, die ermittelten Werte von $1/f$ als Funktion von $d$ auftragen und Gleichung ($\ref{eq:Gullstrand}$) als Modell für die Anpassung verwenden. Verwenden Sie für diese Anpassung die aus dem Modell aus Gleichung ($\ref{eq:Modell_f1f2}$) bestimmten Werte.  

### Hinweise zur Durchführung

