import unittest
import raul_youtube as yt
import ana_db as db

class TestYT(unittest.TestCase):

    def test_guardar(self):

        self.assertEqual(db.SQlite.GuardarVideo('La noche',13,'El día', "04 feb 2018", 5000, 10000,'Este video es chido'), video)
        self.assertEqual(db.SQlite.GuardarVideo(), None)

    def test_mostrarLista(self):
        lista = MostrarLista()
        self.assertEqual(db.SQlite.MostrarLista(), videos)
        self.assertEqual(db.SQlite.MostrarLista(id), 'CHECK: deberia mandar error por psarle un ID')

    def test_mostrarVideo(self):

        self.assertEqual(db.SQlite.MostrarVideo(10), video)
        self.assertEqual(db.SQlite.MostrarVideo('whazup'), 'CHECK: deberia mandar error por mandarle un string')
        self.assertEqual(db.SQlite.MostrarVideo(), 'CHECK: deberia mandar error por no pasarle ID')

    def test_modVideo(self):

        #Buenas noches',13,'Buenas tardes', "10 marzo 2018", 38000, 170000,'Este video es chido', 5
        self.assertEqual(db.SQlite.ModificarVideo(5) , video)
        self.assertEqual(db.SQlite.ModificarVideo(), 'CHECK: deberia mandar error por no darle datos')

    def test_borrar(self):
        self.assertEqual(db.SQlite.BorrarVideo(5), True)
        self.assertEqual(db.SQlite.BorrarVideo(), 'CHECK: deberia mandar error por no pasarle un ID')
        self.assertEqual(db.SQlite.BorrarVideo('hola'), 'CHECK: deberia mandar error por pasarle un String')


    def test_close(self):
        
        self.assertEqual(db.SQlite.Close(), 'Conexión cerrada correctamente')
        #########################################
    """TEST raul_youtube"""

    def test_infoVideo(self):

        self.assertEqual(yt.AppYoutube.InfoVideo('https://www.youtube.com/watch?v=6B9J3lEyffA'), Video)
        self.assertEqual(yt.AppYoutube.InfoVideo('https://www.youtube.com/watch?v=7IXJb'), 'CHECK: deberia mandar un error porque este es un link de YT pero no contiene video')
        self.assertEqual(yt.AppYoutube.InfoVideo('achettp://yutub.com/olakase'),"CHECK: deberia mandar error porque ese ni si quiera es un link, es otro string")
        self.assertEqual(yt.AppYoutube.InfoVideo(1745),"CHECK: deberia mandar error porque ese es un numero")


if __name__ == '__main__':
    unittest.main()
