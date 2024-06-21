import asyncio

async def foo():
    print("Start")
    await printName()
    print("Ended")

async def printName():
    await print("Name") 

