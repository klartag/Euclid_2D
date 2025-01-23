# Geometry Language

## Overview

In general, we have objects of several types:

* Point
* Scalar
* Line
* Circle
* Angle
* Orientation

We have predicates, stating information on objects, such as:

```
between(A, B, C)
equals(A, B)
not_equals(B, C)
```

We have constructors, which allow us to build objects using other objects:

```
Let O := center(c)
Let r := radius(c)
```

We have theorems, which allow us to get more objects and more predicates on them:

```yaml
symmetry_of_between:
  inputs:
    - a: Point
    - b: Point
    - c: Point
  where:
    - between(a, b, c)
  conclude:
    - between(c, b, a)
```

And we have proofs, which are a composition of these:

```
Assumptions:
O, A, B, C: Point
between(A, B, C)
angle(A, O, B) == 20
angle(B, O, C) == 30
Need to prove: 
angle(A, O, C) == 50
Proof:
By angle_sum_simple on O, A, B, C we get angle(A, O, C) == angle(A, O, B) + angle(B, O, C)
```

The language should be flexible, and it should be easy to extend.

## Objects

Objects are introduced in three ways:

* In the proof assumptions. There, objects are just declared in the format:

  ```
  A, B, C: Point
  c: Circle
  ```
* Objects can be explicitly defined using constructors:

  ```
  Let r := distance(A, B)
  Let d = Circle(A, r)
  ```
* Objects can be built using theorems (More on the format used by theorems later):

  ```
  By theorem line_intersection on l1, l2 we get P, P in l1, P in l2 
  ```

The current planned object types are:

* Point
* Scalar
* Line
* Circle
* Angle
* Orientation

## Constructors

Constructors are objects defined to link several object types.

The planned constructors are:

* `distance(a: Point, b: Point) -> Scalar`: The distance between two points.
* `angle(a: Point, b: Point, c: Point) -> Angle`: The directed angle between three points. Always contained in $[-\pi, \pi)$.
* `line_angle(l: Line) -> Angle`: The angle of the line. Since no basis was chosen, only differences can be well defined. We have
  `angle(A,B,C) == line_angle(Line(B, C)) - line_angle(Line(A, B))`. Defined only in $\R / \pi \Z$.
* `center(c: Circle) -> Point`
* `radius(c: Circle) -> Point`
* `log(r: Scalar) -> Scalar`
* `exp(r: Scalar) -> Scalar`
* `orientation(a: Point, b: Point, c: Point) -> bool`: If true, the orientation of the signed triangle `ABC` is always positive, and if false it is always negative.

More possible constructors we can consider are:

* `intersection(l: Line, m: Line)`: The intersection between two lines. I think that this should be left to a theorem, since it

## Predicates

The current predicates are:

#### Equals / Equals_mod

States that two objects are equal. Since equality is extremely common, it can be stated as either:

```
equals(A, B)
A == B
```

This is a logical relation, and the code will maintain its reflexivity and transitivity.

Equals also has versions for angles, which work modulo 180 and 360:

```
A == B mod 180
```

#### Not Equals

States that two objects are not equal. Since it is also extremely common, it can be stated as:

```
not_equals(A, B)
A != B
```

Note that while `not_equals` is usually not a logical relation, in orientations it is.

Not Equals also has mod 180 and mod 360 versions.

#### In / Not in

States that a point is contained in some geometric object. Can be stated as:

```
in(A, C)
A in C
B not in C
```

#### Triangle

States that three points are not on the same line.

```
triangle(A, B, C)
```

#### Distinct

States that none of the points in the list (Of any length) are equal to each other.

```
distinct(A, B, C, D, ...)
```

#### Convex

States that some points form a convex body. This is not properly implemented yet.

```
convex(A, B, C, D)
```

## Theorems

The theorems allow us to get new objects and predicates.

### Prelude: Axioms defined implicitly

We will not formally define all axioms, but allow the LLM to implicitly assume them. I am not sure if this is the best thing to do from an ML perspective, since things like chain-of-thought are claimed to perform better.

A list of implicit axioms:

* The standard axioms of $\R$ for scalars, $\R / \pi \Z$ and $\R/2\pi\Z$ for angles.
* Equality being a logical relation. This means that if `a == b`, every predicate true for `a` becomes automatically true for `b` as well.
* The symmetry of betweenness, of the line passing through two points, of the distance between two points, and of the radical axis between two circles are also implicit.
* Antisymmetry of angles and orientations:

```
angle(A, B, C) == - angle(C, B, A)
orientation(A, B, C) != orientation(C, B, A)
```

The axioms which are covered by this are:

* Transitivity for equidistance (2)

