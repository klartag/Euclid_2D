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

#### Binary operators

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