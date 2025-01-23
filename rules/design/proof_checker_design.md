# Objects



The code has several components:

## GeoObject

The class containing the base objects we are manipulating.

### GeoObject

The base class. Represents a geometric object, with a type and a name.

### ConstructionObject

Represents an object that isn't independent, but constructed of some other object, like `angle(A, B, C)`. The whole thing is an object of type `Angle`, but contains references to the objects `A`, `B`, and `C`. This is necessary since we sometimes want to substitute objects with other objects, such as when applying theorems and merging objects.

### EquationObject

Tracks an equation in some variables, and so contains components as a set of the components and their values. The components should be a `frozendict`, but python doesn't have one, so I use `frozenset[tuple[GeoObject, float]]` instead.

## Predicate

## Proof

## Theorem

## Linear Algebra Tracker



# The Equality System

### Object merging

When merging objects, we maintain:

1. Each equivalence class has a minimal canonical component.
2. For each construction object, the object we get by substituting all its components to their canonical representative exists and is equivalent.

Thus, we have a queue of merged objects. When we merge, we have an object which we have merged. When merging an object, we violate property 2 of all objects containing it, so we have to iterate over them and merge them as well.

### Predicate merging
