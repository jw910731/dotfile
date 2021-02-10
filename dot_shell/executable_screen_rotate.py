#!/usr/bin/env python3
"""
    util for screen auto rotate in xwindow linux env
"""
import re
import subprocess
import sys

DISPLAY = "DisplayPort-0"
SN_ID = "61L0194501Q"
MAPPING = {1: "normal", 2: "left"}


def ddc_get_rotate(monitor):
    # ddcutil --terse --sleep-multiplier .1 --sn <SN_num> getvcp AA
    result = subprocess.run(
        ['ddcutil', '--terse', '--sleep-multiplier', '.1', '--sn', monitor, 'getvcp', 'AA'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if(result.returncode != 0):
        print("ddcutil exit with code {}".format(
            result.returncode), file=sys.stderr)
        print("error output: {}".format(result.stderr), file=sys.stderr)
        exit(1)
    # parse result
    strOut = result.stdout.decode('ascii')
    rawState = int(re.search(r"(0[xX])?[\dA-Fa-f]+$", strOut).group(0), 16)
    return rawState


def set_rotate(side):
    # xrandr --output DisplayPort-0 --rotate left
    subprocess.run(['xrandr', '--output', DISPLAY, '--rotate', side])


def main():
    state = ddc_get_rotate(SN_ID)
    set_rotate(MAPPING[state])


if __name__ == '__main__':
    main()