### Format

To make theorems easier to work with, they are stored in YAML files.

The format is thus:

```yaml
theorem_name:
  for:
    - input_0: Type0
    - input_1: Type1
  where:
    - predicate_0(input_0)
    - predicate_1(input_0, input_1)
    - p2: predicate_2(input_1)
  construct:
    - output_2: Type2
  conclude:
    - predicate_2(input_0, )
    - p3: predicate_3(input_0, input_1, output_2)
  possible_conclusions:
    - p2 => p3
    - theorem_name_2: p2 <= p3
```

All sections are optional.

The first section, `for`, details the names and types of the inputs.

The second section, `where`, details predicates on the inputs. Predicates can be names, in which case they are optional, and are used in the conclusion format.

The third section, `construct`, specifies which objects are constructed by the theorem.

The fourth section, `conclude`, specifies predicates on the results. Again, named predicates are not always used. In addition to unnamed predicates, which follow from the unnamed predicates before, named predicates do not immediately follow, but are used to construct additional flows of the theorem, as in the final line of the example.

The fifth section, `possible_conclusions`, specifies additional flows of the theorem, with more predicates being satisfied leading to more predicates being proved. The additional flows can be given names, which will replace the name of the theorem when the flow is being used. Each flow is parsed as an additional theorem, which could be annoying when a theorem is complex and has a lot of alternative flows.

## Proofs

A proof has three sections: the assumptions, the required predicates, and the proof body.

#### Assumptions

The assumptions start with the title:

```
Assumptions:
```

Followed by object definitions, such as:

```
O, A, B, C: Point
```

Followed by a list of predicates:

```
between(A, B, C)
angle(A, O, B) == 20
angle(B, O, C) == 30
```

#### Need to prove

This sections starts with the section title (`Need to prove:`), followed again by object definitions and predicates.

Objects defined here must also be defined by the proof body.

```
angle(A, O, C) == 50
```

#### Proof body

In the proof body, each line is a statement.

There are four types of statements:

* Theorem statements. Currently the parser accepts statements of the form:

  ```
  By theorem_name on A, B, C, we get X, Y, Z, predicate_name(A, X), predicate_name(C, D, Y, Z) 
  ```

  Here `X`, `Y`, and `Z` are objects constructed by the theorem (Defined in the `construct` section), and the predicates are the predicates defined in the `conclude` or `possible_conclusions` section.
  You can also write:

  ```
  We have X: Circle, Y: Line, Z: Point, predicate_name(A, B), predicate_name(C, D) 
  ```

  This is slower and gives less indicative messages.
* Let statements. These involve giving constructions names for clarity:

  ```
  Let r := distance(A, B)
  Let c := Circle(O, r)
  ```
* `We have shown that` statements. These only mark that something has been proved. They are used in if statements.
* `If` statements. Sometimes, some cases need to be checked. The predicates which can be reversed are:

  - Equals and not-equals.
  - In and not in
  - Between, which can have between(A, B, C), between(B, A, C), between(A, C, B), and A not in Line(B, C).

  The syntax is:

  ```
  If {predicate_1}:
  	...
  Else if predicate_2:
  	...
  Else if predicate_2:
  	...
  ```

  And then, the result predicates are the intersection of the non-false branches.

# List of theorems

The list of theorems here is only the beginning of a plan, and is expected to grow.

This list does not contain all theorems!

## Tarski Core

The theorems here are specified informally, not using the correct format. The exact theorems are in the theorem files.

#### Theorems

##### Reflexivity of distance

```
reflexivity_of_distance:
  inputs:
    - a: Point
    - b: Point
  conclude:
    - distance(a, b) == distance(b, a)
```

```
reflexivity_of_between:
  inputs:
    - a: Point
    - b: Point
  conclude:
    - between(a, b, b)

```

##### Identity of equidistance (3), identity of betweenness (6), and (13)

```
a, b: Point
t1: distance(a, b) == 0
t2: a == b
t3: between(a, b, a)
Then:
t1 <=> t2 <=> t3
```

##### Five-segment axiom (5)

```
a, b, c, d, e, a', b', c', d', e': Point

t1: distance(a, b) > 0 
t2: between(a, b, c)
t3: between(a', b', c')
t4: distance(a, b) == distance(a', b')
t5: distance(b, c) == distance(b', c')
t6: distance(a, d) == distance(a', d')
t7: distance(b, d) == distance(b', d')
t8: distance(c, d) == distance(c', d')

Then:
t1 & t2 & t3 & t4 & t5 & t6 & t7 => t8
t1 & t2 & t3 & t4 & t5 & t6 & t8 => t7  # Not in the original Tarski, but true as well
```

