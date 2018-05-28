import unittest
from unittest.mock import Mock
from raul_youtube import AppYoutube
from ana_db import SQlite
from dime import Video, AbstractRepo, AbstractYoutube

class TestYTapp(unittest.TestCase):

    def setUp(self):

        self.videomock = Mock(Id = 5, Nombre = "Zelda Medley", Duracion = "PT3M37S", Canal = "Melodica Men",  Fecha= "2018-03-05T15:59:48.000Z", Likes = '39987', Vistas = '844974', Descripcion = "Get your melodica at www.melodicamen.com!\n\nLove what we do? Support us on Patreon! https://www.patreon.com/melodicamen")
        self.video = Video(self.videomock.Nombre,self.videomock.Duracion,self.videomock.Canal,self.videomock.Fecha,self.videomock.Likes,self.videomock.Vistas,self.videomock.Descripcion)
        self.sql = SQlite()
        self.sql.GuardarVideo(self.video)
        self.yt = AppYoutube()

        ################################
        self.video1 = Video('La noche',13,'El día', "04 feb 2018", 5000, 10000,'Este video es chido')
        #self.video2 = Video('Video 10.4', 15, 'sup', '25 jul 2016', 10000, 55000, 'Dale like')
        #self.badurl = url('https://www.youtube.com/watch?v=7IXJb')
        #self.nourl = url('achettp://yutub.com/olakase')
        self.id = 1
        #self.lista = MostrarLista()


    def tearDown(self):
        print("Fin de la prueba")

    #Hace las pruebas de guardar un video y que todos sus atributos estén almacenados correctamente
    def test_Video(self):

        print("test_Video")
        self.assertEqual(self.video1.Nombre, ('La noche'))
        self.assertEqual(self.video1.Duracion, 13 )
        self.assertEqual(self.video1.Canal, 'El día' )
        self.assertEqual(self.video1.Fecha, "04 feb 2018" )
        self.assertEqual(self.video1.Likes, 5000 )
        self.assertEqual(self.video1.Vistas, 10000 )
        self.assertEqual(self.video1.Descripcion, 'Este video es chido' )
        #Revisando el tipo de dato
        self.assertNotEqual(self.video1.Duracion, '13')
        self.assertNotEqual(self.video1.Likes, '5000' )
        self.assertNotEqual(self.video1.Vistas, '10000' )

    """TEST raul_youtube"""

    def test_infoVideo(self):

        print("test_infoVideo")

        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=j2KonMkk6To").Nombre, self.video.Nombre)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=j2KonMkk6To").Duracion, self.video.Duracion)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=j2KonMkk6To").Canal, self.video.Canal)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=j2KonMkk6To").Fecha, self.video.Fecha)
    #    self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=j2KonMkk6To").Likes, self.video.Likes)
    #    self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=j2KonMkk6To").Vistas, self.video.Vistas)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=j2KonMkk6To").Descripcion, self.video.Descripcion)


    def test_guardar(self):

        print("test_guardar")
        self.assertIsInstance(self.sql.GuardarVideo(self.video), Video)

    #def test_mostrarLista(self):

    #    self.assertIsInstance(self.lista, videos)
    #    #self.assertRaises(SQlite.lista(self.id), 'CHECK: deberia mandar error por psarle un ID')

    #def test_mostrarVideo(self):

    #    self.assertIsInstance(self.sql.MostrarVideo(5), Video)

    #def test_modVideo(self):

        #Buenas noches',13,'Buenas tardes', "10 marzo 2018", 38000, 170000,'Este video es chido', 5
    #    self.assertEqual(SQlite.ModificarVideo(self.id) , video)
    #    self.assertEqual(SQlite.ModificarVideo(), 'CHECK: deberia mandar error por no darle datos')

    def test_borrar(self):

        print("test_borrar")
        self.assertTrue(self.sql.BorrarVideo(5))

    def test_close(self):

        print("test_close")
        self.assertTrue(self.sql.Close())

if __name__ == '__main__':
    unittest.main()
