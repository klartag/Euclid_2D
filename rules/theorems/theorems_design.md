# constructions
## option 1
If theorem contain construction in its conclusions then the proof generator regard it as a new object that was created. We don't want the proof-generator to be have to construct new object if it want to imply some theorm. We want to imply the theorem only If all objects in its conclusions are already exist in the proof. Hence We put all the object uses in the conclusion of the theorem as inputs objects. For example, If the theorm get point A, B, C
and say something about center(Circle(A, B, C)), we put new input point 'O' which will be center(Circle(A, B, C)) and therefore You can imply thid theorem only If O already exists.
* One drawback - We don't imply this method on the construction 'Line' since it occur many many times.
## option 2 <---- use this
Updated version - A theorem will have minimal set of inputs (don't have to be minimal - reasonable is better, for exaxmple in 'external_angle_bisector_intersect_circle' B' not have to be input but it's good that it is input), but the proof_generator should check if all the objects in the conclusions exist before implying a theorem.

# rank
0 - If we start applying these theorems, we've probably already lost.
1 - Concludes non-degenerecy of types `!=`
2 - Concludes an inequality of types `<` or `>` (such as `between` theorems)
3 - Definitions of objects, theorems that humans will not explicitly write, and theorems that humans will regard as trivial.
4 - Segment and angle chasing.
5 - Observations that are pretty much always useful
6 - Proper good theorems. If these can be applied, apply them at once!

# trivial_if_equal
## option 1 <---- use this
list all set of geometric objects that should not known to be equal apriori. For example, if there is a line:
- [[A, B, C], [A', B', C']] it means that this theorem is correct when (A, B, C) = (A', B', C') (pointwise) but is trivial in this case (or follows from another theorem*), hence in the proof generator we won't apply it on two tuples (A, B, C), (A', B', C') of objects that are known to be equal.
* for example: theorem angles_on_equi_size_chords for (A, B, C) = (C', B', A') is not trivial but it follows from isosceles_angles_segments
### NOT_TRUE_______
** I prefer to compare sets intead of point-wise comparison since its very rare (until now not found) a case where subpart of the event {A, B, C} == {A', B', C'} is not trivial or follows from other theorem. And if I will do point-wise comparison I will need to write all the equalities come from permutations.
___________________________
*** I prefer to compare pointwise istead of comparing sets since there is some cases which the (A, B, C) = (A', B', C') is trivial but some other permutation is not trivial. For example congruence_triangles_heights(A, B, C, A, C, B) have no trivial consequnces. A disadventage of this approuch is that if we want that {A, B, C} != {A', B', C'} we need to list all options of inequalty of tuples.
## option 2
The theorem itself should require distinctness from certain objects. In this option, the theorem could not be imply on trivial cases.
* technical problem - for now we don't have inequality of sets.
** conceptual problem - maybe it's not good that we ca't imply the theorem on trivial cases.
*** chaotic problem - some theorems have equality of objects as conclusion - If the two objects are equal in advance the theorem is trivial hance we won't imply it for objects that we know in advance to be equal. Hence we can't demant the objects to be different in the theorem requrments since this leads to contradiction.

# exists
we add exists as a requirment of theorem from one of the two reasons:
1) The theorem concstruct some construcion in its conclusions. We want the proof generator to impmly this theorems only if all the objects related to this theorem already exists - in order to prevent him from construct too many things.
2) If you want to prevent the proof_generator to imply this theorem too much, you add an exists predicate to object that the theorem not realy use but its only reasonable to imply this theorem if this object already exists. This is added to prevent the proof_generator to impmly this theorm too much since it's too easy to imply. Look for example on the exists in 'distance_nonzero'.


