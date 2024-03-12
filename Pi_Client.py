#111!/usr/bin/env python
# -*- coding: utf-8 -*

#Communicator script for handling sockets between client and server

import RPi.GPIO as GPIO
from websockets.server import serve
import asyncio
import time
import subprocess
from threading import Thread
bool = False

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

def MTX_Setup():
	subprocess.run(["mediamtx"])

Thread(target=MTX_Setup).start()


async def process_input(websocket):
	global bool
	while True:
		async for msg in websocket:
			if (msg == "HIGH"):
				if not bool:
					bool = True
					GPIO.output(17,GPIO.HIGH)
					print("Set High")
			else:
				if bool:
					bool = False
					GPIO.output(17,GPIO.LOW)
					print("Set Low")


loop = asyncio.get_event_loop()
server = serve(process_input, '10.84.3.157', 5446)
loop.run_until_complete(asyncio.gather(server))
loop.run_forever()
