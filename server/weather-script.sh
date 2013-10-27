#!/bin/sh

cd "$(dirname "$0")"

python2 weather-script.py
rsvg-convert --background-color=white -o weather-script-output.png weather-script-output.svg
rm -f done.png
pngcrush -c 0 weather-script-output.png done.png
