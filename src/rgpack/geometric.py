# Created by rglez at 10/13/24
"""
Geometrical functions
"""
import numpy as np


def calc_dihedral(coords1, coords2, coords3, coords4):
    """
    Calculate the dihedral angle between four points in space.

    Args:
        coords1, coords2, coords3, coords4: Coordinates of the four points.

    Returns:
        Dihedral angle in degrees.
    """
    b1 = coords2 - coords1
    b2 = coords3 - coords2
    b3 = coords4 - coords3
    b1xb2 = np.cross(b1, b2)
    b2xb3 = np.cross(b2, b3)
    b1xb2_x_b2xb3 = np.cross(b1xb2, b2xb3)
    y = np.dot(b1xb2_x_b2xb3, b2) * (1.0 / np.linalg.norm(b2))
    x = np.dot(b1xb2, b2xb3)
    return np.degrees(np.arctan2(y, x))
