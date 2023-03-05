# Scripts
1. `autostart.sh`: This script is set to run on startup and calls the fan.py script to turn on the fan.

2. `fan.py`: This script imports the RPi.GPIO library and sets up the GPIO pin for the fan. The fan is turned on by setting the GPIO output to HIGH.

3. `fan_off.py`: This script also imports the RPi.GPIO library and sets up the GPIO pin for the fan. The fan is turned off by setting the GPIO output to LOW.

# Usage
To use these scripts, ensure that the fan is connected to the correct GPIO pin on the Raspberry Pi. Place the `autostart.sh` script in the `/storage/.config/` folder to automatically **turn `ON`** the fan on **startup**. Place the `fan.py` and `fan_off.py` scripts in the `/storage/` folder to manually turn on and off the fan, respectively.