# Hinweise für den Versuch Geometrische Optik

## Aufgabe 2: Vermessung eines Zweilinsensystems (4/4)

### Bestimmung von $f_{1}$ und $f_{2}$

Wir gehen im Folgenden davon aus, dass Sie $X$ exakt zwischen $L_{1}$ und $L_{2}$ gewählt haben. In diesem Fall liegen die Scheitelpunkte der Linsen bei $\pm d/2$ und Sie können $f_{1}$ und $f_{2}$ aus (Gleichung (3) [hier](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische%20Optik/Hinweise-Aufgabe-2.md)), wie folgt bestimmen:
$$
\begin{equation}
\begin{split}
-\frac{d}{2}-h_{x} = h_{1} = -\frac{f\,d}{f_{1}}\qquad &\longrightarrow \qquad h_{x} = \hphantom{-}\frac{f\,d}{f_{1}}-\frac{d}{2};\\
\frac{d}{2}-h_{x}' = h_{2} = \hphantom{-}\frac{f\,d}{f_{2}} \qquad &\longrightarrow \qquad h_{x}' =  -\frac{f\,d}{f_{2}} + \frac{d}{2}. \\
\end{split}
\end{equation}
$$
Wenn Sie $h_{x}$ und $h_{x}'$ in Ihrem Modell aus (Gleichung (4) [hier](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische%20Optik/Hinweise-Aufgabe-2-a.md)) entsprechend einsetzen 
$$
\begin{equation}
\begin{split}
&x(f, h_{x}) = f\left(1+\frac{1}{\beta}\right)+d\left(\frac{f}{f_{1}}-\frac{1}{2}\right); \\
&\\
&x'(f, h_{x}') = f\left(\beta+1\vphantom{\frac{1}{\beta}}\right)-d\left(\frac{f}{f_{2}}- \frac{1}{2}\right), \\
\end{split}
\end{equation}
$$
können Sie aus der Anpassung $f_{1}$, $f_{2}$ und $f$ gemeinsam bestimmen. 

Alternativ können Sie $f_{1}$ und $f_{2}$ direkt aus (Gleichung (1) [hier](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische%20Optik/Hinweise-Aufgabe-2.md)) bestimmen, indem Sie $f$ für verschiedene Werte von $d$ bestimmen, die ermittelten Werte von $1/f$ als Funktion von $d$ auftragen und (Gleichung (1) [hier](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische%20Optik/Hinweise-Aufgabe-2.md)) als Modell für die Anpassung verwenden. Verwenden Sie für diese Anpassung ggf. die aus dem Modell aus Gleichung (2) bestimmten Werte als Startwerte.  

### Hinweise zur Durchführung

- Führen Sie für die Bestimmung von $f$, $h_{x}$ und $h_{x}'$ eine Anpassung an mindestens 5 Wertepaare $(x, x')$ durch. Vergessen Sie für die Anpassung nicht in jedem Punkt Unsicherheiten, sowohl entlang der x- ($\Delta\beta$,  $\Delta(1/\beta)$), als auch der $y$-Achse ($\Delta x$, $\Delta x'$) anzugeben. 

- Als Modell, um $f$, $h_{x}$ und $h_{x}'$ gleichzeitig bestimmen zu können nutzen Sie die Tatsache, dass $x$ relativ zu $X$ mit einem negativen Vorzeichen gemessen wird. Sie können also ein Modell, wie das folgende ansetzen:

  ```python
  def model(B, G, f, hx, hxp):
      if B>0:
          return f*(B/G+1)+hxp
      return f*(-1+G/B)-hx
  ```

  wobei Sie $B$ einen negativen (positiven) Wert für die Messung von $x$ ($x'$) geben. In diesem Modell würden Sie die Unsicherheit auf $G$, als korrelierte Unsicherheit für alle Punkte in $x$ und $x'$ systematisch variieren. Eigentlich müssten zudem die Unsicherheiten auf $B$ in jeweils zwei Punkten, die sich nur durch ihr Vorzeichen unterscheiden korreliert sein, da es sich um die gleiche Messung von $B$ handelt.

- Geben Sie die Korrelationskoeffizienten zwischen $f$, $h_{x}$ und $h_{x}'$ als Ergebnisse der Anpassung mit an. Tun Sie dies auch, wenn Sie das Modell zur Bestimmung von $f$, $f_{1}$ und $f_{2}$ verwenden.  

- Zur Bestimmung von $f$ aus (Gleichung (1) [hier](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische%20Optik/Hinweise-Aufgabe-2.md)) setzen Sie $f$, $f_{1}$ und $f_{2}$ aus der vorherigen Anpassung als Startwerte. Gegebenenfalls können $f$ außerdem auf den zuvor ermittelten Wert fixieren. Die Variation von $f$ sollten Sie in diesem Fall, ebenso wie die Variation von $d$, innerhalb der zuvor bestimmten Grenzen, als systematische Variation quantifizieren. 

# Navigation

 [Main](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Geometrische%20Optik) | [Zurück](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische%20Optik/Hinweise-Aufgabe-2-b.md)
