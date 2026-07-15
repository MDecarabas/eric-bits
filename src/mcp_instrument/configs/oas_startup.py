"""OAS device-registry startup for mcp_instrument (simulated devices).

The ophyd-websocket (OAS) server walks ``vars()`` of this module and registers
any module-level ophyd Device/Signal instance, keyed by its variable name. These
ophyd.sim devices let the device-socket come up without a real EPICS IOC.

This file is intentionally separate from ``mcp_instrument.startup`` (which builds
the bluesky RunEngine for the queue server); OAS only needs the device objects.
"""

from ophyd.sim import motor as sim_motor  # registered as "sim_motor"
from ophyd.sim import noisy_det as sim_det  # registered as "sim_det"

__all__ = ["sim_motor", "sim_det"]
