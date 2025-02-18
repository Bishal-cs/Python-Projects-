import os
import subprocess 
import datetime
import time 
# This module helps to automatically install your module if it is not installed
try:
    import schedule
except:
    subprocess.run("pip install schedule")
    import schedule
import shutil

Source_dir = "" # Enter your file path what you want to backup every day frequently.
Destination_dir = "" # Enter your file path where you want to store your backup file.

def Copy_folder_to_dir(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder Copied to{dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in {dest}")

schedule.every().day.at("00:00").do(lambda: Copy_folder_to_dir(Source_dir, Destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)
