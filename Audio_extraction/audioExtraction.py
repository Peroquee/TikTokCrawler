from moviepy import *
import csv

with open(".idea\\output_csv\\links.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        path = "C:\\Users\\gehst\PycharmProjects\\HerrGoetz1stTry\\" + str(line[0][23:] + ".mp4")
        clip = VideoFileClip(path)
        clip.audio.write_audiofile("C:\\Users\\gehst\PycharmProjects\\HerrGoetz1stTry\\" + str(line[0])[23:] + ".wav")