##### Reflexivity of betweenness (12):

```
between(a, b, b)
```

##### Symmetry of betweenness (14):

```
symmetry_of_between:
  inputs:
    - a: Point
    - b: Point
    - c: Point
  where:
    - between(a, b, c)
  conclude:
    - between(c, b, a)
```

##### Inner Transitivity of betweenness (15):

```
a, b, c, d: Point
between(a, b, d)
between(b, c, d)
Then:
between(a, b, c)
```

##### Outer Transitivity of betweenness (16):

```
a, b, c, d: Point
between(a, b, c)
between(b, c, d)
b != c
Then:
between(a, b, d)
```

##### Transitivity of distances (19):

This axiom is implicitly covered.

```
a, b, c: Point
a == b
Then:
distance(a, c) == distance(b, c)
```

##### Uniqueness of triangles (20)

```
a, b, c, c', d, d', x: Point
distance(a, c) == distance(a, c')
distance(b, c) == distance(b, c')
between(a, d, b)
between(a, d', b)
between(c, d, x)
between(c', d', x)
d != x
d' != x
Then:
c == c'
```

Note here that the points `d`, `d'`, and `x` are all just side specifiers, and the theorem could probably be restated more elegantly.

##### Length sums (23, 24)

This is a neater phrasing of the axioms which we will need anyway:

```
a, b, c: Point
between(a, b, c)
Then:
distance(a, b) + distance(b, c) == distance(a, c)
```

#### Constructions

##### Segment construction (4)

```
a, b: Point
r: Scalar

Then:

c: Point
distance(b, c) == r
between(a, b, c)
```

##### Pasch Axiom (7):

```
a, b, c, p, q: Point
between(a, p, c)
between(b, q, c)
Then:
x: Point
between(a, x, q)
between(b, x, p)
```

##### Lower dimensional axioms (8)

```
a: Point
Then:
b: Point
b != a
```

```
a, b: Point
a != b
Then:
c: Point
!between(a, b, c)
!between(b, a, c)
!between(b, c, a)
```

##### Upper 2-dimensional axiom (9)

The initial phrasing requires a logical OR. I separate it to this:

```
a, b, c, p, q: Point
distance(a, p) == distance(a, q)
distance(b, p) == distance(b, q)
distance(c, p) == distance(c, q)

Then:
l: Line(a, b)
c in l
```

which uses the line axioms.

##### Euclid's Axiom 1 - line intersection (10)

```
a, b, c, d, e: Point
between(a, d, e)
between(b, d, c)
a != d
Then:
x, y: Point
between(a, b, x)
between(a, c, y)
between(x, e, y)
```

##### Euclid's Axiom 2 - incircle (10)

```
a, b, c: Point
c not in Line(a, b)
Then:
x: Point
distance(x, a) == distance(x, b)
distance(x, a) == distance(x, c)
```

##### Continuity (11)

```
a: Point
b, c: List[Point]
between(a, b, c)

Then:
x: Point
between(b, x, c)
```

The axiom schema of continuity will not be implemented.

##### Triangle Construction (21)

```
a, b, p, a', b', c': Point
distance(a, b) == distance(a', b')
Then:
c, x: Point
distance(a, c) == distance(a', c')
distance(b, c) == distance(b', c')
x in Line(a, b)
between(p, x, c)
```

We can also have a variation of this with the other direction, or using angles.

##### Density (22):

```
a, c: Point
a != c
Then:
b: Point
a != b
c != c
between(a, b, c)
```

## Lines

##### Ordering of lines (Also covers axioms 17 and 18):

```
a, b, c: Point
l: Line
t1: a in l
t2: b in l
t3: c in l
t4: between(a, b, c)
t5: between(a, c, b)
t6: between(c, a, b)

Then:
t1 & t2 & t3 <=> t4 | t5 | t6

```

This theorem will not be available in the initial version, since it requires enumeration.

Its negation is weaker, and is a theorem:

```
a, b, c: Point
!between(a, b, c)
!between(b, c, a)
!between(c, a, b)
Then:
a not in Line(b, c)
b not in Line(c, a)
c not in Line(a, b)
```

```
a, b, c: Point
c not in Line(a, b)
Then:
!between(a, b, c)
!between(b, c, a)
!between(c, a, b)
```

## Angles

##### Angle non-zero

```
a, b, c: Point
c not in Line(a, b)
Then:
angle(a, b, c) != 0
```

##### Consistency of angle construction

```
a, b, c: Point
Then:
angle(a, b, c) == angle(line(a, b), line(b, c)) mod 180
```

##### Summation of angles

