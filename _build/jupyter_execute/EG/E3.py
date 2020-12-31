#!/usr/bin/env python
# coding: utf-8

# # 3.3 Circles

# Circle
# : A set of points all of which are equidistant from a given point called the *center*. 
# 
# Radius
# : The common distance between points on the circle and center point.
# 
# Chord
# : A *chord* of a circle is a line segment joining two of the points on the circle. A *secant* is a line which contains a chord.
# 
# Tangent
# : A line which contains exactly one point of a circle. 
# 
# Diameter
# : The length of a chord that contains the center of the circle.
# 
# ````{warning}
# The radius and diameter are defined to be *distances*. Yet, we often refer to relevant line segments as radii or diameters.
# ````
# 
# Central Angle
# : Any angle whose vertex is the center of a circle is a \textbf{central angle}. 
# 
# Arc
# : The set of points on a circle that lie between two points on the circle, including the points themselves. 
# 
# Arc Measure
# : The degree measure of an arc is the measure of the central angle corresponding to the arc. Two distinct points on a circle create two arcs, a *minor arc* and a *major arc*, with the degree measure of the major arc greater than (or equal to) that of the minor arc.
# 
# Inscribed Angle
# : The angle formed when two secant lines intersect at a point on the circle.
# 
# Intercepted Arc
# : The part of the circle that lies between two lines that intersect it.

# ## Theorems 
# 1. In the Euclidean plane, three distinct points uniquely determine a circle.
#     ````{warning}
#     Requires both an existance proof and a uniqueness proof.
#     ````
# 2. If $\overline{AB}$ is a diameter and $\overline{CD}$ is any other chord of the same circle (which is not a diameter), then $AB>CD$.
# 3. If a diameter of a circle is perpendicular to a chord of the circle, then the diameter bisects the chord.
# 4. The perpendicular bisector of a chord of a circle contains a diameter of the circle.
# 5. If a line is tangent to a circle, it is perpendicular to the line joining the point of tangency to the center of the circle.
# 6. **Arc Addition**. If arc $ABC$ and arc $CDE$ are arcs sharing only the same endpoint $C$, then the measure of arc $ABC$ plus the measure of arc $CDE$ equals the measure of arc $ACE}$.
# 
# 7. **Inscribed Angle Theorem**. The measure of an angle inscribed in an arc is one-half the measure of its intercepted arc. 
#     ````{note}
#     Recall the measure of an arc is equal to the measure of the central angle corresponding to the arc.
#     ````
# 8. **Two-Chord Angle Theorem**. If two chords interesect in the interior of a circle to determine an angle, the measure of that angle is the average of the measures of the arcs intercepted by the angle and its vertical angles.
# 9. **Two-Secant Angle Theorem**. If two secants interesect in the exterior of a circle to determine an angle, the measure of the angle at the point of intersection is one-half the positive difference of the two intercepted arcs.
# 
# 10. **Tangent-Chord Angle Theorem**. If $\overleftrightarrow{AB}$ is tangent to a circle at $A$, and if $\overline{AC}$ is a chord of the circle with measure arc $APC=x^{\circ}$, then $m\angle BAC=\frac{x^{\circ}}{2}$.
# 11. **Tangent-Secant Angle Theorem**. If $\overleftrightarrow{AB}$ is tangent to a circle at $A$, and if $\overleftrightarrow{BD}$ is a secant of the circle, then $m\angle ABD$ is half the positive difference of the two intercepted arcs.
# 12. **Two-Tangent Angle Theorem**. The measure of an angle formed by two tangents drawn to a circle is one-half the positive difference of the measures of the intercepted arcs.
# 13. **Corollary**. Tangent segments drawn to a circle from the same (exterior) point are congruent.
# 14. **Chord Segment Product Theorem**. If two chords of a circle intersect, the products of the lengths of the segments of one chord is equal to the product of the lengths of the segments of the other.
# 15. **Secant Segment Product Theorem**. If two secant lines are drawn to a circle from the same exterior point, then the product of the length of the secant segment and the lenth of its exterior portion is the same for both secants.
