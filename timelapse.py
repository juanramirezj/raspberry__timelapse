#based on https://github.com/carolinedunn/timelapse.git
#Juan Ramirez Jardua
#November 2022
#required sudo apt install feh   

from picamera import PiCamera
from os import system
import datetime 
import time
import subprocess

from argparse import ArgumentParser
from sys import stdout
from picamera import Color

def calcProcessTime(starttime, cur_iter, max_iter):

    telapsed = time.time() - starttime
    testimated = (telapsed/cur_iter)*(max_iter)

    finishtime = starttime + testimated
    finishtime = datetime.datetime.fromtimestamp(finishtime).strftime("%H:%M:%S")  # in time

    lefttime = testimated-telapsed  # in seconds
    stelapsed = time.strftime('%Hh %Mm %Ss', time.gmtime(  int(telapsed)))
    slefttime = time.strftime('%Hh %Mm %Ss', time.gmtime(  int(lefttime)))
    return (int(cur_iter), int(max_iter), stelapsed,slefttime, finishtime)



parser= ArgumentParser(description='Timelapse program.')
parser.add_argument('--fps','-f', dest='fps',help='frames per second timelapse video', default=30, type=int, metavar='fps')
parser.add_argument('--tlminutes','-t',dest='tlminutes', help='number of minutes you wish to run your timelapse camera', default=3, type=int, metavar='minutes')
parser.add_argument('--interval','-i',dest='secondsinterval',help='number of seconds delay between each photo taken',default=1, type=int,metavar='seconds')
parser.add_argument('--resolution','-r',dest='resolution',help='resolution of video *1920x1080 1024x768 3840x2160',default='1920x1080', type=str, metavar='pixels', choices=['1024x768', '1920x1080','3840x2160'])
parser.add_argument('--onlyrender',dest='onlyrender',help='Only render, no snapshots', type = str.lower, default='n',choices=['n','y'])
parser.add_argument('--preview','-p',dest='preview',help='Preview last image (every 10 captures)', type = str.lower, default='n', choices=['n','y'])
args=parser.parse_args()
print(args)

tlminutes = args.tlminutes #set this to the number of minutes you wish to run your timelapse camera
secondsinterval = args.secondsinterval #number of seconds delay between each photo taken
fps = args.fps #frames per second timelapse video
numphotos = int((tlminutes*60)/secondsinterval) #number of photos to take

print("number of photos to take = ", numphotos)
print("fps = ", fps)
print("seconds interval =",secondsinterval)
print("duration minutes =",tlminutes)

dateraw= datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M")
print("RPi started taking photos for your timelapse at: " + datetimeformat)

camera = PiCamera()

if args.resolution == '1024x768':
   camera.resolution = (1024, 768)
elif args.resolution == '1920x1080':
  camera.resolution = (1920,1080)
elif args.resolution =='3840x2160':
  camera.resolution = (3840,2160)

nfotos = 0
start = time.time()
camera.annotate_text_size = 30
camera.annotate_foreground = Color('black')
camera.annotate_background = Color('white')

if args.onlyrender == 'n':
   system('rm /home/pi/Pictures/*.jpg') #delete all photos in the Pictures folder before timelapse start
   firsttime = True
   for i in range(numphotos):
       now = datetime.datetime.now()
       this_start = time.time()
       camera.annotate_text = now.strftime("%d-%m-%Y %H:%M:%S")
       fn = '/home/pi/Pictures/image{0:06d}.jpg'.format(i)
       camera.capture( fn )
       if args.preview=='y' and nfotos%10 == 0:
           if firsttime:
               firsttime = False
           else:
               image.kill()
           image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-q", "-B", "black", "-g", "1280x800","--scale-down", fn])
       nfotos = nfotos+1
       prstime = calcProcessTime(start, nfotos, numphotos)
       stdout.write("\r%i of %i run:%s, left:%s, ETA:%s" % prstime)
       stdout.flush()
       this_end = time.time()
       ts = secondsinterval - (this_end-this_start)
       if ts > 0:
            time.sleep(ts)
   if args.preview =='y':
       image.kill()
   stdout.write("\n")
   print("Done taking photos.")
 
print("Please standby as your timelapse video is created.")

if args.resolution == '1024x668':
   system('ffmpeg -r {} -f image2 -s 1024x768 -nostats -loglevel 0 -pattern_type glob -i "/home/pi/Pictures/*.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p /home/pi/Videos/{}.mp4'.format(fps, datetimeformat))
elif args.resolution == '1920x1080':
   system('ffmpeg -r {} -f image2 -s 1920x1080 -nostats -loglevel 0 -pattern_type glob -i "/home/pi/Pictures/*.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p /home/pi/Videos/{}.mp4'.format(fps, datetimeformat))
elif args.resolution =='3840x2160':
   system('ffmpeg -r {} -f image2 -s 3840x2160 -nostats -loglevel 0 -pattern_type glob -i "/home/pi/Pictures/*.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p /home/pi/Videos/{}.mp4'.format(fps, datetimeformat))

#system('rm /home/pi/Pictures/*.jpg')
print('Timelapse video is complete. Video saved as /home/pi/Videos/{}.mp4'.format(datetimeformat))
print('-----------------------------------------------------------------------------')

