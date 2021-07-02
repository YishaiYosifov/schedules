import schedules
Every = schedules.every()
async def test():
    print(1)
Every.second(1).start(target=test, asynchronous=True, repeat=True)