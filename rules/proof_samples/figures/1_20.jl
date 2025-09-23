Assumptions:
A, B, C, D, X, Y, Z, W, T: Point
distinct(A, B, C, D, T, W, X, Y, Z)
distinct(Line(W, X), Line(W, Z), Line(X, Y), Line(Y, Z))
not_collinear(A, B, C)
not_collinear(A, B, D)
not_collinear(A, C, D)
not_collinear(B, C, D)
X == midpoint(A, B)
Y == midpoint(B, C)
Z == midpoint(C, D)
W == midpoint(A, D)
T == line_intersection(Line(W, Y), Line(X, Z))

Embedding:
D := {"x": "0.483825097926760261390910500267636962234973907470703125", "y": "0.87516471284905039684787197984405793249607086181640625"}
A := {"x": "-0.90702353831911619597150320259970612823963165283203125", "y": "-0.4210799222654422191425283017451874911785125732421875"}
W := {"x": "-0.2115992201961779672902963511660345830023288726806640625", "y": "0.227042395291804088852671839049435220658779144287109375"}
C := {"x": "-0.96302908993719793517840344065916724503040313720703125", "y": "-0.269397423771520816426772171325865201652050018310546875"}
Z := {"x": "-0.2396019960052188368937464701957651413977146148681640625", "y": "0.3028836445387647902105499042590963654220104217529296875"}
B := {"x": "-0.93747994545458801507464841051842086017131805419921875", "y": "0.34803929644576425683766274232766591012477874755859375"}
Y := {"x": "-0.950254517695892975126525925588794052600860595703125", "y": "0.0393209363371217202054452855009003542363643646240234375"}
X := {"x": "-0.922251741886852105523075806559063494205474853515625", "y": "-0.036520312909838981152432779708760790526866912841796875"}
T := {"x": "-0.58092686894603547120841113837741431780159473419189453125", "y": "0.13318166581446290452905856227516778744757175445556640625"}

Need to prove:
distance(T, X) == distance(T, Z)
distance(T, W) == distance(T, Y)

Proof:
By in_imply_collinear on T, W, Y we get collinear(T, W, Y)
By in_imply_collinear on T, X, Z we get collinear(T, X, Z)
By log_of_2_times_distance on C, D, Z, D we get log(distance(C, D)) == log(2) + log(distance(D, Z))
By log_of_2_times_distance on A, D, D, W we get log(distance(A, D)) == log(2) + log(distance(D, W))
By log_of_2_times_distance on C, B, B, Y we get log(distance(B, C)) == log(2) + log(distance(B, Y))
By log_of_2_times_distance on A, B, B, X we get log(distance(A, B)) == log(2) + log(distance(B, X))
By between_implies_angles on A, X, B we get 180 == angle(A, X, B) mod 360, 0 == angle(X, B, A) mod 360, 0 == angle(B, A, X) mod 360
By between_implies_angles on C, Y, B we get 180 == angle(C, Y, B) mod 360, 0 == angle(Y, B, C) mod 360, 0 == angle(B, C, Y) mod 360
By between_implies_angles on C, Z, D we get 180 == angle(C, Z, D) mod 360, 0 == angle(Z, D, C) mod 360, 0 == angle(D, C, Z) mod 360
By between_implies_angles on D, W, A we get 180 == angle(D, W, A) mod 360, 0 == angle(W, A, D) mod 360, 0 == angle(A, D, W) mod 360
By same_angle_v1 on Z, X, T, Y we get angle(T, Z, Y) == angle(X, Z, Y) mod 360
By same_angle_v1 on W, Y, T, Z we get angle(T, W, Z) == angle(Y, W, Z) mod 360
By same_angle_v0 on X, Z, T, Y we get angle(T, X, Y) == angle(Z, X, Y) mod 360
By same_angle_v1 on Y, T, W, C we get angle(T, Y, C) == angle(W, Y, C) mod 360
By reverse_direction on X, Y we get 180 == direction(X, Y) - direction(Y, X) mod 360
By reverse_direction on X, A we get 180 == direction(X, A) - direction(A, X) mod 360
By reverse_direction on Y, B we get 180 == direction(Y, B) - direction(B, Y) mod 360
By reverse_direction on A, W we get 180 == direction(A, W) - direction(W, A) mod 360
By reverse_direction on C, Z we get 180 == direction(C, Z) - direction(Z, C) mod 360
By reverse_direction on C, B we get 180 == direction(C, B) - direction(B, C) mod 360
By reverse_direction on W, Y we get 180 == direction(W, Y) - direction(Y, W) mod 360
By reverse_direction on Z, X we get 180 == direction(Z, X) - direction(X, Z) mod 360
By same_angle_v3 on T, W, Y, Z we get angle(W, T, Z) == angle(Y, T, Z) + 180 mod 360
By same_angle_v3 on T, X, Z, W we get angle(X, T, W) == angle(Z, T, W) + 180 mod 360
By sas_similarity on W, D, Z, A, D, C we get similar_triangles(A, C, D, W, Z, D)
By sas_similarity on Y, B, X, C, B, A we get similar_triangles(A, B, C, X, B, Y)
By similar_triangle_basic_properties on C, D, A, Z, D, W we get angle(C, D, A) == angle(Z, D, W) mod 360, angle(D, A, C) == angle(D, W, Z) mod 360, angle(A, C, D) == angle(W, Z, D) mod 360, log(distance(C, D)) + log(distance(D, W)) == log(distance(D, Z)) + log(distance(A, D)), log(distance(A, D)) + log(distance(W, Z)) == log(distance(D, W)) + log(distance(A, C)), log(distance(A, C)) + log(distance(D, Z)) == log(distance(W, Z)) + log(distance(C, D))
By similar_triangle_basic_properties on C, B, A, Y, B, X we get angle(C, B, A) == angle(Y, B, X) mod 360, angle(B, A, C) == angle(B, X, Y) mod 360, angle(A, C, B) == angle(X, Y, B) mod 360, log(distance(B, C)) + log(distance(B, X)) == log(distance(B, Y)) + log(distance(A, B)), log(distance(A, B)) + log(distance(X, Y)) == log(distance(B, X)) + log(distance(A, C)), log(distance(A, C)) + log(distance(B, Y)) == log(distance(X, Y)) + log(distance(B, C))
By similar_triangle_basic_properties on T, Y, X, T, W, Z we get angle(T, W, Z) == angle(T, Y, X) mod 360, angle(W, Z, T) == angle(Y, X, T) mod 360, angle(X, T, Y) == angle(Z, T, W) mod 360, log(distance(T, W)) + log(distance(X, Y)) == log(distance(T, Y)) + log(distance(W, Z)), log(distance(W, Z)) + log(distance(T, X)) == log(distance(X, Y)) + log(distance(T, Z)), log(distance(T, X)) + log(distance(T, W)) == log(distance(T, Z)) + log(distance(T, Y))
