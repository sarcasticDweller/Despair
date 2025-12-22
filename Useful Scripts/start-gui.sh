#!/usr/bin/env bash

# Thank you https://www.freecodecamp.org/news/run-python-gui-in-github-codespaces/ for this script! This script was *ever-so-slightly* tweaked to install xterm on 12/18/2025, but I forgot to update this comment when I made the change
set -e

echo "Installing dependencies..."
sudo apt-get update -y
sudo apt-get install -y xvfb x11vnc fluxbox websockify novnc xterm

echo "Starting virtual display..."
Xvfb :1 -screen 0 1024x768x24 &
export DISPLAY=:1
fluxbox &

echo "Starting VNC server..."
x11vnc -display :1 -nopw -forever -shared -rfbport 5900 &

# if the server fails to start, try manually running `x11vnc -display :1 -nopw -forever -shared -rfbport 5900` in a new terminal

echo "Starting noVNC on port 6080..."
websockify --web=/usr/share/novnc 6080 localhost:5900 &

echo ""
echo "GUI environment is ready!"
echo "Go to the Ports tab, set port 6080 to Public, and open the link."
