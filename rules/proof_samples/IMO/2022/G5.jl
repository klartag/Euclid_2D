Assumptions:

#objects
A, B, C, X_1, X_2, Y_1, Y_2, Z_1, Z_2, D_1, D_2, E_1, E_2, F_1, F_2: Point
l_1, l_2, l_X_1, l_X_2, l_Y_1, l_Y_2, l_Z_1, l_Z_2: Line

#assumptions
distinct(A, B, C, X_1, X_2, Y_1, Y_2, Z_1, Z_2, D_1, D_2, E_1, E_2, F_1, F_2)
triangle(A, B, C)
parallel(l_1, l_2)
l_1 != l_2

X_1 == line_intersection(Line(B, C), l_1)
X_2 == line_intersection(Line(B, C), l_2)
Y_1 == line_intersection(Line(A, C), l_1)
Y_2 == line_intersection(Line(A, C), l_2)
Z_1 == line_intersection(Line(A, B), l_1)
Z_2 == line_intersection(Line(A, B), l_2)

l_X_1 == perpendicular_line(X_1, Line(B, C))
l_X_2 == perpendicular_line(X_2, Line(B, C))
l_Y_1 == perpendicular_line(Y_1, Line(A, C))
l_Y_2 == perpendicular_line(Y_2, Line(A, C))
l_Z_1 == perpendicular_line(Z_1, Line(A, B))
l_Z_2 == perpendicular_line(Z_2, Line(A, B))

D_1 == line_intersection(l_Y_1, l_Z_1)
D_2 == line_intersection(l_Y_2, l_Z_2)
E_1 == line_intersection(l_X_1, l_Z_1)
E_2 == line_intersection(l_X_2, l_Z_2)
F_1 == line_intersection(l_X_1, l_Y_1)
F_2 == line_intersection(l_X_2, l_Y_2)

triangle(D_1, E_1, F_1)
triangle(D_2, E_2, F_2)

# lines are not perpendicular or parallel without reason
line_angle(l_1) - line_angle(Line(A, B)) != 0 mod 180
line_angle(l_1) - line_angle(Line(A, B)) != 90 mod 180
line_angle(l_2) - line_angle(Line(A, B)) != 0 mod 180
line_angle(l_2) - line_angle(Line(A, B)) != 90 mod 180
line_angle(l_1) - line_angle(Line(C, B)) != 0 mod 180
line_angle(l_1) - line_angle(Line(C, B)) != 90 mod 180
line_angle(l_2) - line_angle(Line(C, B)) != 0 mod 180
line_angle(l_2) - line_angle(Line(C, B)) != 90 mod 180
line_angle(l_1) - line_angle(Line(C, A)) != 0 mod 180
line_angle(l_1) - line_angle(Line(C, A)) != 90 mod 180
line_angle(l_2) - line_angle(Line(C, A)) != 0 mod 180
line_angle(l_2) - line_angle(Line(C, A)) != 90 mod 180

# Unchecked. This was proved later, so I assume this is correct.
distinct(Line(Z_1, Z_2), Line(Y_1, Y_2), Line(D_1, D_2))
distinct(Line(Z_1, Z_2), Line(X_1, X_2), Line(E_1, E_2))
distinct(Line(X_1, X_2), Line(Y_1, Y_2), Line(F_1, F_2))
distinct(Line(E_1, E_2), Line(F_1, F_2), Line(D_1, D_2))

Need to prove:
tangent(Circle(D_1, E_1, F_1), Circle(D_2, E_2, F_2))

Proof:
Let w_1 := Circle(D_1, E_1, F_1)
Let w_2 := Circle(D_2, E_2, F_2)


#############################################   proof that lot of things are triangles #####################################
# show that D_1Y_1Z_1 is a triangle
By Line_definition on Y_1, Z_1, l_1 we get l_1 == Line(Y_1, Z_1) 
By Line_definition on Y_1, D_1, l_Y_1 we get l_Y_1 == Line(Y_1, D_1)
By triangle_sufficient_conditions_v1 on Y_1, D_1, Z_1 we get triangle(Y_1, D_1, Z_1)

