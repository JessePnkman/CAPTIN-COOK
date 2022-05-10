
from djtellopy import tello
from time import sleep

me = tello.Tello()
me.connect()

print(me.get.battery())

me.land()
