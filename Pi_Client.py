#111!/usr/bin/env python
# -*- coding: utf-8 -*

#Communicator script for handling sockets between client and server

import RPi.GPIO as GPIO
from websockets.server import serve
import asyncio
import time
import subprocess
from threading import Thread
left = False
right = False
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

def MTX_Setup():
	subprocess.run(["mediamtx"])

Thread(target=MTX_Setup).start()


async def process_input(websocket):
	global bool
	while True:
		async for msg in websocket:
			highbuffer = []
			lowbuffer = []
			if msg == "FORWARD":
				highbuffer.append(17)
				highbuffer.append(27)
			elif msg == "LEFT":
				lowbuffer.append(17)
				highbuffer.append(27)
			elif msg == "RIGHT":
				lowbuffer.append(27)
				highbuffer.append(17)
			elif msg == "STOP":
				highbuffer.append(17)
				highbuffer.append(27)
			print("Activated: " + str(highbuffer))
			print("Deactivated: " + str(lowbuffer))
			GPIO.output(highbuffer,GPIO.HIGH)
			GPIO.output(lowbuffer, GPIO.LOW)
loop = asyncio.get_event_loop()
server = serve(process_input, '10.84.3.157', 5446)
loop.run_until_complete(asyncio.gather(server))
loop.run_forever()