By Line_definition on Y_2, Z_2, l_2 we get l_2 == Line(Y_2, Z_2)
By Line_definition on Y_2, D_2, l_Y_2 we get l_Y_2 == Line(Y_2, D_2)
By triangle_sufficient_conditions_v1 on Y_2, D_2, Z_2 we get triangle(Y_2, D_2, Z_2)

# show that E_1X_1Z_1 is a triangle
By Line_definition on X_1, Z_1, l_1 we get l_1 == Line(X_1, Z_1)
By Line_definition on X_1, E_1, l_X_1 we get l_X_1 == Line(X_1, E_1)
By triangle_sufficient_conditions_v1 on X_1, E_1, Z_1 we get triangle(X_1, E_1, Z_1)

# show that E_2X_2Z_2 is a triangle
By Line_definition on X_2, Z_2, l_2 we get l_2 == Line(X_2, Z_2)
By Line_definition on X_2, E_2, l_X_2 we get l_X_2 == Line(X_2, E_2)
By triangle_sufficient_conditions_v1 on X_2, E_2, Z_2 we get triangle(X_2, E_2, Z_2)

# show that F_1X_1Y_1 is a triangle
By Line_definition on X_1, Y_1, l_1 we get l_1 == Line(X_1, Y_1)
By Line_definition on X_1, F_1, l_X_1 we get l_X_1 == Line(X_1, F_1)
By triangle_sufficient_conditions_v1 on X_1, F_1, Y_1 we get triangle(X_1, F_1, Y_1)

# show that F_2X_2Y_2 is a triangle
By Line_definition on X_2, Y_2, l_2 we get l_2 == Line(X_2, Y_2)
By Line_definition on X_2, F_2, l_X_2 we get l_X_2 == Line(X_2, F_2)
By triangle_sufficient_conditions_v1 on X_2, F_2, Y_2 we get triangle(X_2, F_2, Y_2)

#####################################  Homothety theorem 3 times   ########################################

We have proved parallel(Line(Y_1, Z_1), Line(Y_2, Z_2))
By Line_definition on Z_1, D_1, l_Z_1 we get l_Z_1 == Line(Z_1, D_1)
By Line_definition on Z_2, D_2, l_Z_2 we get l_Z_2 == Line(Z_2, D_2)
We have proved parallel(Line(D_1, Z_1), Line(D_2, Z_2))
By Line_definition on Y_1, D_1, l_Y_1 we get l_Y_1 == Line(Y_1, D_1)
By Line_definition on Y_2, D_2, l_Y_2 we get l_Y_2 == Line(Y_2, D_2)
We have proved parallel(Line(D_1, Y_1), Line(D_2, Y_2))
By Line_definition on Y_1, Y_2, Line(A, C) we get Line(A, C) == Line(Y_1, Y_2)
By Line_definition on Z_1, Z_2, Line(A, B) we get Line(A, B) == Line(Z_1, Z_2)
By homothety_six_points_v1 on Z_1, Y_1, D_1, Z_2, Y_2, D_2 we get concurrent(Line(Z_1, Z_2), Line(Y_1, Y_2), Line(D_1, D_2))
We have proved A in Line(D_1, D_2)
#############################
We have proved parallel(Line(X_1, Z_1), Line(X_2, Z_2))
By Line_definition on Z_1, E_1, l_Z_1 we get l_Z_1 == Line(Z_1, E_1)
By Line_definition on Z_2, E_2, l_Z_2 we get l_Z_2 == Line(Z_2, E_2)
We have proved parallel(Line(E_1, Z_1), Line(E_2, Z_2))
By Line_definition on X_1, E_1, l_X_1 we get l_X_1 == Line(X_1, E_1)
By Line_definition on X_2, E_2, l_X_2 we get l_X_2 == Line(X_2, E_2)
We have proved parallel(Line(E_1, X_1), Line(E_2, X_2))
By Line_definition on X_1, X_2, Line(B, C) we get Line(B, C) == Line(X_1, X_2)
By Line_definition on Z_1, Z_2, Line(A, B) we get Line(A, B) == Line(Z_1, Z_2)
We have proved line_angle(Line(A, B)) != line_angle(Line(B, C)) mod 180
By homothety_six_points_v1 on Z_1, X_1, E_1, Z_2, X_2, E_2 we get concurrent(Line(Z_1, Z_2), Line(X_1, X_2), Line(E_1, E_2))
We have proved B in Line(E_1, E_2)
#############################
We have proved parallel(Line(Y_1, X_1), Line(Y_2, X_2))
By Line_definition on X_1, F_1, l_X_1 we get l_X_1 == Line(X_1, F_1)
By Line_definition on X_2, F_2, l_X_2 we get l_X_2 == Line(X_2, F_2)
We have proved parallel(Line(F_1, X_1), Line(F_2, X_2))
By Line_definition on Y_1, F_1, l_Y_1 we get l_Y_1 == Line(Y_1, F_1)
By Line_definition on Y_2, F_2, l_Y_2 we get l_Y_2 == Line(Y_2, F_2)
We have proved parallel(Line(F_1, Y_1), Line(F_2, Y_2))
By Line_definition on Y_1, Y_2, Line(A, C) we get Line(A, C) == Line(Y_1, Y_2)
By Line_definition on X_1, X_2, Line(C, B) we get Line(C, B) == Line(X_1, X_2)
By homothety_six_points_v1 on X_1, Y_1, F_1, X_2, Y_2, F_2 we get concurrent(Line(X_1, X_2), Line(Y_1, Y_2), Line(F_1, F_2))
We have proved C in Line(F_1, F_2)

