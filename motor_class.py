from gpiozero import Device, OutputDevice
from gpiozero.pins.lgpio import LGPIOFactory
import time

# Required for Raspberry Pi 5
Device.pin_factory = LGPIOFactory()


class Motor:
    def __init__(self, pin1, pin2):
        self._pin1 = pin1
        self._pin2 = pin2
        self._running = False
        self.pin1 = OutputDevice(pin1, active_high=True, initial_value=False)
        self.pin2 = OutputDevice(pin2, active_high=True, initial_value=False)
"""
    def clockwise(self):
        self.pin1.on()
        self.pin2.off()
        self._running = True

    def counterclockwise(self):
        self.pin1.off()
        self.pin2.on()
        self._running = True

    def stop(self):
        self.pin1.off()
        self.pin2.off()
        self._running = False   
        """


class Motor:
    def __init__(self, pin1, pin2):
        self._running = False

        # Initialize pins explicitly OFF
        self.pin1 = OutputDevice(pin1, active_high=True, initial_value=False)
        self.pin2 = OutputDevice(pin2, active_high=True, initial_value=False)

        # Safety: ensure motor is stopped on startup
        self.stop()

    def clockwise(self):
        print(f"[DEBUG] CW → pin1 HIGH, pin2 LOW")
        self.pin1.on()
        time.sleep(0.05)  # small delay helps some drivers register change
        self.pin2.off()
        self._running = True

    def counterclockwise(self):
        print(f"[DEBUG] CCW → pin1 LOW, pin2 HIGH")
        self.pin1.off()
        time.sleep(0.05)
        self.pin2.on()
        self._running = True

    def stop(self):
        print(f"[DEBUG] STOP → both LOW")
        self.pin1.off()
        self.pin2.off()
        self._running = False

    def cleanup(self):
        self.stop()
        self.pin1.close()
