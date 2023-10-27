# Hinweise für den Versuch Datenverarbeitung am Beispiel des Pendels

## Aufgabe 2: Mathematisches Pendel

### $\chi^{2}$-Test

Ungeachtet des Umstandes, dass i.a. ein Satz von Parametern $\{\theta_{j}\}$ existiert, für den $z$ minimal wird, kann die Beschreibung der Daten durch $\Omega(\{\theta_{j}\})$ immer noch unzureichend sein. 

Ein Maß dafür, wie gut $\Omega$ die $\{r_{i}\}$, bei optimaler Wahl der $\{\theta_{j}\}$, beschreibt ist der Wert von $z$ im Minimum
$$
\begin{equation*}
\hat{z}=\min_{\{\theta_{j}\}}\left(z(\{r_{i}\}, \{\theta_{j}\})\right).
\end{equation*}
$$
Dabei gilt: 
$$
\begin{equation*}
\begin{array}{ll}
\hat{z}/n_{\mathrm{dof}}\lesssim 1 & \text{das Modell ist mit den Daten verträglich;} \\
\hat{z}/n_{\mathrm{dof}}\gg 1 & \text{das Modell ist mit den Daten nicht verträglich,} \\
\end{array}
\end{equation*}
$$
Den Wert $\hat{z}$ bezeichnet man als **$\boldsymbol{\chi^{2}}$-Wert**. Die Aussagen zu $\hat{z}/n_{\mathrm{dof}}$ gelten mit mathematischer Strenge, d.h., führt eine (statistisch korrekt implementierte) Anpassung auf einen Wert von $\hat{z}/n_{\mathrm{dof}}\gg 1$, dann ist das zugrundeliegende Modell im Rahmen der angegebenen Unsicherheiten $\{\Delta r_{i}\}$ mit den Datenpunkten $\{r_{i}\}$ **nicht kompatibel**. 

Das lässt sich wie folgt verstehen: Der $\chi^{2}$-Wert ist ein Maß für die mittlere Entfernung zwischen $\Omega$ und den $\{r_{i}\}$. Große $\chi^{2}$-Werte weisen auf eine schlechte und kleine $\chi^{2}$-Werte auf eine gute Übereinstimmung zwischen $\Omega$ und den $\{r_{i}\}$, innerhalb der Streuung ([Varianz](https://de.wikipedia.org/wiki/Varianz_(Stochastik))) der $\{r_{i}\}$, hin. 

Gehen wir davon aus, dass die $\{r_{i}\}$ im Fall wiederholter Messungen *normalverteilt* sind und ihre [Erwartungswerte](https://de.wikipedia.org/wiki/Erwartungswert) wirklich durch $\Omega$ beschrieben werden können, dann folgt $\hat{z}$ der $\chi^{2}(z, n_{\mathrm{dof}})$-Verteilung, deren Erwartungswert $E[\hspace{0.05cm}z\hspace{0.05cm}]=n_{\mathrm{dof}}$ ist. Ein Wert von $\hat{z}^{2}/n_{\mathrm{ndof}}\lesssim1$ deutet darauf hin, dass der Verlauf der Modellvorhersage im Mittel innerhalb der Varianz der $\{r_{i}\}$ liegt. Um diesen Umstand anschaulicher zu machen und weil die Grenzen noch akzeptabler $\chi^{2}$-Werte von $n_{\mathrm{dof}}$ abhängt, wird der $\chi^{2}$-Wert oft zusätzlich in einen ***p*-Wert** übersetzt. 

Der *p*-Wert ist das Integral 
$$
\begin{equation*}
p = \int\limits_{\hat{z}}^{\infty}\chi^{2}(z, n_{\mathrm{ndof}})\,\mathrm{dz}.
\end{equation*}
$$
Er entspricht damit, unter der Annahme, dass die Erwartungswerte der $\{r_{i}\}$ tatsächlich $\Omega$ folgen, der Wahrscheinlichkeit einen Wert von $z\geq\hat{z}$ und damit eine schlechtere Übereinstimmung des Modells mit den $\{r_{i}\}$ zu erhalten, als durch $\hat{z}$ beobachteten. Der *p*-Wert ist selbst wieder eine Zufallsvariable, die, wenn die zu seiner Berechnung gemachten Annahmen erfüllt sind, in ihrem Wertebereich zwischen 0 und 1 gleichverteilt ist. 

**Wir geben ein Beispiel:** Sie nehmen die Anpassung eines Modells $\Omega$ mit $k=5$ Parametern an $n=15$ Messpunkte $\{r_{i}\}$ vor, d.h. $n_{\mathrm{dof}}=10$. Nach Anpassung erhalten Sie einen $\chi^{2}$-Wert von 20, d.h. $\hat{z}^{2}/n_{\mathrm{dof}}=2$. Unter der Annahme, das die $\{r_{i}\}$ normalverteilt sind und ihre Erwartungswerte wirklich $\Omega$ folgen ist ein Ausgang des Experiments mit einem $\chi^{2}$-Wert $\geq20$ mit einer Wahrscheinlichkeit von 3% zu erwarten. Es bleibt Ihnen überlassen, basierend auf dieser Abschätzung die Aussage, dass die Erwartungswerte der $\{r_{i}\}$ tatsächlich $\Omega$ folgen zu verwerfen oder nicht. 

Um für die Beziehung zwischen $\chi^{2}$-Wert und *p*-Wert ein etwas besseres Gefühl zu bekommen können Sie ein paar weitere Beispiele mit dieser [Web-Anwendung der University of Illinois](http://courses.atlas.illinois.edu/spring2016/STAT/STAT200/pchisq.html) durchspielen. 

Falls ein Modell wirklich Probleme bei der Beschreibung von Messpunkten hat kann der *p*-Wert rasch Werte $\mathcal{O}(10^{-3}-10^{-10})$ annehmen. Obwohl man sich manchmal aus pragmatischen Gründen dazu entscheidet, ist es grundsätzlich zweifelhaft die Ergebnisse der Anpassung mit sehr niedrigen *p*-Werten (unkommentiert) anzugeben oder weiter zu verarbeiten. 

### Die Programmpakete kafe2 und PhyPraKit

Bei der Verwendung der Programmpakte *kafe2* und *PhyPraKit* wird zu jeder Parameteranpassung der $\chi^{2}$-Wert mit ausgegeben, was Ihnen eine Aussage über die Güte der Anpassung ([*goodness-of-fit*](https://en.wikipedia.org/wiki/Goodness_of_fit)) erlaubt. Sie sollten diesen Wert bei jeder Parameteranpassung mit beachten und diskutieren. 

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

