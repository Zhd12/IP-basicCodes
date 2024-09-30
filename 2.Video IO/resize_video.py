from moviepy.editor import VideoFileClip

def resized_video(path, outputPath, width, height):
    # load the video
    video = VideoFileClip(path)
    # resized the video
    resized_video = video.resize(newsize=(width, height))
    # write it on itself
    resized_video.write_videofile(outputPath)
