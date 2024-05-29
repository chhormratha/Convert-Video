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

    speed = '1.5'
    flip = 'hflip,' # hflip,

    # Loop through all files in the input directory
    for file in os.listdir(input_dir):
        input_file = os.path.join(input_dir, file)
        filename, ext = os.path.splitext(file)
        if ext:  # Ensuring the file has an extension
            output_file = os.path.join(output_dir, f"{filename}.mp4")

            # Construct FFmpeg command
            command = [
                "ffmpeg", "-y", "-i", input_file,
                "-vf", f"crop=iw-800:ih-100:400:50,scale=1920:1920,setsar=1:1, {flip} setpts=PTS/{speed},eq=saturation=1.5",
                "-af", f"atempo={speed}",
                "-r", "30", "-b:v", "3500k",
                "-c:v", "h264_nvenc", "-c:a", "aac", "-strict", "experimental",
                "-movflags", "+faststart", output_file
            ]

            try:
                # Run FFmpeg command
                subprocess.run(command, check=True)
                
                # Move the original video to the Old Video folder
                os.rename(input_file, os.path.join(old_video_dir, file))
            except subprocess.CalledProcessError as e:
                print(f"Error processing {input_file}: {e}")
                with open(os.path.join(output_dir, "error.log"), "a") as log_file:
                    log_file.write(f"Error processing {input_file}: {e}\n")

if __name__ == "__main__":
    input_dir = r"D:\Downloads\Video\Monkey"
    convert_videos(input_dir)