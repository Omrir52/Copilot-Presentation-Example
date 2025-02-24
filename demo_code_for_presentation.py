import numpy as np

H_spin_half = np.array([[1, 0], [0, -1]])

H = np.array([[1, 0], [0, -1]])


def calculate_pi(num_points: int) -> float:
    """
    Calculate π using Monte Carlo method.

    Args:
        num_points (int): Number of random points to generate

    Returns:
        float: Estimation of π
    """
    points_inside = 0

    for _ in range(num_points):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)

        if x*x + y*y <= 1:
            points_inside += 1

    return 4 * points_inside / num_points


if __name__ == "__main__":
    n_points = 1_000_000
    estimated_pi = calculate_pi(n_points)
    print(f"π estimate with {n_points} points: {estimated_pi}")
    print(f"Actual π: {np.pi}")
    print(f"Difference: {abs(estimated_pi - np.pi)}")
