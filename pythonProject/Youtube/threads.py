# it is just as multi tasking. it means excuting 2 functions on the same time, or 2 programs on the same time
from time import sleep
from threading import *

# class hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("hello")
# class hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("hi")
#
# ob = hello()
# ob2= hi()
#
# ob.start()
# ob2.start()

class hello(Thread):
    def run(self):
        for i in range(8):
            print("hello")
            sleep(1)
class hi(Thread):
    def run(self):
        for i in range(8):
            print("hi")
            sleep(1)  # here we use sleep to allow our program to delay for a second

ob = hello()
ob2= hi()

ob.start()      # to stop the collision from the same thread we use sleep inbetween
sleep(.2)  # here we delay the execution of ob2 by 0.2 seconds
ob2.start()

ob.join()    # we use join to allow them to finish running before the final print("end") we run
ob2.join()
print("end")


