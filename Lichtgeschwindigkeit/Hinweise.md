# Hinweise für den Versuch Lichtgeschwindigkeit

## Aufgabe 1: Messung von $c$ (in Luft) mit Hilfe der Drehspiegelmethode

### Prinzip der Messung

Diese Methode zur Messung von $c$ basiert auf der Vorstellung eines Wellenpakets, das sich mit endlicher *Gruppengeschwindigkeit* zwischen Dreh- und Endspiegel ausbreitet. Um die Strecke zwischen Dreh- und Endspiegel ($a+b$ in der [Skizze](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/Musterprotokoll/Lichtgeschwindigkeit/figures/Drehspiegelmethode.png)) zurückzulegen benötigt das Wellenpaket die endliche Zeit: 

```math
\begin{equation}
\Delta t = \frac{2(a+b)}{c}
\end{equation}
```

In dieser Zeit hat sich der Drehspiegel, der sich mit der Frequenz $\nu$ dreht um den Winkel 

```math
\begin{equation}
\alpha=2\pi\,\nu\Delta t
\end{equation}
```

weiter gedreht. Da für die Reflexion am Drehspiegel Einfallswinkel gleich Ausfallswinkel gilt wird der Strahl unter dem Winkel $2\alpha$ vom Drehspiegel zurück reflektiert. Ohne Drehung des Spiegels würde der Strahl in sich selbst zurück reflektiert werden. Durch die Drehung des Spiegels um den Winkel $\alpha$ erscheint der Strahl auf einem Schirm um die Strecke $s$ zu seinem Ursprung versetzt. Der Versatz $s$ ergibt sich (unter Annahme der Kleinwinkelnäherung) aus $\alpha$ nach

```math
\begin{equation}
\frac{s}{\ell} = \tan(2\alpha)\approx2\alpha
\end{equation}
```

Daraus ergibt sich die Gleichung zur Berechnung von $c$:

```math
\begin{equation}
c = 8\pi\frac{\ell\,\nu\left(a+b\right)}{s}
\end{equation}
```

Im Aufbau durchläuft der Lichtstrahl einen Strahlteiler, so dass ein Teil des Strahls senkrecht zur Lichtquelle auf einen Schirm projiziert wird. Der Winkel des Strahlteilers muss sehr genau justiert sein, was eine potentielle Quelle systematischer Fehlmessungen darstellt.

### Die Sammellinse im Strahlengang

Die Sammellinse hat die Funktion den Strahl auf einen Punkt zu fokussieren. Sie wird so aufgestellt, dass ihr Brennpunkt im Drehspiegel liegt. Lichtstrahlen aus dem Brennpunkt werden hinter der Linse auf parallele Bahnen gebeugt. Auf dem Rückweg vom Endspiegel wird der Strahlengang wieder in den Brennpunkt auf dem Drehspiegel zurück fokussiert. **Dies geschieht nur entlang der optischen Achse der Linse**. Durch diese Konstruktion findet eine Auswahl der Lichtpakete statt, die zu einem festen Zeitpunkt $t_{0}$ genau entlang der optischen Achse der Linse reflektiert werden. Der Drehspiegel hat also zu Beginn der "Laufzeitmessung" immer die gleiche Winkelposition, für die ein Gegenstand ($G$) in ein Bild ($B$) abgebildet wird. Für ($b'$) Bild- und ($g'$) Gegenstandsweite gilt, mit den Angaben aus der [Skizze](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/Musterprotokoll/Lichtgeschwindigkeit/figures/Drehspiegelmethode.png):

```math
\begin{equation}
\begin{split}
&g' = \ell+f \\
&b' = a+b-f
\end{split}
\end{equation}
```