########################## Homothety for E_iD_iF_i #####################################
By Line_definition on E_1, D_1, l_Z_1 we get l_Z_1 == Line(D_1, E_1)
By Line_definition on E_2, D_2, l_Z_2 we get l_Z_2 == Line(D_2, E_2)
We have proved parallel(Line(E_1, D_1), Line(E_2, D_2))
By Line_definition on E_1, F_1, l_X_1 we get l_X_1 == Line(F_1, E_1)
By Line_definition on E_2, F_2, l_X_2 we get l_X_2 == Line(F_2, E_2)
We have proved parallel(Line(E_1, F_1), Line(E_2, F_2))
By Line_definition on F_1, D_1, l_Y_1 we get l_Y_1 == Line(D_1, F_1)
By Line_definition on F_2, D_2, l_Y_2 we get l_Y_2 == Line(D_2, F_2)
We have proved parallel(Line(F_1, D_1), Line(F_2, D_2))
# angle computation
## b, x_2, E_2, Z_2 are concyclic

By Line_definition on E_2, Z_2, l_Z_2 we get l_Z_2 == Line(E_2, Z_2)
By Line_definition on B, Z_2, Line(A, B) we get Line(A, B) == Line(B, Z_2)
By Line_definition on B, X_2, Line(C, B) we get Line(C, B) == Line(B, X_2)
By Line_definition on X_2, E_2, l_X_2 we get l_X_2 == Line(X_2, E_2)
We have proved angle(B, Z_2, E_2) + angle(E_2, X_2, B) == 0 mod 180
By triangle_sufficient_conditions_v1 on Z_2, E_2, B we get triangle(Z_2, E_2, B)
By four_points_concyclic_sufficient_conditions_v0 on B, Z_2, E_2, X_2 we get concyclic(B, Z_2, E_2, X_2)
# TODO: The following line should not be needed, since `exists` on that circle should automatically apply when proving `concyclic`
We introduce Circle(X_2, E_2, Z_2)


By Line_definition on F_2, Y_2, l_Y_2 we get l_Y_2 == Line(Y_2, F_2)
By Line_definition on C, Y_2, Line(A, C) we get Line(A, C) == Line(Y_2, C)
We have proved angle(C, Y_2, F_2) == 90 mod 180

By Line_definition on F_2, X_2, l_X_2 we get l_X_2 == Line(X_2, F_2)
By Line_definition on C, X_2, Line(B, C) we get Line(B, C) == Line(X_2, C)
We have proved angle(C, X_2, F_2) == 90 mod 180
By triangle_sufficient_conditions_v1 on Y_2, F_2, C we get triangle(Y_2, F_2, C )
By four_points_concyclic_sufficient_conditions_v0 on C, Y_2, F_2, X_2 we get concyclic(C, Y_2, F_2, X_2)
# TODO: The following line should not be needed, since `exists` on that circle should automatically apply when proving `concyclic`
We introduce Circle(X_2, F_2, Y_2)

