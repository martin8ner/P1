# Hinweise für den Versuch Vierpole und Leitungen

## Aufgabe 3: Drosselkette

### Leitungseigenschaften der idealen Drosselkette

Aus der Substitution
$$
\begin{equation*}
\cosh\gamma = \frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}}+1
\end{equation*}
$$
 folgt
$$
\begin{equation*}
\sinh\frac{\gamma}{2} = \sqrt{\frac{Z_{\mathrm{L}}}{2\,Z_{\mathrm{C}}}} = \sqrt{-\left(\frac{\omega}{\omega_{0}}\right)^{2}} = i\frac{\omega}{\omega_{0}}.
\end{equation*}
$$
Andererseits gilt:
$$
\begin{equation*}
\sinh\frac{\gamma}{2} = \sinh\left(\frac{\alpha+i\beta}{2}\right) = \sinh\frac{\alpha}{2}\,\cos\frac{\beta}{2} + i\,\cosh\frac{\alpha}{2}\,\sin\frac{\beta}{2},
\end{equation*}
$$
die folgenden Gleichungen müssen also gleichzeitig erfüllt sein: 
$$
\begin{equation*}
\begin{split}
&\sinh\frac{\alpha}{2}\,\cos\frac{\beta}{2} = 0; \\
&\\
&\cosh\frac{\alpha}{2}\,\sin\frac{\beta}{2} = \frac{\omega}{\omega_{0}},
\end{split}
\end{equation*}
$$
woraus man die folgenden Lösungen erhält: 
$$
\begin{equation}
\begin{array}{ccl}
\alpha & \beta & \\
0 &2\,\arcsin\left(\frac{\omega}{\omega_{0}}\right) & \text{f\"ur }\omega<\omega_{0}\\
2\,\arccos\left(\frac{\omega}{\omega_{0}}\right) & \pi & \text{f\"ur }\omega>\omega_{0},\\
\end{array}
\end{equation}
$$
d.h. die (ideale) Drosselkette hat die **Eigenschaft eines Tiefpasses**: 

- Für $\omega<\omega_{0}$ weist sie keine Dämpfung auf, d.h. sie ist als Leitung verlustfrei.
- Für $\omega>\omega_{0}$ steigt die Dämpfung mit $\omega$ steil an. Die Phase des Ausgangssignals ist um $\pi$ zum Eingangssignal verschoben. 

### Hinweise zur Durchführung

#### Aufgabe 3.1: Bestimmung von $Z_{0}$

Bestimmen Sie $Z_{0}$ der Drosselkette wie folgt: 

- Legen Sie eine **rechteckförmige** Wechselspannung niedriger Frequenz an. Wir schlagen $\nu\approx 20\,\mathrm{kHz},\,U_{0}\approx 6\,\mathrm{V_{SS}}$ vor. Mit $\mathrm{V_{SS}}$ ist die Spannungsdifferenz von Signalsitze zu Signalspitze gemeint.

- Schließen Sie die Drosselkette mit der regelbaren Lastimpedanz $Z_{\mathrm{A}}$, als Abschlusswiderstand kurz. 

- Beobachten Sie das Eingangssignal am Oszilloskop. Sie nutzen für diese Messung den Umstand aus, dass das Eingangssignal für $Z_{\mathrm{A}}=Z_{0}$ am Ende der Leitung **nicht** reflektiert wird. Treten Reflexionen am Ende der Leitung auf, ist das beobachtete Signal eine Superposition aus dem ursprünglichen Signal und ggf. mehrerer Reflexionen in der Leitung. Das Signal kann also nicht unverfälscht beobachtet werden. 

- Regeln Sie $Z_{\mathrm{A}}$ solange, bis Sie das Eingangssignal unverfälscht beobachten können und bestimmen Sie den Wert von $Z_{\mathrm{A}}$. Durch die Wahl einer niedrigen Frequenz bestimmen Sie 
  $$
  \begin{equation*}
  Z_{\mathrm{A}}=Z_{0}\approx\sqrt{\frac{L}{C}}
  \end{equation*}
  $$
   unter der Annahme $\omega\ll\omega_{0}$.

#### Aufgabe 3.2: Bestimmung von $\omega_{0}$

Bestimmen Sie die $\omega_{0}$ der Drosselkette wie folgt:

- Legen Sie eine **harmonische** Wechselspannung an. Wir schlagen $\nu\lesssim 1\,\mathrm{MHz},\,U_{0}\approx 6\,\mathrm{V_{SS}}$ vor. Belassen Sie $Z_{\mathrm{A}}$ auf dem zuvor bestimmten Wert für $\omega\ll\omega_{0}$.
- Beobachten Sie das Eingangssignal und überzeugen Sie sich von der Frequenzunabhängigkeit der Eingangsspannung.
- Beobachten Sie das Ausgangssignal und erhöhen Sie $\nu$ schrittweise. Regeln Sie $Z_{\mathrm{A}}$ bei steigenden Werten von $\nu$ entsprechend Ihrer Erwartung für die Frequenzabhängigkeit von $Z_{0}$ (Gleichung (**3**) [hier](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Vierpole_und_Leitungen/doc/Hinweise-Aufgabe-3.md)) nach, um Reflexionen in der Leitung zu vermeiden. 
- Suchen Sie die Schwelle in $\omega$ auf, ab der die Drosselkette Signale mit $\omega>\omega_{0}$ als Tiefpass unterdrückt. Bestimmen Sie $\omega_{0}$ aus der Position für $U_{0}/U_{n}=1/10$. 

#### Aufgabe 3.3: Bestimmung von $C$ und $L$

Bestimmen Sie $C$ und $L$ aus den zuvor bestimmten Werten für $Z_{0}$ (für $\omega<\omega_{0}$) und $\omega_{0}$. Pflanzen Sie die Unsicherheiten Ihrer Messungen von $Z_{0}$ und $\omega_{0}$ entsprechend fort und vergleichen Sie mit den technischen Angaben zu diesem Versuchsteil.  

#### Aufgabe 3.4: Phasendifferenz zwischen Ein- und Ausgangssignal

Für diese Aufgabe betreiben Sie das Oszilloskop im Zweikanalmodus. 

- Bestimmen Sie, für 6–8 Werte von $\nu$ zwischen $10$–$650\,\mathrm{kHz}$, die Phasendifferenz $\Delta\varphi$ zwischen Eingangs- und Ausgangssignal für eine harmonische Wechselspannung als Funktion von $\omega$. Sorgen Sie für einen reflexionsfreien Abschluss der Messanordnung.
- Führen Sie sowohl für die **Drosselkette**, als auch für ein **einzelnes $\pi$-Glied** eine solche Messreihe durch. 
- Überzeugen Sie sich von den folgenden Eigenschaften:
  - Für $\omega=\omega_{0}$ ist $\Delta\varphi$ zwischen Ein- und Ausgangssignal für ein einzelnes $\pi$-Gliedes $\pi$. 
  - Für eine $n$-gliedrige Drosselkette ist $\Delta\varphi$ zwischen Ein- und Ausgangssignal (für kleine Werte von $\Delta\varphi$) gegenüber dem einzelnen $\pi$-Glied $n$ mal größer.
- Bestimmen Sie $\omega$ für $\Delta\varphi=\pi,\,2\pi,\,3\pi,\,4\pi,\,5\pi$ und daraus erneut $\omega_{0}$ (Gleichung (**1**)). Vergleichen den so ermittelten Wert und dessen Unsicherheit mit Ihrem Ergebnis aus Aufgabe 3.2.  

#### Aufgabe 3.5: Reflexion

- Schließen Sie für diesen Versuchsteil das Ende der Drosselkette kurz ($Z_{0}=0\,\Omega$). Dadurch wird das Signal am Kettenende reflektiert. 
- Vermeiden Sie Reflexionen am Leitungsanfang, indem Sie einen Steckwiderstand $Z_{\mathrm{E}}\approx Z_{0}$ zwischen Signalgenerator und Kettenanfang schalten. 
- Schließen Sie eine rechteckförmige Wechselspannung ($\nu\approx20\,\mathrm{kHz}$) an. welche Signalform beobachten Sie am Kettenanfang? Entspricht dies Ihrer Erwartung?   

# Navigation

[Zurück](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Vierpole_und_Leitungen/doc/Hinweise-Aufgabe-3.md) | [Main](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Vierpole_und_Leitungen) | [Weiter](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Vierpole_und_Leitungen/doc/Hinweise-Leitungen-a.md)
