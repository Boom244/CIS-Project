#111!/usr/bin/env python
# -*- coding: utf-8 -*

#Communicator script for handling sockets between client and server

import RPi.GPIO as GPIO
import socket
import os
import time

HOST = None
PORT = None
config = None
flash = True

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

if os.path.exists("recv-server.txt"):
    print("Loading settings:")
    config = open("recv-server.txt").readlines()
    HOST = config[0]
    PORT = int(config[1])
else:
    HOST = input("Config not found. Input host IP:")
    PORT = input("Port:")
    file = open("recv-server.txt","x")
    file.write(HOST)
    file.write(PORT)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,int(PORT)))
    s.listen()
    conn,addr = s.accept()
    with conn:
        print(f"Connected to {addr}")
        while True:
            data = conn.recv(1024)
            if data:
                print("Connected to server, latency: " + str(round(time.time() * 1000) - data) + " ms")
                GPIO.output(18, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(18, GPIO.LOW)
                time.sleep(1)
                GPIO.output(18, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(18, GPIO.LOW)
               



