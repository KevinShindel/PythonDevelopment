# вебсервер на основе библиотеки aiohttp
import asyncio

from aiohttp import web


def home(request):
    query = request.GET.get('query', ''.strip())
    print('Query: {!r}'.format(query))
    if query:
        descriptions = list(index.find_descriptions(query))
        res = '\n'.join(ROW_TPL.format(**vars(descr) for descr in descriptions))
        msg = index.status(query, len(descriptions))
    else:
        descriptions = []
        res = ''
        msg = 'Enter words describing characters'
    html = template.format(query=query, result=res, message=msg)
    print('Sending {} results'.format(len(descriptions)))
    return web.Response(content_type=CONTENT_TYPE, text=html)

@asyncio.coroutine
def init(loop, address, port): # отдает сервер который будет обрабатывать запросы в цикле событий
    app = web.Application(loop=loop) # предоставляет веб-приложение
    app.router.add_route(method='GET', path='/', handler=home) # создаём роутинг
    handler = app.make_handler()  #
    server = yield from loop.create_server(handler, address, port)
    return server.sockets[0].getsocketname()

def main(address='127.0.0.1', port=8888):
    port = int(port)
    loop = asyncio.get_event_loop()
    host = loop.run_until_complete(init(loop, address, port))
    print('Serving on {}. Hit Ctrl-C to stop.'.format(host))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    loop.close()
