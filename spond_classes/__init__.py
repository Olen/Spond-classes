"""
# Introduction

[Spond](https://spond.com/welcome) is a team/group-oriented events system.

The unofficial Python [`spond`](https://github.com/Olen/Spond/) package gets data from
the Spond API and returns `dict` objects.

This unofficial Python [`spond-classes`](https://github.com/elliot-100/Spond-classes)
package parses those `dict`s to [Pydantic](https://docs.pydantic.dev/) class instances.

# Key classes

These are the classes intended for direct user instantiation:

## `Event`

From
- `dict` returned by `spond.spond.Spond.get_event()`;
- `dict` item from the `list` returned by `spond.spond.Spond.get_events()`.

## `Group`

From
- `dict` returned by `spond.spond.Spond.get_group()`;
- `dict` item from the `list` returned by `spond.spond.Spond.get_groups()`.

"""

# Explicitly import classes and functions into the package namespace to define the API.

from .event import Event, EventType, Responses
from .group import Group
from .member import Member
from .profile_ import Profile
from .role import Role
from .subgroup import Subgroup

__all__ = [
    "Event",
    "EventType",
    "Responses",
    "Group",
    "Member",
    "Profile",
    "Role",
    "Subgroup",
]
