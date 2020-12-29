#!/usr/bin/env python
# coding: utf-8

# # 2.1 Congruence, Lines and Angles
# 
# **Definitions**
# 
# * Segment and Angle Congruence. Two segments (or angles) are congruent if and only if their measures are equal.
# * Polygon Congruence. Two polygons are congruent if and only if there exists a one-to-one correspondence between their vertices such that all their corresponding sides (line sgements) and all their corresponding angles are congruent.
# 
# Congruence relations are *equivalance relations* (see Theorem 1). Specifically, congruence relations are symmetric, reflexive and transitive.
# 
# * Collinear. Two points are *collinear* if they lie on the same line.
# * Intersecting Lines. Two lines *intersect* if there exists a point that is on both lines.
# * Parallel Lines. *Parallel* lines are two lines in the same plan which do not intersect.
# * Concurrent Lines. *Concurrent* lines are three or more coplanar lines that have a point in common.
# * Segment. A *segment* $\overline{AB}$ is the set of points $A$, $B$ and all points $P$ such that $P\in\overleftrightarrow{AB}$ and $AP+PB=AB$.
# 
#     In the above definition, we would like to say "...all points $P$ **between** $A$ and $B$," but as you'll see
#     below, we need the concept of *segment* to define the idea of *between*, so we rely upon the SMSG
#     Ruler Postulate (Axiom 3) and Distance Postulate (Axiom 2) to define a segment.
# 
# * Between. A point $B$ is *between* $A$ and $C$ if $B\in \overline{AC}$ but $B\neq A,C$.
# * Ray. A ray $\overrightarrow{AB}$ (also called a half-line) is a subset of the line $\overleftrightarrow{AB}$ that contains a given point $A$ and all the points $C\in\overleftrightarrow{AB}$ such that $A$ is \textbf{not} between $C$ and $B$. The point $A$ is called the \textbf{endpoint} of the ray.
# * Angle. An angle is the union of two rays which have the same endpoint.
# * Angle Interior. A point $P$ is in the interior of $\angle{ABC}$ provided:
#  + $m\angle{ABC}<180^\circ$
#  + there exist points $X,Y$ such that
#    + $X\in\overrightarrow{BA}$,
#    + $Y\in\overrightarrow{BC}$, and
#    + $P$ is between $X$ and $Y$
# 
# 
# * Convex. A set (or polygon) $P$ is convex if $A,B\in P\implies \overline{AB}\in P$.
# * Midpoint. The midpoint C of $\overline{AB}$ lies on $\overline{AB}$ such that $AC = CB$.
# * Angle Bisector. The ray $\overrightarrow{BD}$ is the angle bisector of $\angle{ABC}$ if $m\angle ABD = m\angle DBC$.
# * Right Angle. An angle with angle measure $90^\circ$ (see SMSG Axiom 11).
# * Acute Angle. An angle with angle measure less than $90^\circ$.
# * Perpendicular Bisector. A line which passes through the midpoint of a line segment and which forms a right angle with that segment at the point of intersection.
# * Obtuse Angle. An angle with angle measure greater than $90^\circ$.[^1]
# * Straight Angle. An angle whose rays are distinct but collinear.
# * Vertical Angles.} The angles opposite each other when two lines cross.
# * Supplementary Angles Postulate. (From SMSG Axiom list.) If two angles form a linear pair, they are supplentary.
# * Complementary Angle. If two angles form a right angle, they are complementary.
# 
# [^1]: Note that according to SMSG Axiom 11, angles *must* have measure $\leq 180^\circ$, so we don't yet have the idea (or a way to define) "reflex angles," nor do we have angles with negative measure.

# #### Theorems
# 1. Congruence relations are equivalence relations.
# 2. Every line segment has exactly one midpoint. 
# 3. Every angle has exactly one bisector.
# 4. Supplements and complements of the same angles are congruent. 
# 5. The intersection of two convex polygons is convex.
# 6. Vertical angles are congruent.
# 7. **Pasch's Axiom**. Given a line that contains no vertex of a triangle, if that line intersects one side of the triangle, it must intersect another. 
# 8. **Crossbar Theorem**. If at least one point of $\overrightarrow{AC}$ is in the interior of $\angle{BAD}$ then $\overrightarrow{AC}$ intersects $\overline{BD}$.
