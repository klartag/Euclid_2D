# Theorem format

## File format

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
```

All sections are optional.

The first section, `for`, details the names and types of the inputs.

The second section, `where`, details predicates on the inputs. Predicates can be names, in which case they are optional, and are used in the conclusion format.

The third section, `construct`, specifies which objects are constructed by the theorem.

The fourth section, `conclude`, specifies predicates on the results. Again, named predicates are not always used. In addition to unnamed predicates, which follow from the unnamed predicates before, named predicates do not immediately follow, but are used to construct additional flows of the theorem, as in the final line of the example.

The fifth section, `possible_conclusions`, specifies additional flows of the theorem, with more predicates being satisfied leading to more predicates being proved.



# Proof Format

A proof has three sections: the assumptions, the required predicates, and the proof body.

#### Assumptions

The assumptions start with the title:

```
Assumptions:
```

Followed by object definitions, such as:

```
A, B, C, D: Point
c: Circle
```

Followed by a list of predicates:

```
A in c
B in c
C in c
D in c
distance(A, B) == radius(c)
```

#### Need to prove

This sections starts with the section title (`Need to prove:`), followed again by object definitions and predicates.

Objects defined here must be defined by the proof.

#### Proof body

In the proof body, each line is a statement.

There are two types of statements:

* Theorem statements. These statements have the form:
  ```
  By theorem_name on A, B, C, we get X: Circle, Y: Line, Z: Point, predicate_name(A, B), predicate_name(C, D) 
  ```

* Let statements. These involve giving constructions names for clarity:
  ``` 
  let r = distance(A, B)
  let C := Circle(O, r)
  ```

