#!/usr/bin/env python
# coding: utf-8

# # A.4 SMSG Axioms

# The School Mathematics Study Group was formed during the 1950's space race to help provide rigor to the geometry instruction in US high schools. This set of axioms is *dependent* which means that some axioms could be stated as theorems and proven from the other axioms. However, adding extra axioms provides all the tools we need to begin geometry instruction at a reasonable level.  For instance, in Hilbert's or Birkhoff's axiomatic systems, we have to prove circles exist and then derive their properties. In the SMSG set, we are given the definitions and basic properties as axioms.
# 
# The undefined terms are *point*, *line* and *plane*. Each axiom has a name which makes life easier when quoting them in proofs.
# 
# 1. **Line Uniqueness**. Given any two different points, there is exactly one line which contains both of them.
# 2. **Distance Postulate**. To every pair of different points there corresponds a unique positive number.
# 3. **Ruler Postulate**. The points of a line can be placed in correspondence with the real numbers in such a way that:
#     + To every point of the line there corresponds exactly one real number,
#     + To every real number there corresponds exactly one point of the line, and
#     + The distance between two points is the absolute value of the difference of the corresponding coordinates.
# 
# 4. **Ruler Placement Postulate**. Given any two points $P$ and $Q$ on a line, the coordinate system can be chosen in such a way that the coordinate of $P$ is zero and the corrdinate of $Q$ is positive.
# 5. **Points Exist**. (a) Every plane contains at least three non-collinear points. (b) Space contains at least four non-coplanar points.
# 6. **Points**. If two points lie in a plane, then the whole of the line containing these points lies in the same plane.
# 7. **Plane Uniqueness**. There is at least one plane containing any three points, and exactly one plane containing any three non-collinear points.
# 8. **Plane Intersection**. If two different planes intersect, then their intersection is a line.
# 9. **Plane Separation Postulate**. Given a line and a plane containing it, the points of the plane that do not lie on the line form two sets such that 
#     + Each of the sets is convex, and
#     + If $P$ is in one set and $Q$ is in the other, then the segment $\overline{PQ}$ intersects the line.
# 
# 9. **Space Separation Postulate**. The points of space that do not lie in a given plane form two sets such that
#     + Each of the sets is convex, and
#     + If $P$ is in one set and $Q$ is in the other, then the segment $\overline{PQ}$ intersects the plane.
# 
# 10. **Angle Measurement Postulate**. To every angle there corresponds a real number between $0^{\circ}$ and $180^{\circ}$.
# 11. **Angle Construction Postulate**. Let $\overrightarrow{AB}$ be a ray on the edge of the half-plane $H$. For every $r$ between $0$ and $180$ there is exactly one ray $\overrightarrow{AP}$ with $P$ in $H$ such that $m\angle PAB = r$.
# 12. **Angle Addition Postulate**. If $D$ is a point in the interior of $m\angle BAC$, then $m\angle BAC = m\angle BAD + m\angle DAC$.
# 13. **Supplementary Postulate**. If two angles form a linear pair, then they are supplementary.
# 14. **Side Angle Side Postulate**. Given a one-to-one correspondence between two triangles (or between a triangle and itself), if two sides and the included angle of the first triangle are congruent to the corresponding parts of the second triangle, the correspondence is a congruence.
# 15. **Parallel Postulate**. Through a given external point there is at most one line parallel to a given line.
# 16. **Area Postulate**. To every polygonal region there corresponds a unique positive real number called its area.
# 17. **Equal Areas**. If two triangles are congruent, then the triangular regions have the same area.
# 18. **Polygon Congruence**. Suppose that the region $R$ is the union of two regions $R_1$ and $R_2$. If $R_1$ and $R_2$ intersect in at most a finite number of segments and points, then the area of $R$ is the sum of the areas of $R_1$ and $R_2$.
# 19. **Area of Rectangles**. The area of a rectangle is the product of the length of its base and the length of its altitude.
# 20. **Volume Postulate**. The volume of a rectangular parallelepiped is equal to the product of the length of its altitude and the area of the base.
# 21. **Cavalieri's Principle**. Given two solids and a plane, if for every plane that intersects the solids and is parallel to the given plane the two intersections determine regions that have the same area, then the two solids have the same volume.
