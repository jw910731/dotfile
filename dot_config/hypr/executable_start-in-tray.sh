#!/bin/sh
# start waybar and programs with tray icons after pause
waybar &
sleep 1
nm-applet --indicator &
hime &