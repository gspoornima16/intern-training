from fastapi import FastAPI, WebSocket

app = FastAPI()
clients=[]
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            print("Message received:", message)
            for client in clients:
                await client.send_text(message)
    except Exception:
        if websocket in clients:
            clients.remove(websocket)
        print("Client disconnected")
