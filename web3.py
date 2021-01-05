import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

connected = False

def aiohttp_server():
    async def handler(msg, session):
        global connected
        if msg.type == sockjs.MSG_OPEN:
            connected = True
        if msg.type == sockjs.MSG_CLOSE:
            connected = False

    app = web.Application()
    sockjs.add_endpoint(app, handler)
    return web.AppRunner(app)

async def run_server(ready):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')
    runner = aiohttp_server()
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    ready.set()
    # emulates loop.run_forever()
    await asyncio.get_running_loop().create_future()

def start_server():
    ready = threading.Event()
    threading.Thread(target=asyncio.run, args=(aiohttp_server(ready),),
                     daemon=True).start()
    ready.wait()

    run_server()