```
l, m, n: Line
Then:
full_angle(l, m) + full_angle(m, n) == full_angle(l, n)
```

##### Sum of angles in triangle

```
a, b, c: Point
Then:
full_angle(a, b, c) + full_angle(b, c, a) + full_angle(c, a, b) == 0
```

##### Triangle congruence

```
a, b, c, a', b', c': Point
t1: distance(a, b) == distance(a', b')
t2: distance(b, c) == distance(b', c')
t3: distance(c, a) == distance(c', a')
t4: full_angle(a, b, c) == full_angle(a', b', c')
t5: full_angle(b, c, a) == full_angle(b', c', a')
t6: full_angle(c, a, b) == full_angle(c', a', b')
Then:
t1 & t2 & t4 => t3 & t5 & t6  # Segment-angle-segment congruence
t2 & t4 & t5 => t1 & t3 & t6  # angle-segment-angle congruence
```

Note that things like the angle between the line and itself are also implied by the theorem, since `flat_angle(L, L) == flat_angle(L, L) + flat_angle(L, L)`, and `flat_angle(L, M) + flat_angle(M, L) == flat_angle(L, L) == 0`.

##### Intersection of lines with angle 0

```
l, m: Line
p: Point
p in l
p in m
flat_angle(l, m) == 0
Then:
l == m
```

## Circles

#### Theorems

##### Definition of circle

```
c: Circle
p: Point
t1: p in c
t2: distance(p, c.center) == c.radius
Then:
t1 <=> t2
```

#### Constructions

##### From three points

Already appears above in Euclid's theorem

##### From center and radius

## Log-Length

This is a type similar to the length, since length ratio and similarity statements are too frequent to ignore.

They satisfy:

```
a, b, a', b': Point

d: distance(a, b) == distance(a', b')
l: log_distance(a, b) == log_distance(a', b')

Then:
d <=> l
```

```
a, b, c, a', b', c': Point

c not in Line(a, b)
c' not in Line(a', b')

a1: full_angle(a, b, c) == full_angle(a', b', c')
a2: full_angle(b, c, a) == full_angle(b', c', a')

r1: log_distance(a, b) - log_distance(a', b') == log_distance(b, c) - log_distance(b', c')
r2: log_distance(b, c) - log_distance(b', c') == log_distance(c, a) - log_distance(c', a')

Then:
a1 & a2 => r1 & r2
a1 & r1 => a2 & r2
```

We can now support the radical axis theorem and power of points.

There is an analogous version with anti-similarity:

```
a, b, c, a', b', c': Point

c not in Line(a, b)
c' not in Line(a', b')

a1: full_angle(a, b, c) == -full_angle(a', b', c')
a2: full_angle(b, c, a) == -full_angle(b', c', a')

r1: log_distance(a, b) - log_distance(a', b') == log_distance(b, c) - log_distance(b', c')
r2: log_distance(b, c) - log_distance(b', c') == log_distance(c, a) - log_distance(c', a')

Then:
a1 & a2 => r1 & r2
a1 & r1 => a2 & r2
```

## Orientation

Orientation checks if the area of a triangle is positive or negative. We will treat the representation as a function from triangles to booleans, give relations between orientations, and so on. Orientation is necessary pretty much only to use the segment-segment-segment-orientation congruence.

## More:

Convexity is defined by stating all "between" relations for all intersections.

`raycyclic O A B C` is actually `convex O A B C`.

I will also have to incorporate:

* Orientation
* Directed angles

I still haven't seen a case where we don't know the orientation in advance, since that would require a really bizarre construction. When passing tangents from a point to a circle, we would get two triangles, one of which has positive orientation and one negative.

Theorems I need:

* Radical axis and power of a point

For the Israeli math exams, this solves everything which is purely geometric, and doesn't require algebra (areas, Pythagoras) or trigonometry.

#### Theorems

##### Opposite angles sum to zero

```
c: Circle
w, x, y, z: Point
w in c
x in c
y in c
z in c
Then:
full_angle(w, x, y) + full_angle(y, z, w) == 0
```

##### Angle lying on diameter is a right angle

```
c: Circle
a, b, p: Point
a in c
b in c
p in c
b in Line(a, c.center)  # a, b is a diameter of the circle
a != b
Then:
full_angle(a, p, b) == 0.5
```

##### Triangle inequality

Could be useful?

```
a, b, c: Point
Then:
distance(a, b) + distance(b, c) - distance(c, a) >= 0
```

#### Constructions

##### Midpoint

```
a, b: Point
Then:
m: Point
between(a, m, b)
distance(a, m) == distance(m, b)
```

##### Three-point
