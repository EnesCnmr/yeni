import uvicorn
import asyncio
from fastapi import FastAPI
async def app(scope,receive,send):
    assert scope['type']=='http '
    await send({
        'type':'http.response.start',
        'status':200,
        'headers':[
            [b'content-type',b'text/plain'],
        ],
    })
    await send({
        'type':'http.response.body',
        'body':b'Hello, world!',
    })
    if __name__=="__main__" :
        uvicorn.run("main:app", port=5000 , log_level="info")
        config = uvicorn.Config("main:app", port=5000, log_level="info")
        server = uvicorn.Server(config)
        server.run()
        asyncio.run(())
    