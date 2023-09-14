# Hinweise für den Versuch Vierpole und Leitungen

## Aufgabe 2: Drosselkette [3/3]

### Hinweise zur Durchführung

#### Aufgabe 2.1: Bestimmung der charakteristischen Impedanz $Z_{0}$

Bei dieser Messung nutzen wir den Umstand, dass das Eingangssignal für $Z_{\mathrm{A}}=Z_{0}$ am Ende der Leitung **nicht** reflektiert wird (siehe Diskussion [hier](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Vierpole_und_Leitungen/doc/Hinweise-Leitungen.md)). 

Für den Fall $Z_{\mathrm{A}}\neq Z_{0}$ treten Reflexionen am Leitungsende auf, so dass das beobachtete Signal am Leitungsanfang eine Überlagerung aus dem ursprünglichen Signal und ggf. sogar mehrerer Reflexionen an den Leitungsenden ist.  Wie wählen für die Messung daher eine Signalform aus, mit der wir Überlagerungen möglichst einfach erkennen können. Sobald Sie Sie bei der Reglung von $Z_{\mathrm{A}}$ die charakteristische Impedanz $Z_{\mathrm{A}}=Z_{0}$ erreichen sollten Sie das Eingangssignal unverfälscht beobachten können. Durch die Wahl einer niedrigen Frequenz $\omega\ll\omega_{0}$ bestimmen Sie auf diese Weise in guter Näherung
$$
\begin{equation*}
Z_{\mathrm{A}}=Z_{0}\approx\sqrt{\frac{L}{C}}.
\end{equation*}
$$


Gehen Sie für die Messung wie folgt vor: 

- Legen Sie eine **rechteckförmige** Wechselspannung niedriger Frequenz an. Wir schlagen $\nu\approx 20\hspace{0.05cm}\mathrm{kHz}$, $U_{0}\approx 6\hspace{0.05cm}\mathrm{V_{SS}}$ vor.

- Schließen Sie die Drosselkette mit der regelbaren Lastimpedanz $Z_{\mathrm{A}}$, als Abschlusswiderstand kurz. 

- Beobachten Sie das Eingangssignal am Oszilloskop. 

- Regeln Sie $Z_{\mathrm{A}}$ solange, bis Sie das Eingangssignal unverfälscht beobachten können und lesen Sie den so erhaltenen Wert von $Z_{\mathrm{A}}$ ab. 

#### Aufgabe 2.2: Bestimmung der Grenzfrequenz $\omega_{0}$

Bestimmen Sie $\omega_{0}$ der Drosselkette wie folgt:

- Legen Sie eine **harmonische** Wechselspannung an. Wir schlagen $\nu\lesssim 1\hspace{0.05cm}\mathrm{MHz}$, $U_{0}\approx 6\hspace{0.05cm}\mathrm{V_{SS}}$ vor. Belassen Sie $Z_{\mathrm{A}}$ auf dem zuvor bestimmten Wert für $\omega\ll\omega_{0}$.
- Beobachten Sie das Eingangssignal und überzeugen Sie sich von der Frequenzunabhängigkeit der Eingangsspannung.
- Beobachten Sie das Ausgangssignal und erhöhen Sie $\omega$ schrittweise. Regeln Sie $Z_{\mathrm{A}}$ bei steigenden Werten von $\omega$ entsprechend Ihrer Erwartung für die Frequenzabhängigkeit von $Z_{0}$ (Gleichung **(3)** [hier](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Vierpole_und_Leitungen/doc/Hinweise-Aufgabe-2.md)) nach, um Reflexionen in der Leitung zu vermeiden. 
- Suchen Sie die Schwelle in $\omega$ auf, ab der die Drosselkette Signale mit $\omega>\omega_{0}$ als Tiefpass unterdrückt. Bestimmen Sie $\omega_{0}$ aus der Position für $\left|U_{n}\right|/\left|U_{0}\right|=1/10$. 

#### Aufgabe 2.3: Bestimmung von $C$ und $L$ der in der Drosselkette verbauten Elemente

