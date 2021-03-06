# 3.3 Area and Similarity

How do we define area? Neutral geometry has right triangles but no rectangles, so the traditional idea of a rectangular (or square) area only exists in Euclidean geometry. 

````{warning}
In any non-Eudclidean geometry, calculating the area of a triangle will prove troublesome.
````

The SMSG axioms have an area postulate.

````{epigraph}
The area of a rectangle is the product of the length of its base and the length of its altitude.

--SMSG Axiom 20
````


The following definitions will also be helpful.

Parallel Segments
: We call line segments *parallel* if they are contained in lines that are parallel.

Distance from a point to a line
: Given a point $P$ not on line $l$, the *distance between $P$ and $l$* is the distance $PQ$ where $Q\in l$ and $\overleftrightarrow{PQ}\perp l$.

Trapezoid
: A convex quadrilateral with exactly one pair of parallel sides.

````{warning}
Two definitions of a trapezoid exist: *exactly* one pair of parallel sides, or *at least* one pair of parallel sides. The former excludes parallelograms while the latter includes them. Generally, especially in K-12 mathematics, the "*exactly* one pair of parallel sides" definition is preferred.
````

Kite
: A convex quadrilateral with two pairs of adjacent sides congruent.

Rhombus
: A parallelogram with all sides congruent.

Square
: A parallelogram with a right angle.

Similar Polygons
: Two polygons are *similar* provided (i) corresponding sides of each are in the same proportion, and (ii) corresponding interior angles are congruent.

Congruence is a more primitice geometric idea than similarity, even though, ironically, similarity has less restrictions. All similarity proofs involve using areas of triangles as numerators or deonominators of triangles to establish the required proportion. Until we have proven some results about area, we cannot prove similarity theorems.

The parallelogram decomposition theorem stated that we could always create congruent triangles by drawing the diagonal of a parallelogram and considering the two resulting triangles. The theorem is true in the reverse: given any two congruent triangles, they can be joined to create a parallelogram. We will put the following in our toolbox:

## Theorems
1. The area of a parallelogram is the product of the lengths of its base and height.

2. Parallelogram Recomposition Theorem. If $\triangle{ABC}\cong\triangle{XYZ}$ and $X=B$ and $Y=A$, then $AZBC$ is a parallelogram.

3. The area of a triangle is one-half the product of the any base and the corresponding height.

4. The area of a trapezoid is the product of its height and the arithmetic mean of its bases.

5. **Pythagorean Theorem (Area Proof)**. If $a$ and $b$ are the lengths of the legs of a right triangle the hypotenuse of which has length $c$, then $a^2+b^2=c^2$.

    ````{note}
    Requirement (i) implies a constant ratio of proportionality for any two pairs of side lengths.
    ````

6. **Basic Proportionality Theorem**. A line parallel to one side of a triangle intersects the other two sides in two different points if and only if it divides these sides into segments that are proportional. (The ``two different points" simply requires the point of intersection to not be the vertex.)

7. **AAA Triangle Similarity**. If the interior angles of one triangle are congruent to corresponding angles of a second triangle, then the triangles are similar.

8. **SAS Triangle Similarity**. If an angle of one triangle is congruent to the corresponding angle of a second triangle, and the corresponding sides adjacent to these angles are in proportion, then the triangles are similar.

9. **SAS Triangle Similarity**. If the lengths of the sides of one triangle are proportional to the corresponding side lengths of a second triangle, then the triangles are similar.

