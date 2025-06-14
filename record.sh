#!/usr/bin/env bash
set -e

source .venv/bin/activate
python visualize.py &
VIS_PID=$!

sleep 1

mkdir -p assets

ffmpeg -y \
  -f x11grab -video_size 984x744 -framerate 60 -i :1.0+100,200 \
  -t 8 \
  -vf "fps=15,scale=600:-1:flags=lanczos" \
  assets/quadrants.gif

kill $VIS_PID
echo "Done! GIF saved to assets/quadrants.gif"
