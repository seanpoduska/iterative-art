import numpy as np


def make_grid(width, height, center, scale):
    """Return a complex array of shape (height, width).

    Args:
        width: pixel/array width
        height: pixel/array height
        center: complex number to be designated as central in window
        scale: width of pixel/array in complex plane (how much the complex
               plane changes in the window)

    Returns:
        variable sized array of complex numbers, shaped by width and height,
        scaled by scale, and centered by designated complex number center
    """
    # 1. real axis: width points from center.real - half_span_x to center.real + half_span_x
    half_span_x = scale / 2
    half_span_y = scale * height / width / 2

    xs = np.linspace(center.real - half_span_x, center.real + half_span_x, width)
    ys = np.linspace(center.imag + half_span_y, center.imag - half_span_y, height)

    # 2. imaginary axis: height points, ordered so row 0 is the TOP (largest imag)
    X, Y = np.meshgrid(xs, ys)

    # 3. combine into one 2D complex array
    return X + 1j * Y


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


if __name__ == "__main__":
    print("script running")
    print(make_grid(4, 3, center=0j, scale=2))
