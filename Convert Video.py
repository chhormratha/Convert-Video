import os
import shutil
import subprocess

os.system('cls & color e & title Convert Video - By CHHORM  RATHA')

def convert_videos(input_dir):
    output_dir = os.path.join(input_dir, "Converted Video")
    old_video_dir = os.path.join(input_dir, "Old Video")

    # Create output and old video directories if they don't exist
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(old_video_dir, exist_ok=True)

    vidoe_size = input('\n   Input Video Size (ex: 720:1280) : ')
    if vidoe_size == '': 
        vidoe_size = '720:1280'
    else: vidoe_size = vidoe_size
    speed = input('\n   Input Speed (default: 1) : ')
    if speed == '':
        speed = '1.0'
    else: speed = speed
    flip = input('\n   Flip Video (y/n) : ') # hflip,
    if flip in ['y', 'yes']: 
        flip = 'hflip,'
    else: 
        flip = ''
    framrate = input('\n   Input Framrate (ex. 30) : ')
    if framrate == '':
        framrate = '30'
    else: 
        framrate =  framrate
    bitrate = input('\n   Input Bitrate (ex. 3500) : ')
    if bitrate == '':
        bitrate = '3500k'
    else:
        bitrate = f'{bitrate}k'

    # Loop through all files in the input directory
    for file in os.listdir(input_dir):
        input_file = os.path.join(input_dir, file)
        filename, ext = os.path.splitext(file)
        if ext:  # Ensuring the file has an extension
            output_file = os.path.join(output_dir, f"{filename}.mp4")

            # Construct FFmpeg command
            command = [
                "ffmpeg", "-y", "-i", input_file,
                "-vf", f"crop=iw-20:ih-20:10:10,scale={vidoe_size},setsar=1:1, {flip} setpts=PTS/{speed},eq=saturation=1.5",
                "-af", f"atempo={speed}",
                "-r", f"{framrate}", "-b:v", f"{bitrate}",
                "-c:v", "h264_nvenc", "-c:a", "aac", "-strict", "experimental",
                "-movflags", "+faststart", output_file
            ]

            try:
                # Run FFmpeg command
                subprocess.run(command, check=True)
                
                # Move the original video to the Old Video folder
                os.rename(input_file, os.path.join(old_video_dir, file))
            except : pass

if __name__ == "__main__":
    input_dir = input('\n   Input Video Path : ').replace('"','')
    convert_videos(input_dir)
