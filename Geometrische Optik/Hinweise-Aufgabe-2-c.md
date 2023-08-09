# Hinweise für den Versuch Geometrische Optik

## Aufgabe 2: Vermessung eines Zweilinsensystems

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



# Navigation

 [Main](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Geometrische%20Optik) | Zurück
