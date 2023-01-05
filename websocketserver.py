import asyncio
import websockets

async def handler(websocket, path):
    print("A client just connected")
    try:
        data = await websocket.recv()
        reply = f"Data recieved as:  {data}!"
        await websocket.send(reply)
    except websockets.exceptions.ConnectionClosed:
        print("A client just disconnected")

start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()