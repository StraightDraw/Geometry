# 3. Euclidean Geometry

Along with Bolyai, we have completed our trek through the controversies of parallelism. Euclid's 5th, indeed, is an axiom. We can now launch a new quest to fully establish Euclidean geometry knowing all neutral geometry theorems true. In additon, we finally get to use a parallel postulate.

````{admonition} Playfair's Postulate
Through a given external point there is at most one line parallel to a given line (SMSG Axiom 16).
````

The "at most" wording in the parallel postulate rules out hyperbolic geometry where multiple lines through an external point may be parallel to a given line. 

## Pathways from the Parallel Postulate

Establishing the full power of the Alternate Interior Angles theorem will unlock several important proofs. In neutral geometry, we were only able to prove one direction.

````{admonition} Alternate Interior Angles Theorem (AIA)
If two lines are intersected by a transversal such that a pair of alternate interior angles is congruent, then the lines are parallel.
````

With Axiom 16 ruling out multiple parallels through an external point, we can prove the converse.

````{admonition} Converse of the Alternate Interior Angles Theorem (CAIA)
If two parallel lines are intersected by a transversal, then the alternate interior angles formed are congruent.
````

With CAIA as a tool in our kit, we can immediately show that the angle sums of triangles must be $180^\circ$ and that rectangles exist. The parallel postulate has straightened the curves of the geometry.

## Neutral vs. Euclidean Geometry

The following comparisons show the gap -- often just a sliver -- between neutral geometry theorems and important results in Euclidean geometry.

````{panels}
:column: col-6
:card: border-2
**True in Neutral Geometry**
---
**True in Euclidean Geometry**
````

````{panels}
:column: col-6
:card: border-2
Alternate Interior Angle Theorem
^^^
If two lines are intersected by a transversal such that a pair of alternate interior angles is congruent, then the lines are parallel.
---
Converse of the Alternate Interior Angle Theorem
^^^
If two parallel lines are intersected by a transversal, then the alternate interior angles formed are congruent.
````

````{panels}
:column: col-6
:card: border-2
Perpendicular Uniqueness
^^^
Given a line $l$ and any point $P$ not on $l$, there exists a unique line $m$ such that $P\in m$ and $m\perp l$.
---
Parallel Uniqueness
^^^
Given a line $l$ and any point $P$ not on $l$, there exists a unique line $m$ such that $P\in m$ and $m\parallel l$.
````

````{panels}
:column: col-6
:card: border-2
Corollary to AIA
^^^
Two lines perpendicular to the same line are parallel.
---
Corollary to CAIA
^^^
If a line is perpendicular to one of two parallel lines, then it is perpedicular to the other.
````

````{panels}
:column: col-6
:card: border-2
Saccheri-Legendre
^^^
The angle sum of a triangle is less than or equal to $180^\circ$.
---
Corollary to CAIA
^^^
The angle sum of a triangle is $180^\circ$.
````


```{toctree}
:hidden:
:titlesonly:


E1
E2
E3
E4
E5
E6
E7
E8
```
