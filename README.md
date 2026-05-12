# Euclid 2D

### Table of Contents

| Section                                                                                                                       | Description                                                                                                   | Status? |
|-------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------|
| [Introduction](#introduction)                                                                                                 | What is this repository about?                                                                                |    x    |
| [Geometry Syntax](#syntax)                                                                                                    | How to formulate a geometry problem or proof.                                                                 |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Object Types](#syntax-object-types)                                                                | What are the different types of objects that can appear in a problem statement or proof.                      |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Literals](#syntax-literals)                                                                        | How to describe scalars with values that are known ahead of time.                                             |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Constructions](#syntax-constructions)                                                              | How to use geometric objects to describe more geometric objects.                                              |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Predicates](#syntax-predicates)                                                                    | How to use geometric objects to describe predicates.                                                          |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Declarations](#syntax-declarations)                                                                | How to declare the existence of new geometric objects.                                                        |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Implications](#syntax-implications)                                                                | How to declare that predicates imply other predicates.                                                        |    x    |
| [Geometry Document](#syntax-structure)                                                                                        | All about the file format in which we save geometry problem statements and proofs.                            |         |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Assumptions](#syntax-assumptions)                                                                  | The section containing the given predicates in the problem.                                                   |         |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Embedding](#syntax-embedding)                                                                      | The section containing a coordinate embedding of geometry objects.                                            |         |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Need to prove](#syntax-need-to-prove)                                                              | The section containing the predicates that need to be proved.                                                 |         |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Proof](#syntax-proof)                                                                              | The section containing the proof.                                                                             |         |
| [Geometry Configuration Rules](#configuration)                                                                                | What are the rules that geometric objects abide to?                                                           |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Constructions](#configuration-constructions)                                                       | How constructions are defined.                                                                                |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`inputs`](#configuration-constructions-inputs)                             | The `inputs` section in the definition of a construction.                                                     |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`preprocess`](#configuration-constructions-preprocess)                     | The `preprocess` section in the definition of a construction.                                                 |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`where`](#configuration-constructions-where)                               | The `where` section in the definition of a construction.                                                      |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`construct`](#configuration-constructions-construct)                       | The `construct` section in the definition of a construction.                                                  |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`conclude`](#configuration-constructions-conclude)                         | The `conclude` section in the definition of a construction.                                                   |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`possible_conclusions`](#configuration-constructions-possible-conclusions) | The `possible_conclusions` section in the definition of a construction.                                       |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Predicates](#configuration-predicates)                                                             | How predicates are defined.                                                                                   |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`inputs`](#configuration-predicates-inputs)                                | The `inputs` section in the definition of a predicate.                                                        |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`preprocess`](#configuration-predicates-preprocess)                        | The `preprocess` section in the definition of a predicate.                                                    |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`conclude`](#configuration-predicates-conclude)                            | The `conclude` section in the definition of a predicate.                                                      |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Theorems](#configuration-theorems)                                                                 | How theorems are defined.                                                                                     |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`inputs`](#configuration-theorems-inputs)                                  | The `inputs` section in the definition of a theorem.                                                          |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`where`](#configuration-theorems-where)                                    | The `where` section in the definition of a theorem.                                                           |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`where_embedding`](#configuration-theorems-where-embedding)                | The `where_embedding` section in the definition of a theorem.                                                 |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`conclude`](#configuration-theorems-conclude)                              | The `conclude` section in the definition of a theorem.                                                        |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`possible_conclusions`](#configuration-theorems-possible-conclusions)      | The `possible_conclusions` section in the definition of a theorem.                                            |    x    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`rank`](#configuration-theorems-rank)                                      | The `rank` section in the definition of a theorem.                                                            |         |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`trivial_if_equal`](#configuration-theorems-trivial-if-equal)              | The `trivial_if_equal` section in the definition of a theorem.                                                |         |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [`metadata`](#configuration-theorems-metadata)                              | The `metadata` section in the definition of a theorem.                                                        |         |
| [Generating Problems](#problem-generator)                                                                                     | How to generate geometry problems (just their statements, without proof).                                     |         |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Introduction](#problem-generator-introduction)                                                     | What is this module about?                                                                                    |         |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Capabilities](#problem-generator-capabilities)                                                     | What can we do with it?                                                                                       |         |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Usage](#problem-generator-introduction)                                                            | How do we use it?                                                                                             |         |
| [Solving Problems](#solver)                                                                                                   | How to solve geometry problems                                                                                |         |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Embedding a question](#solver-embedding)                                                           | How to take a geometry problem and embed it in 2D space.                                                      |         |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Generating a proof](#solver-proof-generation)                                                      | How to take a geometry problem and generate a proof.                                                          |         |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Trimming proofs](#solver-trimming)                                                                 | How to shorten a proof until its length is locally optimal.                                                   |         |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Checking + Validating a proof](#solver-checking)                                                   | How to make sure a written proof is correct.                                                                  |         |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Running an interactive terminal](#solver-interacting)                                              | How to evaluate expressions and predicates in a geometry problem (possibly with a partially-written proof).   |         |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Prettifying](#solver-prettifying)                                                                  | How to make a proof easier to read by humans.                                                                 |         |

## <span id="introduction"> Introduction </span>

This is an open-source research project focused on using AI to solve, invent, and analyze problems in 2D Euclidean geometry.

The subject has a rich history, including Tarski's work on the decidability of Euclidean geometry in the 1920s and the practical contributions of Chou, Gao, and Zhang in the 1990s, which came close to achieving IMO-level problem-solving. Recent interest in the field was reignited by Google DeepMind's press release in July 2024, suggesting that Alpha Geometry 2 has mastered IMO-level geometry questions. However, as of January 2025, Google has not disclosed Alpha Geometry 2. We believe that open-source projects like this can increase the likelihood of AI becoming a useful tool for advancing mathematics and benefiting the mathematical community.

We focus on Large Language Models (LLMs), hoping to integrate an LLM proficient in geometry with those knowledgeable in other domains. We hope this integration will create a synergistic effect, enhancing the capabilities of LLMs across a broad spectrum of logical and geometrical applications.

We are testing the following hypotheses.

Hypothesis 1: LLMs of moderate size (< 70B parameters) can learn to solve Euclidean geometry problems.

Hypothesis 2: With the support of accompanying software (e.g., verifiers or numerical embeddings), such LLMs can solve Euclidean geometry problems.

The level of Euclidean Geometry problems we are aiming at is roughly that of e.g. Akopyan's book "Geometry in Figures". We acknowledge the support of MSR for this project during its initial phase.

Google bucket link:
https://console.cloud.google.com/storage/browser/euclid_2d?inv=1&invt=Ab4r5g&project=versatile-bolt-330819

## <span id="syntax"> Geometry Syntax </span>
### <span id="syntax-object-types"> Object Types </span>

Throughout this repository, we will be describing different objects that are relevant to geometry problems.
These will be referred to as **geometry objects**.
There are a few types of objects, each type having a different range of values.

1. Points
2. Lines
3. Circles
4. Scalars

Points, lines, and circles are objects that can be embedded in a 2D plane.
Scalars are real numbers.

Objects will have names, usually marked by a single letter.
Sometimes they might have longer names, an index associated with them, and a prime (`'`) symbol on them.
Here are some examples of valid names for objects:
* `A`
* `B_1`
* `M2`
* `C'`
* `AQ`

The name of an object does not contain information on its type, and any object type of object could potentially have any name.
Although for geometry objects that can be embedded in a plane (i.e., objects that are **not** scalars), we will usually follow the following conventions:

| Object type | Naming convention | Common names                |
|-------------|-------------------|-----------------------------|
| Point       | Capital letters   | `A, B, C, P, Q, R, X, Y, Z` |
| Line        | Lowercase letters | `f, g, h, p, q, r, s, t`    |
| Circle      | Lowercase letters | `c, d, e, o, w`             |

These conventions are for the base name. There are no specified conventions for whether to use underscores for indexing, or whether to use primes (`'`).
Those can appear on any object.

### <span id="syntax-literals"> Literals </span>

Scalars can also be described by simply typing the number describing its value.
Examples are `1` or `3.14` or `-90`.

### <span id="syntax-constructions"> Constructions </span>

Geometry objects are expressed with a string of text defining it.
Some objects are given simply by their names (as described in the [previous section](#syntax-object-types)).
We call those objects **atoms**.

We can use these, together with **constructions**, to create more geometry objects.

#### Construction functions

Many constructions are used exactly like a function, that takes geometry objects as input, and returns a geometry object in its output.

Here are some examples:

1. `midpoint` is a construction that takes two points, and returns a third point.
  Given two points `A` and `B`, the object described by
  ```
  midpoint(A, B)
  ```
  is also a point. Specifically, it is the point in the center of the segment from `A` to `B`.

2. `parallel_line` is a construction which takes two parameters: The first a point and the second a line. Like so:
  ```
  parallel_line(A, l)
  ```
  This returns an object whose definition is "The line which is parallel to `l` and passes through `A`".

3. `Circle` is a construction that takes three points, and returns the circle passing through those three points:
  ```
  Circle(A, B, C)
  ```

  Note that although most constructions are written in lowercase, very few constructions have a capital letter in the beginning.
  This is important, as construction names are case-sensitive.

4. `angle` is a construction that takes three points:
  ```
  angle(A, B, C)
  ```
  and returns a scalar describing by how much the ray from B in the direction of A
  must be rotated clockwise to reach the ray from B in the direction of C.

Each construction has a predefined number of parameters it must receive, and each parameter has a predefined type.
A construction cannot be called on a different number of parameters, or with parameters of the wrong type.

The full list of construction functions can be found in this [file](rules/constructions_and_predicates/constructions_database.yml).
The format of this file is described [further down in this document](#configuration-constructions).

#### Binary construction operators

Some constructions are simply binary operators on real numbers.
The four basic arithmetic operations can be used as binary operators: `+, -, *, /`.

For example, if `x` is a scalar, and `A, B, C` are points, the following are valid uses of arithmetic operators:
```
x + angle(A, B, C)
(x - 2) * 3
3 * angle(A, B, C) / 2
distance(A, B) / distance(A, C)
```
Usually, we will not write expressions such as `(x - 2) * 3`, as our proof engine does not know to apply the distributive property.
Nonetheless, this expression is valid and will parse.

### <span id="syntax-predicates"> Predicates </span>

Predicates are statements that have a boolean value (are either true or false).
Like [geometry objects](#syntax-object-types), they are depicted by a string of text.
Predicates are very useful, and will be used in order to describe a few things:

1. The givens in a geometry problem
2. The statement that the geometry problem requires we prove
3. The results that each step of a proof gives us

Predicates could be seen as a type of geometry object, but they are described by a separate Python class.

#### Predicate functions

Like geometry objects, many predicates are described by a function that take geometry objects as parameters.
Some examples are:

1. `concyclic` is a predicate that takes four points as input:
```
concyclic(A, B, C, D)
```
and states that all four of those points lie on a single circle.

2. `concurrent` is a predicate that takes three lines as input:
```
concurrent(f, g, h)
```
and states that all three of these lines intersect at a single point.

3. `congruent_triangles` takes six points:
```
congruent_triangles(A, B, C, X, Y, Z)
```
and states that the triangles `ΔABC` and `ΔXYZ` are congruent.

Some predicates are a bit unusual in the way they take parameters:

4. `tangent` is a predicate that takes two curves:
```
tangent(c, d)
```
and states that they are tangent to each other.
This predicate is unusual in that it takes multiple parameter types:
At least one of `c` and `d` must be a circle, but the other parameter can be either a circle or a line.

5. `distinct` is a predicate that takes a list of geometry objects, and states that no two are equal.
It can take an arbitrary number of parameters:
```
distinct(f, g, h, j, k, l)
```
but all the parameters must be of the same object type.

#### Binary predicate operators

Some predicates are not described by functions, but rather by binary operators.

1. One of them is the `==` operator,
that states that two scalars are equal: If `x`, `y`, and `z` are scalars, then one could write
```
2 * x + 1 == y + z
```

2. Another is the `!=` operator, which states that two values are not equal.
```
2 * x + 1 != y + z
```

3. A variant of the `==` predicate checks whether two values are equal modulo 360°.
This predicate is called by adding the suffix `mod 360` to the predicate. For example,
if `A, B, C, D` are points, then one could write the predicate
```
angle(A, B, C) + 180 == angle(C, D, A) mod 360
```

4. The `!=` operator can also be written together with the `mod 360` suffix, and its meaning at this point is self-explanatory.

5. The `in` predicate, which takes a list of points (say, `A, B`) and a list of curves (say, `c, l`).
As long as each curve is either a line or a circle, its type does not matter.
Then, the predicate
```
A, B in c, l
```
states that each of the curves on the right side of the `in` operator contains each of the points on the left side of the `in` operator.

6. The `not in` predicate, which states the negation of the `in` predicate. I.e., the predicate
```
A, B not in c, l
```
states that no curve on the right side of the `in` operator may touch any of the points on the left side of the `in` operator.

#### Where can I find the full list of possible predicates?

A mostly complete list of predicate functions can be found in this [file](rules/constructions_and_predicates/predicates_database.yml).
The format of this file is described [further down in this document](#configuration-predicates).

The rest of the predicates (the more unusual ones) are defined inside this [directory](rules/predicates/implementations).


### <span id="syntax-declarations"> Declarations </span>

In various locations, it will be required to prescribe, for each geometric object that is an **atom**, what its type is.
This is important because while, it is clear that `midpoint(A, B)` is a point, it may not be clear whether an object `C` is also a point.

The way it is declared is with a line of text following the following syntax:
```yml
A: Point
```
This line of text says that the object on the left side of the colon, has the type named on the right side of the colon.
It is also possible to declare multiple objects at once, so long as they have the same type:
```yml
A, B, C: Point
f, g, h, l: Line
c, d: Circle
x, y, z, w, t: Scalar
```

### <span id="syntax-implications"> Implications </span>

In various locations, it will be important to mention, that a predicate implies another predicate.
These sorts of implication statements will have the following syntax:
```
[Predicate 1] [Symbol] [Predicate 2]
```
Where `[Predicate 1]` and `[Predicate 2]` are predicates (using the usual [predicate](#syntax-predicates) syntax),
and `[Symbol]` is precisely what you would expect:

| Symbol | Meaning                                               |
|--------|-------------------------------------------------------|
| `=>`   | `[Predicate 1]` implies `[Predicate 2]`.              |
| `<=`   | `[Predicate 2]` implies `[Predicate 1]`.              |
| `<=>`  | `[Predicate 1]` and `[Predicate 2]` imply each other. |

## <span id="syntax-structure"> Geometry Document </span>
### <span id="syntax-assumptions"> Assumptions </span>
### <span id="syntax-embedding"> Embedding </span>
### <span id="syntax-need-to-prove"> Need to prove </span>
### <span id="syntax-proof"> Proof </span>
## <span id="configuration"> Geometry Configuration Rules </span>

The [Geometry Syntax](#syntax) section above dealt with the *grammar* of the language in which we use our **constructions** and **predicates**.
The [Geometry Document](#syntax-structure) section above dealt with the *grammar* of the language in which we define problem statements,
and the subsection [Proof](#syntax-proof) dealt with how to call our **theorems** to prove geometry problems.  
The current section is going to deal with what one might call the '*nouns*' of this language.

I.e., which constructions, predicates, and theorems exist?
And where do we define what they do?

### <span id="configuration-constructions"> Constructions </span>

Before reading this section, it is recommended to be acquainted more or less with the grammar on how to [use constructions](#syntax-constructions).

The definitions of all constructions can be found in this [file](rules/constructions_and_predicates/constructions_database.yml).
Each  `.yml` mapping in the top-level of the file represents a different construction.
The definition of each construction includes a few sections.
The general shape of a construction may look more or less as follows:

```yml
construction:
  inputs:
    ...
  preprocess: ...
  where:
    ...
  construct:
    ...
  conclude:
    ...
  possible_conclusions:
    ...
```

The word `construction` is replaced with the name of the construction.
The sections `inputs` and `construct` are required, and the rest of the sections are optional and may be completely omitted.
For example, the following construction `center` is defined as follows:
```yml
center:
  inputs:
    - c: Circle
  construct:
    - O: Point
```
and omits all of the optional sections.

Next, we will be going over what the different sections mean, and how to read them:

#### <span id="configuration-constructions-inputs"> `inputs` </span>

This section declares what the parameters of a construction are.

It is a section with a list of lines, each line following [object declaration](#syntax-declarations) syntax.

For example, consider the following construction:
```yml
circle_circle_other_intersection: 
  inputs:
    - P: Point
    - c, d: Circle
  ...
```
This construction declares that the construction `circle_circle_other_intersection` takes **three** parameters as inputs.
The order of the parameters is read from left to right, top to bottom.
E.g., given a point `A`, and two circles `x`, `y`,
the construction call `circle_circle_other_intersection(A, x, y)`
will take `A` to be the point `P`, `x` to be the circle `c`, and `y` to be the circle `d`.

#### <span id="configuration-constructions-preprocess"> `preprocess` </span>

Sometimes the order of parameters does not matter in a construction.
For example, when defining the circumcircle of three points, one does not care about the order of the points.
This is written as follows:

```yml
Circle:
  ...
  preprocess: symmetric
  ...
```

Setting `preprocess` to `symmetric` immediately tells our grammar that, for example, the objects `Circle(A, B, C)` and the object `Circle(B, A, C)` are equal.

Another example for a value that `preprocess` can take is `between`:
```yml
internal_angle_bisector:
  inputs:
    - A, B, C: Point
  preprocess: between
  ...
```

This value tells us that if the order of parameters is reversed, the object is identical. I.e., `interal_angle_bisector(A, B, C)` equals `internal_angle_bisector(C, B, A)`.

The full list of values that the `preprocess` tag may have can be found in the [symmetry.py](rules/symmetry.py) file.

#### <span id="configuration-constructions-where"> `where` </span>

This section is a list of which constraints have to be true before this construction may be *defined*.
A good example is the construction `isogonal_conjugate`:
```yml
isogonal_conjugate:
  inputs:
    - P, A, B, C: Point
  ...
  where:
    - not_collinear(A, B, C)
    - not_collinear(P, A, B)
    - not_collinear(P, B, C)
    - not_collinear(P, A, C)
  ...
```
which is only defined when no three points out of the four inputs are collinear.

These predicates affect our code in two ways:
1.  When a construction is declared in the [problem statement](#syntax-assumptions), then all the predicates under their `where` section are immediately assumed.
2.  When a construction is declared in the [proof](#syntax-proof), if not all predicates under the `where` section have been proven, the code will throw an error.

#### <span id="configuration-constructions-construct"> `construct` </span>

This section is a declaration of the type of object that this construction returns.
For example, the construction `point_circle_tangent_line`
```yml
point_circle_tangent_line:
  inputs:
    - P: Point
    - c: Circle
  ...
  construct:
    - l: Line
  ...
```
takes a point and circle as input, and constructs the line tangent to the circle at this point.
(Presumeably the point must be on the circle, but this is taken care of in the [`where`](#configuration-constructions-where) section of this construction.)

The declaration of the `construct` section follows [object declaration](#syntax-declarations) syntax,
but **only one object** may be declared in the `construct` section.

This is the return type of the construction:
I.e., the object `point_circle_tangent_line(A, c)` is of the Line type.

The reason this object is given a name (in the case of `point_circle_tangent_line`, it is called `l`), is so it can be called in the
[`conclude`](#configuration-constructions-conclude) and [`possible_conclusions`](#configuration-constructions-possible-conclusions) sections.

#### <span id="configuration-constructions-conclude"> `conclude` </span>

This section lists predicates that can be immediately derived from the existence of this construction.
Whenever a construction is declared, all the predicates are assumed to be true.

For example, consider the construction `incenter`:
```yml
incenter:
  inputs:
    - A, B, C: Point
  ...
  construct:
    - P: Point
  conclude:
    - P in internal_angle_bisector(A, B, C), internal_angle_bisector(A, C, B), internal_angle_bisector(C, A, B)
    - P == line_intersection(internal_angle_bisector(A, B, C), internal_angle_bisector(A, C, B))
```

Inside the predicates listed in the `conclude` block, the name `P` references the result of the construction `incenter(A, B, C)`.
So for example, given three points `X, Y, Z`, creating the object `incenter(X, Y, Z)` in a geometry problem statement or proof will automatically make the system assume the predicate `incenter(X, Y, Z) in internal_angle_bisector(X, Y, Z)`.

#### <span id="configuration-constructions-possible-conclusions"> `possible_conclusions` </span>

Much like the `conclude` section, this section lists predicates that can be immediately derived from the existence of this construction.
The difference is that the predicates in this section are conditioned.
I.e., they are only derived, if another additional predicate is satisfied.

For example, consider the construction `projection`:
```yml
projection:
  inputs:
    - P: Point
    - l: Line
  construct:
    - Q: Point
  ...
  possible_conclusions:
    - P not in l => perpendicular_line(P, l) == Line(P, Q)
    - P in l => P == Q
```

Each item in the `possible_conclusions` block follows [predicate implication](#syntax-implications) syntax,
but they may only use the `=>` form of implications.

Given a point `A` and a line `f`, creating the object `projection(A, f)` will not automatically create the predicate `A == projection(A, f)`.
(Which it shouldn't, of course. That would be a false conclusion.)
But if the predicate `A in f` is known, then `A == projection(A, f)` will be immediately assumed.

Note that in the example above **all** of the predicates on the right-hand side of the `=>` operator contain `Q`, as these are supposed to be predicates **about** the object `Q`
(which was declared in the `construct` section).
On the other hand, **none** of the predicates on the left-hand side of the `=>` operator contain `Q`, as these are supposed to be predicates that it makes sense
to speak of **before** the object `projection(P, l)` is defined.
In the grammar of the langauge it is legitimate to have predicates on the left-hand side that contain `Q`, or predicates on the right-hand side that do not contain `Q`,
but this would be bad practice and is not recommended.

### <span id="configuration-predicates"> Predicates </span>

Before reading this section, it is recommended to be acquainted more or less with the grammar on how to [use predicates](#syntax-predicates).

The definitions of all predicates can be found in this [file](rules/constructions_and_predicates/predicates_database.yml).
Each  `.yml` mapping in the top-level of the file represents a different predicate.
The definition of each predicate includes a few sections.
The general shape of a predicate may look more or less as follows:

```yml
predicate:
  inputs:
    ...
  preprocess: ...
  conclude:
    ...
```

The word `predicate` is replaced with the name of the predicate.
The sections `inputs` and `conclude` are required, while `preprocess` is optional and may be completely omitted.
For example, the following construction `trapezoid` is defined as follows:
```yml
trapezoid:
  inputs:
    - A, B, C, D: Point
  preprocess: pi_rotate
  conclude:
    - convex(A, B, C, D)
    - parallel(Line(A, B), Line(C, D))
```


#### <span id="configuration-predicates-inputs"> `inputs` </span>

The `inputs` section is declared precisely in the same way as [the same section in the construction configuration file](#configuration-constructions-inputs):
The parameters are declared using the [object declaration](#syntax-declarations) syntax,
and read from left-to-right and top-to-bottom.

#### <span id="configuration-predicates-preprocess"> `preprocess` </span>

The `preprocess` section has the same values and meanings as [the same section in the construction configuration file](#configuration-constructions-preprocess).

#### <span id="configuration-predicates-conclude"> `conclude` </span>

The `conclude` section contains a list of predicates that work in [the same way as the corresponding section in the construction configuration file](#configuration-constructions-conclude),
except for one crucial difference:

Sometimes, the `conclude` section will also contain an item called `self`.
Two examples for this behavior is in the definitions of the `concyclic` and `collinear_and_not_between` predicates:

```yml
concyclic:
  inputs:
    - A, B, C, D: Point
  preprocess: symmetric
  conclude:
    - self
```

```yml
collinear_and_not_between:
  inputs:
  - A, B, C: Point
  preprocess: between 
  conclude:
    - self
    - collinear(A, B, C)
```

The reason for these items is due to the following feature:

> The predicates in the `conclude` section of a predicate definition,
> are assumed to be **necessary and sufficient** conditions for the predicate.

I.e., if all items in the `conclude` section of a predicate have been proved, our system will conclude that the predicate itself is true.
This is useful at times, when a predicate is not interesting in itself, but is more of a sort of "macro" that combines other predicates
(such as the `trapezoid` example above).
Other predicates, such as `concyclic`, are sort of atomic, and cannot *really* be described by a simpler set of predicates.
The `self` predicate, in a sense, adds the predicate itself to the list of necessary and sufficient conditions for the predicate.
It's a bit of a funny way of saying this, but the point is that predicates that have the `self` item in their `conclude` section,
will never be automatically assumed given other predicates.

### <span id="configuration-theorems"> Theorems </span>

The definitions of all theorems can be found under this [directory](rules/theorems).
The theorems are organized in a tree of directories, each containing `.yml` files.
Any `.yml` file anywhere under the [rules/theorems] directory will be parsed into a list of theorems.

Each  `.yml` mapping in the top-level of each file represents a different theorem, that can be used in a [proof](#syntax-proof).
The definition of each theorem includes a few sections.
The general shape of a theorem may look more or less as follows:

```yml
theorem:
  inputs:
    ...
  where:
    ...
  where_embedding:
    ...
  conclude:
    ...
  possible_conclusions:
    ...
  rank: ...
  trivial_if_equal: ...
  metadata: ...
```

The word `theorem` is replaced with the name of the theorem.
The sections `inputs` and `where` are required.
The rest of the sections are optional, although if neither the `conclude` nor the `possible_conlcusions` sections exist,
the theorem will be meaningless.

For example, the theorem `radical_axis_is_perpendicular_to_center_line` is defined as follows:
```yml
radical_axis_is_perpendicular_to_center_line:
  inputs:
    - l: Line
    - c, d: Circle
  where:
    - l == radical_axis(c, d)
    - exists(Line(center(c), center(d)))
  conclude:
    - perpendicular(Line(center(c), center(d)), l)
  rank: 5
```

This is the theorem that states:
> Given two circles and their radical axis line,
> The radical axis is perpendicular to the line connecting the centers of the circles.

This theorem can be found in this [file](rules/theorems/circles/radical_axis.yml), together with other theorems about radical axes.

#### <span id="configuration-theorems-inputs"> `inputs` </span>

The `inputs` section is declared precisely in the same way as [the same section in the construction configuration file](#configuration-constructions-inputs):
The parameters are declared using the [object declaration](#syntax-declarations) syntax,
and read from left-to-right and top-to-bottom.

#### <span id="configuration-theorems-where"> `where` </span>

The `where` section is declared precisely in the same way as [the same section in the construction configuration file](#configuration-constructions-where).
This describes the predicates that must be proved for it to be allowed to apply the theorem as a step in a proof.

#### <span id="configuration-theorems-where-embedding"> `where_embedding` </span>

The `where_embedding` section is declared precisely in the same way as the `where` section.
It also describes predicates that must be true for the theorem to be applied,
but instead of requiring that the predicates be proved, it is only required that the predicates are true.

This is saved for predicates that are inequalities, such as "The point A is on the left side of the line BC".
These are predicates that we allow to be checked numerically in an embedding, while still considering it a valid proof.

For example, a `where_embedding` predicate might require that a set of objects are distinct:

```yml
concyclic_definition_0:
  inputs:
    - A, B, C, D: Point
  where:
    - concyclic(A, B, C, D)
  where_embedding:
    - distinct(A, B, C)
  conclude:
    - D in Circle(A, B, C)
  ...
```
Here, it is required that `A`, `B`, and `C` are distinct points, because otherwise the object `Circle(A, B, C)` would not be defined.

#### <span id="configuration-theorems-conclude"> `conclude` </span>

The `conclude` section is declared precisely in the same way as [the same section in the construction configuration file](#configuration-constructions-conclude).
These are the predicates that can be deduced, whenever the theorem is applied.

#### <span id="configuration-theorems-possible-conclusions"> `possible_conclusions` </span>

The `possible_conclusions` section is declared precisely in the same way as [the same section in the construction configuration file](#configuration-constructions-possible-conclusions).

For example, consider the theorem `tangent_chord_angle`, which speaks of the angle between a line tangent to a circle, and a chord with an endpoint on the point of tangency:

```yml
tangent_chord_angle:
  inputs:
    - A, B, C, D: Point
  ...
  possible_conclusions:
    - angle(B, C, A) == angle(B, A, D) mod 360 => tangent(Line(A, D), Circle(A, B, C))
    - angle(B, C, A) == angle(B, A, D) + 180 mod 360 => tangent(Line(A, D), Circle(A, B, C))
```

This theorem is essentially two theorems packed in one:
If `angle(B, C, A) == angle(B, A, D) mod 360`, one can conclude some predicate,
and if `angle(B, C, A) == angle(B, A, D) + 180 mod 360`, then one concludes a different predicate.

Because the inputs to the theorems and some of the conditions in order to apply the theorem are similar,
it is comfortable to use both of them under the same theorem name.

<span id="giving-theorems-names-given-possible-conclusions"> </span>

The way these are used in a proof, is that the theorem is not called by its name (`tangent_chord_angle`),
but rather by its name, and appended to it, is the index of the relevant possible conclusion in the list.

I.e., if we apply the first item in the list, we use a theorem called `tangent_chord_angle_v0`.
If we apply the second item in the list, we use a theorem called `tangent_chord_angle_v1`.

Unlike the [`possible_conclusions`](#configuration-constructions-possible-conclusions) section for constructions,
it is allowed to use all three sorts of implication symbols in this section: `=>`, `<=`, and `<=>`.

The `<=>` symbol is special, in the sense that it splits the theorem into **two** further theorems:
The one stating that the left hand side implies the right, and the one stating that the right hand side implies the left.

For example, consider the theorem `double_perpendicular_and_parallel`, which speaks of a triplet of lines that has two perpendicular pairs:

```yml
double_perpendicular_and_parallel:
  inputs:
    - k, l, m: Line
  where:
    - perpendicular(k, l)
  possible_conclusions:
    - perpendicular(l, m) <=> parallel(k, m)
  ...
```

In this case, in order to call the `=>` direction of the theorem, we will use a theorem named `double_perpendicular_and_parallel_v0_r`.
To call the `<=` direction, we will use a theorem named ``double_perpendicular_and_parallel_v0_l`.

The 0 index here refers to the fact that this is the item in index 0 in the list of possible conclusions
(just as was mentioned a [few paragraphs earlier](#giving-theorems-names-given-possible-conclusions)).

#### <span id="configuration-theorems-rank"> `rank` </span>
#### <span id="configuration-theorems-trivial-if-equal"> `trivial_if_equal` </span>
#### <span id="configuration-theorems-metadata"> `metadata` </span>

## <span id="problem-generator"> Generating Problems </span>
### <span id="problem-generator-introduction"> Introduction </span>
### <span id="problem-generator-capabilities"> Capabilities </span>
### <span id="problem-generator-introduction"> Usage </span>

## <span id="solver"> Solving Problems </span>
### <span id="solver-embedding"> Embedding a question </span>
### <span id="solver-proof-generation"> Generating a proof </span>
### <span id="solver-trimming"> Trimming proofs </span>
### <span id="solver-checking"> Checking + Validating a proof </span>
### <span id="solver-interacting"> Running an interactive terminal </span>
### <span id="solver-prettifying"> Prettifying </span>