#This is a timelapse program based on a raspberry pi (4 in my case) and a camera
##It takes a series of photos and after it creates a timelapse video in mp4 format.

To run:
`python3 timelapsev2.py [options]`

You have several options for creating the timelapse
-**-f or --fps f**:  generates the video using f frames per second. Default: 30 fps
-**-t or --tlminutes m**: captures photos during m minutes. Default: 3 menutes
-**-i or --interval i**: takes a photo every i seconds. Default: 1 second 
-**-r or --resolution 1920x1080 or 1024x768 or 3840x2160**. Sets the video resolution. Default: 1920x1080


>The raspberry has the Raspberry Pi OS 64-bit, than includes picamera2 and ffmpeg installed as default. If you are using a different model, you might need to install both manually.


