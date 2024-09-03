# This is a timelapse program based on a raspberry pi (model 4 in my case) and a pi camera
## It takes a series of photos and after it creates a timelapse video in mp4 format.

To run:
`python3 timelapsev2.py [options]`

You have several options for creating the timelapse
+ **-f or --fps f**:  generates the video using f frames per second. Default: 30 fps
+ **-t or --tlminutes m**: captures photos during m minutes. Default: 3 minutes
+ **-i or --interval i**: takes a photo every i seconds. Default: 1 second 
+ **-r or --resolution 1920x1080 or 1024x768 or 3840x2160**. Sets the video resolution. Default: 1920x1080

Camera used for my setup: Raspberry PiHQ Camera Module with Arducam 8-50mm C-Mount Zoom Lens
![Camera used for my setup: Raspberry PiHQ Camera Module with Arducam 8-50mm C-Mount Zoom Lens](https://github.com/juanramirezj/raspberry_timelapse/blob/master/images/camera.jpg)

I've used an Eleclab 7 inch 1024x600 touchscreen monitor
![I've used an Eleclab 7 inch 1024x600 touchscreen monitor](https://github.com/juanramirezj/raspberry_timelapse/blob/master/images/raspberry_front.jpg)

Raspberry Pi 4 4Gb Ram, Raspberry Pi OS 64 bits
![Raspberry Pi 4 4Gb Ram, Raspberry Pi OS 64 bits](https://github.com/juanramirezj/raspberry_timelapse/blob/master/images/raspberry_back.jpg)


> The raspberry has the Raspberry Pi OS 64-bit, than includes picamera2 and ffmpeg installed as default. If you are using a different model, you might need to install both manually.
> The programs requires opencv. You can create a virtual environment with `python3 -m venv --system-site-packages my-venv`, activate with `source my-venv/bin/activate` and install with `pip install opencv-python`