Bestimmen Sie $C$ und $L$ aus den zuvor bestimmten Werten für $Z_{0}$ (für $\omega<\omega_{0}$) und $\omega_{0}$. Pflanzen Sie die Unsicherheiten Ihrer Messungen von $Z_{0}$ und $\omega_{0}$ entsprechend fort und vergleichen Sie mit den technischen Angaben zu diesem Versuchsteil.  

#### Aufgabe 2.4: Bestimmung der Phasendifferenz $\Delta\varphi$

Betreiben Sie für diese Aufgabe das Oszilloskop im Zweikanalmodus. 

- Legen Sie eine harmonische Wechselspannung als Eingangssignal an die Drosselkette.
- Bestimmen Sie für 6–8 verschiedene Frequenzen zwischen $10$–$650\,\mathrm{kHz}$, $\Delta\varphi$ als Funktion von $\omega$. Sorgen Sie dabei für einen reflexionsfreien Abschluss der Messanordnung, wie für Aufgabe 2.2. Für die Einstellungen am Frequenzgenerator bieten sich z.B. die folgenden Werte an: $\nu=10,100,300,500,600,650,690\,\mathrm{kHz}$ an. 
- Die vorliegende Schaltung erlaubt es Ihnen auch ein Signal nach Durchlaufen nur eines einzelnen $\pi$-Glieds auszulesen. Führen Sie die gleiche Messreihe sowohl für die gesamte **Drosselkette**, als auch für ein **einzelnes $\pi$-Glied** durch. 

Bestimmen Sie abschließend nochmals $\omega_{0}$, diesmal aber aus $\Delta\varphi$. Gehen Sie dabei wie folgt vor:

- Betreiben Sie das Oszilloskop im Zweikanalmodus. Legen Sie dabei $U_{0}$ auf einen und $U_{1}$ auf den anderen Eingang. So können Sie den Verlauf beider Signale als [Lissajous-Figur](https://de.wikipedia.org/wiki/Lissajous-Figur) darstellen und Vielfache von $\Delta\varphi=n\,\pi,\,n\in\mathbb{N}$ leicht aus den sich einstellenden Diagonalen ablesen.

- Für das $\pi$-Glied gilt $\Delta\varphi=\pi$ für $\omega=\omega_{0}$. Für die sechsgliedrige Drosselkette ist $\Delta\varphi$ um den Faktor $n=6$ relativ zum $\pi$-Glied verstärkt. Bestimmen Sie $\omega$ für die am Oszilloskop bestimmten Werte von $\Delta\varphi=1\pi,2\pi,3\pi,4\pi,5\pi$. 
- Tragen Sie die ermittelten Werte für $\omega$ gegen $n\cdot\pi/6, \,n=1\ldots5$ auf und passen Sie eine Gerade an den Verlauf der Messwerte an. Aus der Steigung der Geraden erhalten Sie eine Messung für $\omega_{0}$. 

Vergleichen den so ermittelten Wert und dessen Unsicherheit mit Ihrem Ergebnis aus Aufgabe 2.2.  

#### Aufgabe 2.5: Reflexionen

- Schließen Sie für diesen Versuchsteil das Ende der Drosselkette kurz ($Z_{0}=0\,\Omega$). Dadurch wird das Signal am Kettenende mit einem Phasensprung von $\pi$ reflektiert (siehe Diskussion [hier](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Vierpole_und_Leitungen/doc/Hinweise-Leitungen.md)). 
- Vermeiden Sie Reflexionen am Leitungsanfang, indem Sie einen Steckwiderstand $Z_{\mathrm{E}}\approx Z_{0}$ zwischen Signalgenerator und Kettenanfang schalten. Ersetzen Sie hierzu den Kurzschlussstecker zwischen Generator und Kettenanfang durch den zur Verfügung stehenden $200\,\Omega$-Steckwiderstand.  
- Schließen Sie eine rechteckförmige Wechselspannung ($\nu\approx20\,\mathrm{kHz}$) an. welche Signalform beobachten Sie am Kettenanfang? Entspricht dies Ihrer Erwartung?   

# Navigation

[Zurück](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/Vierpole_und_Leitungen/doc/Hinweise-Aufgabe-2-a.md) | [Main](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/tree/main/Vierpole_und_Leitungen)
