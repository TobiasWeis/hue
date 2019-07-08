# hue
Python scripts to read and plot hue sensors.
Follow the official instructions at https://developers.meethue.com/develop/get-started-2/ to create a username for your Philips Hue bridge. This is needed to access the API.

## Install packages
```python
pip install -r requirements.txt
```

## Config
open Hue.py and insert the username for your bridge the names of your sensor

## Run
```bash
./Hue.py
```

## Plot
The following command plots the values of motion, light and temperature:
```bash
./plot.py
```
<img src="https://github.com/TobiasWeis/hue/raw/master/images/kitchen_motion.png" width="230">
<img src="https://github.com/TobiasWeis/hue/raw/master/images/kitchen_light.png" width="230">
<img src="https://github.com/TobiasWeis/hue/raw/master/images/kitchen_temp.png" width="230">

## TODO
- [ ] Put sensor-names in config
- [ ] Autodiscovery for sensors
- [ ] Web-back/front-end for plotting
