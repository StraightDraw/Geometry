#!/usr/bin/env python
# coding: utf-8

# # 3.2 Area and Congruence

# We have discussed several issues with Euclid. We have arrived at another: How do we define area? If rectangular area is defined, then we can calculate the area of triangles. Using triangles and rectangles, we can calcuate polygon areas. Since rectangles don't exist in neutral geometry, our standard notion of area only exists in Euclidean geometry. In any other geometry, calculating an area will prove troublesome. However, we're developing Euclidean geometry in this section. Please note that SMSG Axiom 20 states that "the area of a rectangle is the product of the length of its base and the length of its altitude."
# 
# Similar Polygons
# : Two polygons are *similar* provided that 
#   + corresponding sides of each are in the same proportion, and 
#   + corresponding interior angles are congruent.
#     ````{note}
#     Note the first requirement implies a constant ratio of proportionality for any two pairs of side lengths.
#     ````
# 
# ## Theorems
# 1. The area of a parallelogram is the product of the lengths of its base and height.
# 2. The area of a triangle is one-half the product of the any base and the corresponding height.
# 
#     ````{warning}
#     Two different definitions of a trapezoid are both in use: possessing *exactly* one pair of parallel sides vs. possessing *at least* one pair of parallel sides. The first means no parallelograms are trapezoids while the second means all parallelograms are trapezoids. More common is the one defined above where parallelograms are *not* trapezoids. High school teachers should note carefully which definition is used in their curriculum materials especially when using classrooms resources and activities from the interwebs.
#     ````
# 
# 3. The area of a trapezoid is the product of its height and the arithmetic mean of its bases.
# 4. **Basic Proportionality Theorem**. A line parallel to one side of a triangle intersects the other two sides in two different points if and only if it divides these sides into segments that are proportional.
#     ````{tip}
#     The "two different points" simply requires the point of intersection to not be the vertex.
#     ````
# 5. **AAA Triangle Similarity**. If the interior angles of one triangle are congruent to corresponding angles of a second triangle, then the triangles are similar.
# 6. **SAS Triangle Similarity**. If an angle of one triangle is congruent to the corresponding angle of a second triangle, and the corresponding sides adjacent to these angles are in proportion, then the triangles are similar.
# 7. **SAS Triangle Similarity**. If the lengths of the sides of one triangle are proportional to the corresponding side lengths of a second triangle, then the triangles are similar.
# 8. **Pythagorean Theorem**. If $a$ and $b$ are the lengths of the legs of a right triangle the hypotenuse of which has length $c$, then $a^2+b^2=c^2$.
#     
