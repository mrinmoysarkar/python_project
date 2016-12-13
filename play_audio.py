import vlc
import os
from playsound import playsound
import os
import time



home_dir  = "/home/pi/Music/" 
list_of_file = os.listdir(home_dir)
#print(list_of_file)
file_name = "mpg321 \"" + home_dir + list_of_file[7] + "\" &"
print(file_name)

os.system(file_name)
time.sleep(30)
print ("killling app\n")
os.system('pkill mpg321')
#playsound(file_name)

#p = vlc.MediaPlayer(file_name)
#p.play()

#p.stop()
