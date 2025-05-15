import os

# Base directory path
BASE_DIR = "G:\\anapulse"

# Data directory
DATA_DIR = os.path.join(BASE_DIR, "data")
CALIBRATION_FILE = os.path.join(DATA_DIR, "calibration_values.json")

# Serial configuration
SERIAL_PORT = "COM3"  # Change as needed for your system
BAUD_RATE = 115200
SERIAL_TIMEOUT = 2

# Sensor calibration settings
MQ135_CALIBRATION_MODES = {
    "instant": 10,      # 10 values
    "quick": 60,       # 30-60 values (5-10 mins)
    "standard": 250,   # 180-250 values (30-45 mins)
    "best": 400        # 400+ values (1 hour+)
}

# Sensor reading delays and timeouts
COLOR_SENSOR_DELAY = 1.0  # seconds between readings
ULTRASONIC_DELAY = 0.5
MQ135_DELAY = 0.5

# Threshold values for sensor readings
COLOR_DELTA_THRESHOLD = 20
BREATH_DELTA_THRESHOLD = 50
ELASTICITY_THRESHOLD = 5
