import websockets
import asyncio

PORT = 7890  # should be local variable

print("server listening on port " + str(PORT))
print("Waiting for connections")


async def echo(websocket, path):
    print("A client has connected")
    try:
        async for message in websocket:
            print("Receive message from client: " + message)
#            await websocket.send("Pong: " + message)
#            while True:
            command = input("Enter command: ")
            await websocket.send(command)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client disconnected")
#        print(e)

start_server = websockets.serve(echo, "localhost", PORT)  # 0.0.0.0

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# I need a way to check multiple connections, for that probably will need the input
# object to go up.