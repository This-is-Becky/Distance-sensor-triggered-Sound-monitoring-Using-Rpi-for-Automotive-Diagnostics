# Distance-sensor-triggered-Sound-monitoring-Using-Rpi-for-Automotive-Diagnostics
Smart audio recording system that uses a distance sensor to detect nearby objects (like vehicles) and a microphone to record sound only when the object is close and stable.  Idle for various applications, e.g.,  automotive diagnostics etc., which helps capture sound data for diagnostics or performance analysis

## for Distance.ino file
Connect VL53L0X sensor to ESP32 and upload the script on ESP32 

## For Sh file
need to confirm the format of the file is UNIX, if not sure, type:
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
