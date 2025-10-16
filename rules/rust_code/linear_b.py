# Shim so "from . import linear_b" works even when the extension is top-level.
from linear_b import *  # re-export everything from the compiled module
