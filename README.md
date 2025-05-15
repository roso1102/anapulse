# Anapulse

Anapulse is a low-cost, Arduino-powered, multi-sensor system that uses AI to perform preliminary anemia screening and respiratory health analysis. It is intended for use in remote healthcare settings, educational demos, or early-stage screening kiosks. This hybrid hardware-software project uses physiological measurements, sensor fusion, and AI-based interpretation via the Gemini API, presented through an intuitive Streamlit UI.

---

## 🌍 What Makes Anapulse Unique?

* ✨ Combines multiple sensors: TCS3200 color sensor, MQ135 air quality sensor, ultrasonic sensor.
* ⚖️ Custom calibration protocols for accuracy and adaptability.
* 🤖 AI-based analysis using Gemini API for decision making.
* 📊 Rule-based + LLM-based health interpretation.
* 📅 Designed for event-based, kiosk-style deployments.

---

## 🚀 Project Workflow

 Sensor Testing & Calibration

1. **Sensor Testing**:

   * Python scripts are used to test the sensors individually.
   * Arduino IDE monitors raw sensor values via Serial.

2. **MQ135 Calibration**:

   * Run `calibration_mq135.py`
   * Choose one of 4 modes: Instant, Quick, Standard, Best.
   * Median baseline gas value is stored in a local file.

 Main Data Acquisition

3. **Main Processor Flow** (`main_processor.py`):

   * Triggers sensor readings one-by-one.
   * Color Sensor: Takes bare hand + tied string perfusion reading.
   * MQ135: Captures user's exhaled breath and calculates delta.
   * Ultrasonic Sensor: Measures elasticity via displacement.
   * All deltas are calculated and formatted.

 AI-Based Analysis

4. **Gemini API Call** (`gemini_api.py`):

   * Sends the sensor delta values to Gemini API.
   * Uses both custom thresholds + AI reasoning.
   * Gets structured output: probability score, explanation, advisory.

 UI + Display

5. **Streamlit UI** (`app.py`):

   * Live sensor readings
   * Control buttons
   * Final AI analysis shown with medical advisory

---

## 🔺 Folder Structure

```bash
anapulse/
├── arduino_code/
│   ├── sensor_reading_arduino.ino
│   ├── test_tcs3200.ino
│   ├── test_mq135.ino
│   └── test_ultrasonic.ino
├── python/
│   ├── tests/
│   │   ├── test_color_sensor.py
│   │   ├── test_mq135.py
│   │   └── test_ultrasonic.py
│   ├── calibration/
│   │   └── calibration_mq135.py
│   │   └── calibrate_tcs3200.py
│   ├── core/
│   │   ├── serial_handler.py
│   │   ├── sensor_logic.py
│   │   ├── config.py
│   │   └── gemini_api.py
│   ├── main_processor.py
│   └── requirements.txt
├── streamlit_ui/
│   └── app.py
├── data/
│   └── calibration_values.json
├── .gitignore
└── README.md
```

---

## 🧵 Hardware Used

* Arduino UNO R4 WiFi
* TCS3200 Color Sensor
* MQ135 Gas Sensor
* HC-SR04 Ultrasonic Sensor
* Thin rubber string for perfusion test
* USB cable for Serial + power

---

## ⚖️ Calibration Modes (for MQ135)

* Instant: 10 values
* Quick: 5-10 mins (30-60 values)
* Standard: 30-45 mins (180-250 values)
* Best: 1 hour+ (400+ values)

Calibration base value saved in data/calibration\_values.json

---

## 🪡 Novelty

* First hybrid, non-invasive anemia detection prototype using delta analysis on perfusion.
* Combines breath CO2, blood elasticity, and skin color changes.
* Sensor fusion via serial + Python + AI
* Rule-based fallback in case of Gemini API failure
* Event-friendly: handles recalibration, user guidance, set distances

---

## 🚪 How to Run

1. Upload Arduino sketch (sensor\_reading\_arduino.ino) via Arduino IDE
2. Activate virtualenv (optional) and install Python packages:

```bash
pip install -r requirements.txt
```

3. Run test scripts in python/tests/
4. Calibrate MQ135:

```bash
python python/calibration/calibration_mq135.py
```

5. Run main program:

```bash
python python/main_processor.py
```

6. Run Streamlit UI:

```bash
streamlit run streamlit_ui/app.py
```

---


dont use && because we are in power shell


