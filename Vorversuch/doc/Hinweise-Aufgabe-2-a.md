# Hinweise für den Versuch Datenverarbeitung am Beispiel des Pendels

## Aufgabe 2: Mathematisches Pendel

### Parameterschätzung mit der $\chi^{2}$-Methode

Bei der [Parameterschätzung](https://de.wikipedia.org/wiki/Sch%C3%A4tzfunktion) legen Sie einer Menge von $n$ Datenpunkten $\{r_{i}=(x_{i}, y_{i}):\hspace{0.05cm} i=1\ldots n\}$ ein Modell $\Omega(\{\theta_{j}\})$ zugrunde das von einem oder mehreren Parametern $\{\theta_{j}\}$ abhängen kann. Im Rahmen einer [Optimierungsaufgabe](https://de.wikipedia.org/wiki/Optimierungsproblem) sind die Werte der $\{\theta_{j}\}$ zu bestimmen, mit denen $\Omega(\{\theta_{j}\})$ die $\{r_{i}\}$ am besten beschreibt. Für physikalische Messungen wird die Möglichkeit des Modells die Daten zu beschreiben auf Grundlage der Unsicherheiten $\{\Delta r_{i}=(\Delta x_{i}, \Delta y_{i})\}$ eingeschätzt, mit denen die $\{r_{i}\}$ bestimmt wurden. 

Die Übersetzung dieser Aufgabenstellung in ein mathematisches [Modell](https://de.wikipedia.org/wiki/Statistisches_Modell) erfolgt mit Hilfe einer **Kostenfunktion**, die bei dieser Methode der [Zustandssumme](https://de.wikipedia.org/wiki/Zustandssumme) der Abstände zwischen der Modellvorhersage $\Omega(\{\theta_{j}\})$ und den $\{r_{i}\}$
$$
\begin{equation}
\chi^{2} = \sum\limits_{i=1}^{n}\frac{||\Omega(\{\theta_{j}\}-r_{i}||_{2}}{\Delta r_{i}}
\end{equation}
$$
entspricht. Die Optimierungsaufgabe besteht darin, den kleinsten Wert von $\chi^{2}$ im Raum der Parameter $\{\theta_{j}\}$ zu finden.  

Zur Vereinfachung der Diskussion macht man in Textbüchern oft die folgenden Annahmen, **die i.a. jedoch eher selten gegeben sind**:  

- Die Werte $\{x_{i}\}$ sind [Ausprägungen](https://de.wikipedia.org/wiki/Statistische_Variable) einer [Zufallsgröße](https://de.wikipedia.org/wiki/Zufallsvariable) $x$, die *keine* Unsicherheiten haben;
- Das Modell $\Omega(\{\theta_{j}\},x)$ ist eine Funktion von $x$ und der Parameter $\{\theta_{j}\}$.

In diesem Fall nimmt Gleichung **(1)** die geläufigere Form 
$$
\begin{equation}
\chi^{2} = \sum\limits_{i=1}^{n}\frac{\left(\Omega(\{\theta_{j}\},x_{i})-y_{i}\right)^{2}}{\Delta y_{i}}
\end{equation}
$$
an. 

Die Optimierungsaufgabe für Gleichung **(2)** kann grundsätzlich analytisch geschlossen gelöst werden, solange $\Omega$ nur *linear* von den Parametern $\{\theta_{j}\}$ abhängt. Heutzutage werden solche (und weitaus kompliziertere) Parameteranpassungen algorithmisch von Computern durchgeführt. Mit den Programmpakten *kafe2* und *PhyPraKit* stehen Ihnen geeignete Werkzeuge hierzu zur Verfügung. 

### $\chi^{2}$-Test

Ungeachtet des Umstandes, dass i.a. ein Satz von Parametern $\{\theta_{j}\}$ existiert, für den $\chi^{2}$ minimal wird, kann die Beschreibung der Daten durch $\Omega(\{\theta_{j}\})$ immer noch unzureichend sein. 

Ein Maß dafür, wie gut $\Omega$ die $\{r_{i}\}$, bei optimaler Wahl der $\{\theta_{j}\}$ beschreibt ist der Wert der Kostenfunktion in ihrem Minimum
$$
\begin{equation*}
\hat{\chi}^{2}=\min_{\{\theta_{j}\}}\left(\chi^{2}(\{r_{i}\}, \{\theta_{j}\})\right).
\end{equation*}
$$
Dabei gilt: 
$$
\begin{equation*}
\begin{array}{ll}
\hat{\chi}^{2}/n_{\mathrm{dof}}\lesssim 1 & \text{das Modell ist mit den Daten verträglich;} \\
\hat{\chi}^{2}/n_{\mathrm{dof}}\gg 1 & \text{das Modell ist mit den Daten nicht verträglich,} \\
\end{array}
\end{equation*}
$$
wobei $n_{\mathrm{dof}} = n-||\{\theta_{j}\}||$ der Anzahl der Datenpunkte abzüglich der Anzahl $||\{\theta_{j}\}||$ der Modellparameter entspricht. Die Größe $n_{\mathrm{dof}}$ wird auch als [*Anzahl der Freiheitsgrade*](https://de.wikipedia.org/wiki/Anzahl_der_Freiheitsgrade_(Statistik)) der Anpassung bezeichnet. Dieser Begriff leitet sich aus der folgenden beispielhaften Vorstellung ab: 

In der Ebene wird eine Gerade durch zwei Datenpunkte $(x_{1}, y_{1})$ und $(x_{2}, y_{2})$ bestimmt. Das mathematische Modell zur Beschreibung einer geraden $\Omega(a_{0}, a_{1}, x) = a_{1}\hspace{0.05cm}x+a_{0}$ besitzt zwei Parameter $a_{0}$ und $a_{1}$. Durch die Punkte $(x_{1}, y_{1})$ und $(x_{2}, y_{2})$ sind $a_{0}$ und $a_{1}$ eindeutig bestimmt und es besteht keine Freiheit die Parameter zu variieren. Ein Modell, das genauso viele Parameter besitzt wie Datenpunkte zur Anpassung zur Verfügung stehen, bezeichnet man als *saturiert*. Sobald ein weiterer Punkt $(x_{3}, y_{3})$ hinzukommt ist nicht mehr garantiert, dass $\Omega$ durch geeignete Wahl der Parameter $a_{0}$ und $a_{1}$ jeden Punkt exakt berührt und das Minimum von $\chi^{2}$ wird nicht mehr trivial gefunden. 

Die oben getroffenen Aussagen zu $\hat{\chi}^{2}/n_{\mathrm{dof}}$ gelten mit mathematischer Strenge, d.h.: Führt eine (statistisch korrekt implementierte) Anpassung auf einen Wert von $\hat{\chi}^{2}/n_{\mathrm{dof}}\gg 1$, dann ist das zugrundeliegende Modell im Rahmen der angegebenen Unsicherheiten $\{\Delta r_{i}\}$ mit den Datenpunkten $\{r_{i}\}$ **nicht kompatibel**. Obwohl man sich manchmal aus pragmatischen Gründen dazu entscheidet, ist es in einem solchen Fall grundsätzlich zweifelhaft die Ergebnisse der Anpassung (unkommentiert) anzugeben oder weiter zu verarbeiten. 

Bei der Verwendung der Programmpakte *kafe2* und *PhyPraKit* wird zu jeder Parameteranpassung der $\hat{\chi}^{2}/n_{\mathrm{dof}}$-Wert mit ausgegeben, was Ihnen eine Aussage über die Güte der Anpassung ([*goodness-of-fit*](https://en.wikipedia.org/wiki/Goodness_of_fit)) erlaubt. Sie sollten diesen Wert bei jeder Parameteranpassung mit beachten und diskutieren. 

# Navigation

[Zurück](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Vorversuch/doc/Hinweise-Aufgabe-2.md) | [Main](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Vorversuch) | [Weiter](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Vorversuch/doc/Hinweise-Aufgabe-2-b.md)

