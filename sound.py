#computer sound song
import winsound
y = 330
x = 1
z = 230
audio = open("song.mp3", "w")
endloop = 10
while x <= endloop:
 winsound.Beep(130, 210)
 winsound.Beep(210, 230)
 winsound.Beep(190, 290)
 winsound.Beep(231, 232)
 winsound.Beep(131, 231)
 winsound.Beep(130, 122)
 winsound.Beep(234, 210)
 x=x+1
 y=y+1
 z=z+1 
 if x == 5:
     winsound.Beep(100, 400)
     
    
