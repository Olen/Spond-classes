"""Tests for SpondSubgroup class."""

import pytest

from spond_classes import SpondSubgroup
from tests.utils import public_attributes, sets_equal


def test_create():
    """Test that SpondSubgroup is created from required fields only.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_ssg = SpondSubgroup("001", "My subgroup")
    valid_attributes = [
        "uid",
        "name",
        "members",
    ]
    assert sets_equal(public_attributes(my_ssg), valid_attributes)

    assert my_ssg.uid == "001"
    assert my_ssg.name == "My subgroup"
    assert my_ssg.members == []


@pytest.fixture
def simplest_subgroup_dict():
    """Represent the simplest possible Subgroup in this implementation.

    Item from 'groups' (root) -> 'group' -> 'subGroups'.
    """
    return {
        "id": "8CC576609CF3DCBC44469A799E76B22B",
        "name": "Subgroup A1",
    }


def test_from_dict(simplest_subgroup_dict):
    """Test that a minimal SpondSubgroup is created from the simplest possible dict
    representation.

    Verify that only expected attributes exist.
    Verify values of all attributes.
    """
    my_ssg = SpondSubgroup.from_dict(simplest_subgroup_dict)
    valid_attributes = [
        "uid",
        "name",
        "members",
    ]
    assert sets_equal(public_attributes(my_ssg), valid_attributes)

    assert my_ssg.uid == "8CC576609CF3DCBC44469A799E76B22B"
    assert my_ssg.name == "Subgroup A1"
    assert my_ssg.members == []
