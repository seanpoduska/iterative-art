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
    """Return an int array shaped like c: iterations until |z| > 2 for each point.
    counts: number of iterations it takes to escape
    Points that never escape are assigned max_iter

    Args:
        c: the array of values to run the escape test on. Each iteration goes
        through z = z**2 + c
        max_iter: the maximum number of iterations c goes through before the
        loop ends and max_iter is returned.

    Returns:
        An array of integers with each pixel's escape time.
        For single value calculation, use escape_time_single()
    """
    z = np.zeros_like(c, dtype=complex)  # array of zeroes shape c
    counts = np.full(c.shape, max_iter)  # array of max_iter, return canvas
    active = np.ones(c.shape, dtype=bool)  # bool array to track active pixels

    for i in range(max_iter):
        z[active] = z[active] ** 2 + c[active]  # update active pixels
        escaped = (np.abs(z) > 2) & active
        counts[escaped] = i + 1
        active[escaped] = False
        if not active.any():
            break
    return counts


if __name__ == "__main__":
    print("script running")
    testGrid = make_grid(4, 3, center=0j, scale=2)
    print(testGrid)

    print(escape_time(testGrid, 50))
