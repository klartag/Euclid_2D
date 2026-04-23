# Euclid 2D

### Table of Contents

| Section                                                                           | Description                                                                                                   |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [Introduction](#introduction)                                                     | What is this repository about?                                                                                |
| [Geometry Syntax](#syntax)                                                        | How to formulate a geometry problem or proof.                                                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Object Types](#syntax-object-types)                    | What are the different types of objects that can appear in a problem statement or proof.                      |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Literals](#syntax-literals)                            | How to describe scalars with values that are known ahead of time.                                             |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Constructions](#syntax-constructions)                  | How to use geometric objects to describe more geometric objects.                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Predicates](#syntax-predicates)                        | How to use geometric objects to describe predicates.                                                          |
| [Geometry Configuration Rules](#configuration)                                    | What are the rules that geometric objects abide to?                                                           |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Constructions](#configuration-constructions)           | How constructions are defined.                                                                                |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Predicates](#configuration-predicates)                 | How predicates are defined.                                                                                   |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Theorems](#configuration-theorems)                     | How theorems are defined.                                                                                     |
| [Geometry Document](#syntax-structure)                                            | All about the file format in which we save geometry problem statements and proofs.                            |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Assumptions](#syntax-assumptions)                      | The section containing the given predicates in the problem.                                                   |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Embedding](#syntax-embedding)                          | The section containing a coordinate embedding of geometry objects.                                            |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Need to prove](#syntax-need-to-prove)                  | The section containing the predicates that need to be proved.                                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Proof](#syntax-proof)                                  | The section containing the proof.                                                                             |
| [Generating Problems](#problem-generator)                                         | How to generate geometry problems (just their statements, without proof).                                     |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Introduction](#problem-generator-introduction)         | What is this module about?                                                                                    |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Capabilities](#problem-generator-capabilities)         | What can we do with it?                                                                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Usage](#problem-generator-introduction)                | How do we use it?                                                                                             |
| [Solving Problems](#solver)                                                       | How to solve geometry problems                                                                                |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Embedding a question](#solver-embedding)               | How to take a geometry problem and embed it in 2D space.                                                      |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Generating a proof](#solver-proof-generation)          | How to take a geometry problem and generate a proof.                                                          |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Trimming proofs](#solver-trimming)                     | How to shorten a proof until its length is locally optimal.                                                   |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Checking + Validating a proof](#solver-checking)       | How to make sure a written proof is correct.                                                                  |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Running an interactive terminal](#solver-interacting)  | How to evaluate expressions and predicates in a geometry problem (possibly with a partially-written proof).   |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Prettifying](#solver-prettifying)                      | How to make a proof easier to read by humans.                                                                 |

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
The format in which that file is written is described [further down in this document](#configuration-constructions).

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
The format in which that file is written is described [further down in this document](#configuration-predicates).

The rest of the predicates (the more unusual ones) are defined inside this [directory](rules/predicates/implementations).

## <span id="configuration"> Geometry Configuration Rules </span>
### <span id="configuration-constructions"> Constructions </span>
### <span id="configuration-predicates"> Predicates </span>
### <span id="configuration-theorems"> Theorems </span>

## <span id="syntax-structure"> Geometry Document </span>
### <span id="syntax-assumptions"> Assumptions </span>
### <span id="syntax-embedding"> Embedding </span>
### <span id="syntax-need-to-prove"> Need to prove </span>
### <span id="syntax-proof"> Proof </span>

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