# 3.1 Building Blocks

We proved parallel lines exist in neutral geometry using only Euclid's first four axioms. 

````{note}
Right angles and perpendicularity work reasonably well in neutral geometry.
````

Since two lines perpendicular to the same line are parallel, we know that we construct some parallel lines. Now that we have a parallel postulate, we only need a few definitions to be ready to prove important results.

Median
: A line passing through a vertex and the midpoint of the side opposite that vertex.

Parallel Segments
: We call line segments *parallel* if they are contained in lines that are parallel.

Distance from a point to a line
: Given a point $P$ not on line $l$, the *distance between $P$ and $l$* is the distance $PQ$ where $Q\in l$ and $\overleftrightarrow{PQ}\perp l$.

Trapezoid
: A convex quadrilateral with *exactly one pair* of parallel sides.

Isosceles Trapezoid
: A trapezoid with non-parallel sides congruent.

Kite
: A quadrilateral with two pairs of adjacent sides congruent.

Rhombus
: A parallelogram with all sides congruent.

## Theorems
1. Converse of the Alternate Interior Angle Theorem. If two parallel lines are intersected by a transversal, then the alternate interior angles formed are congruent.
2.  The sum of the measures of the interior angles of triangle is $180^\circ$. 

    ````{tip}
    For a neutral geometry, the angle sum for triangle was at most $180^\circ$. What forces the equality in Euclidean space?
    ````

3.  **Euclidean Exterior Angle Theorem**. The measure of an exterior angle of a triangle is equal to the sum of the measures of the two remote interior angles.

4. **Parallelogram Decomposition Theorem**. [^1]  In parallelogram $ABCD$, $\triangle{ABD} \cong \triangle{CDB}$ and $\triangle{ABC}\cong\triangle{CDA}$.

    <iframe scrolling="no" title="Angle Interior" src="https://www.geogebra.org/material/iframe/id/hakjwjtn/width/1000/height/400/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/true/ctl/false" width="100%" height="100%" style="border:0px;" allowfullscreen; style="display:block" > </iframe>

    ````{note}
    Two important corrolaries of the Parallelogram Decomposition theorem will be quite useful.
    ```{panels}
    :column: col-6
    :card: border-2
    Segments
    ^^^
    Opposite *sides* of a parallelogram are *congruent*.
    ---
    Angles
    ^^^
    Opposite *angles* of a parallelogram are *congruent*.
    ```
    ````

    ````{note}
    The next few important theorems identify key relationship about the diagonals of quadrilaterals.
    ```{seealso}
    The Isosceles Triangle theorem and its corollary -- both proved in neutral geometry -- are useful in proving the theorems below.
    ```
    ````

5. The diagonals of a quadrilateral bisect each other if and only the quadrilateral is a parallelogram.
6. Exactly one diagonal of a quadrilateral is the perpendicular bisector of the other if and only if the quadrilateral is a kite.

    ````{margin}
    ```{seealso}
    After Theorem 7, we can prove our {doc}`Second Construction Theorem</CN/C1>`.
    ```
    ````

7. The diagonals of a quadrilateral are perpendicular bisectors of one another if and only if the quadrilateral is a rhombus.

9. The diagonals of a quadrilateral are congruent perpendicular bisectors of one another if and only if the quadrilateral is a square.

