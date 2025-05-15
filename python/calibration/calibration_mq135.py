import json
import time
import statistics
import os
from ..core.config import *
from ..core.serial_handler import SerialHandler

def calibrate_mq135(mode='standard'):
    if mode not in MQ135_CALIBRATION_MODES:
        raise ValueError(f"Invalid mode. Choose from: {list(MQ135_CALIBRATION_MODES.keys())}")
    
    num_readings = MQ135_CALIBRATION_MODES[mode]
    readings = []
    
    serial_handler = SerialHandler(
        port=SERIAL_PORT,
        baudrate=BAUD_RATE,
        timeout=SERIAL_TIMEOUT
    )
    
    try:
        print(f"\nStarting MQ135 calibration in {mode} mode")
        print(f"Taking {num_readings} readings...")
        
        while len(readings) < num_readings:
            value = serial_handler.get_mq135_reading()
            if value is not None:
                readings.append(value)
                print(f"Reading {len(readings)}/{num_readings}: {value}")
                time.sleep(MQ135_DELAY)
        
        baseline = statistics.median(readings)
        
        # Ensure data directory exists
        os.makedirs(DATA_DIR, exist_ok=True)
        
        # Save calibration value
        calibration_data = {}
        if os.path.exists(CALIBRATION_FILE):
            with open(CALIBRATION_FILE, 'r') as f:
                calibration_data = json.load(f)
        
        calibration_data['mq135_baseline'] = baseline
        calibration_data['mq135_calibration_mode'] = mode
        calibration_data['mq135_calibration_date'] = time.strftime('%Y-%m-%d %H:%M:%S')
        
        with open(CALIBRATION_FILE, 'w') as f:
            json.dump(calibration_data, f, indent=2)
            
        print(f"\nCalibration complete!")
        print(f"Baseline value: {baseline}")
        print(f"Saved to: {CALIBRATION_FILE}")
        
    except KeyboardInterrupt:
        print("\nCalibration interrupted!")
    finally:
        serial_handler.close()

if __name__ == "__main__":
    print("MQ135 Calibration Modes:")
    print("1. Instant  (10 values)")
    print("2. Quick    (5-10 mins, 30-60 values)")
    print("3. Standard (30-45 mins, 180-250 values)")
    print("4. Best     (1 hour+, 400+ values)")
    
    mode_map = {
        "1": "instant",
        "2": "quick",
        "3": "standard",
        "4": "best"
    }
    
    choice = input("\nSelect mode (1-4): ").strip()
    if choice in mode_map:
        calibrate_mq135(mode_map[choice])
    else:
        print("Invalid choice. Using standard mode.")
        calibrate_mq135('standard')
