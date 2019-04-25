from enum import Enum


class status(Enum):
    operational = 1
    under_maintenance = 2
    degraded_performance = 3
    partial_outage = 4
    major_outage = 5
