from argparse import ArgumentParser

parser= ArgumentParser(description='Timelapse program.')
parser.add_argument('--fps','-f', dest='fps',help='frames per second timelapse video', default=30, type=int, metavar='fps')
parser.add_argument('--tlminutes','-t',dest='tlminutes', help='number of minutes you wish to run your timelapse camera', default=3, type=int, metavar='minutes')


args = parser.parse_args()
print(args)
print(args.fps)
print(args.tlminutes)

