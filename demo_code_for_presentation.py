from unittest.mock import patch
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


def demonstrate_mock_pi():
    """
    Demonstrate mocking of calculate_pi function.
    Shows how the mock returns a fixed value instead of running the calculation.
    """
    # Create mock that always returns 3.14
    with patch(__name__ + '.calculate_pi', return_value=3.14):
        # This will use the mock instead of actual calculation
        fake_pi = calculate_pi(1000000)  # number of points doesn't matter now
        print(f"Mocked π value: {fake_pi}")

        # The real function isn't called, so this is very fast
        fake_pi_2 = calculate_pi(1000000000)  # even large numbers are instant
        print(f"Another mocked π value: {fake_pi_2}")


if __name__ == "__main__":
    n_points = 1000
    estimated_pi = calculate_pi(n_points)
    print(f"π estimate with {n_points} points: {estimated_pi}")
    print(f"Actual π: {np.pi}")
    print(f"Difference: {abs(estimated_pi - np.pi)}")

    print("\nRunning with mock:")
    demonstrate_mock_pi()
