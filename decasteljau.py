import numpy as np;
from matplotlib import pyplot as plt;

#Initial Settings

# POINTS = np.array([
#     (0, 0),
#     (1, 1),
#     (2, 1),
#     (3, 0)
# ]);

POINTS = np.array([
    (0, 0),
    (1, 1),
    (2, 3),
    (4, 5),
    (5, 2),
    (6, -2)
]);

T = 0.5;

DEPTH = 5;

def interpolate(t: float,
    a: float,
    b: float):
    return (t * a) + ((1 - t) * b);

def interpolate_2d(t: float,
    a: np.ndarray,
    b: np.ndarray) -> np.ndarray:

    return np.array((
        interpolate(t, a[0], b[0]),
        interpolate(t, a[1], b[1])
    ));

def get_intermediate_points(pts: np.ndarray,
    t: float) -> np.ndarray:

    assert pts.ndim == 2; #Should be a list of points
    assert pts.shape[1] == 2; #Each point should 2-value

    if pts.shape[0] <= 1: #If less than 2 points, don't try interpolating anything
        return pts;

    out = np.ndarray((pts.shape[0] - 1, 2));

    for i in range(pts.shape[0] - 1):

        out[i] = interpolate_2d(t, pts[i], pts[i+1]);
    
    return out;

def casteljau(pts: np.ndarray,
    t: float,
    depth: int) -> np.ndarray:

    if depth == 0:
        return pts;

    head = [];
    tail = [];

    curr = np.copy(pts);

    for i in range(depth):

        if curr.shape[0] <= 0:
            break;

        if curr.shape[0] == 1:
            tail.append(np.copy(curr[0]));
            break;

        head.append(np.copy(curr[0]));
        tail.append(np.copy(curr[-1]));

        curr = get_intermediate_points(curr, t);

    if curr.shape[0] > 1:
        head.extend(np.copy(curr));

    out = head + tail[::-1];

    return out;

def coordinate_list_to_xys(pts):

    xs = [];
    ys = [];

    for p in pts:

        xs.append(p[0]);
        ys.append(p[1]);

    return xs, ys;

def main():

    curve_pts = casteljau(POINTS, T, DEPTH);

    curve_xs, curve_ys = coordinate_list_to_xys(curve_pts);
    points_xs, points_ys = coordinate_list_to_xys(POINTS);

    plt.figure();

    plt.plot(points_xs, points_ys);
    plt.plot(curve_xs, curve_ys);

    plt.show();

if __name__ == "__main__":
    main();