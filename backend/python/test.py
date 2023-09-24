import json
import asyncio
import websockets

async def send_message():
    async with websockets.connect('ws://localhost:8080') as websocket:
        message = {
            'type': 'message',
            'message': 'Hello, world!',
            'nickname': "donald"
        }
        await websocket.send(json.dumps(message))

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(send_message())