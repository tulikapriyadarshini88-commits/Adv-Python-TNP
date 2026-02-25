# Traffic Light Simulation System
"""
1.three light enter(if-else condition)
2.timer ("how long each light stays on")
3.zebra croseing for walking people

"""
import time

def traffic_light_simulation(): 
    lights=["red","yellow","green"]
    i=0

    while True:
        current_light=lights[i]

        if current_light=="red":
           print("\nred light on:🔴:")
           print("cars stop:.✋.:")
           print("pedustrain can cross🚶:")
           time.sleep(5)

        elif current_light=="yellow":
           print("\nyellow light on:🟡:")
           print("cars ready to go:.👍.:")
           print("pedustrain stop.✋.")
           time.sleep(2)

        else:
           print("\ngreen light on:🟢:")
           print("cars go:👌:")
           print("pedustrain can be stop:.✋.:")
           time.sleep(5)
         
        i = (i + 1) % 3 

traffic_light_simulation()