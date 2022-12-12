import logging
import time
from typing import Union

logger = logging.getLogger(__name__)


class Timer:
    """ """

    def __init__(self, duration: Union[float, int] = 10):
        """Simple timer to control actions with time limit

        ---
        ### Exemplo de uso:\n
        ```
        from PythonUtils.Timer import Timer
        timer = Timer(5)
        while timer.not_expired:
            # do something
            if try_again:
                continue
            if reset_timer: # something that resets the timer
                timer.reset()
            if somethign_bad:
                timer.explode() # force timer exit
            print(f"Timer is at: '{timer.at}'")
            # everything is ok, break the loop
            break
        if timer.expired:
            print(f"Timer expired before break condition")
            return False
        ```
        ---
        Parameters
        ------
        `duration` : int, float
            How long the timer should last. Use ``-1`` para um loop infinito
        """
        self.duration = duration
        self.start = time.perf_counter()
        return

    @property
    def not_expired(self) -> bool:
        if self.duration == -1:
            return True
        return False if time.perf_counter() - self.start > self.duration else True

    @property
    def expired(self) -> bool:
        return not self.not_expired

    @property
    def at(self):
        """How long since the timer started"""
        return time.perf_counter() - self.start

    def reset(self):
        """Restart the timer"""
        self.start = time.perf_counter()
        return

    def explode(self):
        """Force timer to expire"""
        self.duration = 0
        return

    def increment(self, seconds: Union[int, float] = 0):
        """Increase timer duration"""
        self.duration += seconds
        return
