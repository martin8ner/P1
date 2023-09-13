# Hinweise für den Versuch Vierpole und Leitungen

## Aufgabe 2: Drosselkette [2/3]

### Leitungseigenschaften

Aus der Substitution (Gleichung (**6**) [hier](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Vierpole_und_Leitungen/doc/Hinweise-Aufgabe-2.md))
$$
\begin{equation*}
\cosh\gamma\equiv\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}+1;\qquad \sinh\gamma\equiv\frac{Z_{\mathrm{L}}}{Z_{0}}
\end{equation*}
$$
 folgt
$$
\begin{equation*}
\begin{split}
&\sinh\gamma = \sqrt{\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}} = \sqrt{-\left(\frac{\omega}{\omega_{0}}\right)^{2}} = i\frac{\omega}{\omega_{0}} \\
&\\
&\text{mit:}\\
&\\
&\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}} = -\left(\frac{\omega}{\omega_{0}}\right)^{2}.
\end{split}
\end{equation*}
$$
Andererseits gilt (aus den [Additionstheoremen](https://de.wikipedia.org/wiki/Sinus_hyperbolicus_und_Kosinus_hyperbolicus) des $\sinh(\,\cdot\,)$):
$$
\begin{equation*}
\sinh\gamma = \sinh\left(\alpha+i\beta\right) = \sinh\alpha\,\cos\beta + i\,\cosh\alpha\,\sin\beta,
\end{equation*}
$$
die folgenden Gleichungen müssen also gleichzeitig erfüllt sein: 
$$
\begin{equation*}
\begin{split}
&\sinh\alpha\,\cos\beta = 0, \\
&\\
&\cosh\alpha\,\sin\beta = \frac{\omega}{\omega_{0}},
\end{split}
\end{equation*}
$$
woraus man die folgenden Lösungen erhält: 
$$
\begin{equation*}
\begin{array}{ccl}
\alpha & \beta & \\
0 & \arcsin\left(\frac{\omega}{\omega_{0}}\right) & \text{f\"ur }\omega<\omega_{0}\\
\mathrm{arccosh}\left(\frac{\omega}{\omega_{0}}\right) & \pi & \text{f\"ur }\omega>\omega_{0},\\
\end{array}
\end{equation*}
$$
d.h. die (ideale) Drosselkette hat die **Eigenschaft eines Tiefpasses**: 

- Für $\omega<\omega_{0}$ weist sie keine Dämpfung auf, d.h. sie ist als Leitung **verlustfrei**.
- Für $\omega>\omega_{0}$ steigt die Dämpfung mit $\omega$ steil an. Die Phase des Ausgangssignals ist um $\pi$ zum Eingangssignal verschoben. 

# Navigation

[Zurück](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Vierpole_und_Leitungen/doc/Hinweise-Aufgabe-2.md) | [Main](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Vierpole_und_Leitungen) | [Weiter](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Vierpole_und_Leitungen/doc/Hinweise-Aufgabe-2-b.md)
