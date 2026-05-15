# разработка серверов с помощью пакета asyncio

# TCP сервер
import asyncio
import sys

handle_queries = lambda x: x


def main(address='127.0.0.1', port=2323): # функцию можно вызвать без аргументов
    port = int(port)
    loop = asyncio.get_event_loop()
    server_coro = asyncio.start_server(handle_queries, host=address, port=port) # возвращает asyncio.Server
    server = loop.run_until_complete(server_coro) # управляя сопрограммой получаем обьект server
    host = server.sockets[0].getsockname() # получаем адресс и порт сервера
    print('Serving on {}. Hit CTRL-C to stop.'.format(host))
    try:
        loop.run_forever() # выполняем цикл обработки событий
    except KeyboardInterrupt:
        pass # обработка Ctrl-C
    print('Server shutting down')
    server.close() # закрываем сервер
    loop.run_until_complete(server.wait_closed()) # wait_closed возвращает будующий обьект его нужно завершить
    loop.close() # завершаем циклы событий


if __name__ == '__main__':
    main(*sys.argv[1:]) # краткий способ передать аргументы в функцию


