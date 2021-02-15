# 3.1b Building Blocks

The content of this section is being reorganized -- still under construction.

Median
: A line passing through a vertex and the midpoint of the side opposite that vertex.

Parallel Segments
: We call line segments *parallel* if they are contained in lines that are parallel.

Distance from a point to a line
: Given a point $P$ not on line $l$, the *distance between $P$ and $l$* is the distance $PQ$ where $Q\in l$ and $\overleftrightarrow{PQ}\perp l$.

Trapezoid
: A convex quadrilateral with exactly one pair of parallel sides.

Kite
: A quadrilateral with two pairs of adjacent sides congruent.

Rhombus
: A parallelogram with all sides congruent.

## Theorems

6. **Angle Sum Theorem**. The angle sum of a convex quadrilateral is $360^\circ$. Moreover, the angle sum of an $n$-sided convex polygon is $(n-2)180^\circ$.

    ````{tip}
    The angle-sum theorem is true without the word "convex," but it is easier prove with this restriction.
    ````

7. If a transversal intersects three parallel lines in such a way as to make congruent segments between the paralllels, then every transversal interesecting these parallel lines will do likewise.

    ````{tip}
    Construct additional well-placed transversals, and use similar triangles.
    ````
8. If a transversal intersects $n$ parallel lines ($n>2$) in such a way as to make congruent segments between the paralllels, then every transversal interesecting these parallel lines will do likewise. 
    ````{tip}
    Use induction.
    ````

9. **Median Concurrence Theorem**. The three medians of a triangle are concurent at a point called the centroid. 
    ````{tip} 
    Consider $\triangle DFG$ with median $\overline{DM}$. Note $M$ is the midpoint of $\overline{FG}$. Call the centroid point $C$. Then the measure of $\overline{DC}$ is exactly twice the measure of $\overline{CM}$. This is true - but must be proven. Theorems 5 and 6 along with this fact provide an outline for the proof.
    ````
10. Medians of a triangle intersect at a point that is two-thirds the distance from any vertex to the midpoint of the opposite side.

    ````{note} 
    The following theorems are direct consequences of the Euclidean parallel postulate and establish many common notions in Euclidean geometry.
    ````

11. Two lines parallel to another line are parallel to each other.
12. If a line intersects one of two parallel llines, then it interesects the other.
13. Each diagonal of a parallelogram partitions the parallelogram into a pair of congruent triangles.
14. The diagonals of a parallelogram bisect each other.
15. If the diagonals of a quadrilateral bisect each other, the quadrilateral is a parallelogram.
16. If a line segment has as its endpoints the midpoints of two sides of a triangle, then the segment is parallel to and one-half the length of the third side of the triangle. 
17. The diagonals of a rhombus are perpendicular.
18. If the diagonals of a quadrilateral bisect each other and are perpendicular, then the quadrilateral is a rhombus.
19. In a right triangle, the median from the right angle to the hypotenuse is one-half the length of the hypotenuse.
20. In a right triangle, one of the angles measures $30^\circ$ if and only if the side opposite this angle is one-half the length of the hypotenuse. 
    ````{note} This result along with the Pythagorean Theorem gives us the $1-2-\sqrt3$ ratio of side lengths for $30-60-90$ right triangles. The Pythagorean Theorem will be proven later.
    ````
21. The midpoints of the sides of a quadrilateral are the vertices of a convex parallelogram.

[^1]: The theorem name "Parallelogram Decomposition Theorem" is non-standard, invented and used in this document only, and describes the functional relationship between a parallelogram and two corresponding congruent triangles that connect across a diagonal.