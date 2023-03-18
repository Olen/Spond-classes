"""Custom classes for Spond entities, and methods to create them."""
from __future__ import annotations

from dataclasses import dataclass, field

from .member import Member
from .role import Role
from .subgroup import Subgroup


@dataclass
class Group:
    """Group.

    May contain zero, one or more SpondMembers.
    May contain zero, one or more SpondSubgroups.
    """

    uid: str  # from API 'id'
    name: str  # from API 'name'
    members: list[Member] = field(default_factory=list, repr=False)
    # derived from API 'members', but uses object refs instead of uid.
    subgroups: list[Subgroup] = field(default_factory=list, repr=False)
    # derived from API 'subgroups'
    roles: list[Role] = field(default_factory=list, repr=False)
    # derived from API 'roles'

    def __str__(self: Group) -> str:
        """Return simple human-readable description."""
        return f"Group '{self.name}'"

    @staticmethod
    def core_from_dict(group_data: dict) -> Group:
        """Create a Group object from the simplest possible dict representation."""
        if not isinstance(group_data, dict):
            raise TypeError
        uid = group_data["id"]
        name = group_data["name"]
        return Group(uid, name)

    @staticmethod
    def from_dict(group_data: dict) -> Group:
        """Create a full-feature Group object from dict representation."""
        group = Group.core_from_dict(group_data)

        # create child SpondMembers
        group.members = [
            Member.from_dict(member_data)
            for member_data in group_data.get("members", [])
        ]
        # create child SpondSubgroups
        group.subgroups = [
            Subgroup.from_dict(subgroup_data)
            for subgroup_data in group_data.get("subGroups", [])
        ]
        # create child SpondRoles
        group.roles = [Role.from_dict(role) for role in group_data.get("roles", [])]

        for member_data in group_data.get("members", []):
            member_data_id = member_data.get("id")

            for subgroup_data_id in member_data.get("subGroups", []):
                # populate child SpondMembers' subgroup attributes
                group.member_by_id(member_data_id).subgroups.append(
                    group.subgroup_by_id(subgroup_data_id),
                )
                # populate child SpondSubgroups' members attribute
                group.subgroup_by_id(subgroup_data_id).members.append(
                    group.member_by_id(member_data_id),
                )

            for role_data_id in member_data.get("roles", []):
                # populate child SpondMembers' roles attribute
                group.member_by_id(member_data_id).roles.append(
                    group.role_by_id(role_data_id),
                )

                # populate child SpondRoles' members attribute
                group.role_by_id(role_data_id).members.append(
                    group.member_by_id(member_data_id),
                )

        return group

    def subgroup_by_id(self: Group, subgroup_uid: str) -> Subgroup:
        """Return the child Subgroup with matching id, or an error."""
        for subgroup in self.subgroups:
            if subgroup.uid == subgroup_uid:
                return subgroup
        raise IndexError

    def member_by_id(self: Group, member_uid: str) -> Member:
        """Return the child Member with matching id, or an error."""
        for member in self.members:
            if member.uid == member_uid:
                return member
        raise IndexError

    def role_by_id(self: Group, role_uid: str) -> Role:
        """Return the child Role with matching id, or an error."""
        for role in self.roles:
            if role.uid == role_uid:
                return role
        raise IndexError