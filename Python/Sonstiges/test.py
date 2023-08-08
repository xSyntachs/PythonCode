from PyP100 import PyP100

p100 = PyP100.P100("192.168.0.131", "lrumke5@gmail.com", "Tonino2105??!")
p100.handshake()
p100.login()
p100.turnOff() # Turns the connected plug off
p100.turnOn() # Turns the connected plug on
