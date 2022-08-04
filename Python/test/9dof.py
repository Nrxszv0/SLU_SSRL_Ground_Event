# SPDX-FileCopyrightText: 2020 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import threading
import time
import board
import busio
from adafruit_lis3mdl import LIS3MDL
from math import atan2, degrees

SAMPLE_SIZE = 500


class KeyListener:
    """Object for listening for input in a separate thread"""

    def __init__(self):
        self._input_key = None
        self._listener_thread = None

    def _key_listener(self):
        while True:
            self._input_key = input()

    def start(self):
        """Start Listening"""
        if self._listener_thread is None:
            self._listener_thread = threading.Thread(
                target=self._key_listener, daemon=True
            )
        if not self._listener_thread.is_alive():
            self._listener_thread.start()

    def stop(self):
        """Stop Listening"""
        if self._listener_thread is not None and self._listener_thread.is_alive():
            self._listener_thread.join()

    @property
    def pressed(self):
        "Return whether enter was pressed since last checked" ""
        result = False
        if self._input_key is not None:
            self._input_key = None
            result = True
        return result


def main():
    # pylint: disable=too-many-locals, too-many-statements
    i2c = busio.I2C(board.SCL, board.SDA)

    magnetometer = LIS3MDL(i2c)
    key_listener = KeyListener()
    key_listener.start()

    ############################
    # Magnetometer Calibration #
    ############################

    print("Magnetometer Calibration")
    print("Start moving the board in all directions")
    print("When the magnetic Hard Offset values stop")
    print("changing, press ENTER to go to the next step")
    print("Press ENTER to continue...")
    while not key_listener.pressed:
        pass

    mag_x, mag_y, mag_z = magnetometer.magnetic
    min_x = max_x = mag_x
    min_y = max_y = mag_y
    min_z = max_z = mag_z

    while not key_listener.pressed:
        mag_x, mag_y, mag_z = magnetometer.magnetic

        print(
            "Magnetometer: X: {0:8.2f}, Y:{1:8.2f}, Z:{2:8.2f} uT".format(
                mag_x, mag_y, mag_z
            )
        )

        min_x = min(min_x, mag_x)
        min_y = min(min_y, mag_y)
        min_z = min(min_z, mag_z)

        max_x = max(max_x, mag_x)
        max_y = max(max_y, mag_y)
        max_z = max(max_z, mag_z)

        offset_x = (max_x + min_x) / 2
        offset_y = (max_y + min_y) / 2
        offset_z = (max_z + min_z) / 2

        field_x = (max_x - min_x) / 2
        field_y = (max_y - min_y) / 2
        field_z = (max_z - min_z) / 2

        print(
            "Hard Offset:  X: {0:8.2f}, Y:{1:8.2f}, Z:{2:8.2f} uT".format(
                offset_x, offset_y, offset_z
            )
        )
        print(
            "Field:        X: {0:8.2f}, Y:{1:8.2f}, Z:{2:8.2f} uT".format(
                field_x, field_y, field_z
            )
        )
        mag_calibration = (offset_x, offset_y, offset_z)
        heading1 = degrees(atan2(mag_y,mag_x))
        if heading1 < 0:
            heading1 += 360 
        heading2= degrees(atan2(mag_y+offset_y,mag_x+offset_x))
        if heading2 < 0:
            heading2 += 360 
        heading3 = degrees(atan2(mag_y-offset_y,mag_x-offset_x))
        heading4 = heading3 -30

        if heading3 < 0:
            heading3 += 360 
        heading4 = heading3 
        print(
            "Heading:        0: {0:8.2f}, +:{1:8.2f}, -:{2:8.2f}, -30:{3:8.2f} uT".format(
                heading1,heading2,heading3, heading4
            )
        )
        print("")
        time.sleep(0.01)

    


    print(
        "Final Magnetometer Calibration: X: {0:8.2f}, Y:{1:8.2f}, Z:{2:8.2f} uT".format(
            offset_x, offset_y, offset_z,
        )
    )

    


if __name__ == "__main__":
    main()