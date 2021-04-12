# 3.3 Area and Similarity

How do we define area? Neutral geometry has right triangles but no rectangles, so the traditional idea of a rectangular (or square) area only exists in Euclidean geometry. 

````{warning}
In any non-Eudclidean geometry, calculating the area of a triangle will prove troublesome.
````

Our work is made much easier because the SMSG axiom set has an area postulate which provides the normal definition of rectangular area.

````{epigraph}
The area of a rectangle is the product of the length of its base and the length of its altitude.

--SMSG Axiom 20
````

We can use the SMSG Area Postulate to derive the typical formuals for the areas of triangles, trapezoids and parallelograms. The following definitions will also be helpful.

Parallel Segments
: We call line segments *parallel* if they are contained in lines that are parallel.

Distance from a point to a line
: Given a point $P$ not on line $l$, the *distance between $P$ and $l$* is the distance $PQ$ where $Q\in l$ and $\overleftrightarrow{PQ}\perp l$.

Kite
: A convex quadrilateral with two pairs of adjacent sides congruent.

Rhombus
: A parallelogram with all sides congruent.

Rectangle
: A parallelogram with a right angle.

Square
: A rhombus with a right angle.

Similar Polygons
: Two polygons are *similar* provided (i) corresponding sides of each are in the same proportion, and (ii) corresponding interior angles are congruent.

Congruence is a more primitive geometric idea than similarity, even though, ironically, similarity has fewer restrictions. 

````{tip}
Similarity proofs often use areas of triangles as numerators or deonominators to establish the required proportion. Until we have proven some results about area, proving similarity theorems is difficult.
````

The parallelogram decomposition theorem stated that we could always create congruent triangles by drawing the diagonal of a parallelogram and considering the two resulting triangles. The theorem is true in the reverse: given any two congruent triangles, they can be joined to create a parallelogram. We will put the following in our toolbox:

## Theorems
1. The area of a parallelogram is the product of the lengths of its base and height.

2. Parallelogram Recomposition Theorem. If $\triangle{ABC}\cong\triangle{XYZ}$ and $X=B$ and $Y=A$, then $AZBC$ is a parallelogram.

    <iframe scrolling="no" title="Angle Interior" src="https://www.geogebra.org/material/iframe/id/mdz5ks7k/width/840/height/500/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/true/ctl/false" width="100%" height="100%" style="border:0px;" allowfullscreen; style="display:block" > </iframe>

3. The area of a triangle is one-half the product of the any base and the corresponding height.

4. The area of a trapezoid is the product of its height and the arithmetic mean of its bases.

    ````{margin}
    ![Pythagorean Theorem](https://www.mathsisfun.com/geometry/images/pythagoras.svg)
    Area Proof of Pythagorean Theorem
    ````

5. **Pythagorean Theorem (Area Proof)**. If $a$ and $b$ are the lengths of the legs of a right triangle the hypotenuse of which has length $c$, then $a^2+b^2=c^2$.

6. **Basic Proportionality Theorem**. A line parallel to one side of a triangle intersects the other two sides in two different points if and only if it divides these sides into segments that are proportional. 

    ````{figure} ../images/Proportion.png
    ---
    width: "50%"
    name: Medians of a triangle
    ---
    Proportionality theorem: $\overline{DE}\parallel\overline{BC}\implies \frac{AD}{DB}=\frac{AE}{EC}$.
    ````


    ````{note}
    The "two different points" verbiage requires the point of intersection to not be the vertex.
    ````

7. **AA Triangle Similarity**. If two interior angles of one triangle are congruent to corresponding angles of a second triangle, then the triangles are similar.

8. **SAS Triangle Similarity**. If an angle of one triangle is congruent to the corresponding angle of a second triangle, and the corresponding sides adjacent to these angles are in proportion, then the triangles are similar.

9. **SSS Triangle Similarity**. If the lengths of the sides of one triangle are proportional to the corresponding side lengths of a second triangle, then the triangles are similar.

10. **Converse of Pythagorean Theorem.** Given $\triangle ABC$ with side lengths $a,b,c$ such that $c$ is the longest side, then $a^2 +b^2 = c^2$ only if $\triangle ABC$ is a right triangle.