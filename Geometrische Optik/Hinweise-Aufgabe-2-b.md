# Hinweise für den Versuch Geometrische Optik

## Aufgabe 2: Vermessung eines Zweilinsensystems (3/4)

### Bestimmung von $H_{1}$, $H_{2}$ und $f$

Die Bestimmung von $f$, $h_{x}$ und $h_{x}'$ läuft nun wie folgt ab: 

- Sie variieren den Abstand $x$. Dabei variieren Sie effektiv $g$, während $h_{x}$ durch die feste Wahl von $X$ immer gleich bleibt. Beachten Sie die Lage des Nullpunkts in $X$, $x$ ist demnach mit negativem und $x'$ mit positivem Vorzeichen zu messen.
- Justieren Sie zu jedem gewählten Wert von $x$ den Abstand des Schirms $x'$, so dass $B$ wieder scharf darauf abgebildet wird. Beachten Sie die Unsicherheiten auf $x$ und $x'$.  
- Bestimmen Sie den Abbildungsmaßstab $\beta$ zu jedem Wertepaar, bestehend aus $x$ und $x'$. Berechnen Sie die Unsicherheiten auf $\beta$ in jedem Punkt aus den Unsicherheiten auf $G$ und $B$, mittels linearer Fehlerfortpflanzung. 

Zwar sind $g$ und $b$ nicht bekannt, $\beta$ kann aber aus $G$ und $B$ bestimmt werden. Trägt man $x(f, h_{x})$ als Funktion von $(1+1/\beta)$ und $x'(f, h'_{x})$ als Funktion von $(\beta+1)$ auf sollte sich jeweils ein linearer Zusammenhang ergeben, aus dem sich $f$ als Steigung und $h_{x}$ ($h'_{x}$) als Achsenabschnitt ablesen lassen. Mit einem geeigneten Modell können Sie $f$, $h_{x}$ und $h_{x}'$ **gleichzeitig** anpassen.

Sowohl $h_{x}$ als auch $h_{x}^{\prime}$ können sowohl positive als auch negative Werte annehmen, je nachdem ob sich die entsprechende Hauptebene links oder rechts von $X$ befindet. Aus $h_{x}$ und $h_{x}^{\prime}$ lässt sich der Abstand der Hauptebenen $a=h_{x}'-h_{x}$ bestimmen, der von der Wahl von $X$ unabhängig ist. Sie können $a$ auch direkt in Ihrem Modell implementieren, indem Sie z.B.  $h_{x}'$ als $h_{x}'=a+h_{x}$ ausdrücken. 

# Navigation

 [Main](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Geometrische%20Optik) | [Zurück](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische%20Optik/Hinweise-Aufgabe-2-a.md) | [Weiter](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische%20Optik/Hinweise-Aufgabe-2-c.md)
