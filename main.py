import aiohttp
from aiohttp import web

from controller import Controller

page = open('index.html').read()

engineA = Controller(7, 11)
engineB = Controller(13, 15)
engineC = Controller(29, 31)
engineD = Controller(33, 37)


def stop():
    engineA.stop()
    engineB.stop()
    engineC.stop()
    engineD.stop()


def forward():
    print('forward')
    engineA.forward()
    engineB.forward()
    engineC.forward()
    engineD.forward()


def back():
    engineA.back()
    engineB.back()
    engineC.back()
    engineD.back()


def turn_left():
    engineA.back()
    engineB.forward()
    engineC.back()
    engineD.forward()


def turn_right():
    engineA.forward()
    engineB.back()
    engineC.forward()
    engineD.back()


async def index(request):
    return web.Response(text=page, content_type='text/html')


async def websocket(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            print(msg.data)
            if msg.data == '0':
                stop()
            elif msg.data == '1':
                forward()
            elif msg.data == '2':
                back()
            elif msg.data == '3':
                turn_left()
            elif msg.data == '4':
                turn_right()

        if msg.type == aiohttp.WSMsgType.ERROR:
            print(ws.exception())
            return


app = web.Application()

app.add_routes([web.get('/', index), web.get('/websocket', websocket)])

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8888)
