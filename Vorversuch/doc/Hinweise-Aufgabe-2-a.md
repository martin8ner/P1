# Hinweise für den Versuch Datenverarbeitung am Beispiel des Pendels

## Aufgabe 2: Mathematisches Pendel

### Parameterschätzung mit der $\chi^{2}$-Methode

Bei der [Parameterschätzung](https://de.wikipedia.org/wiki/Sch%C3%A4tzfunktion) legen Sie einer Menge von $n$ Datenpunkten $\{r_{i}=(x_{i}, y_{i}):\hspace{0.05cm} i=1\ldots n\}$ ein Modell $\Omega(\{\theta_{j}\})$ zugrunde das von $k$ Parametern $\{\theta_{j}\}$ abhängen kann. Im Rahmen einer [Optimierungsaufgabe](https://de.wikipedia.org/wiki/Optimierungsproblem) sind die Werte der $\{\theta_{j}\}$ zu bestimmen, mit denen $\Omega(\{\theta_{j}\})$ die $\{r_{i}\}$ am besten beschreibt. Für physikalische Messungen wird die Möglichkeit des Modells die Daten zu beschreiben auf Grundlage der Unsicherheiten $\{\Delta r_{i}=(\Delta x_{i}, \Delta y_{i})\}$ eingeschätzt, mit denen die $\{r_{i}\}$ bestimmt wurden. 

Die Übersetzung dieser Aufgabenstellung in ein mathematisches [Modell](https://de.wikipedia.org/wiki/Statistisches_Modell) erfolgt mit Hilfe einer **Kostenfunktion**, die bei der im Praktikum vorwiegend verwendeten Methode zur Parameterschätzung der [Zustandssumme](https://de.wikipedia.org/wiki/Zustandssumme) der Abstände zwischen $\Omega(\{\theta_{j}\})$ und den $\{r_{i}\}$
$$
\begin{equation}
z = \sum\limits_{i=1}^{n}\frac{||\Omega(\{\theta_{j}\}-r_{i}||_{2}^{2}}{\Delta r_{i}}
\end{equation}
$$
entspricht. Die Optimierungsaufgabe besteht darin, den kleinsten Wert von $z$ im Raum der Parameter $\{\theta_{j}\}$ zu finden. Diese Methode wird als "Methode der kleinsten Quadrate" oder $\chi^{2}$-Methode bezeichnet. Der Name leitet sich aus der folgenden Tatsache ab: 

Interpretieren wir die $\{r_{i}\}$ als [Zufallsvariablen](https://de.wikipedia.org/wiki/Zufallsvariable), die nach einer allgemeinen [Wahrscheinlichkeitsdichte](https://de.wikipedia.org/wiki/Wahrscheinlichkeitsdichtefunktion) verteilt sind, dann ist $z$, als Funktion von Zufallsvariablen, ebenfalls eine Zufallsvariable. Man bezeichnet $z$ allgemein als [Schätzfunktion](https://de.wikipedia.org/wiki/Sch%C3%A4tzfunktion), die wiederum selbst nach einer Wahrscheinlichkeitsdichte, der [Stichprobenverteilung](https://de.wikipedia.org/wiki/Sch%C3%A4tzfunktion#Stichprobenverteilung), verteilt ist. Im allgemeinen ist es nicht möglich für die Stichprobenverteilung eine mathematisch geschlossene Form anzugeben. Sind die $\{r_{i}\}$ aber *normalverteilt*, dann folgt die Zufallsvariable $z$ der [$\chi^{2}(z, n_{\mathrm{dof}})$-Verteilung](https://de.wikipedia.org/wiki/Chi-Quadrat-Verteilung)  für $n_{\mathrm{dof}}$ Freiheitsgrade, mit $n_{\mathrm{dof}}\equiv n-k$. Der Begriff [Freiheitsgrad](https://de.wikipedia.org/wiki/Anzahl_der_Freiheitsgrade_(Statistik)) leitet sich aus der folgenden beispielhaften Vorstellung ab: 

In der $xy$-Ebene wird eine Gerade durch zwei Datenpunkte $(x_{1}, y_{1})$ und $(x_{2}, y_{2})$ bestimmt. Das mathematische Modell zur Beschreibung einer Geraden, $\Omega(a_{0}, a_{1}, x): a_{1}\hspace{0.05cm}x+a_{0}=0$, besitzt zwei Parameter $a_{0}$ und $a_{1}$. Durch die Punkte $(x_{1}, y_{1})$ und $(x_{2}, y_{2})$ sind $a_{0}$ und $a_{1}$ eindeutig bestimmt und es besteht keine Freiheit die Parameter zu variieren. Ein Modell, das genauso viele Parameter besitzt, wie Messpunkte zur Anpassung zur Verfügung stehen, bezeichnet man als *saturiert*. Sobald ein weiterer Punkt $(x_{3}, y_{3})$ hinzukommt ist nicht mehr garantiert, dass $\Omega$ durch geeignete Wahl der Parameter $a_{0}$ und $a_{1}$ jeden Punkt exakt berührt und das Minimum von $z$ wird nicht mehr trivial gefunden. Das Modell hat einen Freiheitsgrad, aus dem ein nicht-triviales Minimum abgeleitet werden kann.  

Zur Vereinfachung der Diskussion macht man in Textbüchern oft die folgenden Annahmen, **die i.a. jedoch eher selten gegeben sind**:  

- Die Werte $\{x_{i}\}$ sind [Ausprägungen](https://de.wikipedia.org/wiki/Statistische_Variable) einer [Zufallsgröße](https://de.wikipedia.org/wiki/Zufallsvariable) $x$, die *keine* Unsicherheiten haben;
- Das Modell $\Omega(\{\theta_{j}\},x)$ ist dann eine Funktion von $x$ und der Parameter $\{\theta_{j}\}$.

In diesem Fall nimmt Gleichung **(1)** die geläufigere Form 
$$
\begin{equation}
z = \sum\limits_{i=1}^{n}\frac{\left(\Omega(\{\theta_{j}\},x_{i})-y_{i}\right)^{2}}{\Delta y_{i}}
\end{equation}
$$
an. 

Die Optimierungsaufgabe für Gleichung **(2)** kann grundsätzlich analytisch geschlossen gelöst werden, solange $\Omega$ nur *linear* von den Parametern $\{\theta_{j}\}$ abhängt. Heutzutage werden solche (und weitaus kompliziertere) Parameterschätzungen algorithmisch von Computern durchgeführt. Mit den Programmpakten *kafe2* und *PhyPraKit* stehen Ihnen geeignete Werkzeuge hierzu zur Verfügung. 

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

# Navigation

[Zurück](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Vorversuch/doc/Hinweise-Aufgabe-2.md) | [Main](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Vorversuch) | [Weiter](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/Vorversuch/doc/Hinweise-Aufgabe-2-b.md)

