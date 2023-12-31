import blynklib
import blynktimer
import random

BLYNK_AUTH = '13C11QioOoHqQmMyjxYRqxpOC3AWdmpi'  # insert your Auth Token here
blynk = blynklib.Blynk(BLYNK_AUTH)

# create timers dispatcher instance
timer = blynktimer.Timer()

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_WRITE] Pin: V{} Value: '{}'"

# Code below: register two timers for different pins with different intervals
# run_once flag allows to run timers once or periodically
@timer.register(vpin_num=0, interval=4, run_once=False)
@timer.register(vpin_num=1, interval=7, run_once=False)
def write_to_virtual_pin(vpin_num=0):
    value = random.randint(0, 20)
    print(WRITE_EVENT_PRINT_MSG.format(vpin_num, value))
    blynk.virtual_write(vpin_num, value)


while True:
    blynk.run()
    timer.run()