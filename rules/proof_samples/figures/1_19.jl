Assumptions:
A, B, C, D, X, Y, Z, W: Point
distinct(A, B, C, D, W, X, Y, Z)
distinct(Line(W, X), Line(W, Z), Line(X, Y), Line(Y, Z))
not_collinear(A, B, C)
not_collinear(A, B, D)
not_collinear(A, C, D)
not_collinear(B, C, D)
X == midpoint(A, B)
Y == midpoint(B, C)
Z == midpoint(C, D)
W == midpoint(A, D)

Embedding:
D := {"x": "0.992679405274923709612266975454986095428466796875", "y": "0.1207791304117714348276280134086846373975276947021484375"}
A := {"x": "0.18139907494650697739047018330893479287624359130859375", "y": "-0.98340956656346978359550803361344151198863983154296875"}
W := {"x": "0.587039240110715343501368579381960444152355194091796875", "y": "-0.43131521807584917438394001010237843729555606842041015625"}
C := {"x": "-0.759695379808827286893802011036314070224761962890625", "y": "0.65027911691605300159579883256810717284679412841796875"}
Z := {"x": "0.1164920127330482113592324822093360126018524169921875", "y": "0.38552912366391221821171342298839590512216091156005859375"}
B := {"x": "0.2102788452502812877042970285401679575443267822265625", "y": "-0.9776414512694355796185163853806443512439727783203125"}
Y := {"x": "-0.27470826727927299959475249124807305634021759033203125", "y": "-0.163681167176691289011358776406268589198589324951171875"}
X := {"x": "0.195838960098394132547383605924551375210285186767578125", "y": "-0.980525508916452681607012209497042931616306304931640625"}

Need to prove:
parallelogram(W, X, Y, Z)

Proof:
By log_of_2_times_distance on D, A, A, W we get log(distance(A, D)) == log(2) + log(distance(A, W))
By log_of_2_times_distance on B, C, Y, B we get log(distance(B, C)) == log(2) + log(distance(B, Y))
By log_of_2_times_distance on D, A, W, D we get log(distance(A, D)) == log(2) + log(distance(D, W))
By log_of_2_times_distance on D, C, D, Z we get log(distance(C, D)) == log(2) + log(distance(D, Z))
By log_of_2_times_distance on B, A, X, A we get log(distance(A, B)) == log(2) + log(distance(A, X))
By log_of_2_times_distance on D, C, C, Z we get log(distance(C, D)) == log(2) + log(distance(C, Z))
By log_of_2_times_distance on B, C, Y, C we get log(distance(B, C)) == log(2) + log(distance(C, Y))
By log_of_2_times_distance on A, B, X, B we get log(distance(A, B)) == log(2) + log(distance(B, X))
By between_implies_angles on A, X, B we get 180 == angle(A, X, B) mod 360, 0 == angle(X, B, A) mod 360, 0 == angle(B, A, X) mod 360
By between_implies_angles on C, Z, D we get 180 == angle(C, Z, D) mod 360, 0 == angle(Z, D, C) mod 360, 0 == angle(D, C, Z) mod 360
By between_implies_angles on D, W, A we get 180 == angle(D, W, A) mod 360, 0 == angle(W, A, D) mod 360, 0 == angle(A, D, W) mod 360
By between_implies_angles on B, Y, C we get 180 == angle(B, Y, C) mod 360, 0 == angle(Y, C, B) mod 360, 0 == angle(C, B, Y) mod 360
By sas_similarity on B, C, D, Y, C, Z we get similar_triangles(B, C, D, Y, C, Z)
By sas_similarity on W, A, X, D, A, B we get similar_triangles(A, B, D, A, X, W)
By sas_similarity on A, D, C, W, D, Z we get similar_triangles(A, C, D, W, Z, D)
By sas_similarity on Y, B, X, C, B, A we get similar_triangles(A, B, C, X, B, Y)
By parallel_line_angles_v1 on Z, Y, B, D we get parallel(Line(B, D), Line(Y, Z))
By parallel_line_angles_v1 on W, X, B, D we get parallel(Line(B, D), Line(W, X))
By parallel_line_angles_v1 on Y, X, A, C we get parallel(Line(A, C), Line(X, Y))
By parallel_line_angles_v1 on C, A, W, Z we get parallel(Line(A, C), Line(W, Z))
By parallel_lines_are_transitive on Line(W, X), Line(B, D), Line(Y, Z) we get parallel(Line(W, X), Line(Y, Z))
By parallel_lines_are_transitive on Line(W, Z), Line(A, C), Line(X, Y) we get parallel(Line(W, Z), Line(X, Y))
By parallelogram_parallel_definition on W, X, Y, Z we get parallelogram(W, X, Y, Z)
