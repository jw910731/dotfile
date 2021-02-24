#!/bin/bash
for i in {1..6}; do env DISPLAY=$(w -f $(id -un) | awk 'NF > 7 && $2 ~ /tty[0-9]+/ {print $3; exit}') XAUTHORITY=$HOME/.Xauthority $HOME/.shell/screen_rotate.py; sleep 10; done;