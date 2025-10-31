# hall_keyboard_scan.py
# MicroPython for Raspberry Pi Pico
# 4x CD74HC4067 multiplexers with 61 analog Hall sensors
# Shared select pins (GP8–GP11), shared ADC (GP26), individual enable pins (GP12–GP15)

from machine import Pin, ADC
import time

# ---- CONFIG ----
SELECT_PINS = [8, 9, 10, 11]       # S0..S3
ENABLE_PINS = [12, 13, 14, 15]     # MUX0..MUX3 EN pins (active LOW)
ADC_PIN = 26                       # Common analog read pin

TOTAL_SENSORS = 61
CH_PER_MUX = 16
THRESHOLD_PERCENT = 10.0           # 10% magnetic increase = pressed
# -----------------

# Setup pins
selects = [Pin(p, Pin.OUT) for p in SELECT_PINS]
enables = [Pin(p, Pin.OUT) for p in ENABLE_PINS]
adc = ADC(ADC_PIN)

def set_mux_enabled(mux_index, enabled):
    # Active LOW
    enables[mux_index].value(0 if enabled else 1)

def set_channel(ch):
    for i, pin in enumerate(selects):
        pin.value((ch >> i) & 1)

def disable_all_muxes():
    for i in range(len(enables)):
        enables[i].value(1)

def read_adc():
    return adc.read_u16()

def sensor_to_mux_chan(sensor_idx):
    mux = sensor_idx // CH_PER_MUX
    ch = sensor_idx % CH_PER_MUX
    return mux, ch

# --- Calibration ---
def calibrate(samples=30):
    print("Calibrating... Keep magnets away.")
    baseline = [0]*TOTAL_SENSORS
    for _ in range(samples):
        for s in range(TOTAL_SENSORS):
            mux, ch = sensor_to_mux_chan(s)
            disable_all_muxes()
            set_mux_enabled(mux, True)
            set_channel(ch)
            time.sleep_us(500)
            baseline[s] += read_adc()
        time.sleep_ms(5)
    baseline = [b//samples for b in baseline]
    print("Calibration done.")
    return baseline

# --- Main Loop ---
def main():
    baseline = calibrate()
    pressed = [False]*TOTAL_SENSORS
    disable_all_muxes()
    print("Scanning...")

    while True:
        for s in range(TOTAL_SENSORS):
            mux, ch = sensor_to_mux_chan(s)
            disable_all_muxes()
            set_mux_enabled(mux, True)
            set_channel(ch)
            time.sleep_us(300)
            val = read_adc()
            disable_all_muxes()

            # Percent relative to baseline
            diff = val - baseline[s]
            pct = (diff / 65535) * 100
            if pct >= THRESHOLD_PERCENT and not pressed[s]:
                pressed[s] = True
                print("Key", s, "pressed")
            elif pct < (THRESHOLD_PERCENT / 2) and pressed[s]:
                pressed[s] = False
                print("Key", s, "released")
        time.sleep_ms(10)

main()
