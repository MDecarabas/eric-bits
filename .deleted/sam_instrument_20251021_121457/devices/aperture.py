"""This is a copy of the apstools Slits support with signals for the tweak PV."""

import logging

from ophyd_async.core import StandardReadable

from .motor import Motor

__all__ = ["ApertureSlits", "SlitAxis"]

log = logging.getLogger(__name__)


# Make *readback* and *setpoint* available to match other slits
class SlitMotor(Motor):
    @property
    def readback(self):
        return self.user_readback

    @property
    def setpoint(self):
        return self.user_setpoint


class SlitAxis(StandardReadable):
    def __init__(self, prefix: str, name: str = ""):
        with self.add_children_as_readables():
            self.size = SlitMotor(f"{prefix}Size")
            self.center = SlitMotor(f"{prefix}Center")
        super().__init__(name=name)


class ApertureSlits(StandardReadable):
    """A rotating aperture that functions like a set of slits.

    Unlike the blade slits, there are no independent parts to move,
    so each axis only has center and size.

    Based on the 25-ID-A whitebeam slits.

    """

    _ophyd_labels_ = {"slits"}

    def __init__(
        self,
        prefix: str,
        name: str = "",
    ):
        # Individual slit directions
        with self.add_children_as_readables():
            self.horizontal = SlitAxis(f"{prefix}h")
            self.vertical = SlitAxis(f"{prefix}v")
        super().__init__(name=name)