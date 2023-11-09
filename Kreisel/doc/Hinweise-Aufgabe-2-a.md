# Hinweise für den Versuch Kreisel

## Aufgabe 2: Kardanisch gelagerter Kreisel

Der genaue Ablauf dieser Bewegung hängt von der Beschaffenheit des Kreisels ab: 

- Für den prolaten Kreisel ($\theta_{z}<\theta_{\perp}$, **Skizze 3** mittig, **Skizze 4** links) liegt $\vec{\omega}$ zwischen $\hat{z}$ und $\vec{L}$; der *äußere* Mantel des Gangpolkegels rollt auf dem äußeren Mantel des Rastpolkegels ab; in $K$ kreisen $\vec{\omega}$ und $\hat{z}$ in Phase um $\vec{L}$.  
- Für den oblaten Kreisel ($\theta_{z}>\theta_{\perp}$, **Skizze 3** rechts, **Skizze 4** rechts) liegt $\vec{L}$ zwischen $\hat{z}$ und $\vec{\omega}$; der *innere* Mantel des Gangpolkegels rollt auf dem äußeren Mantel des Rastpolkegels ab; in $K$ kreisen $\vec{\omega}$ und $\hat{z}$ gegenphasig um $\vec{L}$. 

<img src="../figures/Polkegel.png" width="900" style="zoom:100%;" />

**Skizze 4** (Bewegungsablauf des Kreisels für den (links) prolaten und (rechts) oblaten symmetrischen Kreisel)

---

Um die Nutation quantitativ besser zu verstehen empfiehlt es sich $\vec{\omega}$ in einen Anteil $\vec{\omega}_{\hat{z}}$ parallel zu $\hat{z}$ und einen Anteil $\vec{\omega}_{N}$ parallel zu $\vec{L}$ zu zerlegen:
$$
\begin{equation*}
\vec{\omega} = \vec{\omega}_{N} + \vec{\omega}_{\hat{z}},
\end{equation*}
$$
wie in **Skizze 5** dargestellt. Ebenfalls in die Skizze eingetragen sind der Öffnungswinkel des Gangpolkegels $\alpha$ und der Öffnungswinkel des Nutationskegels $\beta$. 

<img src="../figures/Nutation.png" width="900" style="zoom:100%;" />

**Skizze 5** (Definitionen zum quantitativen Verständnis der Nutation)

---

Mit diesen Definitionen ergeben sich die folgenden Zusammenhänge: 
$$
\begin{equation*}
\begin{split}
& \tan\alpha = \frac{\omega_{\perp}}{\omega_{z}};\qquad\tan\beta = \frac{L_{\perp}}{L_{z}} = \frac{\theta_{\perp}\,\omega_{\perp}}{\theta_{z}\,\omega_{z}} = \frac{\theta_{\perp}}{\theta_{z}}\tan\alpha; \\
&\\
& \sin\alpha = \frac{\omega_{\perp}}{\omega};\qquad \sin\beta = \frac{\omega_{\perp}}{\omega_{N}} \\
&\\
& \omega_{N} = \frac{\omega_{\perp}}{\sin\beta} = \frac{\omega}{\sin\beta}\,\sin\alpha = \frac{\omega}{\sin\beta}\,\sqrt{\frac{\tan^{2}{\alpha}}{1+\tan^{2}\alpha}}\\
&\\
&\text{mit:}\\
&\\
&\tan\alpha = \frac{\theta_{z}}{\theta_{\perp}}\tan\beta \\
&\\
&\omega_{N} = \frac{\omega}{\sin\beta}\,\sqrt{\frac{1}{1/\tan^{2}\alpha+1}} = \omega\,\sqrt{\frac{\theta_{z}^{2}}{\theta_{\perp}^{2}\cos^{2}\beta+\theta_{z}^{2}\sin^{2}\beta}}.
\end{split}
\end{equation*}
$$
 Für kleine Werte von $\beta$ ergibt dies:
$$
\begin{equation}
\omega_{N} = \omega\,\sqrt{\frac{\theta_{z}^{2}}{\theta_{\perp}^{2}\cos^{2}\beta+\theta_{z}^{2}\sin^{2}\beta}} \approx \omega\,\frac{\theta_{z}}{\theta_{\perp}}
\end{equation}
$$
Wie aus Gleichung **(1)** ersichtlich gilt für den oblaten (prolaten) Kreisel $\omega_{N}>\omega$ ($\omega_{N}<\omega$).

Die obigen Betrachtungen gelten für einen einfachen symmetrischen Kreisel. Im Fall des in **Abbildung 1** gezeigten, kardanisch gelagerten Kreisels, wie er im Praktikum zum Einsatz kommt, müssen die Trägheitsmomente der *massiven* Kardanrahmen bei der Beschreibung der Kreiselbewegung berücksichtigt werden. Bei Drehungen um $\hat{x}$ dreht sich der innere und bei Drehungen um $\hat{y}$ sowohl der innere, als auch der äußere Kardanrahmen mit. Für die Trägheitsmomente gilt daher: 
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
