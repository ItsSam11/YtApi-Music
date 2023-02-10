import requests
import pafy
import vlc
import time
import os
import asyncio

api_key = '*****'
instance = vlc.Instance()
player = instance.media_player_new()
    
async def yt_video(query):
    
    try:
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={api_key}&maxResults=1"
        response = requests.get(url)
        data = response.json()

    except Exception as e:
        print(e)

    global lst
    global name
    lst = dict()
    for item in data["items"]:
        ids = item['id']['videoId']
        name = item['snippet']['title']
        lst[name] = ids

    urlyt = f'https://www.youtube.com/watch?v={lst[name]}'

    return urlyt

async def yt_duration():
    url = f'https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id={lst[name]}&key={api_key}'

    response = requests.get(url)
    data = response.json()
    duration = data['items'][0]['contentDetails']['duration']

    return duration

async def main():

    while True:
        query = str(input('Escribe una cancion con su artista: '))

        if len(query) > 0 :
            print(f'Lo que quieres escuchar es: {query}')

            url = await yt_video(query)
            video = pafy.new(url)
            b_audio = video.getbestaudio()
            audio_stream = b_audio.url

            # d = await yt_duration()
            # print(d)

            print(audio_stream)

            media = instance.media_new(audio_stream)
            player.set_media(media)
            player.play()

        else:
            print('¡Escribe un artista o canción!')
            time.sleep(2.5)
            os.system('cls')

if __name__ == '__main__':
    asyncio.run(main())