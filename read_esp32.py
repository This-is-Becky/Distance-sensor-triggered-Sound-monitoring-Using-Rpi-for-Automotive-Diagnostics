import serial

# Parameters setting
ser = serial.Serial(
    port='/dev/ttyUSB0',  #Serial port define
    baudrate=115200,      #Need to match the baudrate on Distance sensor setting
    timeout=1             

# Read Value
def read_from_esp32():
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            print(data)

try:
    read_from_esp32()
except KeyboardInterrupt:
    print("Program interrupted by user.")
finally:
    ser.close()
