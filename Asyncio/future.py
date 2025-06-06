import asyncio

async def set_future_result(future, value):
    await asyncio.sleep(2)
    #set the result for future 
    future.set_result(value)
    print(f"Set the future's result to: {value}")

async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    asyncio.create_task(set_future_result(future, "Future result is ready"))

    result = await future
    print(f"Received the future's result: {result}")

asyncio.run(main())