By angles_on_chord on E_2, X_2, Z_2, B, Circle(E_2, X_2 ,Z_2) we get angle(E_2, Z_2, X_2) == angle(E_2, B, X_2) mod 180
By angles_on_chord on F_2, X_2, Y_2, C, Circle(F_2, X_2, Y_2) we get angle(F_2, Y_2, X_2) == angle(F_2, C, X_2) mod 180

We have proved line_angle(Line(F_1, F_2)) - line_angle(Line(E_1, E_2)) == line_angle(Line(X_1, X_2)) - line_angle(Line(E_1, E_2)) +  line_angle(Line(F_1, F_2)) - line_angle(Line(X_1, X_2))
By Line_definition on B, E_2, Line(E_1, E_2) we get  Line(E_1, E_2) == Line(B, E_2)
We have proved Line(B, X_2) == Line(X_1, X_2)
We have proved angle(E_2, B, X_2) == line_angle(Line(X_1, X_2)) - line_angle(Line(E_1, E_2)) mod 180
By Line_definition on C, F_2, Line(F_1, F_2) we get  Line(F_1, F_2) == Line(C, F_2)
We have proved Line(C, X_2) == Line(X_1, X_2)
We have proved angle(X_2, C, F_2) == line_angle(Line(F_1, F_2)) - line_angle(Line(X_1, X_2)) mod 180
We have proved line_angle(Line(F_1, F_2)) - line_angle(Line(E_1, E_2)) == angle(X_2, Y_2, F_2) + angle(E_2, Z_2, X_2) mod 180
We have proved l_2 == Line(Z_2, X_2)
We have proved l_2 == Line(Z_2, Y_2)
We have proved line_angle(Line(F_1, F_2)) - line_angle(Line(E_1, E_2)) == line_angle(Line(A, C)) - line_angle(Line(A, B)) mod 180
We have proved line_angle(Line(F_1, F_2)) - line_angle(Line(E_1, E_2)) != 0 mod 180

#################################################################################

By homothety_six_points_v1 on F_1, E_1, D_1, F_2, E_2, D_2 we get concurrent(Line(E_1, E_2), Line(F_1, F_2), Line(D_1, D_2)), not_one_of(line_intersection(Line(E_1, E_2), Line(F_1, F_2)), F_1, E_1, D_1, F_2, E_2, D_2)#line_intersection(Line(E_1, E_2), Line(F_1, F_2)) != E_1, line_intersection(Line(E_1, E_2), Line(F_1, F_2)) != E_2, line_intersection(Line(E_1, E_2), Line(F_1, F_2)) != F_1, line_intersection(Line(E_1, E_2), Line(F_1, F_2)) != F_2
Let H := line_intersection(Line(E_1, E_2), Line(F_1, F_2))

###### show that A, Y_i, D_i, Z_i are concyclic
We have proved l_Y_1 == Line(Y_1, D_1)
By Line_definition on Y_1, A, Line(A, C) we get Line(A, C) == Line(A, Y_1)
We have proved Line(A, C) == Line(Y_1, A)

We have proved angle(A, Y_1, D_1) == 90 mod 180
By Line_definition on Z_1, A, Line(A, B) we get Line(A, B) == Line(A, Z_1)
We have proved Line(A, B) == Line(A, Z_1)
We have proved angle(D_1, Z_1, A) == 90 mod 180
By triangle_sufficient_conditions_v1 on Y_1, A, D_1 we get triangle(A, Y_1, D_1)
By four_points_concyclic_sufficient_conditions_v0 on A, Y_1, D_1, Z_1 we get concyclic(A, Y_1, D_1, Z_1)

