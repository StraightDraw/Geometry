# A.1 Affine Coordinates.

Affine Geometry
: A geometry in which the Euclidean parallel postulate holds. 

Slope of line $l$:
: The unique $m\in\mathbb{R}$ such that, for any two points $N(x_1,y_1)$ and $M(x_2,y_2)$ on $l$, $$m=\frac{y_1-y_2}{x_1-x_2}$$

Affine coordinates can be created for any (non-finite) affine geometry, and they will have the properties we associate with Cartesian Coordinates. The SMSG Axioms provide everything needed to create the typical Cartesian Coordinate System which can, with a bit more work, include the $z$-axis as well.

## Distance in a Coordinate System $O_{xy}$

At the moment, distances have only been defined along the axes. Notice that the value of the coordinates of point $P(x,y)$ are determined by creating a rectangle and measuring distances on the $x$- and $y$-axis using the SMSG Ruler Axioms. The next two theorems will establish the validity of the Euclidean distance metric.

## Theorems

1. For two distinct points with the same $y$-coordinate, say, $P(x_1,y)$ and $Q(x_2,y)$, the distance between $P$ and $Q$ is $\text{Dist}(P,Q)=|x_1-x_2|$. For two distinct points with the same $x$-coordinate, say, $P(x,y_1)$ and $Q(x,y_2)$, the distance between $P$ and $Q$ is $\text{Dist}(P,Q)=|y_1-y_2|$.

    ````{note}
    From the algebraic properties of real numbers, we know that for any distinct $a,b\in\mathbb{R}$
    
    $$|b-a|^2=|a-b|^2=(a-b)^2$$
    
    which makes the *distance formula* much easier to establish.
    ````
2. **Distance Formula.** Prove that, for any two distinct points $P(x_1,y_1)$ and $Q(x_2,y_2)$ in the coordinate plane, $\text{Dist}(P,Q)=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$.

    ````{hint}
    The distance formula is simply the anlaytic geometry version of the Pythagorean Theorem.
    ````
3. **Midpoint Formula.** Prove that the midpoint $M$ of line segment $\overline{AB}$ where $A(x_1,y_1)$ and $B(x_2,y_2)$ is given by:$$M(x,y)=\left( \frac{x_1+x_2}{2},\frac{y_1+y_2}{2} \right)$$

4. **Linear Equations.** For any line $l$ not parallel to the $y$-axis, prove all points $P(x,y)$ satisfy the relationship $y=mx+b$ for some $m,b\in\mathbb{R}$.

    ````{note}
    Lines parallel to the $y$-axis have equations of the form $x=k$ for some $k\in\mathbb{R}$. We say the slope of such lines is \textbf{undefined}. Some textbooks refer to these types of lines as having "no slope." This is very confusing especially for high school students: "no slope" seems almost the same as "zero slope" due to how we communicate in real life. In this course, we will always refer to these lines as having *undefined slope*.
    ````