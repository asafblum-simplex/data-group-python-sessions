import enum
import random
from typing import Tuple, Set, Optional


def is_alive(device: str):
    return


def is_able_to(device_status: str = "unknown", caps: Optional[Set[str]] = None):
    capabilities = caps if caps is not None else set()
    capabilities.add(f'cap.bar {random.random()}')
    # return capabilities


device_caps = set()
is_able_to(caps=device_caps)
is_able_to(caps=device_caps)
device_caps.add('some other value')
is_able_to(caps=device_caps)
is_able_to(caps=device_caps)
is_able_to(caps=device_caps)

caps_b = is_able_to(caps=set())

caps_c = is_able_to()
is_able_to(caps=caps_b)
is_able_to()
caps_a = is_able_to()  # 1 (?)
caps_b = is_able_to(['cap.fuzz'])  # 1 (?) | 2 (?)

print(len(caps_a), len(caps_b))


class DeviceStatus(enum.Enum):
    ON = 'ON',
    OFF = 'OFF',
    UNKNOWN = "UNKNOWN",
    IDLE = "IDLE"
    ACTIVE = "ACTIVE"


class Thing:
    status: DeviceStatus
    capabilities: frozenset[str]


# raw_device = {
#     caps: ['light', 'windows', 'tv', 'light']
# }
def test(device):
    pass
