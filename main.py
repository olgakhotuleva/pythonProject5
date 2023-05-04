import asyncio
import os
import aiofiles
import requests
import re
from bs4 import BeautifulSoup

# async def download(url: str) -> None:
#     result = await wget.download(url)
#     print(f"file {result} is downloaded")

async def download(url: str) -> None:
    title = re.search(r"/([\w-]+)\-mp3\.mp3$", url)
    print("\nStart download:" + url)
    async with aiofiles.open(title.group(1) + '.mp3', 'wb') as f:
        await f.write(requests.get(url).content)
        print(f"file {title.group(1)} is downloaded in \"{os.getcwd()}\"")


async def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    URL_TEMPLATE = "https://mp3uks.ru/"

    r = requests.get(URL_TEMPLATE)
    bs = BeautifulSoup(r.text, "lxml")

    await asyncio.gather(*[download('https:' + link.get('href')) for link in bs.find_all('a', 'track-dl')])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(print_hi('PyCharm'))
