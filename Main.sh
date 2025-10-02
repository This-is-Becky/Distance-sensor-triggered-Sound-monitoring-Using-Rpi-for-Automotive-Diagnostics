#!/bin/bash
echo "Checking audio recording device..."
arecord -l

echo "Checking USB serial device..."
ls /dev/ttyUSB*

echo "Starting Plate Recorder Python script..."
cd ~/Downloads
python3 Sound_record.py