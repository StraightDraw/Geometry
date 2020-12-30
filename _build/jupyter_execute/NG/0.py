#!/usr/bin/env python
# coding: utf-8

# # Neutral Geometry

# ## Geometry without a Parallel Property

# We will explore *neutral geometry* where no parallel postulate exists. Most triangle theorems go through just fine, but the big bump in the road is quadrilaterals, a bump that confused mathematicians for more than two thousand years. The animation below shows triangles and quadrilaterals in a hyperbolic geometry. The angles are Euclidean, but the distances are not. Curiously, this type of geometry is allowed if we do not include a parallel axiom.
# 
# ![Poincare Disk Model of Hyperbolic Geometry](https://mathworld.wolfram.com/images/gifs/poincare.gif)
# 
# Spherical geometry is a special case of elliptical geometry where the lines of the geometry are great circles of the sphere. In spherical geometry, triangles have angle sums greater than $180^{\circ}$. Elliptical and spherical geometry develops along a separate path from Euclidean and hyperbolic geometries, and the axioms and theorems of neutral geometry do not typically apply.
# 
# ![Visual Comparison of Euclidean, Hyperbolic and Elliptical Geometries](https://www.mu6.com/rieman/Euclide_non-Euclidi_geometry.jpg)
# 
# ````{warning}
# Geometric notation has conventions we need to follow. The notation $\overline{AB}$ describes a **line segment** but $AB$ indicates **length** or the distance between $A$ and $B$. We refer to the angle as $\angle BAC$ (with vertex $A$), but $m\angle BAC$ indicates its measure.
# ````

# ## Axiomatics of Neutral Geometry
# 
# When undergraduate math majors encounter proofs for the first time, they often wonder why in the world anyone would need to prove that the number $\sqrt 2$ exists. Mathematicians prove every single result starting from the axioms and defined terms. Undergraduate math majors often roll their eyes. What's the point of proving that the point where two lines intersect is actually on both lines? For many students, these exercises are tedious at best, confusing at worst.
# 
# ```{dropdown} Problem of Completeness
# The biggest problem for geometers is that geometric lines are not necessarily *complete*. We can have sequences of points on a line where the distances between successive terms get smaller and smaller, yet the limiting point is nowhere to be found. The completeness property means that any two lines that "cross" each other actually intersect.
# ```
# <iframe width="560" height="315" src="https://www.youtube.com/embed/n-tWaJcUeR4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# 
# The SMSG Axioms form a bridge to the most interesting and accessible results of Euclidean geometry. The tedium of proving the continuity and completeness of all lines is avoided, and "real" geometry takes place almost immediately. For neutral geometry, we will assume only the first 15 of the SMSG axioms are true. Axiom 16 is the parallel postulate. 
# 
# ````{note}
# Neutral geometry assumes only the first 15 axioms of the SMSG set.
# ````
# 
# The undefined terms for the SMSG axioms are often said to be *points*, *lines* and *plane*. The hidden gold of the SMSG axioms is that they provide tools from three categories of mathematics.
# 
# * Sets
# * Logic
# * Algebraic properties of real numbers
# 
# <iframe width="560" height="315" src="https://www.youtube.com/embed/caZqcrkW3IY?start=583" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# 
# The three sets of tools provide immense and immediate aid. When the notions of *sets* like containment and equality all make sense, we can immediately use and understand statements like "$\triangle ABC$ contains the point D" or "point $Z$ lies on line $\overleftrightarrow{AB}$." We also assume that basic set operations like intersections, unions and set subtraction work properly. The SMSG axioms use the defined term  *space* which is the *universal set*: the set of all points, lines and planes in the geometry. 
# 
# We may use the formal laws of *logic*. For example, to prove a statement false, we need only one counterexample. Proving the contrapositive is equivalent to proving the original statement. Just because a statement is true does not imply its converse is true. We do not prove these logical constructs work, we simply use them.
# 
# The *algebraic properties of real numbers* provide a huge ski jump that sends us flying past many tedious and technical proofs.
# 
# ````{note}
# Geometric distances and angle measures are **real numbers**, so we can solve equations, distribute, cancel and take square roots. Additive and multiplicative identies exist and work properly. When we multiply through an inequality by a negative real number, the inequality "flips." All the normal machinery works.
# ````
# 
# In the Ruler Postulate below, every line in our geometry inherits all the properties of the real number line. *Cotinuity* and *completeness* come along, too. Any real number we can imagine exists and can be placed precisely in relation to any other quantity. SMSG axioms like the Distance Postulate and Angle Measurement Postulate leverage the properties of real numbers so that we can construct things like midpoints of segments and bisectors of angles. Defined terms like *angle measure*, *area* and *volume* make sense only because they correspond to real number quanities.
# 
# #### SMSG Axioms 1 to 15
# 
# 1. **Line Uniqueness**. Given any two different points, there is exactly one line which contains both of them.
# 2. **Distance Postulate**. To every pair of different points there corresponds a unique positive number.
# 3. **Ruler Postulate**. The points of a line can be placed in correspondence with the real numbers in such a way that:
#     1. To every point of the line there corresponds exactly one real number,
#     2. To every real number there corresponds exactly one point of the line, and
#     3. The distance between two points is the absolute value of the difference of the corresponding real numbers.
# 
# 
# 4. **Ruler Placement Postulate**. Given any two points $P$ and $Q$ on a line, the coordinate system can be chosen in such a way that the coordinate of $P$ is zero and the corrdinate of $Q$ is positive.
# 5. **Points Exist**. 
#     1. Every plane contains at least three non-collinear points. 
#     2. Space contains at least four non-coplanar points.
# 
# 
# 6. **Points**. If two points lie in a plane, then the whole of the line containing these points lies in the same plane.
# 7. **Plane Uniqueness**. There is at least one plane containing any three points, and exactly one plane containing any three non-collinear points.
# 8. **Plane Intersection**. If two different planes intersect, then their intersection is a line.
# 9. **Plane Separation Postulate**. [^1] Given a line and a plane containing it, the points of the plane that do not lie on the line form two sets such that
#     1. each of the sets is convex, and
#     2. if $P$ is in one set and $Q$ is in the other, then the segment $\overline{PQ}$ intersects the line.
# 
# 
# 10. **Space Separation Postulate**. The points of space that do not lie in a given plane form two sets such that
#     1. each of the sets is convex, and
#     2. if $P$ is in one set and $Q$ is in the other, then the segment $\overline{PQ}$ intersects the plane.
# 
# 
# 11. **Angle Measurement Postulate**. To every angle there corresponds a real number between $0^{\circ}$ and $180^{\circ}$.
# 12. **Angle Construction Postulate**. Let $\overrightarrow{AB}$ be a ray on the edge of the half-plane $H$. For every $r$ between $0$ and $180$ there is exactly one ray $\overrightarrow{AP}$ with $P$ in $H$ such that $m\angle PAB = r$.
# 13. **Angle Addition Postulate**. If $D$ is a point in the interior of $m\angle BAC$, then $m\angle BAC = m\angle BAD + m\angle DAC$.
# 14. **Supplementary Postulate**. If two angles form a linear pair, then they are supplementary.
# 15. **Side Angle Side Postulate**. Given a one-to-one correspondence between two triangles (or between a triangle and itself), if two sides and the included angle of the first triangle are congruent to the corresponding parts of the second triangle, the correspondence is a congruence.

# [^1]: A version of Pasch's Axiom.

# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# 1
# 2
# ```
# 
