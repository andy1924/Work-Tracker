import time
import threading


class IdleTracker:
    def __init__(self, work_tracker):
        self.work_tracker = work_tracker

    def track_idle_time(self):
        """Continuously tracks idle time and updates WorkTracker."""
        while True:
            current_time = time.time()
            if current_time - self.work_tracker.last_active > 5:  # If idle for 5 sec
                self.work_tracker.idle_time += 1
            time.sleep(1)
