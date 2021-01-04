#!/usr/bin/env python
# coding: utf-8

# ## 1.1 Finite Geometries

# Finite geometries are the most primitive axiomatic systems with a finite set of points and lines. The geometric ideas we meet studying finite geometry are robust and apply to more sophisticated geometries. The Incidence Axioms (see below) govern the relationship between points and lines and provide the building blocks necessary for ideas like *intersect* and *parallel*. 
# 
# ````{admonition} Important
# :class: warning
# All finite geometries in this course will have the same three and the same defined terms *intersect*, *parallel* and *concurrent*.
# ````
# 
# We can define several basic geometry terms.
# 
# Intersect
# : Two lines on the same point are said to *intersect* at that point and are called *intersecting lines*.
# 
# Parallel
# : Two lines that do not intersect are called *parallel* lines.
# 
# Concurrent
# : Three or more lines that intersect at the same point are called *concurrent*.
# 
# 
# ````{tip}
# We used the exact same definitions above that will be used throughout this book.
# ````
# 

# ## Four Point Geometry
# 
# ````{margin}
# ```{figure} Fig1_4PG.png
# ---
# width: 90%
# name: 4PG
# ---
# Model for the Four Point Geometry
# ```
# ````

# The axioms below together with the standard undefined terms for finite geometry describe the Four Point Geometry (4PG).
# 
# ````{admonition} Axioms for the 4PG
# :class: note
# 1. There exist exactly four points.
# 2. Any two distinct points have exactly one line on both of them.
# 3. Each line is on exactly two points.
# ````
# We would normally say two lines intersect if they contain the same point. However, we have not defined what *contain* means. We use the undefined term "on" to refer both to a line being on some points and to points being on a line.

# ## 4PG Theorems
# 
# 1. In the Four Point Geometry, if two lines intersect, they have exactly one point in common.
# 2. The Four Point Geometry has exactly six lines.
# 3. In the Four Point Geometry, each point has exactly three lines on it.
# 4. In the Four Point Geometry, each line has at least one line that is parallel to it.
# 5. Prove that there exists a set of two lines in the Four Point Geometry that contain all of the points in the geometry.
# 
# The Four Point Geometry can be extended to five, six or more points by simply changing the first axiom. We will explore the Five Point Geometry in the next section, but some of the properties will be different.
# 
