# 2.1 Congruence, Lines and Angles

````{warning}
The concepts included in our SMSG Axioms jump far ahead of our definitions, so we gain ideas about objects before they are even defined.
````

````{margin}
```{seealso}
Distances are defined by the {doc}`SMSG</AX/A4>` Distance Postulate, Axiom 2, so we can immediately define segment congruence, circles and other terms that rely upon distance.
```
````

Definitions depend heavily upon the set of axioms and undefined terms. Read each definition below and make note of the ones that feel awkward. All definitions have to work within the set of axioms, so be sure to check out the {doc}`SMSG Axioms</AX/A4>` page.

Segment
: A *segment* $\overline{AB}$ is the set of points $A$, $B$ and all points $P$ such that $P\in\overleftrightarrow{AB}$ and $AP+PB=AB$.

````{warning}
Segments are often defined as "all points on a line **between** $A$ and $B$" (plus endpoints). But we haven't defined *between* yet. That requires knowing what a segment is.
````
Between
: A point $B$ is *between* $A$ and $C$ if $B\in \overline{AC}$ but $B\neq A,C$.

````{note}
Saying point $P$ is *between* two points requires it to be on a line or segement that joins those two points. We use the idea of *between* to define rays (see below).
````

Segment Congruence
: Two segments are congruent if the distances between their endpoints are equal.

Circle
: The set of all points equidistant from a point called the *center*.

````{margin}
```{seealso}
We can now prove the first construction theorem in {doc}`Section C.1</CN/C1>`, that radii of congruent circle are congruent.
```
````

Angle Congruence
: Two angles are congruent if their measures are equal.

Polygon Congruence
: Two polygons are congruent if and only if there exists a one-to-one correspondence between their vertices such that all their corresponding sides (line sgements) and all their corresponding angles are congruent.

````{note}
Congruence relations are *equivalance relations* (see Theorem 1). Specifically, congruence relations are symmetric, reflexive and transitive.
````

Collinear
: Two points lying on the same line.

Intersecting Lines
: Two lines *intersect* if there exists a point that is on both lines.

Parallel Lines
: Two lines in the same plane which do not intersect.

Concurrent Lines
: Three or more coplanar lines that have a point in common.

````{note}
Defining a ray can be tricky. The one below was inspired by Hilbert and his use of "betweeness" axioms.
````
Ray
: A *ray* $\overrightarrow{AB}$ (also called a half-line) is a subset of the line $\overleftrightarrow{AB}$ that contains a given point $A$ and all the points $C\in\overleftrightarrow{AB}$ such that $A$ is not between $C$ and $B$. The point $A$ is called the *endpoint* of the ray.

````{margin}
Animation shows how rays are defined: the point $A$ can never be between $B$ and $C$.
````

<iframe scrolling="no" title="Definition of Ray" src="https://www.geogebra.org/material/iframe/id/zyyfrpxb/width/1180/height/360/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/true/ctl/false" width="100%" height="100%" style="border:0px;" allowfullscreen; style="display:block" > </iframe>

Angle
: The union of two rays which have the same endpoint.

Straight Angle
: An angle whose rays are distinct but collinear.

Angle Interior
: A point $P$ is in the *interior* of $\angle{ABC}$ provided:
 + $\measuredangle{ABC}<180^\circ$
 + there exist points $X,Y$ such that
   + $X\in\overrightarrow{BA}$,
   + $Y\in\overrightarrow{BC}$, and
   + $P$ is between $X$ and $Y$

````{margin}
Animation demonstrates the angle interior: points $P$ in the interior must be between points $X$ and $Y$.
````

<iframe scrolling="no" title="Angle Interior" src="https://www.geogebra.org/material/iframe/id/x4x9bxqm/width/1180/height/360/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/true/ctl/false" width="100%" height="100%" style="border:0px;" allowfullscreen; style="display:block" > </iframe>


Convex
: A polygon $P$ is *convex* if $X,Y\in P\implies \overline{XY}\in P$.

````{margin}
Animation demonstrates definition of convex: all points on the segment $\overline{XY}$ must lie in the interior of the polygon if $X$ and $Y$ do.
````

<iframe scrolling="no" title="Definition of Convex" src="https://www.geogebra.org/material/iframe/id/yevmvetn/width/1180/height/360/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/true/ctl/false" width="100%" height="100%" style="border:1px;" allowfullscreen; style="display:block" > </iframe>

Midpoint
: The *midpoint* $C$ of $\overline{AB}$ lies on $\overline{AB}$ such that $AC = CB$.

Angle Bisector
: The ray $\overrightarrow{BD}$ is the angle bisector of $\angle{ABC}$ if $\measuredangle ABD = m\measuredangle DBC$.

Right Angle
: An angle with angle measure $90^\circ$ (see SMSG Axiom 11).

Acute Angle
: An angle with angle measure less than $90^\circ$.

Perpendicular Bisector
: A line which passes through the midpoint of a line segment and which forms a right angle with that segment at the point of intersection.

Obtuse Angle
: An angle with angle measure greater than $90^\circ$.

````{warning}
Angles *must* have measure between $0^\circ$ and $180^\circ$ (inclusive), so we can't yet define reflex angles, nor are we allowed to have angles with negative measure.
````

Vertical Angles
: The angles opposite each other when two lines cross.

Linear Pair
: Two distinct angles that share a ray whose non-shared rays are colinear.

````{hint}
The SMSG Supplementary Postulate (Axiom 14) uses the term *linear pair* which we must define, else the term *supplementary* will have no meaning.
````

Supplementary Angle Postulate
: If two angles form a linear pair, they are supplementary.

````{warning}
The SMSG Axioms introduce a non-standard geometry term *linear pair*, but let's embrace it and define the term *right angle pair*, too!
````

Right Angle Pair
: Two distinct angles that share a ray whose non-shared rays form a right angle.

Complementary Angle
: If two angles form a right angle pair, they are complementary.

## Theorems
1. Congruence relations are equivalence relations.
2. Every line segment has exactly one midpoint. 
3. Every angle has exactly one bisector.
4. Supplements and complements of the same angles are congruent. 
5. The intersection of two convex polygons is convex.
6. Vertical angles are congruent.

    ````{tip}
    Pasch's Axiom is equivalent to the SMSG Plane Seperation Postulate (Axiom 9) and thus will not need to be proven.
    ````

7. **Pasch's Axiom**. Given a line that contains no vertex of a triangle, if that line intersects one side of the triangle, it must intersect another. 

    ````{margin}
    Animation demonstrates Pasch's Axiom.
    ````

    <iframe scrolling="no" title="Pasch's Axiom" src="https://www.geogebra.org/material/iframe/id/czt3guuj/width/1180/height/360/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/true/ctl/false" width="100%" height="100%" style="border:1px;" allowfullscreen; style="display:block" > </iframe>

8. **Crossbar Theorem**. If at least one point of $\overrightarrow{AC}$ is in the interior of $\angle{BAD}$ then $\overrightarrow{AC}$ intersects $\overline{BD}$.

![Crossbar Theorem Illustration](Fig2.png)

````{tip}
Euclid often used a version of the Crossbar theorem to prove that lines in his constructions actually intersected.
````

The Crossbar theorem is a direct result of Pasch's Axiom. We don't need to prove this theorem when using the SMSG Axioms because the Ruler Postulate and Distance Postulates guarantee that all lines in our geometry have the same properties as the real number line, and the Plane Separation Postulate (or Pasch's Axiom) guarantees the intersections that Euclid was justifying.