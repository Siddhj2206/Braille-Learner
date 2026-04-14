"""Simulation display for testing without hardware.

Prints Braille patterns to console instead of controlling servos.
"""

from .base import Display


class SimulationDisplay(Display):
    """
    Simulation display for testing without hardware.

    Prints Braille patterns to console instead of controlling servos.
    """

    def __init__(self):
        self._initialized = True

    def set_pattern(self, pattern: list[int]) -> None:
        pass

    def reset(self) -> None:
        print("↩ Reset")

    def cleanup(self) -> None:
        """No cleanup needed for simulation."""
        pass
