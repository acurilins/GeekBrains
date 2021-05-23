from time import sleep


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        i = 0
        while i < 3:
            print(f'Traffic Lights has changed the color to: \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# import time
# import itertools

# class TrafficLight:
#     __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]
    
#     def running(self):
#         for light in itertools.cycle(self.__color):
#             print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
#             time.sleep(light[1][0])
            
            
# trafficlight = TrafficLight()
# trafficlight.running()
