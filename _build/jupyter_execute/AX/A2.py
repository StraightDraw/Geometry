# A.2 Hilbert's Axioms

The system begins with undefined terms *point*, *line* and *plane* and the fundamental **incidence relation**. We need two more relations: the *betweenness relation* denoted by $*$, and the *congruence relation* denoted by $\cong$. All three relations are undefined and are given meaning within the corresponding set axioms. A quick note about incidence: although the relation $P\in l$ should, strictly speaking, be read: "$P$ and $l$ are incident," we shall use "$l$ contains $P$," "$P$ lies on $l$" or any obviously logical equivalent.

## Incidence Axioms

1. For every pair of distinct points $A$ and $B$ there is a unique line $l$ containing $A$ and $B$.
2. Every line contains at least two points.
3. There are at least three points that do not lie on the same line.

## Betweenness Axioms
The next group of axioms deals with the relation "$B$ lies between $A$ and $C$."  We will use the notation $A*B*C$ for "$B$ lies between $A$ and $C$."

1. If $A*B*C$, then $A$, $B$ and $C$ are distinct points on a line, and $C*B*A$ also holds.
2. Given two distinct points $A$ and $B$, there exists a point $C$ such that $A*B*C$.
3. If $A$, $B$ and $C$ are distinct points on a line, then one and only one of the relations $A*B*C$, $B*C*A$ and $C*A*B$ is satisfied.
4. Let $A$, $B$ and $C$ be points not on the same line and let $l$ be a line which contains none of them. If $D\in l$ and $A*D*B$, there exists an $E$ on $l$ such that $B*E*C$, or an $F$ on $l$ such that $A*F*C$, but not both.

If we think of $A$, $B$ and $C$ as the vertices of a triangle, another formulation of B4 is this: If a line $l$ goes through a side of a triangle but none of its vertices, then it also goes through exactly one of the other sides. This formulation is also called **Pasch’s Axiom**. Note that this is not true in $\mathbb{R}^n$ where $n\geq3$. Hence, I.3 and B.4 together define the geometry as "2-dimensional."

## Congruence Axioms
We have two sets of three congruence axioms, the first for congruent line segments, the second for angle congrunce.
    
1. Given a segment $AB$ and a ray $r$ from $C$, there is a uniquely determined point $D$ on $r$ such that $CD\cong AB$.
2. $\cong$ is an equivalence relation on the set of segments.
3. If $A*B*C$ and $A'*B'*C'$ and both $AB\cong A'B'$ and $BC\cong B'C'$, then also $AC\cong A'C'$.
4. Given a ray $\overrightarrow{AB}$ and an angle $\angle B'A'C'$, there are angles $\angle BAE$ and $\angle BAF$ on opposite sides of $\overrightarrow{AB}$ such that $\angle BAE \cong \angle BAF \cong \angle B'A'C'$.
5. $\cong$ is an equivalence relation on the set of angles.
6. Given triangles $\triangle ABC$ and $\triangle A'B'C'$. If $AB \cong A'B'$, $AC\cong A'C'$ and $\angle BAC\cong \angle B'A'C'$, then the two triangles are congruent: $BC\cong B'C'$, $\angle ABC \cong \angle A'B'C'$ and $\angle BCA \cong \angle B'C'A'$.
