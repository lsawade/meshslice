
import numpy as np
from meshslice.utils.cart2geo import cart2geo


def test_cart2geo1():
    """Tests ``lwsspy.math.geo2cart``"""

    # Input
    rtp = (1., 35.264389682754654, 45.0)

    # Solution
    xyz = (1/np.sqrt(3), 1/np.sqrt(3), 1/np.sqrt(3))

    # Check
    np.testing.assert_almost_equal(rtp, cart2geo(*xyz))


def test_cart2geo2():
    """Tests ``lwsspy.math.geo2cart``"""

    # Input
    rtp = (1., 35.264389682754654, -45.0)

    # Solution
    xyz = (1/np.sqrt(3), -1/np.sqrt(3), 1/np.sqrt(3))

    # Check
    np.testing.assert_almost_equal(rtp, cart2geo(*xyz))


def test_cart2geo3():
    """Tests ``lwsspy.math.geo2cart``"""

    # Input
    rtp = (1., 35.264389682754654, -135.0)

    # Solution
    xyz = (-1/np.sqrt(3), -1/np.sqrt(3), 1/np.sqrt(3))

    # Check
    np.testing.assert_almost_equal(rtp, cart2geo(*xyz))


def test_cart2geo4():
    """Tests ``lwsspy.math.geo2cart``"""

    # Input
    rtp = (1., 35.264389682754654, 135.0)

    # Solution
    xyz = (-1/np.sqrt(3), 1/np.sqrt(3), 1/np.sqrt(3))

    # Check
    np.testing.assert_almost_equal(rtp, cart2geo(*xyz))
