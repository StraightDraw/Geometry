#!/usr/bin/env python
# coding: utf-8

# # 3.4 Triangle Centers and Euler Line

# Recall that Theorem 7, the Median Concurrence Theorem, established the centroid of the triangle. The centroid is the "center of mass" of a triangle. If the triangle and its interior were made of metal with perfectly constant mass, thickness and density, the centroid would be the balance point for that object. We have several triangle concurrence theorems and several notions of the center of a circle:
# 
# Concurrence Point Idea
# Median Centroid Center of Mass
# Perpendicular Bisector Circumcenter Center of circumscribing circle
# Altitude Orthocenter
# Angle Bisector Incenter Center of incscribed circle
#     
# Circumscribe
# : A circle which contains all vertices of a polygon is said to *circumscribe* it.
# 
# Incircle.
# : A circle which can be inscribed in that triangle (e.g. tangent to all three sides of the triangle and otherwise interior to the triangle).
# 
# Altitude
# : The perpendicular line sement from the vertex of an angle to the side opposite.
# 
# ## Theorems
# 1. **Perpendicular Bisector Concurrence**. The three perpendicular bisectors of the sides a triangle are concurrent. The concurrent point is called the \textbf{circumcenter} of the triangle. The center of the unique circle that circumscribes a triangle is the circumcenter (see Theorem 48).
# 
#     ````{hint}
#     We often instruct students to think intuitively about the distance from a point to a line as the "minimum distance" from $P$ to $l$. This idea is equivalent to the defition because any other line segment drawn from $P$ to $l$ would be the hypotenuse of a right triangle. The Pythagorean Theorem then implies the new segment has a length greater than the distance from $P$ to $l$.
#     ````
# 
# 2. A point is on the bisector of angle if and only if it is equidistant from both rays of the angle.
# 3. **Angle Bisector Concurrence**. The bisectors of the interior angles of a triangle are concurrent at a point called the *incenter*.
# 4. **Altitude Concurrence**. The three altitudes of a triangle are concurrent at a point called the *orthocenter*.
# 5. An angle bisector of an interior angle of a triangle is concurrent with the angle bisectors of the exterior angles of the two remaining angles of the triangles at a point called the *excenter*. This construction will lead to three distinct excenters.
# 6. Each excenter of a triangle is the center of a circle which is externally tangent to one side of the triangle and tangent to the extensions of the other two sides.
# 7. In an equilateral triangle, the incenter, circumcenter, centroid and orthocenter are all concurrent.
# 8. **Euler Line**. The orthocenter, centroid and circucenter of a triangle are collinear. The line that contains these three points is called the *Euler Line*.
