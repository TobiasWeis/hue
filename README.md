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
```bash
./plot.py
```
![motion](images/kitchen_motion.png "Motion sensor" | width=100)
![temperature](images/kitchen_temp.png "Temperature sensor" | width=100)
![lightlevel](images/kitchen_light.png "Light sensor" | width=100)

