# The Rule-Set



## Desired properties



* Completeness. The rule-set should suffice to prove any theorem in geometry.
  * This can be obtained by incorporating the axioms of geometry into the rule-set. Tarski's axioms, or some simplification of them, should suffice.
* Clarity. 
  * Any geometry problem can be stated via the rule-set.
  * Geometry proofs using the rule-set should be similar to proofs written by people.
* Ease of use
  * The theorems should not contain many if-elses.
  * The theorems should be short, if possible.



## Possible design

The rule-set will have several parts:

### Design

Objects which we like:

* Points
* Lines and segments
* Scalars
* Circles
* Angles
* Triangles

Objects should have types.

Three spaces in which we could work:

* $\R^2$
* $\C^2$
* $\mathbb{P}^2(\C)$

The second and third make algebra far better, while the first is uglier. However, the geometry we have is less complete.



### Rules

#### Part 1 - Points, line segments, and scalars - based on Tarski

The first part will be the 24 axioms of Tarski. These define points and line segments.

There are some axioms that rely on first-order logic, and I am not sure how to incorporate them.

If points at infinity are allowed, distances involving them are no defined, but things are perfectly defined algebraically if I homogenize, or use projective scalars.

##### Introduced objects

* Point
* Scalar

##### Relations

* between(Point a, Point b, Point c)
* equal(Point a, Point b) and not_equal
* equal(Scalar a, Scalar b) and not_equal

##### Constructions:

* `distance(a: Point, b: Point) -> Scalar`

* Segment construction:

  `segment(a: Point, b: Point, r: Scalar) -> Point` Constructs a point `x` with `between(a, b, x)` and `distance(b, x) == r`.

* Pasch

  * Constructs the second intersection of a line with a triangle.

* Lower two-dimensional 

* Euclid

* Continuity

  * Here we encounter nuance. The axiom of continuity could require first order logic. We usually don't need to define arbitrary geometric bodies, so it should be fine, but this is a dangerous point.

* Existence of triangle construction.

  * This is another theorem with an OR condition.

* Density axiom

* Equality of points on the same line with equal distances (Inner and outer versions)

##### Axioms:

* Reflexivity for equidistance
  * This is obtained by treating the distance as a scalar. 

* Transitivity for equidistance
  * This is obtained by treating the distance as a scalar.
* Reflexivity for betweenness.
* Identity of betweenness
* Inner transitivity of betweenness and outer transitivity

* Identity from equidistance
  * `equal(distance(a, b), 0) -> equal(a, b)`
* Equal points have equal distances.
* Five-segment axiom
  * Gives us the triangle congruence relations, with angles represented in Tarski form.
* Upper 2D axiom
* Inner connectivity:
  * This states that if `b` and `c` are both between `a` and `d`, then either `between(a, b, c)` or `between(a, c, b)`. This is an annoying point, since we might require proof trees.
* Outer connectivity:
  * The same as inner connectivity, but with both `c` and `d` to the right of `a` and `b`.
* Uniqueness of triangle construction.

#### Part 2 - Scalars

Scalars can be used to measure lengths and represent theorems of the form "$D(a, b)D(c,d) = D(e,f)$".

They also allow the prover to use Grobner-style logic.

* Each point has two scalars: $x$ and $y$. Points with the same $x$ and $y$ are the same.
* Each line has three scalars: $ax + by + c = 0$ satisfied by the points on it.
* The distance between two points is a scalar with Euclid's theorem.

I don't like ordering scalars, but it can be done to connect them to the "between" property of Tarski.



The easiest way to work with scalars is to take this out of the LLM and the formal deduction system. Instead of having the LLM do the computation by hand, have a language to state relations:

```
between Point a, Point b, Point c -> distance(a, c) == distance(a, b) + distance(b, c)
triangle {a, b, c} -> angle abc + angle bca + angle cab == 0
```

Then, the model can state things like:

```
angle abc == angle def # Computation
```

And this will be verified by linear algebra (For lengths over $\R$, for angles over $\R / \pi$, which is a $\Z$-module)

A scalar should have a nonzero property to allow division.

#### Part 3 - Circles

Circles are defined with a center and radius.

```rust
struct Circle {
	center: Point,
	radius: Scalar,
}
```

Circles satisfy:

* The distance between the center and any point on the circle is the radius.

To construct a circle from two points, construct a circle with one point in its center and the distance scalar as the radius. To construct a circle tangent to a line, create the altitude line/intersect, and then take the distance to the line. (This could be inlined in a later stage, but I think that inlining it now is a mistake)

#### Part 4 - Angles

There are two models of angles I can think of:

* Angles modulo $2\pi$. There are the normal angles.
* Angles modulo $\pi$. These are used in the full-angle method, and are prettier in some respects. When defining angles algebraically, you get only angles modulo $\pi$, so this isn't that much less expressive. Theorems become much prettier when you don't chase the extension down.

#### Part 5 - Triangles

Triangles are defined as:

```Rust
struct Triangle {
	p1: Point,
	p2: Point,
	p3: Point
}
```

As such, they don't have any new data, and are mostly used as a way to organize data for other theorems.

