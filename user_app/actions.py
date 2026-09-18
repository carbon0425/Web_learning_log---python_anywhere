from collections import namedtuple
from enum import IntEnum

class Status(IntEnum):
    PENDING = 0
    ACCEPTED = 1
    REJECTED = 2

friend_apply = namedtuple("friend_apply", ["sender", "to", "status"])
apply_check = namedtuple("apply_check", ["apply_obj"])
normal = namedtuple("normal", [])

ACTION_MAP = {
    "normal": normal,
    "friend_apply": friend_apply,
    "apply_check": apply_check
}
