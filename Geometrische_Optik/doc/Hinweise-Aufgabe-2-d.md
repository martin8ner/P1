# Hinweise für den Versuch Geometrische Optik

## Aufgabe 2: Vermessung eines Zweilinsensystems $L$ (5/5)

### Hinweise zur Durchführung

- Führen Sie für die Bestimmung von $f$, $h_{x}$ und $h_{x}'$ eine Anpassung an mindestens 5 Wertepaare $(x, x')$ durch. Vergessen Sie für die Anpassung nicht in jedem Punkt Unsicherheiten, sowohl entlang der x- ($\Delta\beta$,  $\Delta(1/\beta)$), als auch der $y$-Achse ($\Delta x$, $\Delta x'$) anzugeben. 

- Als Modell, um $f$, $h_{x}$ und $h_{x}'$ gleichzeitig bestimmen zu können nutzen Sie die Tatsache, dass $x$ relativ zu $X$ mit einem negativen Vorzeichen gemessen wird. Sie können also ein Modell, wie das folgende ansetzen:

  ```python
  def model(B, G, f, hx, hxp):
      if B>0:
          return f*(B/G+1)+hxp
      return f*(-1+G/B)-hx
  ```

  wobei Sie $B$ einen negativen (positiven) Wert für die Messung von $x$ ($x'$) geben. In diesem Modell würden Sie die Unsicherheit auf $G$, als korrelierte Unsicherheit für alle Punkte in $x$ und $x'$ systematisch variieren. Eigentlich müssten zudem die Unsicherheiten auf $B$ in jeweils zwei Punkten, die sich nur durch ihr Vorzeichen unterscheiden korreliert sein, da es sich um die gleiche Messung von $B$ handelt.

- Geben Sie die Korrelationskoeffizienten zwischen $f$, $h_{x}$ und $h_{x}'$ als Ergebnisse der Anpassung mit an. Tun Sie dies auch, wenn Sie das Modell zur Bestimmung von $f$, $f_{1}$ und $f_{2}$ verwenden.  

- Zur Bestimmung von $f$ aus (Gleichung (1) [hier](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische_Optik/doc/Hinweise-Aufgabe-2.md)) setzen Sie $f$, $f_{1}$ und $f_{2}$ aus der vorherigen Anpassung als Startwerte. Gegebenenfalls können $f$ außerdem auf den zuvor ermittelten Wert fixieren. Die Variation von $f$ sollten Sie in diesem Fall, ebenso wie die Variation von $d$, innerhalb der zuvor bestimmten Grenzen, als systematische Variation quantifizieren. 

# Navigation

[Zurück](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Geometrische_Optik/doc/Hinweise-Aufgabe-2-c.md) | [Main](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Geometrische_Optik) 
