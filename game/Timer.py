import time
import threading

class Timer:
    def __init__(self, callback):
        self.callback = callback
        self._running = False
        self._start_time = None
        self._elapsed_time = 0
        self._timer_thread = None

    def start(self):
        if not self._running:
            self._start_time = time.time() - self._elapsed_time
            self._running = True
            self._timer_thread = threading.Thread(target=self._run_timer)
            self._timer_thread.start()

    def stop(self):
        if self._running:
            self._running = False
            self._timer_thread.join()

    def reset(self):
        self._elapsed_time = 0
        self.callback(self._elapsed_time)

    def _run_timer(self):
        while self._running:
            time.sleep(1)
            self._elapsed_time = time.time() - self._start_time
            self.callback(round(self._elapsed_time))
