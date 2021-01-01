#!/usr/bin/env python
# coding: utf-8

# # 3.1 Building Blocks

# Neutral geometry has parallel lines, in fact, too many. Infinitely many are possible. SMSG Axioms 1-15 force parallels to be possible, but the question of unique parallels vs. infintely many remains unanswered until we add SMSG Axiom 16 (Playfair's Postulate). By saying "at most one," we force unique parallels. The possibility of "no parallels at all" has already been eliminated. This restriction immediately allows for the proof of several important theorems. First, let's lay out the definitions we will need.

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
# 
#     ````{tip}
#     For a neutral geometry, the angle sum for triangle was at most $180^\circ$. What forces the equality in Euclidean space?
#     ````
# 
# 3.  **Euclidean Exterior Angle Theorem**. The measure of an exterior angle of a triangle is equal to the sum of the measures of the two remote interior angles.
# 
# 4. **Parallelogram Decomposition Theorem**. [^1]  In parallelogram $ABCD$, $\triangle{ABD} \cong \triangle{CDB}$ and $\triangle{ABC}\cong\triangle{CDA}$.
# 
#     ````{note}
#     Two important corrolaries provide facts about parallelograms that are quite useful in our proofs.
#     ````
#     + Opposite *sides* of a parallelogram are *congruent*.
#     + Opposite *angles* of a parallelogram are *congruent*.
# 
# 
#     ````{note}
#     The next few important theorems identify key relationship about the diagonals of quadrilaterals.
#     ````
# 
# 5. The diagonals of a quadrilateral bisect each other if and only the quadrilateral is a parallelogram.
# 
#     We have enough theorems to formally prove several important theorems that will help prove our compass and straitedge constructions have the required properties. The behavior of the diagonals of kites are the lever we use to create perpendicular lines and find midpoints of segments. The proof for all three relies upon a result of the Isosceles Triangle theorem.
# 
# 6. Corrollary to the Isosceles Triangle Theorem. A point is on the perpendicular bisector of a line segment if and only if it is equidistant from the endpoints of the line segment.
# 
# 7. One diagonal of a quadrilateral is the *perpendicular bisector* of the other if and only if the quadrilateral is a kite.
# 
# 8. The diagonals of a quadrilateral are *perpendicular bisectors* of one another if and only if the quadrilateral is a rhombus.
# 
# 9. The diagonals of a quadrilateral are \emph{congruent perpendicular bisectors} of one another if and only if the quadrilateral is a square.
# 
# **CCT1** Consider two circles $p$ and $q$ with centers $P$ and $Q$ respectively. If $p$ and $q$ intersect in exactly two points, say, $R$ and $S$, then quadrilateral $PRQS$ is a kite. If $p\cong q$, $PQRS$ is a rhombus. If $p\in Q$ and $q\in P$, $\triangle{PRQ}$ is equilateral, as is $\triangle{PSQ}$.
