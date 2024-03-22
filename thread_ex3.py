import asyncio
import random

async def show(x):
    x = random.sample([1,2,3,4,5], k=1)
    await asyncio.sleep(x[0])
    print(x)
count = 0
async def main():       # 비동기 처리
    await asyncio.gather(
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
    )

def xx():
    print("동기 처리")

asyncio.run(main())

xx()    # 동기 처리