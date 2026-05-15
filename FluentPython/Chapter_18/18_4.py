# от обратных вызовов к будущим объектам и сопрограмам
import asyncio

#JS style

# func api_call1(request1, (response1)=> {
#     var request2 = step(response1);
# })

# Python function style

def stage1(response1):
    request2 = step1(response1)
    api_call2(request2, stage2)


def stage2(response2):
    request3 = step2(response2)
    api_call3(request3, stage3)


def stage3(response3):
    step3(response3)

api_call(reqest, stage1)


# python asyncio style
@asyncio.coroutine
def three_stages(request1):
    response1 = yield from api_call(request1)
    request2 = step1(response1)
    response2 = yield from api_call2(request2)
    request3 = step2(response2)
    response3 = yield from api_call3(request3)
    stage3(response3)


def run_loop():
    loop = asyncio.get_event_loop()
    loop.create_task(three_stages(request1)) # запланировать выполнение сопрограммы