We have proved l_Y_2 == Line(Y_2, D_2)
By Line_definition on Y_2, A, Line(A, C) we get Line(A, C) == Line(A, Y_2)
We have proved Line(A, C) == Line(Y_2, A)
We have proved angle(A, Y_2, D_2) == 90 mod 180
By Line_definition on Z_2, A, Line(A, B) we get Line(A, B) == Line(A, Z_2)
We have proved Line(A, B) == Line(A, Z_2)
We have proved angle(D_2, Z_2, A) == 90 mod 180
By triangle_sufficient_conditions_v1 on Y_2, A, D_2 we get triangle(A, Y_2, D_2)
By four_points_concyclic_sufficient_conditions_v0 on A, Y_2, D_2, Z_2 we get concyclic(A, Y_2, D_2, Z_2)

################### angle computing #############
By Line_definition on H, E_1, Line(E_1, E_2) we get Line(E_1, E_2) == Line(H, E_1)
We have proved Line(H, E_1) == Line(E_1, E_2)
By Line_definition on H, F_1, Line(F_1, F_2) we get Line(F_1, F_2) == Line(H, F_1)
We have proved Line(H, F_1) == Line(F_1, F_2)

We have proved line_angle(Line(F_1, H)) - line_angle(Line(E_1, H)) == line_angle(Line(F_1, F_2)) - line_angle(Line(E_1, E_2))
We have proved line_angle(Line(F_1, H)) - line_angle(Line(E_1, H)) == line_angle(Line(A, C)) - line_angle(Line(A, B)) mod 180
We have proved line_angle(Line(F_1, H)) - line_angle(Line(E_1, H)) == line_angle(Line(A, Y_1)) - line_angle(Line(A, Z_1)) mod 180
We have proved line_angle(Line(F_1, H)) - line_angle(Line(E_1, H)) == line_angle(Line(D_1, Y_1)) - line_angle(Line(D_1, Z_1)) mod 180
We have proved line_angle(Line(F_1, H)) - line_angle(Line(E_1, H)) == line_angle(Line(D_1, F_1)) - line_angle(Line(D_1, E_1)) mod 180
By triangle_sufficient_conditions_v1 on H, E_1, F_1 we get triangle(H, E_1, F_1)
It is almost always true that distinct(H, D_1, E_1, F_1)
By four_points_concyclic_sufficient_conditions_v0 F_1, H, E_1, D_1 we get concyclic(F_1, H, E_1, D_1)
###################
By Line_definition on H, E_2, Line(E_1, E_2) we get Line(E_1, E_2) == Line(H, E_2)
We have proved Line(H, E_2) == Line(E_1, E_2)
By Line_definition on H, F_2, Line(F_1, F_2) we get Line(F_1, F_2) == Line(H, F_2)
We have proved Line(H, F_2) == Line(F_1, F_2)

We have proved line_angle(Line(F_2, H)) - line_angle(Line(E_2, H)) == line_angle(Line(F_1, F_2)) - line_angle(Line(E_1, E_2))
We have proved line_angle(Line(F_2, H)) - line_angle(Line(E_2, H)) == line_angle(Line(A, C)) - line_angle(Line(A, B)) mod 180
We have proved line_angle(Line(F_2, H)) - line_angle(Line(E_2, H)) == line_angle(Line(A, Y_2)) - line_angle(Line(A, Z_2)) mod 180
We have proved line_angle(Line(F_2, H)) - line_angle(Line(E_2, H)) == line_angle(Line(D_2, Y_2)) - line_angle(Line(D_2, Z_2)) mod 180
We have proved line_angle(Line(F_2, H)) - line_angle(Line(E_2, H)) == line_angle(Line(D_2, F_2)) - line_angle(Line(D_2, E_2)) mod 180
By triangle_sufficient_conditions_v1 on H, E_2, F_2 we get triangle(H, E_2, F_2)
It is almost always true that distinct(H, D_2, E_2, F_2)
By four_points_concyclic_sufficient_conditions_v0 F_2, H, E_2, D_2 we get concyclic(F_2, H, E_2, D_2)
####################################################################################
By homothety_six_points_v2 on D_1, E_1, F_1, D_2, E_2, F_2 we get tangent(Circle(D_1, E_1, F_1), Circle(D_2, E_2, F_2))
#We have proved H in w_1