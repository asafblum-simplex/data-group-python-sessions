import asyncio

async def numbers(nums):
    for i in range(nums):
        yield i
        await asyncio.sleep(0.5)

async def main():
    odd_nums = [i async for i in aiter(numbers(10)) if i % 2 == 0]
    print(odd_nums)


if __name__ == '__main__':
    print(__name__ == '__main__')    
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main())
    finally:
        event_loop.close()
