#!/bin/bash
call=4
echo "Scrapin :3"
python test.py
echo "purging"
convert "$call".png -shave 40X0 "$call".png
convert -crop 1000x1000 "$call".png "$call"_%d.png
convert "$call"_*.png  -page A4 "$call".pdf