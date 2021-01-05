#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#https://docs.python.org/3/library/asyncio-task.html#asyncio.run
#原代码报错后，参考了https://stackoverflow.com/questions/59719022/aiohttp-application-make-handler-is-deprecated-adding-multiprocessing
#------------Day 1
import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time

from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Hello Me and You</h1>',content_type='text/html')

#@asyncio.coroutine 在版本3已经改成async def的格式，更加简便
async def init(loop):
#	app = web.Application(loop=loop) loop=loop已被取消
	app = web.Application()
	app.router.add_route('GET','/',index)
#	srv = await loop.create_server(app_runner,'127.0.0.1', 9000） 被后4句取代
	app_runner = web.AppRunner(app)
	await app_runner.setup()
	srv = web.TCPSite(app_runner,'127.0.0.1',9000)
	await srv.start()
	logging.info('server started at http://127.0.0.1:9000...')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

app = web.Application(loop=loop, middlewares=[
    logger_factory, response_factory
])
init_jinja2(app, filters=dict(datetime=datetime_filter))
add_routes(app, 'handlers')
add_static(app)