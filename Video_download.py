'''for use this use python 3.8 or higher version of pyhon '''
# this is used to install the module if the module is not installed
import subprocess
try:
    from pytubefix import YouTube 
except ModuleNotFoundError:
    subprocess.run("pip install pytubefix")
    from pytubefix import YouTube

import tkinter as tk 
from tkinter import filedialog  

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        high_res_stream = streams.get_highest_resolution()
        high_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter the YouTube video URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Start Downloading...")
        download_video(video_url, save_dir)
    else:
        print("No folder selected. Exiting.")