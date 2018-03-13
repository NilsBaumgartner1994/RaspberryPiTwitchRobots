#!/bin/bash
RTMP_URL=rtmp://live-fra.twitch.tv/app/
STREAM_KEY=live_60571661_eMyGKli6Lq6JXikzJlld0KCOfNOhon
while :
do
  raspivid -n -vf -hf -t 0 -w 720 -h 405 -fps 25 -b 500000 -o - | ffmpeg -i - -vcodec copy -an -metadata title="Streaming from raspberry pi camera" -f flv $RTMP_URL/$STREAM_KEY
  sleep 2
done 