Unter Verwendung der [Linsengleichung](https://de.wikipedia.org/wiki/Linsengleichung) lässt sich so der Abstand $\ell$ zwischen Laser und Drehspiegel bestimmen, bei dem der Laserstrahl ($G$) als Bild $B$ im Endspiegel abgebildet wird:

```math
\begin{equation}
\begin{split}
&\frac{1}{f} = \frac{1}{g'} + \frac{1}{b'} = \frac{1}{\ell+f} + \frac{1}{a+b-f}; \\
&\\
&\frac{1}{\ell+f} = \frac{1}{a+b-f} - \frac{1}{f} = \frac{a+b-2f}{(a+b-f)\,f}; \\
&\\
&\ell = \frac{(a+b-f)\,f}{a+b-2f} -f = \frac{(a+b-f)\,f - (a+b-2f)\,f}{a+b-2f};\\
&\\
&\ell= \frac{f^{2}}{a+b-2f}.
\end{split}
\end{equation}
```

Mit den vorgegebenen Werten von $a$, $b$, $f$ und der Position des Drehspiegels ergibt sich die optimale Position $\ell$ des Lasers.

### Hinweise zur Durchführung

- Tragen Sie Messpunkte für 10–12 Wertepaare aus $\nu$ und $s$ graphisch auf und nehmen Sie eine geeignete Anpassung vor. Begründen Sie das der Anpassung zu Grunde gelegte Modell.
- Geben Sie ein Maß für die Güte der Anpassung (*goodness of fit*) als $\chi^{2}/\mathrm{ndof}$ und als $p$-Wert an und bewerten Sie die Anpassung. 
- Überlegen Sie welche äußeren Parameter Sie für die Bestimmung von $c$ noch kontrollieren müssen und wie gut dies der Fall ist.
- Geben Sie Ihr Ergebnis aus der Anpassung mit statistischen und systematischen Unsicherheiten an. 

---

## Aufgabe 2: Messung von $c$ (in Luft) mit Hilfe einer Phasenvergleichmethode

### Prinzip der Messung

Diese Methode zur Messung von $c$ basiert auf der Messung der Phasenverschiebung $\Delta\varphi$ zwischen einem Empfänger- und einem Referenzsignal. Aus $\Delta\varphi$ lässt sich bei gegebener Kreisfrequenz $\omega$ des Referenzsignals eine Zeitdifferenz $\Delta t$ bestimmen und bei bekanntem Abstand $\ell$ zwischen Sender und Empfänger so die *Phasengeschwindigkeit* berechnen. 

Bei der Bestimmung von $c$ mit Hilfe einer [Lissajous](https://de.wikipedia.org/wiki/Lissajous-Figur)-Figur messen Sie bei vorgegebenem $\Delta\varphi$ die Wegdifferenz $\Delta\ell$ des verschobenen Senders. In allen anderen Fällen bestimmen Sie $\Delta\varphi$ für vorgebenene Werte von $\ell$.   

### Messbereichserweiterung des Oszilloskops

Mit der Zeitauflösung eines einfachen Oszilloskops ist die beabsichtigte Messung mit dem vorliegenden Aufbau nicht ohne weiteres möglich. Sie können die Messung trotzdem mit den im Praktikum zur Verfügung stehenden Mitteln durchführen. Hierzu nutzen wir eines der [Additionstheoreme](https://de.wikipedia.org/wiki/Formelsammlung_Trigonometrie#Produkte_der_Winkelfunktionen) der Kosinus-Funktion: 

```math
\begin{equation}
\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta,
\end{equation}
```

woraus sich der folgende Zusammenhang leicht ableiten lässt: 

```math
\begin{equation}
\cos\alpha\cos\beta = \frac{1}{2}\Bigl(\cos(\alpha+\beta)+\cos(\alpha-\beta)\Bigr).
\end{equation}
```

Wir wählen zur Beschreibung des funktionalen Zusammenhangs des (ursprünglichen) Referenzsignals eine Kosinus-Funktion $\cos(\omega\,t+\varphi)$, wobei $\omega$ der Kreisfrequenz und $\varphi$ einer freien Phase entsprechen. Wir modulieren (mit Hilfe der in das Hauptnetzgerät eingebauten Mischstufen) die Amplitude des Referenzsignals multiplikativ mit einem gleichen Signal mit geringfügig niedrigerer Frequenz $\omega'\lesssim\omega$. Für das so veränderte (endgültige) Referenzsignal ergibt sich dadurch der folgende funktionale Zusammenhang zur Beschreibung seiner Amplitude: 

```math
\begin{equation}
\cos(\omega\,t+\varphi)\cos(\omega'\,t) = \frac{1}{2}\Bigl(\cos((\omega+\omega')\,t+\varphi) + \cos((\omega-\omega')\,t+\varphi)\Bigr).
\end{equation}
```

Wir interessieren uns für den zweiten Term in der Klammer auf der rechten Seite der Gleichung, der den Verlauf $\cos((\omega-\omega')\,t+\varphi)$ aufweist. Der hochfrequente Term $\cos((\omega+\omega')\,t+\varphi)$ kann durch einen Tiefpassfilter unterdrückt werden. 

Sie können feststellen, dass die Phase $\varphi$ unverändert vom ursprünglichen Referenzsignal (der Form $\cos(\omega\,t+\varphi)$) auf den Term $\cos((\omega-\omega')\,t+\varphi)$ übertragen wird, so dass auch die später zu messende Phasendifferenz $\Delta\phi$ zwischen Empfänger- und Referenzsignal erhalten bleibt, d.h. eine Phasendifferenz $\Delta\varphi$ im nicht modulierten Eingangssignal entspricht der gleichen Phasendifferenz $\Delta\overline{\varphi}$ in der späteren Darstellung auf dem Oszilloskop. Zur Unterscheidung stellen wir die auf dem Oszilloskop dargestellten Größen überstrichen dar. 

Wie diskutiert gilt $\Delta\varphi=\Delta\overline{\varphi}$, die Frequenzen $\omega$ und $\overline{\omega}\equiv\omega-\omega^{\prime}$ unterscheiden sich jedoch. Der Verlauf auf der Zeitachse des Oszilloskops erscheint daher um den Faktor $\omega/\overline{\omega}$  gedehnt:

```math
\begin{equation}
\begin{split}
\Delta \overline{\varphi} &= \Delta \varphi;\qquad
\overline{\omega}\,\Delta\overline{t} = \omega\,\Delta t; \qquad
\Delta \overline{t} &= \omega/\overline{\omega}\,\Delta t,
\end{split}
\end{equation}
```

wobei $\Delta \overline{t}$ einem auf dem Oszilloskop dargestellten Zeitfenster (mit dem Verlauf $\cos((\overline{\omega})\,t+\varphi)$) und $\Delta t$ einem Zeitfenster des ursprünglichen Signals (mit dem Verlauf $\cos(\omega\,t+\varphi)$) entsprechen. Durch den gedehnten Maßstab können auch sehr kurze Zeitdifferenzen im Eingangssignal aufgelöst werden. Es handelt sich also effektiv um eine **"Messbereichserweiterung" des Oszilloskops zu kürzeren Zeitabständen**.

Um $\Delta\varphi$ deutlich sichtbar zu machen wird das Referenzsignal mit einem Störsignal der Frequenz $59,9\,\mathrm{MHz}$ multiplikativ gemischt. Mittels eines Tiefpassfilters werden die hochfrequenten Anteile des gemischten Signals unterdrückt und die niederfrequenten Anteile auf einem einfachen computergestützten Oszilloskop, als Funktion der Zeit dargestellt.

### Hinweise zur Durchführung

- Bestimmen Sie $\Delta\overline{\varphi}$ für mindestens fünf verschiedene Werte von $\ell$. Beachten Sie den Zeit Dehnungsfaktor $\omega/\overline{\omega}$ bei der Bestimmung von $\Delta t$. 
- Tragen Sie die Wertepaare graphisch auf und nehmen Sie eine geeignete Anpassung vor. Begründen Sie das der Anpassung zu Grunde gelegte Modell.
- Geben Sie ein Maß für die Güte der Anpassung (*goodness of fit*) als $\chi^{2}/\mathrm{ndof}$ und als $p$-Wert an und bewerten Sie die Anpassung. 
- Überlegen Sie welche äußeren Parameter Sie für die Bestimmung von $c$ noch kontrollieren müssen und wie gut dies der Fall ist.
- Geben Sie Ihr Ergebnis aus der Anpassung mit statistischen und systematischen Unsicherheiten an.

---

## Aufgabe 3: Bestimmung des Brechungsindex $n$ von Wasser oder Plexiglas

In optisch dichten Medien ist $c$ niedriger, als im Vakuum (oder Luft). Das Maß in dem $c$ abnimmt wird durch den Brechungsindex $n$ (auch optische Dichte genannt) quantifiziert. Wir bestimmen den Brechungsindex durch die erhöhte Laufzeit des Lichtes im optisch dichteren Medium. Dazu bringen wir in einen Teil des Laufwegs $\ell$ des Lichtstrahls ein Behältnis der Länge $d<\ell$ mit dem optisch dichteren Medium ein. Damit gilt für die Laufzeit:

```math
\begin{equation*}
\begin{split}
&\Delta t = \frac{\ell-d}{c}+\frac{n\,d}{c}; \\
&\\
& n = \frac{c\,\Delta t-\ell}{d}+1. \\
\end{split}
\end{equation*}
```

 Für Aufgabe 3.1 wird $\Delta t$ analog zu Aufgabe 2 bestimmt, die Abmessungen $\ell$ und $d$ sind gegeben. 

Auch der Laserentfernungsmesser gibt die Entfernung zu einer reflektierenden Oberfläche (Reflektor) basierend auf einer Laufzeitmessung des ausgesandten Laserlichtes unter Annahme von $c$ (in Luft) an: 

```math
\begin{equation*}
\Delta t = \frac{2 \ell}{c}
\end{equation*}
```

Wird ein Teil $d$ des Weges $\ell$ zum Reflektor durch ein Medium der optischen Dichte $n$ ersetzt ändert (verfälscht) dies die Längenmessung, woraus sich $n$ bestimmen lässt: 

```math
\begin{equation*}
\begin{split}
\Delta t' &= 2\frac{\ell-d}{c} + 2\frac{d\,n}{c}; \\
&\\
\ell' &= \frac{c}{2}\Delta t' = \ell-d+d\,n; \\
&\\
&n = \frac{\ell'-\ell}{d}+1, \\
\end{split}
\end{equation*}
```

wobei $\ell$ die unverfälschte Anzeige ohne und $\ell'$ die verfälschte Anzeige mit optisch dichterem Medium ist.

### Hinweise zur Durchführung

- Führen Sie die Messung für Aufgabe 3.2 mindestens viermal durch, indem Sie den Laserstrahl einmal quer und einmal längs durch die Küvette laufen lassen und jeweils noch einmal $\ell$ variieren. 

- Bestimmen Sie jeweils ein Ergebnis für $n_{i}$ mit entsprechender Unsicherheit $\Delta n_{i}$. 

- Das Ergebnis Ihrer Messung ist dann das gewichtete Mittel $\overline{n}$ der Einzelmessungen:

  ```math
  \begin{equation*}
  \begin{split}
  &\overline{n} = \frac{\sum w_{i}n_{i}}{\sum w_{i}}\qquad \text{mit:}\qquad w_{i}=\frac{1}{\Delta n_{i}}; \\
  &\\
  &\mathrm{var}[\overline{n}] = \frac{N}{N-1}\frac{\sum w_{i}\left(n_{i}-\overline{n}\right)^{2}}{\sum w_{i}}; \qquad \sigma_{\overline{n}} = \sqrt{\mathrm{var}[\overline{n}]}, \\
  \end{split}
  \end{equation*}
  ```

  wenn $N$ die Länge Ihrer Stichprobe ist.