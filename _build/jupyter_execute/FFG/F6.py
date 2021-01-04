#!/usr/bin/env python
# coding: utf-8

# # 1.6  Searching for a Parallel Posutlate

# Euclid's *Elements* introduced both axiomatics and formal geometry to the world. Though many of the results were probably known before Euclid, his book survived from antiquity and for more than two thousand years served as the main textbook for students of geometry. 
# 
# ````{margin}
# ![Euclid](https://cdn.britannica.com/s:250x250,c:crop/46/8446-050-BC92B998/Euclid-woodcut-1584.jpg)
# Euclid
# ````

# The 19th century produced a revolution in formal logic and the study of axiomatics. One result was that it became clear that Euclid's system was both incomplete and, insofar as it went, failed to meet the modern standards of rigor. German mathematician [David Hilbert](https://en.wikipedia.org/wiki/David_Hilbert) attempted to rectify these issues and published a new system of axioms in his book *Grundlagen der Geometrie* in 1898.
# 
# Hilbert's set of axioms was independent and complete. His formulation also split the axioms into differents sets: *incidence* axioms, *betweeness* axioms and *congruence* axioms. His idea is obvious: he knew the properties and theorems needed to make Euclidean Geometry work "correctly," and he developed structures within each set of axioms to force those properties into the system. 
# 
# Another important set of independent and complete Euclidean axioms was provided by Birkhoff. Where Hilbert had more than a dozen axioms, Birkhoff's elegant approach had only four axioms. The final important set of Eculidean axioms we will work with is a dependent system but was designed for use in secondary mathematics textbooks (SMSG). More axioms are given than are needed, but students aren't stuck proving theorems like "two lines on the same two points are the same line." The additional axioms move the starting point into interesting and important ideas for school mathematics.
# 
# The study of Euclidean Geometry has to focus on the Fifth Postulate, Euclid's Parallel Postulate, which has been controversial since antiquity. Euclid himself appears to have worried about it. Greek geometers argued it wasn't an axiom, it was a theorem. The idea is simple: *If two lines are parallel, they never meet*.

# ````{epigraph}
# If a straight line crossing two straight lines makes the interior angles on the same side less than two right angles, the two straight lines, if extended indefinitely, meet on that side on which are the angles less than the two right angles.
# 
# --Euclid's Fifth Postulate
# `````
# 
# <iframe scrolling="no" title="Handshakes8" src="https://www.geogebra.org/material/iframe/id/jns8hmzd/
# width/1480/
# height/540/
# border/888888/
# sfsb/true/
# smb/false/
# stb/false/
# stbh/false/
# ai/false/
# asb/false/
# sri/false/
# rc/false/
# ld/false/
# sdz/true/
# ctl/false"  width="100%" height="100%" style="border:1px;" allowfullscreen; style="display:block" > > </iframe>
# 
# Attempts to prove it from the other axioms failed. Attempts to explain why included the idea that Euclid hadn't stated his postulate properly. The various restatements and proof attempts actually led to many important discoveries and, eventually, to non-Euclidean geometry.
# 
# The most famous restatment is the **Playfair Postulate**. 
# 
# ````{epigraph}
# In a plane, given a line and a point not on it, at most one line parallel to the given line can be drawn through the point.
# 
# -- [John Playfair](https://www.maa.org/press/periodicals/convergence/teaching-mathematics-with-ephemera-who-was-john-playfair)
# ````
# 
# This is the modern idea of parallel. The *at most* turns out to be equivalent to *exactly one* because, using the other Euclidean axioms, we can prove that there is *at least* one.
# 
# Two possible ways exist to change the parallel condition, and both lead to non-Euclidean geometries.
# 
# * In a plane, given a line and a point not on it, ***more than one line*** parallel to the given line can be drawn through the point.
# * In a plane, given a line and a point not on it, ***no line*** parallel to the given line can be drawn through the point.

# On our way to Euclidean Geometry, we can ask the following question: "What theorems can be proven without using any parallel axiom at all?" A set of Eudlidean axioms without a parallel axiom is called  **neutral geometry** or ([absolute geometry](https://en.wikipedia.org/wiki/Absolute_geometry)).
# 
# The way forward is clear: we will start with Hilbert's version of Euclidean Geometry, thinking about each group of axioms. We will postpone any parallel postulate as long as possible and establish key results in *neutral geometry*. These results will be true regardless of the choice of parallel postulate we use. We will then use Playfair's Postulate (or a reasonable atlernative) to investigate those results which are only true in Euclidean Geometry before moving on to study non-Euclidean Geometry. 
# 
# The {doc}`Axioms</AX/A0>` chapter  gives four different formulations of Euclidean geometry, starting with Euclid's set of postulates. The axiomatic systems of Hilbert and Birkhoff follow. Both are rigorous in the modern sense and, as such, are complete, independent and have as a model the Euclidean plane. Finally, we have the SMSG axiom set which is rigorous, suitable for high school students, but which happens to be dependent.
# 
# ## Incidence Geometries
# Hilbert's formulation of Euclid is especially helpful. While we will use the SMSG axiom set for neutral and Euclidean geometry, we'll consider some of Hilbert's axioms for the rest of this section. His first set of axioms describe *incidence* or connnection. We need to know when a line contains a point, or when two lines intersect at a given point. Incidence geometries can be either finite or infinite.
# 
# ````{admonition} Incidence Axioms
# :class: note
# 1. For every pair of distinct points $A$ and $B$ there is a unique line $l$ containing $A$ and $B$.
# 2. Every line contains at least two points.
# 3. There are at least three points that do not lie on the same line.
# ````
# 
# Note that all the finite geometries discussed in this chapter are all incidence geometries, and the definition of parallel and concurrent will be identical to what we used for our finite geometries. The parallel condition separates finites geometries into two classes.
# 
# Affine Geometry
# : An incidence geometry that exhibits the Euclidean parallel property.
# 
# Projective Geometry
# : An incidence geometry that has no parallel lines and in which each line has at least three points.
# 
# Projective geometries are exactly what they sound like: the projection of a geometry onto a plane or hyperplane. Think about a globe projected onto a map of the world where the geometry of a sphere is projected onto a plane [^1]. We will probably not encounter them much in this course. 
# 
# In any incidence geometry, finite or otherwise, the following three statements hold.

# ## Theorems for Incidence Geometry
# 1. If two distinct lines intersect, then the intersection is exactly one point.
# 2. For each point there exist at least two lines containing it. 
# 3. There exist three lines that do not share a common point.

# ### Possible Parallel Postulates
# 
# **Parallel Possibilities.** Given an arbitrary line $l$ and any point $P$ not on $l$, exactly three possibilities exist:

# ````{panels}
# **No Parallels**
# ^^^
# There exist *no lines* through $P$ parallel to $l$.
# ---
# 
# **Unique Parallel**
# ^^^
# There exists exactly *one line* through $P$ parallel to $l$.
# ---
# 
# **Multiple Parallels**
# ^^^
# There exist *many lines* through $P$ parallel to $l$.
# ````

# A unique parallel is the Euclidean or *affine* parallel condition, and any geometry whose axioms imply an equivalent statement is said to have the Euclidean parallel property. If we chose either of the other options, we will have a non-Euclidean geometry. Our various finite geometries provide excellent examples of incidence geometries which have various parallel conditions.
# 
# You should be able to prove the Four Point, Five Point, Fano's and Young's geometries are all incidence geometries, and be able to determine and prove what type of parallel properties each one has, either affine or projective.

# [^1]: The earth isn't spherical, but globes are. It's an approximation.
