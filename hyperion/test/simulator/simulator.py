# hyperion/test/simulator.py

class Simulator:
    """Simulate a Hyperion instance."""

    def __init__(self):
        """Initialize the simulator."""
        self.brightness = 50
        self.color_temperature = 3000
        self.saturation = 0.5

    def set_brightness(self, brightness):
