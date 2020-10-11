import os
import threading
import time
from mutagen.mp3 import MP3
from pygame import mixer
import random 
happy_playlist = ["happy\\song1.mp3","happy\\song2.mp3","happy\\song3.mp3","happy\\song4.mp3","happy\\song5.mp3","happy\\song6.mp3","happy\\song7.mp3"]
sad_playlist=["sad\\sad1.mp3","sad\\sad2.mp3","sad\\sad3.mp3","sad\\sad4.mp3","sad\\sad5.mp3","sad\\sad6.mp3","sad\\sad7.mp3"]
angry_playlist=["angry\\angry1.mp3","angry\\angry2.mp3","angry\\angry3.mp3","angry\\angry4.mp3","angry\\angry5.mp3","angry\\angry6.mp3"]
surprised_playlist=["surprised\\sur1.mp3","surprised\\sur2.mp3","surprised\\sur3.mp3","surprised\\sur4.mp3","surprised\\sur5.mp3","surprised\\sur6.mp3"]
disgusted_playlist=["disgusted\\dis1.mp3","disgusted\\dis2.mp3","disgusted\\dis3.mp3","disgusted\\dis4.mp3","disgusted\\dis5.mp3"]
fear_playlist=["fear\\f1.mp3","fear\\f2.mp3","fear\\f3.mp3","fear\\f4.mp3","fear\\f5.mp3","fear\\f6.mp3","fear\\f7.mp3"]
confused_playlist=["confused\\con1.mp3","confused\\con2.mp3","confused\\con3.mp3","confused\\con4.mp3","confused\\con5.mp3","confused\\con6.mp3"]
calm_playlist=["calm\\calm1.mp3","calm\\calm2.mp3","calm\\calm3.mp3","calm\\calm4.mp3","calm\\calm5.mp3","calm\\calm6.mp3",]

mixer.init()  # initializing the mixer
mixer.music.set_volume(0.7)

def stop_music():
    mixer.music.stop()

def show_details(play_song):
    file_data = os.path.splitext(play_song)

    if file_data[1] == '.mp3':
        audio = MP3(play_song)
        total_length = audio.info.length
    else:
        a = mixer.Sound(play_song)
        total_length = a.get_length()

    # div - total_length/60, mod - total_length % 60
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print ("Total Length" + ' - ' + timeformat)

    t1 = threading.Thread(target=start_count, args=(total_length,))
    t1.start()

def start_count(t):
    # mixer.music.get_busy(): - Returns FALSE when we press the stop button (music stop playing)
    # Continue - Ignores all of the statements below it. We check if music is paused or not.
    current_time = 0
    while current_time <= t and mixer.music.get_busy():
        if 0:
            continue
        else:
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print ("Current Time" + ' - ' + timeformat)
            time.sleep(1)
            current_time += 1

def play_music(play_it):
    if 0:
        mixer.music.unpause()
    else:
        stop_music()
        time.sleep(1)
        mixer.music.load(play_it)
        mixer.music.play()
        show_details(play_it)
    

def playHappy():
 print ('Playing Happy Songs Playlist')
 k=random.choice(happy_playlist)
 play_music(k)

def playSad():
 print ('Playing Sad Songs Playlist')
 k=random.choice(sad_playlist)
 play_music(k)

def playAngry():
 print ('Playing Angry Songs Playlist')
 k=random.choice(angry_playlist)
 play_music(k)

def playSurprised():
 print ('Playing Surprised Songs Playlist')
 k=random.choice(surprised_playlist)
 play_music(k)

def playDisgusted():
 print ('Playing Disgusted Songs Playlist')
 k=random.choice(disgusted_playlist)
 play_music(k)

def playFear():
 print ('Playing Fear Songs Playlist')
 k=random.choice(fear_playlist)
 play_music(k)

def playConfused():
 print ('Playing Confused Songs Playlist')
 k=random.choice(confused_playlist)
 play_music(k)

def playCalm():
 print ('Playing Calm Songs Playlist')
 k=random.choice(calm_playlist)
 play_music(k)

#playHappy()
