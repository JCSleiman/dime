from apiclient.discovery import build
from dime import Video
from dime import AbstractYoutube
import emoji

class AppYoutube(AbstractYoutube):
    def InfoVideo(self, url):

        API_KEY = 'AIzaSyAF3BIAdtEu6Y3NR_BtkhViMfOGRxCD84Q'
        youtube = build('youtube', 'v3', developerKey=API_KEY)

        ids = url[32:43]
        results = youtube.videos().list(id=ids, part='snippet').execute()
        for result in results.get('items', []):
            NombreCanal = emoji.demojize(result['snippet']['channelTitle'])
            Titulo = emoji.demojize(result['snippet']['title'])
            Descripcion = emoji.demojize(result['snippet']['description'])
            Publicacion = result['snippet']['publishedAt']


        results1 = youtube.videos().list(id=ids, part='statistics').execute()
        for result2 in results1.get('items', []):
            Likes = result2['statistics']['likeCount']
            Vistas = result2['statistics']['viewCount']


        results4 = youtube.videos().list(id=ids, part='contentDetails').execute()
        for result5 in results4.get('items', []):
            Duracion = result5['contentDetails']['duration']

        return Video(Titulo, Duracion, NombreCanal, Publicacion, Likes, Vistas, Descripcion)

if __name__ == '__main__':
    y = AppYoutube()
    #https://www.youtube.com/watch?v=j2KonMkk6To
    vid = y.InfoVideo('achettp://yutub.com/olakase')

    print(vid.Descripcion)
