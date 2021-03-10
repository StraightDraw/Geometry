# A.1 Affine Coordinates.

An affine geometry is one in which the Euclidean parallel postulate holds. Affine coordinates can be created for any (non-finite) affine geometry, and they will have the properties we associate with Cartesian Coordinates. We refer to a coordinate system as $O_{xy}$ where $O$ is the origin and $x$ and $y$ refer to two mutually perpendicular lines called the $x$-axis and $y$-axis that intersect at $O$. By Theorem 1, these axis lines uniquely determine a plane, specifically, the Cartesian Coordinate Plane. Also included in the definition of this coordinate system is a positive real number $e$, the unit measure of distance. To sum up, the SMSG Axioms provide everything needed to create the typical Cartesian Coordinate System which can, with a bit more work, include the $z$-axis as well.

**Distance in a Coordinate System $O_{xy}$**. At the moment, distances have only been defined along the axes. Notice that the value of the coordinates of point $P(x,y)$ are determined by creating a rectangle and measuring distances on the $x$- and $y$-axis using the SMSG Ruler Axioms. The next two theorems will establish the validity of the Euclidean distance metric:

Eventually, we will need to work lines in our coordinate system that satisfy equations of the form $y=mx+b$. Before we can do so, we must define slope.

Slope of line $l$:
: The unique $m\in\mathbb{R}$ such that, for any two points $N(x_1,y_1)$ and $M(x_2,y_2)$ on $l$, $$m=\frac{y_1-y_2}{x_1-x_2}$$



### Theorems

1. For two distinct points with the same $y$-coordinate, say, $P(x_1,y)$ and $Q(x_2,y)$, the distance between $P$ and $Q$ is $\text{Dist}(P,Q)=|x_1-x_2|$. For two distinct points with the same $x$-coordinate, say, $P(x,y_1)$ and $Q(x,y_2)$, the distance between $P$ and $Q$ is $\text{Dist}(P,Q)=|y_1-y_2|$.
2. For any distinct $a,b\in\mathbb{R}$, $|b-a|^2=|a-b|^2=(a-b)^2$.

    Note that the Ruler Axiom gives linear distance in terms of the absolute value of differences in coordinates, but the Euclidean distance metric is defined in terms of the squares of those differences. The above lemma makes the following theorem easier to prove.

3. **Distance Formula.** For any two distinct points $P$ and $Q$ in the coordinate plane, $\text{Dist}(P,Q)=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$.

4. **Linear Equations.** For any line $l$ not parallel to the $y$-axis, all points $P(x,y)$ satisfy the relationship $y=mx+b$ for some $m,b\in\mathbb{R}$.

    ````{note}
    Lines parallel to the $y$-axis have equations of the form $x=k$ for some $k\in\mathbb{R}$. We say the slope of such lines is \textbf{undefined}. Some textbooks refer to these types of lines as having "no slope." This is very confusing especially for high school students: "no slope" seems almost the same as "zero slope" due to how we communicate in real life. In this course, we will always refer to these lines as having *undefined slope*.
    ````

5. **Equations of Circles.** All points on a circle with center point $C(h,k)$ and radius $r>0$ satisfy the relationship $$(x-h)^2+(y-h)^2=r^2$$