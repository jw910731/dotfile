#!/usr/bin/env python3
"""
    util for screen auto rotate in xwindow linux env
"""
import re
import subprocess
import sys
import os

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


def set_rotate(side, display):
    # xrandr --output DisplayPort-0 --rotate left
    subprocess.run(['xrandr', '--output', display, '--rotate', side])


def query_rotation(display):
    result = subprocess.run(
        ['/bin/bash', '-c', """xrandr --query --verbose | grep "DisplayPort-0" | cut -d ' ' -f 6"""], stdout=subprocess.PIPE)
    if result.returncode != 0:
        return None
    else:
        return result.stdout.decode('ascii')


def get_desktop_session():
    result = subprocess.run(['/bin/bash', '-c',
                             """w $(id -un) -f | awk 'NF > 7 && $2 ~ /tty[0-9]+/ {print $8; exit}'"""], stdout=subprocess.PIPE)
    if result.returncode != 0:
        return None
    else:
        return result.stdout.decode('ascii')


def reload_wallpaper():
    if 'i3' in get_desktop_session():
        subprocess.run(['nitrogen', '--restore'],
                       stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)


def main():
    state = ddc_get_rotate(SN_ID)
    if MAPPING[state] != query_rotation:
        set_rotate(MAPPING[state], DISPLAY)
        reload_wallpaper()


if __name__ == '__main__':
    main()
