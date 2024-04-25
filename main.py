import asyncio
async def pizza():
    print("Заказываем")
    await asyncio.sleep(3)
    print("Пицца доставлена")
async def film():
    print("Смотрим фильм")
    await asyncio.sleep(12)
    print("Фильм окончен!")
async def main():
    pizza_task = asyncio.create_task(pizza())
    movie_task = asyncio.create_task(film())
    await pizza_task
    await movie_task
asyncio.run(main())