from fastapi import FastAPI
from asyncio import sleep
from sse_starlette.sse import EventSourceResponse

app=FastAPI()
async def countdown():
    count=0
    while True:
        count+=1
        yield f"Count: {count}"
        await sleep(5)

@app.get("/events")
async def events():
    return EventSourceResponse(countdown())