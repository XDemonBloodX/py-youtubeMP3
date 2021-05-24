import pafy
import sys

if len(sys.argv)<2:
    link='https://www.youtube.com/watch?v=iRTuu9FPAq4'
else: 
    link=sys.argv[1]

if "https://www.youtube.com/watch?v=" not in link:
    print("Error: bad link -> "+link)
    sys.exit()

video = pafy.new(link)
audiostreams = video.videostreams

for i in audiostreams:
    print('byte: %s, ext %s, size %0.2fMb' % (i.bitrate, i.extension, i.get_filesize()/1024/1024))

#audiostreams[1].download(filepath = "./")
bestaudio = video.getbestaudio()
bestaudio.download("./convert")

print("download music finished")
import converter
