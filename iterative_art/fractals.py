import numpy as np


def make_grid(width, height, center, scale):
    """
    Return a complex array of shape (height, width).

    Document: what are center and scale? Which way is +imaginary?
    """
    # TODO: build the real and imaginary axes (np.linspace)
    # TODO: combine them into one complex array (np.meshgrid, then x + 1j*y


def escape_time_single(c, max_iter):
    """Returns # of z -> z^2 + c updates needed until |z| > 2. (max returned is
    max_iter)

    Args:
        c: complex number (point) to test
        max_iter: maximum number of updates before loop stops

    Returns:
        The number of iterations of z^2 + c until the number escapes
        abs(z) > 2. If doesn't escape before reaching max_iter, return
        max_iter.
    """
    z = 0

    # repeat until z escapes 2
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = z**2 + c
    # if loop finishes, return max_iter
    return max_iter


def escape_time(c, max_iter):
    """
    Return an int array: iteration at which each point escaped (max_iter if never).
    """
    # TODO: z stars at zeros, counts starts at zeros
    # TODO: loop up to max_iter times (a loop over iterations is fine, a loop
    #       over pixels is not)
    # TODO: update z only where the point hasn't escaped yet


print("script running")
