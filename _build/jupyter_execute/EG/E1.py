#!/usr/bin/env python
# coding: utf-8

# # 3.1 Building Blocks

# Neutral geometry has parallel lines, in fact, too many. Infinitely many are possible. SMSG Axioms 1-15 force parallels to be possible, but the question of unique parallels vs. infintely many remains unanswered until we add SMSG Axiom 16 (Playfair's Postulate). By saying "at most one," we force unique parallels. The possibility of "no parallels at all" has already been eliminated. This restriction immediately allows for the proof of several important theorems. First, let's lay out the definitions we will need.
# 
# Median
# : A line passing through a vertex and the midpoint of the side opposite that vertex.
# 
# Parallel Segments
# : We call line segments *parallel* if they are contained in lines that are parallel.
# 
# Distance from a point to a line
# : Given a point $P$ not on line $l$, the *distance between $P$ and $l$* is the distance $PQ$ where $Q\in l$ and $\overleftrightarrow{PQ}\perp l$.
# 
# Trapezoid
# : A convex quadrilateral with exactly one pair of parallel sides.
# 
# Kite
# : A quadrilateral with two pairs of adjacent sides congruent.
# 
# Rhombus
# : A parallelogram with all sides congruent.

# ## Theorems
# 1. Converse of the Alternate Interior Angle Theorem. If two parallel lines are intersected by a transversal, then the alternate interior angles formed are congruent.
# 2.  The sum of the measures of the interior angles of triangle is $180^\circ$. 
#     ````{tip}
#     For a neutral geometry, the angle sum for triangle was at most $180^\circ$. What forces the equality in Euclidean space?
#     ````
# 3.  The measure of an exterior angle of a triangle is equal to the sum of the measures of the two remote interior angles.
# 4. The opposite sides of a prallelgoram are congruent. 
#     ````{tip}
#     Use triangle congruence.
#     ````
# 5. If a transversal intersects three parallel lines in such a way as to make congruent segments between the paralllels, then every transversal interesecting these parallel lines will do likewise.
#     ````{tip}
#     Construct additional well-placed transversals, and use similar triangles.
#     ````
# 6. If a transversal intersects $n$ parallel lines ($n>2$) in such a way as to make congruent segments between the paralllels, then every transversal interesecting these parallel lines will do likewise. 
#     ````{tip}
#     Use induction.
#     ````
# 7. **Median Concurrence Theorem**. The three medians of a triangle are concurent at a point called the centroid. 
#     ````{tip} 
#     Consider $\triangle DFG$ with median $\overline{DM}$. Note $M$ is the midpoint of $\overline{FG}$. Call the centroid point $C$. Then the measure of $\overline{DC}$ is exactly twice the measure of $\overline{CM}$. This is true - but must be proven. Theorems 5 and 6 along with this fact provide an outline for the proof.
#     ````
# 8. Medians of a triangle intersect at a point that is two-thirds the distance from any vertex to the midpoint of the opposite side.
# 
#     ````{note} 
#     The following theorems are direct consequences of the Euclidean parallel postulate and establish many common notions in Euclidean geometry.
#     ````
# 9. Two lines parallel to another line are parallel to each other.
# 10. If a line intersects one of two parallel llines, then it interesects the other.
# 11. Each diagonal of a parallelogram partitions the parallelogram into a pair of congruent triangles.
# 12. The diagonals of a parallelogram bisect each other.
# 13. If the diagonals of a quadrilateral bisect each other, the quadrilateral is a parallelogram.
# 14. If a line segment has as its endpoints the midpoints of two sides of a triangle, then the segment is parallel to and one-half the length of the third side of the triangle. 
# 15. The diagonals of a rhombus are perpendicular.
# 16. If the diagonals of a quadrilateral bisect each other and are perpendicular, then the quadrilateral is a rhombus.
# 17. In a right triangle, the median from the right angle to the hypotenuse is one-half the length of the hypotenuse.
# 18. In a right triangle, one of the angles measures $30^\circ$ if and only if the side opposite this angle is one-half the length of the hypotenuse. 
#     ````{note} This result along with the Pythagorean Theorem gives us the $1-2-\sqrt3$ ratio of side lengths for $30-60-90$ right triangles. The Pythagorean Theorem will be proven later.
#     ````
# 19. The midpoints of the sides of a quadrilateral are the vertices of a convex parallelogram.
