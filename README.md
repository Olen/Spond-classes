# Spond-classes

## About

The unofficial Python [`Spond` library package](https://github.com/Olen/Spond/) gets
data from the Spond  API and returns `dict` objects.

This unofficial Python `Spond-classes` package parses those `dict` objects to create
class instances, i.e. provides an object abstraction layer.

Experimental, very partial, read-only implementation.

## Install

Not yet available at PyPI. Install from GitHub:

`
pip install "Spond-classes @ git+https://github.com/elliot-100/spond-classes"
`

or for a specific version e.g:

`
pip install "Spond-classes @ git+https://github.com/elliot-100/spond-classes@v0.4.0"
`

If you're using Poetry:

`
poetry add git+https://github.com/elliot-100/spond-classes.git
`

or for a specific version:

`
poetry add git+https://github.com/elliot-100/spond-classes.git@v0.4.0
`

## Key features

* Create `Group` class instance from the dict returned by the corresponding `Spond`
method:

```
spond_classes.Group.from_dict()
```

* Then access instance (and child instance) attributes and methods:

```
Group.uid: str
Group.name: str
Group.members: List[Member]
Group.member_by_id() -> Member
Group.roles: List[SpondRoles]
Group.role_by_id() -> Role
Group.subgroups: List[Subgroup]
Group.subgroup_by_id() -> Subgroup

Member.uid: str
Member.created_time: datetime
Member.first_name: str
Member.last_name: str
Member.name: str
Member.roles: List[Role]
Member.subgroups: List[Subgroup]

Role.uid: str
Role.members: List[Member]
Role.name: str

Subgroup.uid: str
Subgroup.members: List[Member]
Subgroup.name: str
```
* Create `Event` class instance from the dict returned by the corresponding `Spond`
method:

```
spond_classes.Event.from_dict()
```

* Then access attributes:

```
Event.uid: str
Event.heading: str
Event.name: str
Event.start_time: datetime
Event.accepted_uids: list
Event.declined_uids: list
Event.unanswered_uids: list
Event.waiting_list_uids: list
Event.unconfirmed_uids: list
```
## Example code

Adapting the example code in [`Spond`](https://github.com/Olen/Spond/) README:

```
import asyncio
from spond import spond
import spond_classes

username = 'my@mail.invalid'
password = 'Pa55worD'
group_id = 'C9DC791FFE63D7914D6952BE10D97B46'  # fake

async def main():
    s = spond.Spond(username=username, password=password)
    group_data = await s.get_group(group_id)
    await s.clientsession.close()

    # create class instance
    group = spond_classes.Group.from_dict(group)

    # use class properties instead of dict keys
    print(group.name)

asyncio.run(main())
```
