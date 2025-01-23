from torch import Tensor, tensor
import torch

DEFAULT_PREC = 1e-5

class ImpreciseTensor:
    """
    An ImpreciseTensor represents both values and their imprecision.
    This is useful in geometric calculations to avoid numeric errors.
    """
    mean: Tensor
    """The value stored by the ImpreciseTensor."""
    variance: Tensor
    """The variance of the value."""

    def __init__(self, val, imprec=None):
        if isinstance(val, Tensor):
            self.mean = val
        else:
            self.mean = tensor(val)
        if imprec is not None:
            self.variance = imprec
        else:
            self.variance = (val * DEFAULT_PREC)**2

    def __add__(self, other) -> 'ImpreciseTensor':
        if not isinstance(other, ImpreciseTensor):
            other = ImpreciseTensor(other)
        return ImpreciseTensor(self.mean + other.mean, self.variance + other.variance)
    
    def __sub__(self, other) -> 'ImpreciseTensor':
        if not isinstance(other, ImpreciseTensor):
            other = ImpreciseTensor(other)
        return ImpreciseTensor(self.mean - other.mean, self.variance + other.variance)
    
    def __truediv__(self, other) -> 'ImpreciseTensor':
        if not isinstance(other, ImpreciseTensor):
            other = ImpreciseTensor(other)
        return self * other.inv()
    
    def __mul__(self, other) -> 'ImpreciseTensor':
        if not isinstance(other, ImpreciseTensor):
            other = ImpreciseTensor(other)
        return ImpreciseTensor(self.mean * other.mean, self.variance * other.mean**2 + other.variance * self.mean**2 + self.variance * other.variance)
    
    def __pow__(self, other: Tensor | float | int) -> 'ImpreciseTensor':
        if not isinstance(other, Tensor):
            other = torch.tensor(other)
        return ImpreciseTensor(self.mean ** other, self.variance * torch.abs(other) * self.mean**(2 * (other - 1)))

    def __mod__(self, other: 'ImpreciseTensor') -> 'ImpreciseTensor':
        return self -  other * (self.mean // other.mean)

    def inv(self) -> 'ImpreciseTensor':
        """
        Computes the inverse of the value.
        """
        return ImpreciseTensor(1 / self.mean, self.variance / self.mean**4)
    
    def item(self) -> float:
        return self.mean.item()
    
    def approx_eq(self, val: 'float | Tensor | ImpreciseTensor', err_prob: float) -> Tensor:
        """
        Checks if the value is close to the target value with about the given probability.
        """
        if isinstance(val, ImpreciseTensor):
            sigmas = (self.mean - val) / torch.sqrt(self.variance + val.variance)
        else:
            sigmas = (self.mean - val) / torch.sqrt(self.variance)

        return sigmas < err_prob

    def approx_ne(self, val: 'float | Tensor | ImpreciseTensor', err_prob: float) -> Tensor:
        """
        Checks if the value is different from the target value with about the given probability.
        """
        if isinstance(val, ImpreciseTensor):
            diff = (self.mean - val.mean)**2 / 2 / (self.variance + val.variance)
        else:
            diff = (self.mean - val)**2 / 2 / self.variance

        return torch.exp(-diff) < err_prob

    def __neg__(self) -> 'ImpreciseTensor':
        return ImpreciseTensor(-self.mean, self.variance)
    
    def abs(self) -> 'ImpreciseTensor':
        return ImpreciseTensor(torch.abs(self.mean), self.variance)
    
    def sqrt(self) -> 'ImpreciseTensor':
        # Square root is not numerically stable near zero.
        # Thus, when near zero, we switch to just taking the square root of the variance.
        # There is some factor involved, but it is not very important.
        is_almost_zero = self.mean**2 <= self.variance

        new_mean = self.mean.abs().sqrt()
        large_var = self.variance / 4 / self.mean.sqrt()
        small_var = self.variance.sqrt()

        new_var = torch.where(is_almost_zero, small_var, large_var)

        return ImpreciseTensor(new_mean, new_var)
    
    def atan2(self, x: 'ImpreciseTensor'):
        ddx = -self.mean / (self.mean**2 + x.mean**2)
        ddy = x.mean / (self.mean**2 + x.mean**2)

        return ImpreciseTensor(self.mean.atan2(x.mean), ddx**2 * x.variance + ddy**2 * x.variance)
    
    def neg(self) -> 'ImpreciseTensor':
        return ImpreciseTensor(-self.mean, self.variance)

    def log(self) -> 'ImpreciseTensor':
        return ImpreciseTensor(self.mean.log(), self.variance / self.mean**2)

    def exp(self) -> 'ImpreciseTensor':
        res = self.mean.exp()
        return ImpreciseTensor(res, self.variance * res**2)

    def __repr__(self) -> str:
        return f'N({self.mean:.3f}, {self.variance:.3})'

    def __str__(self) -> str:
        return str(self.mean.item())
    
    def cos(self) -> 'ImpreciseTensor':
        return ImpreciseTensor(self.mean.cos(), self.variance * self.mean.sin()**2)
    
    def sin(self) -> 'ImpreciseTensor':
        return ImpreciseTensor(self.mean.sin(), self.variance * self.mean.cos()**2)