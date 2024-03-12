#111!/usr/bin/env python
# -*- coding: utf-8 -*

#Communicator script for handling sockets between client and server

import RPi.GPIO as GPIO
from websockets.server import serve
import asyncio
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)


async def process_input(websocket):
	async for message in websocket:
		msg = await websocket.recv()
		print(msg)

async def main():
    async with serve(process_input, "10.84.3.157", 5446):
        await asyncio.Future()  # run forever

asyncio.run(main())
