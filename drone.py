from djitellopy import tello
from time import sleep

tello = tello.Tello()
me.connect()
print(me.get_battery())

# takeoff to 200 cm
tello.takeoff()
tello.move_up(120)

# fly for 456 cm and turn
tello.move_forward(456)
tello.rotate_counter_clockwise(90)
sleep(.5)

# fly for 400 cm and turn
tello.move_forward(400)
tello.rotate_counter_clockwise(90)
sleep(.5)

# fly for 456 cm and turn
tello.move_forward(456)
tello.rotate_counter_clockwise(90)
sleep(.5)

# fly for 400 cm and land
tello.move_forward(400)
tello.land()
