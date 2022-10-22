'''
Some Configurations
'''

# Notice!! Don't use .mkv as sources video format!!!
video_format = ['flv', 'mp4', 'avi']


'''
ArgParser Part
'''

import argparse

parser = argparse.ArgumentParser('python addsub.py')
parser.add_argument('-folder', metavar='"..."',type=str, required=True, help='input the videos folder.')
args = parser.parse_args()

'''
FFmpeg Part
'''

import ffmpeg
import os

folder = os.path.abspath(args.folder)
print(f'Executing Script in "{folder}"')

for file in os.listdir(folder):
  if file.split('.')[-1] in video_format:
    file_name = file[:-4]
    print(f'Dealing with file : "{file}"')

    file_path = os.path.abspath(f'{folder}/{file}')
    ass_path = os.path.abspath(f'{folder}/{file_name}.ass')
    ass_path = ass_path.replace('\\', '/')
    ass_path = ass_path.replace(':', '\\\\:')

    task = ffmpeg.input(file_path, hwaccel='cuda')
    task = ffmpeg.output(
      task,
      f'{folder}/{file_name}.mkv',
      loglevel='error',
      **{'y':None},
      **{'stats':None},
      vf=f'fps=60,scale=1920:1080,subtitles={ass_path}',
      vcodec='h264_nvenc',
      video_bitrate='5000k',
      acodec='aac',
      audio_bitrate='320k'
    )
    ffmpeg.run(task)
    



'''
Original Console command:
ffmpeg
-hwaccel cuda
-c:v h264_cuvid
-y
-hide_banner
-i [input video]
-vf fps=fps=60,scale=1920:1080,subtitles=[input ass]
-b:v 5000k
-vcodec h264_nvenc
-c:a aac
-b:a 320k
[output video]
'''