# Hinweise für den Versuch Geometrische Optik

## Aufgabe 2: Vermessung eines Zweilinsensystems $L$ (4/5)

### Bestimmung von $f_{1}$ und $f_{2}$

Wir gehen im Folgenden davon aus, dass Sie $X$ exakt zwischen $L_{1}$ und $L_{2}$ gewählt haben. In diesem Fall liegen die Scheitelpunkte der Linsen bei $\pm d/2$ und Sie können $f_{1}$ und $f_{2}$ aus (Gleichung (3) [hier](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische_Optik/doc/Hinweise-Aufgabe-2.md)), wie folgt bestimmen:
$$
\begin{equation}
\begin{split}
-\frac{d}{2}-h_{x} = h_{1} = -\frac{f\,d}{f_{1}}\qquad &\longrightarrow \qquad h_{x} = \hphantom{-}\frac{f\,d}{f_{1}}-\frac{d}{2};\\
\frac{d}{2}-h_{x}' = h_{2} = \hphantom{-}\frac{f\,d}{f_{2}} \qquad &\longrightarrow \qquad h_{x}' =  -\frac{f\,d}{f_{2}} + \frac{d}{2}. \\
\end{split}
\end{equation}
$$
Wenn Sie $h_{x}$ und $h_{x}'$ in Ihrem Modell aus (Gleichung (4) [hier](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische_Optik/doc/Hinweise-Aufgabe-2-a.md)) entsprechend einsetzen 
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

Alternativ können Sie $f_{1}$ und $f_{2}$ direkt aus (Gleichung (1) [hier](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische_Optik/doc/Hinweise-Aufgabe-2.md)) bestimmen, indem Sie $f$ für verschiedene Werte von $d$ bestimmen, die Kehrwerte der ermittelten Werte von $f$ als Funktion von $d$ auftragen und (Gleichung (1) [hier](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische_Optik/doc/Hinweise-Aufgabe-2.md)) als Modell für die Anpassung verwenden. Verwenden Sie für diese Anpassung ggf. die aus dem Modell aus Gleichung (2) bestimmten Werte als Startwerte.  

# Navigation

 [Main](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Geometrische_Optik) | [Zurück](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische_Optik/doc/Hinweise-Aufgabe-2-b.md) | [Weiter](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische_Optik/doc/Hinweise-Aufgabe-2-d.md)
