# Hinweise für den Versuch Datenverarbeitung am Beispiel des Pendels

## Aufgabe 2: Mathematisches Pendel

### Lineare Fehlerfortpflanzung nach Gauß

Als lineare [Fehlerfortpflanzung](https://de.wikipedia.org/wiki/Fehlerfortpflanzung) bezeichnet man den Vorgang, bei dem die Unsicherheit $\Delta\hat{\theta}$ auf einen bestimmten Wert $\hat{\theta}$ eines Parameters $\theta$, z.B. im Rahmen einer Abbildung
$$
\begin{equation*}
X\to Y: \quad \theta\to f(\theta)
\end{equation*}
$$
als Unsicherheit $\Delta f(\hat{\theta})$ auf einen Funktionswert $f(\hat{\theta})$ übertragen wird. Handelt es sich bei $f(\theta)$ um eine in $\theta$ stetig differenzierbare Abbildung, innerhalb der reellen Zahlen, erhält man $\Delta f(\hat{\theta})$ z.B. durch Entwicklung der [Taylorreihe](https://de.wikipedia.org/wiki/Taylorreihe):
$$
\begin{equation*}
\begin{split}
&f(\theta) = f(\hat{\theta}) + \underbrace{\frac{\partial f}{\partial\theta}(\hat{\theta})\,\Delta\hat{\theta}}+\ldots\\
&\hphantom{f(\theta) = f(\hat{\theta}) +,}\equiv\Delta f(\hat{\theta})
\end{split}
\end{equation*}
$$
Dem Umstand, dass die Taylorreihe bereits nach dem ersten Term abbricht tragen wir durch das Attribut *lineare* Fehlerfortpflanzung Rechnung. 

Liegen Unsicherheiten auf mehrere Parameter $\{\hat{\theta}_{j}:\hspace{0.05cm}j=1\ldots n\}$ vor, muss in $n$ Dimensionen gerechnet werden: 
$$
\begin{equation}
\begin{split}
&\Delta f(\boldsymbol{\theta}) = 
\left(\begin{array}{cccc} \partial_{\theta_{0}}f & \partial_{\theta_{1}}f & \ldots & \partial_{\theta_{n}}f
\end{array}\right)\cdot
\underbrace{
\left(\begin{array}{cccc} 
\sigma_{1}^{2} & \sigma_{12} & \ldots & \sigma_{1n} \\
\sigma_{21} & \sigma_{2}^{2} & \ldots & \sigma_{2n}f \\
\vdots &  & \ddots & \vdots \\
\sigma_{n1} & \sigma_{n2} & \ldots & \sigma_{n}^{2} \\
\end{array}\right)}
\cdot
\left(\begin{array}{c} \partial_{\theta_{0}}f \\\partial_{\theta_{1}}f \\ \vdots \\ \partial_{\theta_{n}}f
\end{array}\right).\\
&\hphantom{\Delta f(\boldsymbol{\theta}) =\left(\begin{array}{cccc} \Delta\theta_{0} & \Delta\theta_{1} & \Delta\theta_{1} & \Delta\theta_{1} & \ldots & \Delta\theta
\end{array}\right)}\equiv \Sigma\\
\end{split}
\end{equation}
$$
Dabei entspricht $\boldsymbol{\theta}=\{\theta_{j}\}$ und $\Sigma$ der [Kovarianzmatrix](https://de.wikipedia.org/wiki/Kovarianzmatrix) des Problems, die die Unsicherheiten und [linearen Korrelationen](https://de.wikipedia.org/wiki/Korrelation) der $\{\hat{\theta}_{j}\}$ abbildet.  

Gebräuchlicher ist Gleichung **(1)** in der Gestalt
$$
\begin{equation}
\begin{split}
&\Delta f(\boldsymbol{\theta}) = \sum\limits_{j=1}^{n}\left(\frac{\partial f(\boldsymbol{\theta})}{\partial\theta_{j}}\,\Delta\hat{\theta}_{j}\right)^{2}, \\
&\text{mit:}\\
&\\
&\Delta\hat{\theta}_{j}^{2} = \sigma_{j}^{2},\\
\end{split}
\end{equation}
$$
die dem Spezialfall entspricht, dass die $\{\theta_{j}\}$ alle paarweise unabhängig sind, wofür $\Sigma$ die Form einer [Diagonalmatrix](https://de.wikipedia.org/wiki/Diagonalmatrix) annimmt. 

Schwierigkeiten bei der linearen Fehlerfortpflanzung bestehen darin, dass die $\{\theta_{j}\}$ i.a. nicht unabhängig und die Korrelationen zwischen den $\{\theta_{j}\}$ nicht bekannt sind. Auch kann es nicht-triviale Korrelationen zwischen den $\{\theta_{j}\}$ geben, für die $\sigma_{ij}=0$ gilt. 

Bei der Anwendung von Gleichung **(2)** sollten Sie sicherstellen (und entsprechend argumentieren), warum Sie annehmen (können), dass die $\{\theta_{j}\}$ paarweise unabhängig sind. Wenn Sie die Möglichkeit haben, einen Parameter $\theta_{j}\pm\Delta \theta_{j}$ direkt und ohne weitere Fehlerfortpflanzung aus einer Parameteranpassung zu bestimmen sollten Sie dieses Vorgehen der linearen Fehlerfortpflanzung nach Möglichkeit vorziehen. 

# Navigation

[Zurück](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Vorversuch/doc/Hinweise-Aufgabe-2-a.md) | [Main](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Vorversuch) | [Weiter](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Vorversuch/doc/Hinweise-Aufgabe-2-c.md)

