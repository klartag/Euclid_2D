/// A trait that allows number types to define Tau directly
/// without having to access their `std::<type>::consts` module.
pub trait Tau {
    const TAU: Self;
}

impl Tau for f32 {
    const TAU: f32 = 6.28318530717958647692528676655900577_f32;
}

impl Tau for f64 {
    const TAU: f64 = 6.28318530717958647692528676655900577_f64;
}
