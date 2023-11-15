# Add all constants we will use here
from enum import Enum


class TaskStatus(Enum):
    NOT_YET_STARTED = "NOT YET STARTED"
    ONGOING = "ONGOING"
    DONE = "DONE"
    CANCELLED = "CANCELLED"
    WILL_NOT_DO = "WILL_NOT_DO"
