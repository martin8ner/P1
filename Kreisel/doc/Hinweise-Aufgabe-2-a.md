# Hinweise für den Versuch Kreisel

## Aufgabe 2: Kardanisch gelagerter Kreisel

Die obigen Betrachtungen gelten für einen einfachen symmetrischen Kreisel. Im Fall des in (**Abbildung 1** [hier](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Kreisel/doc/Hinweise-Aufgabe-2.md)) gezeigten, kardanisch gelagerten Kreisels, wie er im Praktikum zum Einsatz kommt, müssen die Trägheitsmomente der *massiven* Kardanrahmen bei der Beschreibung der Kreiselbewegung berücksichtigt werden. Bei Drehungen um $\hat{x}$ dreht sich der innere, bei Drehungen um $\hat{y}$ sowohl der innere, als auch der äußere Kardanrahmen mit. Für die Trägheitsmomente gilt daher: 
$$
\begin{equation*}
\begin{split}
&\theta_{x}^{\prime} = \theta_{x} + \theta_{x}^{\mathrm{K,i}}; \\
&\theta_{y}^{\prime} = \theta_{y} + \theta_{y}^{\mathrm{K,i}} + \theta_{y}^{\mathrm{K,a}}; \\
&\theta_{z}^{\prime} = \theta_{z}, \\
\end{split}
\end{equation*}
$$
wobei $\theta_{x}=\theta_{y}$ die Trägheitsmomente des Rotors, $\theta_{x,y}^{\mathrm{K,i}}$ die Trägheitsmomente des inneren und $\theta_{x,y}^{\mathrm{K,a}}$ die Trägheitsmomente des äußeren Kardanrahmens sind. Unter diesen Voraussetzungen ergibt sich für kleine Werte von $\beta$
$$
\begin{equation}
\omega_{N} = \frac{\theta_{z}^{\prime}}{\sqrt{\theta_{x}^{\prime}\,\theta_{y}^{\prime}}}
\end{equation}
$$

# Navigation

[Zurück](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Kreisel/doc/Hinweise-Aufgabe-2.md) | [Main](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Kreisel)
