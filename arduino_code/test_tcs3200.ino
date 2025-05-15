// Optional: sensor-only test sketches for TCS3200
// ...
import serial
import time

PORT = "COM3"  # Change as per your system
BAUD = 115200

def read_tcs3200(ser):
    ser.write(b'READ_TCS3200\n')
    line = ser.readline().decode().strip()
    if line.startswith("TCS3200_RED:"):
        val = int(line.split(":")[1])
        return val
    return None

def main():
    with serial.Serial(PORT, BAUD, timeout=2) as ser:
        time.sleep(2)  # wait for connection to establish
        print("Starting TCS3200 test, press Ctrl+C to stop")

        try:
            while True:
                red_value = read_tcs3200(ser)
                if red_value is not None:
                    print(f"TCS3200 Red Frequency: {red_value}")
                time.sleep(1)
        except KeyboardInterrupt:
            print("Test ended")

if __name__ == "__main__":
    main()
