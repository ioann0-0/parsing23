import os
import aiohttp
import asyncio
from PIL import Image
from io import BytesIO

output_folder = 'images_aiohttp'
os.makedirs(output_folder, exist_ok=True)

url = 'https://randompicture.xyz/'

async def fetch_image(session, i):
    async with session.get(f'{url}?random={i}') as response:
        if response.status == 200:
            img_data = await response.read()
            img = Image.open(BytesIO(img_data))
            img.save(os.path.join(output_folder, f'image_{i+1}.jpg'))

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_image(session, i) for i in range(10)]
        await asyncio.gather(*tasks)

asyncio.run(main())
