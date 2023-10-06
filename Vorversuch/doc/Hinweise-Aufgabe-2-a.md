# Hinweise für den Versuch Datenverarbeitung am Beispiel des Pendels

## Aufgabe 2: Mathematisches Pendel

### Parameterschätzung mit der $\chi^{2}$-Methode

Bei der [Parameterschätzung](https://de.wikipedia.org/wiki/Sch%C3%A4tzfunktion) legen Sie einer Menge von $n$ Datenpunkten $\{r_{i}=(x_{i}, y_{i}):\hspace{0.05cm} i=1\ldots n\}$ ein Modell $\Omega(\{\theta_{j}\})$ zugrunde das von einem oder mehreren Parametern $\{\theta_{j}\}$ abhängen kann. Im Rahmen einer [Optimierungsaufgabe](https://de.wikipedia.org/wiki/Optimierungsproblem) sind die Werte der $\{\theta_{j}\}$ zu bestimmen, mit denen $\Omega(\{\theta_{j}\})$ die $\{r_{i}\}$ am besten beschreibt. Die Möglichkeit des Modells die Daten zu beschreiben wird auf Grundlage der Unsicherheiten $\{\Delta r_{i}=(\Delta x_{i}, \Delta y_{i})\}$ eingeschätzt, mit denen die $\{r_{i}\}$ bestimmt wurden. 

Die Übersetzung der Aufgabenstellung in ein mathematisches Modell erfolgt mit Hilfe einer **Kostenfunktion**, die bei dieser Methode der [Zustandssumme](https://de.wikipedia.org/wiki/Zustandssumme) der Abstände zwischen der Modellvorhersage $\Omega(\{\theta_{j}\})$ und den $\{r_{i}\}$
$$
\begin{equation}
\chi^{2} = \sum\limits_{i=1}^{n}\frac{\min||\Omega(\{\theta_{j}\}-r_{i}||_{2}}{\Delta r_{i}}
\end{equation}
$$
entspricht. Die Optimierungsaufgabe besteht darin, den kleinsten Wert von $\chi^{2}$ im Raum der Parameter $\{\theta_{j}\}$ zu finden.  

Zur Vereinfachung der Diskussion macht man in Textbüchern oft die folgenden Annahmen, **die jedoch i.a. eher selten gegeben sind**:  

- Die Werte $\{x_{i}\}$ sind [Ausprägungen](https://de.wikipedia.org/wiki/Statistische_Variable) einer Größe $x$, die *keine* Unsicherheiten haben;
- Das Modell $\Omega(\{\theta_{j}\},x)$ ist eine Funktion von $x$ und der Parameter $\{\theta_{j}\}$.

In diesem Fall nimmt Gleichung **(4)** die geläufigere Form 
$$
\begin{equation}
\chi^{2} = \sum\limits_{i=1}^{n}\frac{\left(\Omega(\{\theta_{j},x_{i})-y_{i}\}\right)^{2}}{\Delta y_{i}}
\end{equation}
$$
an. 

Die Optimierungsaufgabe für Gleichung **(5)** kann grundsätzlich analytisch geschlossen gelöst werden, solange $\Omega$ nur *linear* von den Parametern $\{\theta_{j}\}$ abhängt. Heutzutage werden solche Parameteranpassungen algorithmisch von Computern durchgeführt. Mit den Programmpakten *kafe2* und *PhyPraKit* stehen Ihnen geeignete Werkzeuge hierzu zur Verfügung. 

### $\chi^{2}$-Test

Ungeachtet des Umstandes, dass i.a. ein Satz von Parametern $\{\theta_{j}\}$ existiert, für den $\chi^{2}$ minimal wird, kann die Beschreibung der Daten durch $\Omega(\{\theta_{j}\})$ immer noch unzureichend sein. 

Ein Maß dafür, wie gut $\Omega$ die $\{r_{i}\}$, bei optimaler Wahl der $\{\theta_{j}\}$ beschreibt ist der Wert der Kostenfunktion im ihrem Minimum
$$
\begin{equation*}
\min_{\{\theta_{j}\}}\left(\chi^{2}(\{r_{i}\}, \{\theta_{j}\})\right).
\end{equation*}
$$
Dabei gilt: 
$$
\begin{equation*}
\begin{array}{ll}
\chi^{2}/n_{\mathrm{dof}}\lesssim 1 & \text{das Modell ist mit den Daten verträglich;} \\
\chi^{2}/n_{\mathrm{dof}}\gg 1 & \text{das Modell ist mit den Daten nicht verträglich,} \\
\end{array}
\end{equation*}
$$
wobei $n_{\mathrm{dof}} = n-||\{\theta_{j}\}||$ der Anzahl der Datenpunkte abzüglich der Anzahl $||\{\theta_{j}\}||$ der Modellparameter entspricht. Die Größe $n_{\mathrm{dof}}$ wird auch als [*Anzahl der Freiheitsgrade*](https://de.wikipedia.org/wiki/Anzahl_der_Freiheitsgrade_(Statistik)) der Anpassung bezeichnet. Dieser Begriff leitet sich aus der folgenden beispielhaften Vorstellung ab: 

In der Ebene wird eine Gerade durch zwei Datenpunkte $(x_{1}, y_{1})$ und $(x_{2}, y_{2})$ bestimmt. Das mathematische Modell einer geraden $\Omega(a_{0}, a_{1}, x) = a_{1}\hspace{0.05cm}x+a_{0}$ besitzt ebenfalls zwei Parameter $a_{0}$ und $a_{1}$. Durch die Punkte $(x_{1}, y_{1})$ und $(x_{2}, y_{2})$ sind $a_{0}$ und $a_{1}$ eindeutig bestimmt und es besteht keine Freiheit zur Anpassung der Parameter. Ein solches Modell bezeichnet man als *saturiert*. Sobald ein weiterer Punkt $(x_{3}, y_{3})$ hinzukommt ist nicht mehr garantiert, dass $\Omega$ durch geeignete Wahl der Parameter $a_{0}$ und $a_{1}$ jeden Punkt exakt berührt und das Minimum von $\chi^{2}$ wird nicht mehr trivial gefunden. 

Die oben getroffenen Aussagen zu $\chi^{2}/n_{\mathrm{dof}}$ gelten mit mathematischer Strenge, d.h.: Führt eine (statistisch korrekt implementierte) Anpassung auf einen Wert von $\chi^{2}/n_{\mathrm{dof}}\gg 1$, dann ist das zugrundeliegende Modell im Rahmen der angegebenen Unsicherheiten $\{\Delta r_{i}\}$ mit den Datenpunkten $\{r_{i}\}$ **nicht kompatibel**. Es ist in einem solchen Fall grundsätzlich zweifelhaft die Ergebnisse der Anpassung anzugeben oder weiter zu verarbeiten. 

Bei der Verwendung der Programmpakte *kafe2* und *PhyPraKit* wird zu jeder Parameteranpassung der $\chi^{2}/n_{\mathrm{dof}}$-Wert mit ausgegeben, was Ihnen eine Aussage über die Güte der Anpassung ([*goodness-of-fit*](https://en.wikipedia.org/wiki/Goodness_of_fit)) erlaubt. Sie sollten diesen Wert bei jeder Parameteranpassung mit beachten und diskutieren. 

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
Dem Umstand, dass die Taylorreihe bereits nach dem ersten Term abgebrochen wird tragen wir durch das Attribut *lineare* Fehlerfortpflanzung Rechnung. 

Liegen Unsicherheiten $\{\Delta\hat{\theta}_{j}\}$ auf mehrere Parameter $\{\hat{\theta}_{j}:\hspace{0.05cm}j=1\ldots n\}$ vor, muss in $n$ Dimensionen gerechnet werden: 
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

Gebräuchlicher ist Gleichung **(6)** in der Gestalt
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
die dem Spezialfall entspricht, dass die $\{\theta_{j}\}$ alle paarweise unabhängig voneinander sind, wofür $\Sigma$ die Form einer [Diagonalmatrix](https://de.wikipedia.org/wiki/Diagonalmatrix) annimmt. 

Schwierigkeiten bei der linearen Fehlerfortpflanzung bestehen darin, dass die $\{\theta_{j}\}$ i.a. nicht unabhängig und die Korrelationen zwischen den $\{\theta_{j}\}$ nicht bekannt sind. Auch kann es nicht-triviale Korrelationen zwischen den $\{\theta_{j}\}$ geben, für die $\sigma_{ij}=0$ gilt. 

Bei der Anwendung von Gleichung **(7)** sollten Sie sicherstellen und entsprechend argumentieren, warum Sie annehmen (können), dass die $\{\theta_{j}\}$ unabhängig sind. Wenn Sie die Möglichkeit haben, einen Parameter $\theta_{j}\pm\Delta \theta_{j}$ direkt und ohne weitere Fehlerfortpflanzung aus einer Parameteranpassung zu bestimmen sollten Sie dieses Vorgehen der linearen Fehlerfortpflanzung nach Möglichkeit vorziehen. 

## Hinweise zur Durchführung

Die zusätzlichen Angaben der Parameter, die Sie zur Lösung dieser Aufgabe benötigen, finden Sie in den Dateien `parameters_Aufgabe_2.py` oder Datenblatt.md.

### Aufgabe 2.1 Referenzmessung von $T$

- Wählen Sie zur Bestimmung der Referenzmessung einen kurzen Abschnitt aus dem vorliegenden Datensatz frei aus, der ungefähr eine Periode der Pendelschwingung einschließt. Bestimmen Sie daraus $T\pm\Delta T$. 
- Berechnen Sie, mit Hilfe von Gleichung **(2)**, aus $T$ den Wert $g^{(2.1)}\pm\Delta g_{\Delta T}^{(2.1)}$. Den Wert der Größe $\ell$, den Sie für diese Berechnung ebenfalls benötigen, finden Sie z.B. in der Datei Datenblatt.md. 
- Berücksichtigen Sie auch den Einfluss der Unsicherheit $\Delta\ell$ auf die Bestimmung von $g^{(2.2)}$, **durch lineare Fehlerfortpflanzung**. Bestimmen Sie diese als zusätzliche Komponente $\Delta g_{\Delta\ell}^{(2.1)}$. 
- Da die Messung von $\ell$ sicher unabhängig von der Bestimmung von $g_{\Delta T}^{(2.1)}$ erfolgte ist es legitim $\Delta g_{\Delta\ell}^{(2.1)}$ (als unkorrelierte Unsicherheitsquelle) quadratisch zu $\Delta g_{\Delta T}^{(2.1)}$ zu addieren, um eine Gesamtunsicherheit $\Delta g^{(2.1)}$ zu erhalten.
- Vergleichen Sie Ihr Ergebnis von $g^{(2.1)}\pm\Delta g^{(2.1)}$ im Rahmen seiner Unsicherheiten zu $g_{\mathrm{exp}}\pm\Delta g_{\mathrm{exp}}$. 

### Aufgabe 2.2: Erste Erweiterung der Methodik

Das Modell zur Beschreibung der Daten ist durch Gleichung **(2)** gegeben. Bei der Verwendung von *PhyPraKit* können Sie ein solches Modell zur Anpassung an die Daten z.B. durch einen solchen "Funktionsblock" in der `yaml`-Datei zur Ansteuerung des Skripts *run_phyFit.py* definieren:

```yaml
model_label: "HARMONIC_PLAIN"
model_function: |
  def my_model(t, A=0.8, T=1.6, phi=0.):
      return A*np.cos(2*np.pi/T*t+phi)
```

Der Funktionsname `my_model` oder das Label `HARMONIC_PLAIN` sind ist dabei frei gewählt. Beachten Sie, dass die `yaml`-Datei mit diesem Modell auch mit dem Skript *plotData.py* verwendet werden kann. In diesem Fall wird das Modell zusammen mit den Daten dargestellt. Die dabei verwendeten Modellparameter entsprechen den Defaultwerten der Funktionsargumente im oben angegebenen Funktionsblock. 

Wenn Sie das Modell *an die Daten anpassen* möchten führen Sie das Skript *run_phyFit.py* mit der gleichen `yaml`-Datei aus. Aus einer Code-Zelle des Jupyter-notebook könnte dies z.B. so aussehen:

```shell
%run /opt/conda/bin/run_phyFit.py foo.yaml 
```

Die Größe $\chi^{2}/n_{\mathrm{dof}}$ und die Werte und Unsicherheiten der angepassten Parameter $A$, $\omega$ und $\phi$ sind Ausgaben der Anpassung. Gehen Sie bei der Bearbeitung dieses Aufgabenteils wie folgt vor: 

- Ermitteln Sie $g^{(2.2)}\pm\Delta g_{\Delta T}^{(2.2)}$ mit Hilfe der Anpassung und vergleichen Sie Ihr Ergebnis im Rahmen seiner Unsicherheiten zu $g_{\mathrm{exp}}\pm\Delta g_{\mathrm{exp}}$. 
- Diskutieren und erklären Sie alle Beobachtungen, die Sie dabei machen. Wie kommt es, dass $\Delta g_{\Delta T}^{(2.2)}$ so viel kleiner ist, als $\Delta g_{\Delta T}^{(2.1)}$ und wie steht es um den Vergleich mit $g_{\mathrm{exp}}$?

###  Aufgabe 2.3: Zweite Erweiterung der Methodik

Sie können auf die Fehlerfortpflanzung nach Gauß bis zu einem gewissen Grad  verzichten, indem Sie $g\pm\Delta g$ direkt als Modellparameter bestimmen. Unter Verwendung von *PhyPraKit* könnte ein entsprechend verändertes Modell so aussehen: 

```yaml
model_label: "HARMONIC_G"
model_function: |
  def model(t, A=0.8, g=9.8, phi=0):
      return x0*np.cos(np.sqrt(g/0.6285)*t+phi)
```

Bei der Zahl `0.6385` handelt es sich um die Länge $\ell$ des Pendels (siehe Datenblatt.md), die wir als **äußeren Parameter** bestimmt haben und als solchen in das Modell einbringen. 

Aus dieser Modifikation ergeben sich tiefere Einsichten in die Diskussion der berücksichtigten Unsicherheiten:

Die Größe $\ell$ hat selbst eine Unsicherheit $\Delta\ell$, die wir in der Bestimmung von $\Delta g$ berücksichtigen sollten. Da $\ell$, als *von außen eingebrachter* Parameter, nicht immanent, aus der Anpassung selbst, bestimmt werden kann, müssen wir $\Delta\ell$ ebenfalls von außen in die Bestimmung von $g$ einbringen.  Am einfachsten erreichen wir dies, indem wir $\ell$ um $\pm\Delta\ell$ variieren und die Anpassung erneut (insgesamt also $3\times$) durchführen. Die Unsicherheit $\Delta\ell$ wird entsprechend auf $g$ propagiert und führt so zu einer Unsicherheit $\Delta g_{\Delta\ell}^{(2.2)}$ unter Variation von $\ell$ um den Betrag $\pm\Delta\ell$. 

Die Unsicherheit $\Delta g_{\Delta\ell}$, die sich aus der ungenügenden Kenntnis von $\ell$ ergibt bezeichnet man in diesem Bild als epistemische, oder **systematische Unsicherheit**. In der Physik sind systematische Unsicherheiten i.d.R. mit systematischen Variationen verbunden. Im Gegensatz dazu bezeichnet man $\Delta g_{\Delta T}$, das die Unsicherheiten der Datenpunkte, an die das Modell angepasst wurde und damit die eigentliche Messung repräsentiert, als **statistische Unsicherheit**.

Nach der Anpassung an die Daten können Sie $g^{(2.3)}$ direkt als Ausgabewert der Anpassung ablesen. Es handelt sich lediglich um eine Umparametrisierung des Modells aus Aufgabe 2.1 für die Sie die folgenden Eigenschaften feststellen sollten: 

- Der Wert von $g^{(2.3)}$ ist der gleiche, wie für $g^{(2.2)}$ aus Aufgabe 2.2;
- Der Wert von $\Delta g_{\Delta T}^{(2.3)}$ ist der gleiche, wie für $\Delta g_{\Delta T}^{(2.2)}$ aus Aufgabe 2.2;
- Der Wert von $\chi^{2}/n_{\mathrm{dof}}$ für die Güte der Anpassung ist der gleiche, wie aus Aufgabe 2.2.

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Vorversuch)

