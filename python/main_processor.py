import time
import json
from core.config import *
from core.serial_handler import SerialHandler
from core.sensor_logic import process_readings
from core.gemini_api import analyze_readings

def main():
    # Initialize serial connection
    serial_handler = SerialHandler(
        port=SERIAL_PORT,
        baudrate=BAUD_RATE,
        timeout=SERIAL_TIMEOUT
    )
    
    try:
        # Load calibration values
        with open(CALIBRATION_FILE, 'r') as f:
            calibration_data = json.load(f)
            
        mq135_baseline = calibration_data.get('mq135_baseline', None)
        if not mq135_baseline:
            print("Error: MQ135 not calibrated. Please run calibration first.")
            return
            
        # Main processing loop
        while True:
            readings = serial_handler.get_all_readings()
            if readings:
                processed_data = process_readings(readings, mq135_baseline)
                analysis = analyze_readings(processed_data)
                print(json.dumps(analysis, indent=2))
                
            time.sleep(0.5)  # Small delay between readings
            
    except KeyboardInterrupt:
        print("\nStopping sensor readings...")
    finally:
        serial_handler.close()

if __name__ == "__main__":
    main()
