#!/usr/bin/env python
# coding: utf-8

# # 2.2 Triangles

# Triangles exist in a neutral geometry and have many familiar Euclidean properties from Euclidean geometry.
# 
# ````{warning}
# In neutral geometry, not all triangles have angle sums that are $180^\circ$. Crazy, right? We can only prove the **Saccheri-Legendre Theorem** which states that triangles must have angle sums that are *less than or equal* to $180^\circ$. 
# ````
# 
# Since most triangle theorems can be proven without any parallel axiom at all, we can see why the ancients misunderstood and questioned Euclid's Fifth postulate.

# Triangle
# : A triangle is the union of three line segments determined by three non-collinear points.
# 
# Right Triangle
# : A triangle with a right angle.
# 
# Isosceles Triangle
# : A triangle with a pair of congruent sides.
# 
# Equilateral Triangle
# : A triangle with all three sides congruent.
# 
# Scalene Triangle
# : The sides of a scalene triangle all have different lengths.
# 
# Angle Sum of a Triangle
# : The sum of the measures of all three angles in a triangle.

# ## Theorems
# 1. **Isosceles Triangle Theorem**. Two sides of a triangle are congruent if and only if the angles opposite these sides are congruent ($\impliedby$ only).
# 
#     ````{warning}
#     Proving that an isosceles triangle has congruent angles is easy ($\impliedby$). Proving the converse, that a triangle with two congruent angles is isosceles ($\implies$) is much easier after we have a congruence theorem.
#     ````
# 
# 2. A point is on the perpendicular bisector of a line segment if and only if it is equidistant from the endpoints of the line segment.
# 
#     ````{margin}
#     Animation demonstrating that points $P$ on the perpendicular bisector of a segment are equidistant from the endpoints.
#     ````
# 
#    <iframe scrolling="no" title="Pasch's Axiom" src="https://www.geogebra.org/material/iframe/id/psw3qjcq/width/1180/height/360/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/true/ctl/false" width="100%" height="100%" style="border:1px;" allowfullscreen; style="display:block" > </iframe> 
# 
# 3. **Exterior Angle Theorem**. Each exterior angle of a triangle is greater in measure than either of the nonadjacent interior angles of the triangle.
# 4. **ASA Triangle Congruence**. If two angles and the included side of one triangle are congruent, repsectively, to two angles and the included side of a second triangle, then the triangles are congruent.
# 5. **AAS Triangle Congruence**. If the vertices of two triangles are in one-to-one correspondence such that two angles and a non-included side in one triangle are congruent to their corresponding parts of a second triangle, then the triangles are congruent.
# 6. **Isosceles Triangle Theorem**. If two angles of a triangle are congruent, then the sides opposite these angles are congruent ($\implies$).
#    
# 7. **Triangle Inequality**. The sum of the measures of two sides of a triangle is greater than the measure of the third side.
# 8. **Hinge Theorem**. If two sides of one triangle are congruent to two sides of another triangle, and the included angle of the first is larger than the included angle of the second, then the third side of the first triangle is longer than the third side of the second triangle. 
#     
#     ````{note}
#     The Hinge Theorem is Euclid's Proposition 24 and is sometimes called the ``Open Mouth Theorem."
#     ````
# 9. **SSS Triangle Congruence**. If the sides of one triangle are congruent to corresponding sides of another triangle, the triangles are congruent.
# 
#     ````{hint}
#     Use the Hinge Theorem to help prove SSS Triangle Congruence.
#     ````
#     
# 10. In a scalene triangle, the angle with the largest measure is opposite the side with the largest length, and the angle with the smallest measure is opposite the side with the smallest length.
# 11. Equilateral trianges are equiangular.
# 
#     ```{note}
#     We have yet to prove that any parallel lines exist. The next theorem demonstrates that parallel lines do exist in neutral geometry and shows how to locate them.
#     ````
# 
# 12. **Alternate Interior Angle Theorem**. If two lines are intersected by a transversal such that a pair of alternate interior angles is congruent, then the lines are parallel.
# 
#     ````{tip}
#     The Alternate Interior Angle Theorem is so important, it gets an acronym: the **AIA** theorem. Its converse is equivalent to the Euclidean parallel condition and is also acronym worthy: **CAIA**.
#     ````
#     
# 13. *Corollary to AIA*. Two lines perpendicular to the same line are parallel.
# 
#     ````{warning}
#     Parall lines are a hot mess in neutral geometry, but perpendicularity and right angles work well. 
#     ````
# 
# 14. The sum of the measures of any two angles of a triangle is less than $180^\circ$.
# 15. For any $\triangle ABC$ there exists $\triangle A'B'C'$ having the same angle sum as $\triangle ABC$ but where $\measuredangle A'\leq\frac{1}{2}\measuredangle A$.
# 
#     ````{hint}
#     Use both of the previous two theorems to help you prove the Saccheri-Legendre Theorem.
#     ````
# 
# 15. **Saccheri-Legendre Theorem**. The angle sum of any triangle is less than or equal to $180^\circ$. 
# 
# 
# 16. The angle sum of any convex quadrilateral is less than or equal to $360^\circ$.
# 
# 17. **Unique Perpendicular**. Given a line $l$ and any point $P$ not on $l$, there exists a unique line $m$ such that $P\in m$ and $m\perp l$.

# If we switched the word "perpendicular" to "parallel" in the theorem above, we would have Playfair's Postulate which is the Euclidean parallel condition. Perhaps we can emphathize with the ancient geometers who were confused. Tons of Eudlidean geometry goes through just fine without any parallel axiom at all. Perpendicular lines behave nicely, and triangles work really well with the exception of their angle-sums. We even get half of the AIA theorem: congrunet alternate interior angles implies two lines are parallel.
# 
# We have reached the breaking point, however. Rectangles do not even exist in neutral geometry. Parallelograms exist, yet, weirdly, opposite side of parallelograms need not be congruent. The next section explores the weirdness of quadrilaterals that live in a geometry with no parallel axiom.
