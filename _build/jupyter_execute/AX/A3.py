# A.3 Birkhoff Axioms

Birkhoff's Axiom set is an example of what is called a *metric geometry*. A metric geometry has axioms for distance and angle measure which leverage the properties of real numbers and the real number line. Birkhoff used the following undefined terms:

* Points
* Sets of points called *lines*
* *Distance* between any two points $A$ and $B$: a non-negative real number $d(A,B)$ such that $d(A,B)=d(B,A)$
* *Angle* formed by three ordered points $A$, $O$, $B$ ($A \neq O$, $B \neq O$): $\angle AOB$ a real number (mod $2\pi$). The point $O$ is called the \textbf{vertex} of the angle.

````{note}
Note that lines are sets of points, and Birkhoff intentionally invites basic set theory into his geometric system including opeations like intersections, unions and set subtraction.
````

Birkhoff used only four axioms:

1. **Line Measure Axiom**. The points $A,B,\dots$  of any line $l$ can be placed into one-to-one correspondence with the real numbers $x$ so that $|x_A - x_B| = d(A,B)$ for all points $A$, $B$.
2. **Point-Line Axiom**. One and only one line $l$ contains two given points $P$, $Q$ $(P \neq Q)$.
3. **Angle Measure Axiom**. The half-lines $l,m,\dots$ through any point $O$ can be placed into one-to-one correspondence with the real numbers $a(mod 2\pi)$ so that if $A \neq O$ and $B \neq O$ are points of $l$ and $m$, respectively, the difference $(a_m - a_n)(mod 2\pi)$ is $\angle AOB$.
4. **Similarity Axiom**. If in two triangles $\triangle ABC$, $\triangle A'B'C'$ and for some constant $k > 0$, $d(A',B') = kd(A,B)$, $d(A',C') = kd(A,C)$, and $m\angle B'A'C' = \pm\angle BAC$, then also $d(B',C') = kd(B,C)$, $m\angle A'B'C' = \pm\angle ABC$, and $\angle A'C'B' = \pm\angle ACB$.

#### Birkhoff's defined terms

* A point $B$ is *between* $A$ and $C$ $(A \neq C)$, if $d(A,B) + d(B,C) = d(A,C)$.
* The points $A$ and $C$, together with all points $B$ between $A$ and $C$, form *line segment* $\overline{AC}$.
* The *half-line* $l'$ with *endpoint* $O$ is defined by two points $O, A$ in line $l$ $(A \neq O)$ as the set of all points $A'$ of $l$ such that $O$ is not between $A$ and $A'$. 
* If two distinct lines have no point in common, they are *parallel*. A line is always regarded as parallel to itself.
* Two half-lines through $O$ are said to form a *straight angle* if $m\angle mOn=\pm \pi$. Two half-lines through $O$ are said to form a *right angle* if $m\angle mOn=\pm \frac{\pi}{2}$, in which case we also say that $m$ is \textbf{perpendicular} to $n$.
* If $A, B, C$ are three distinct points, the segments $\overline{AB}, \overline{BC}, \overline{CA}$ are said to form a *triangle* $\triangle ABC$ with sides $\overline{AB}, \overline{BC}, \overline{CA}$ and vertices $A, B, C$. If $A, B, C$ are collinear, then $\triangle ABC$ is said to be *degenerate*.
* Any two geometric figures are *similar* if there exists a one-to-one correspondence between the points of the two figures such that all corresponding distances are in proportion and corresponding angles have equal mesure (except, perhaps, for their sign). Any two geometric figures are *congruent* if they are similar with a constant of proportionality $k=1$.