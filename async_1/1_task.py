import asyncio
import time


async def interviews(*args):
    async def process_interview(name, time_prof1, time_def1, time_prof2, time_def2):
        print(f"{name} started the 1 task.")
        await asyncio.sleep(time_prof1 / 100)
        print(f"{name} moved on to the defense of the 1 task.")
        await asyncio.sleep(time_def1 / 100)
        print(F"{name} completed the 1 task.")

        print(f"{name} is resting.")
        await asyncio.sleep(5 / 100)

        print(f"{name} started the 2 task.")
        await asyncio.sleep(time_prof2 / 100)
        print(f"{name} moved on to the defense of the 2 task.")
        await asyncio.sleep(time_def2 / 100)
        print(F"{name} completed the 2 task.")

    tasks = []
    for name, time_prof1, time_def1, time_prof2, time_def2 in args:
        tasks.append(asyncio.create_task(process_interview(
            name, time_prof1, time_def1, time_prof2, time_def2)))
    await asyncio.gather(*tasks)