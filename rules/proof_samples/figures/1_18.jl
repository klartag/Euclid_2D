Assumptions:
A, B, C, D, E: Point
distinct(A, B, C, D, E)

Embedding:
E := {"x": "-0.398504130997942962455482529549044556915760040283203125", "y": "0.91716653753698096362967362438212148845195770263671875"}
D := {"x": "0.42419241597830581458339338496443815529346466064453125", "y": "-0.90557208118762577697680171695537865161895751953125"}
C := {"x": "0.292103824299447201173762778125819750130176544189453125", "y": "-0.95638661420454729178430852698511444032192230224609375"}
B := {"x": "0.947543804266081313159020282910205423831939697265625", "y": "0.319625936051757542077922380485688336193561553955078125"}
A := {"x": "-0.53067646510001276194401498287334106862545013427734375", "y": "0.84757447424338760999518171956879086792469024658203125"}

Need to prove:
180 == angle(A, C, E) + angle(B, D, A) + angle(C, E, B) + angle(D, A, C) + angle(E, B, D) mod 360

Proof:
By reverse_direction on D, B we get 180 == direction(D, B) - direction(B, D) mod 360
By reverse_direction on C, A we get 180 == direction(C, A) - direction(A, C) mod 360
By reverse_direction on C, E we get 180 == direction(C, E) - direction(E, C) mod 360
By reverse_direction on B, E we get 180 == direction(B, E) - direction(E, B) mod 360
By reverse_direction on A, D we get 180 == direction(A, D) - direction(D, A) mod 360
