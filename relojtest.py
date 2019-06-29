import time
import datetime
import SDL_DS1307


ds1307 = SDL_DS1307.SDL_DS1307(1, 0x68)
ds1307.write_now()

# Main Loop - sleeps 10 seconds, then reads and prints values of all clocks

t0 = ds1307._read_hours()

while True:


 print ""
 print "Raspberry Pi=\t" + time.strftime("%Y-%m-%d %H:%M:%S")

 print "DS1307=\t\t%s" % ds1307.read_datetime()

 time.sleep(2.0)
 t1 = ds1307._read_hours()
 print ("tiempo = "+ str(t1-t0))
 t0=t1

