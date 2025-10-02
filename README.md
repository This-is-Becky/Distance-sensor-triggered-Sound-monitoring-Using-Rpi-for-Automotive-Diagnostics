# Distance-sensor-triggered-Sound-monitoring-Using-Rpi-for-Automotive-Diagnostics
Smart audio recording system that uses a distance sensor to detect nearby objects (like vehicles) and a microphone to record sound only when the object is close and stable.  Ideal for various applications, e.g.,  automotive diagnostics etc., which helps capture sound data for diagnostics or performance analysis

## for Distance.ino file
Connect VL53L0X sensor to ESP32 and upload the script on ESP32 

## For read_esp32.py file
This code is simple coding to test whether the ESP32 and the distance sensor can successfully connect to rpi and the data can be read by Rpi, easy for debugging and validate before running the Main code

Connect the Rpi and ESP32 via the connection of USB port, use `ls /dev/ttyUSB**` to check which USB port that has been connect to the ESP32, then adjust the following serial port if needed.
```
ser = serial.Serial(port='/dev/ttyUSB1', baudrate=115200, timeout=1)
```

## For Sound_record.py
- Function: Automatically records audio when an object is detected within a certain distance using a serial-connected sensor.

- Distance Trigger: Starts recording when the measured distance is less than or equal then the thersold value and remains stable for 3 seconds.

- Recording Setup: Uses arecord to capture audio for up to 120 seconds or until the object moves out of range.

- File Management: Saves recordings in a date-based folder under `./Sound.`folder, 
Filenames include the user-input plate number and timestamp.

**NOTE**
  Need Manually create a folder and named it as `"Sound"`
  
- Automatically deletes folders older than 10 days.

- Multithreading:
RecorderThread: Handles distance monitoring and audio recording.
CleanupThread: Periodically deletes old folders.

## For Sh file
need to confirm the format of the file is **UNIX**, if not sure, type:
`dos2unix Main.sh` to convert the format from DOS to UNIX

Edit the Serial port `ttyUSB*` according to the result of the USB serial device, which will shown after running the Main.sh file
```
ser = serial.Serial(port='/dev/ttyUSB1', baudrate=115200, timeout=1)
```

Also the `plughw:2,0` according to the audio recording device, which will shown after running the Main.sh file
```
process = subprocess.Popen(['arecord', '-D', 'plughw:2,0', '--format=FLOAT_LE', '--rate=44100', '-c2', filename])
```
<img width="647" height="165" alt="image" src="https://github.com/user-attachments/assets/93ce1653-71ed-4edc-b0b3-2e3fc128a486" />
