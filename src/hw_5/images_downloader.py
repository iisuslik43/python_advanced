from argparse import ArgumentParser
from pathlib import Path
import aiohttp
import asyncio
import aiofiles


async def download_one_image(filename):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://picsum.photos/200') as response:
            print('Downloading file', filename)
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            f = await aiofiles.open(filename, mode='wb')
            await f.write(await response.read())
            await f.close()


async def download_images(directory: str, images_count: int):
    tasks = []
    for i in range(images_count):
        filename = Path(directory) / f'img{i + 1}.jpeg'
        tasks.append(download_one_image(filename))
    await asyncio.gather(*tasks)


def main():
    parser = ArgumentParser()
    parser.add_argument('--dir', type=str, required=True)
    parser.add_argument('--count', type=int, required=True)
    args = parser.parse_args()
    directory, images_count = args.dir, args.count
    asyncio.run(download_images(directory, images_count))


if __name__ == '__main__':
    main()
