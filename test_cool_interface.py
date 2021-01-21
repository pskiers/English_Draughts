from cool_interfce import get_coordinates_from_mouse


def test_get_coordinates_from_mouse():
    pos = (233, 334)
    cord = get_coordinates_from_mouse(pos)
    assert cord == (3, 2)
