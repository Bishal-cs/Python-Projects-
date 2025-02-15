from pytube import YouTube 

# where to save 
SAVE_PATH = "Youtube_Downloader\Downloaded_Videos" #to_do 

# link of the video to be downloaded 
link=["https://youtu.be/StpojvYoxvc?si=f7DF6rb9ep_75THX"]

for i in link:
    try: 
        # object creation using YouTube 
        yt = YouTube(link) 
    except: 
        #to handle exception 
        print("Connection Error") 

    # Get all streams and filter for mp4 files
    mp4_streams = yt.streams.filter(file_extension='mp4').all()

    # get the video with the highest resolution
    d_video = mp4_streams[-1]

    try: 
        # downloading the video 
        d_video.download(output_path=SAVE_PATH)
        print('Video downloaded successfully!')
    except: 
        print("Some Error!")