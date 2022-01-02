# Raspi DHT22 Sensor
This python script uses the Adafruit DHT Library to pull
temperature and humidity data from a DHT22 sensor
connected to a Raspberry Pi.

## Circuit Diagram
1. Connect the `vcc` pin on the DHT22 sensor to a `5v` pin on the Raspberry Pi.
1. Connect the `ground` pin to one of the `ground` pins on the Raspberry Pi.
1. Connect the `data` pin to one of the `GPIO` pins on the Raspberry Pi
1. Connect the `vcc` pin to the `data` pin with a 10k ohm resistor
```
+--------------------+
|                    |
|    DHT22 Sensor    |
|                    |
+--------------------+
 |     |     |      |
vcc   dat   nul    gnd
 |     |            |
 |~10k~|            |
 |     |            |
5v   gpio          gnd
```

## Install Dependencies
```bash
pip3 install adafruit-circuitpython-dht
sudo apt-get install libgpiod2
```

## Run
```bash
python3 dht22.py
```
