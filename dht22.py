#!/usr/bin/env python3

import time
import board
import adafruit_dht

# Connect the data pin to GPIO 4 (or update the value below)
# See README for a circuit diagram
dht_device = adafruit_dht.DHT22(board.D4)

try:
    while True:
        try:
            temperature_c = dht_device.temperature
            humidity = dht_device.humidity
            print("Temp: {:.1f} C    Humidity: {}% ".format(
                temperature_c, humidity))
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            print("Exception")
            print(repr(error))

        time.sleep(2.0)

except KeyboardInterrupt:
    print('Exiting due to keyboard interrupt')

finally:
    dht_device.exit()
    print("Goodbye!")
