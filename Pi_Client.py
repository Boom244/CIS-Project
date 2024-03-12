#111!/usr/bin/env python
# -*- coding: utf-8 -*

#Communicator script for handling sockets between client and server

import RPi.GPIO as GPIO
from websockets.server import serve
import asyncio
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)


async def process_input(websocket):
	while True:
		async for message in websocket:
			msg = await websocket.recv()
			if (msg == "HIGH"):
				GPIO.output(17,GPIO.HIGH)
			else:
				GPIO.output(17,GPIO.LOW)


loop = asyncio.get_event_loop()
server = serve(process_input, '10.84.3.157', 5446)
loop.run_until_complete(asyncio.gather(server))
loop.run_forever()