#Creado por Fede

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QMessageBox
from PyQt5 import uic
import random
import urllib.request, zipfile
import os

random1 = random.randint(0,600)
random = random.randint(0,600)
#Clase Heredada de QmainWindows
class Options(QWidget):
	def __init__(self):
		QApplication.__init__(self)
		if os.name == "nt"
			uic.loadUi("ui\\options.ui",self)
		else:
			uic.loadUi("ui/option.ui",self)
		self.download.clicked.connect(self.descargar)
	def descargar(self):
		try:
			self.ubicacion = os.getcwd()
			now = time.time()
			aD = "https://codeload.github.com/sqlmapproject/sqlmap/zip/master"
			aG = "sqlmap.zip"
			fG = urllib.request.urlopen(aD)	
			fichero = open(aG,"wb")
			fichero.write(fG.read())
			fichero.close()

			extraer = zipfile.ZipFile("sqlmap.zip")
			extraer.extractall(self.ubicacion)
			extraer.close()
			if os.name == "nt":
				os.system("DEL sqlmap.zip")
			else:
				os.system("rm sqlmap.zip")
			elapsed = time.time() - now
			QMessageBox.information(self, "Exito","SQLMAP Descargado con exito\n Duracion: {}".format(elapsed))
		except:
			QMessageBox.warning(self, "Error","Error al Descargar SQLMAP Revisar su Conexion a Internet")

class Ventana(QMainWindow):
 	#Metodo Constructor de la clase
 	def __init__(self):
 		#Iniciar Objeto QMainWindows
 		QMainWindow.__init__(self)
 		#Cargar la configurcion del archivo .ui
 		if os.name == "nt":
 			uic.loadUi("ui\\main.ui",self)
 		else:
 			uic.loadUi("ui/main.ui",self)
 	#CheckBoxs
 		self.D.stateChanged.connect(self.d)
 		self.T.stateChanged.connect(self.t)
 		self.C.stateChanged.connect(self.c)
 		self.pagina.stateChanged.connect(self.Pagina)
 		self.gdork.stateChanged.connect(self.Gdork)
 		self.dbs.stateChanged.connect(self.db)
 		self.colums.stateChanged.connect(self.co)
 		self.tables.stateChanged.connect(self.ta)
 		self.randomagent.stateChanged.connect(self.random)
 		self.dump.stateChanged.connect(self.du)
 		self.dumpall.stateChanged.connect(self.duall)
 		self.passwords.stateChanged.connect(self.passw)
 		self.all.stateChanged.connect(self.todo)
 		self.tor.stateChanged.connect(self.Tor)
 		self.proxy.stateChanged.connect(self.Proxy)
 		self.data.stateChanged.connect(self.Data)
 		self.banner.stateChanged.connect(self.B)
 		self.cookie.stateChanged.connect(self.Cookie)
 	#Botones
 		self.Atacar.clicked.connect(self.ataque)
 		self.opciones.clicked.connect(self.option)
 	#Checkboxs Conexiones
 	def Cookie(self):
 		if self.cookie.stateChanged == 0:
 			self.cookies.setEnabled(False)
 			self.cookie.stateChanged = 1
 		else:
 			self.cookies.setEnabled(True)
 			self.cookie.stateChanged = 0
 	def B(self):
 		if self.banner.stateChanged == 0:
 			self.banner.stateChanged = 1
 		else:
 			self.banner.stateChanged = 0
 	def Data(self):
 		if self.data.stateChanged == 0:
 			self.dato.setEnabled(False)
 			self.data.stateChanged = 1
 		else:
 			self.dato.setEnabled(True)
 			self.data.stateChanged = 0
 	def Proxy(self):
 		if self.proxy.stateChanged == 0:
 			self.proxy.stateChanged = 1
 			self.proxi.setEnabled(False)
 		else:
 			self.proxi.setEnabled(True)
 			self.proxy.stateChanged = 0
 	def Tor(self):
 		if self.tor.stateChanged == 0:
 			self.tor.stateChanged = 1
 		else:
 			self.tor.stateChanged = 0
 	def todo(self):
 		if self.all.stateChanged == 0:
 			self.all.stateChanged = 1
 		else:
 			self.passwords.setChecked(False)
 			self.dbs.setChecked(False)
 			self.tables.setChecked(False)
 			self.colums.setChecked(False)
 			self.all.stateChanged = 0
 	def passw(self):
 		if self.passwords.stateChanged == 0:
 			self.passwords.stateChanged = 1
 		else:
 			self.all.setChecked(False)
 			self.dbs.setChecked(False)
 			self.colums.setChecked(False)
 			self.tables.setChecked(False)
 			self.passwords.stateChanged = 0

 	def du(self):
 		if self.dump.stateChanged == 0:
 			self.dump.stateChanged = 1
 		else:
 			self.dumpall.setChecked(False)
 			self.dump.stateChanged = 0
 	def duall(self):
 		if self.dumpall.stateChanged == 0:
 			self.dumpall.stateChanged = 1
 		else:
 			self.dump.setChecked(False)
 			self.dumpall.stateChanged = 0
 	def random(self):
 		if self.randomagent.stateChanged == 0:
 			self.randomagent.stateChanged = 1
 		else:
 			self.randomagent.stateChanged = 0
 	def ta(self):
 		if self.tables.stateChanged == 0:
 			self.tables.stateChanged = 1
 		else:
 			self.all.setChecked(False)
 			self.passwords.setChecked(False)
 			self.T.setChecked(False)
 			self.colums.setChecked(False)
 			self.dbs.setChecked(False)
 			self.tables.stateChanged = 0
 	def co(self):
 		if self.colums.stateChanged == 0:
 			self.colums.stateChanged = 1
 		else:
 			self.all.setChecked(False)
 			self.passwords.setChecked(False)
 			self.C.setChecked(False)
 			self.tables.setChecked(False)
 			self.dbs.setChecked(False)
 			self.colums.stateChanged = 0
 	def db(self):
 		if self.dbs.stateChanged == 0:
 			self.dbs.stateChanged = 1
 		else:
 			self.all.setChecked(False)
 			self.passwords.setChecked(False)
 			self.D.setChecked(False)
 			self.colums.setChecked(False)
 			self.tables.setChecked(False)
 			self.dbs.stateChanged = 0
 	def Pagina(self):
 		if self.pagina.stateChanged == 0:
 			self.paog.setText("")
 			self.pageorgd.setEnabled(False)
 			self.pagina.stateChanged = 1
 		else:
 			self.gdork.setChecked(False)
 			self.pageorgd.setEnabled(True)
 			self.paog.setText("Pagina:")
 			self.pagina.stateChanged = 0
 	def Gdork(self):
 		if self.gdork.stateChanged == 0:
 			self.pageorgd.setEnabled(False)
 			self.paog.setText("")
 			self.gdork.stateChanged = 1
 		else:
 			self.pagina.setChecked(False)
 			self.pageorgd.setEnabled(True)
 			self.paog.setText("Google Dork:")
 			self.gdork.stateChanged = 0
 	def d(self):
 		if self.D.stateChanged == 0:
 			self.DataBase.setEnabled(False)
 			self.D.stateChanged = 1
 		else:
 			self.dbs.setChecked(False)
 			self.DataBase.setEnabled(True)
 			self.D.stateChanged = 0
 	def t(self):
 		if self.T.stateChanged == 0:
 			self.Tabla.setEnabled(False)
 			self.T.stateChanged = 1
 		else:
 			self.tables.setChecked(False)
 			self.Tabla.setEnabled(True)
 			self.T.stateChanged = 0
 	def c(self):
 		if self.C.stateChanged == 0:
 			self.Columna.setEnabled(False)
 			self.C.stateChanged = 1
 		else:
 			self.colums.setChecked(False)
 			self.Columna.setEnabled(True)
 			self.C.stateChanged = 0
 	#Conexion Botones
 	def option(self):
 		v.show()
 	def ataque(self):
 		if os.name == "nt":
 			opcion = ""
 			opcion1 = ""
 			opcion2 = ""
 			opcion3 = ""
 			opcion4 = ""
 			opcion5 = ""
 			opcion6 = " --level={}".format(self.level.value())
 			opcion7 = " --risk={}".format(self.risk.value())
 			opcion8 = ""
 			opcion9 = ""
 			opcion10 = ""
 			opcion11 = ""
 			opcion12 = ""
 			if self.pagina.stateChanged == 0:
 				opcion = "-u {}".format(self.pageorgd.text())
 			elif self.gdork.stateChanged == 0:
 				opcion = "-g {}".format(self.pageorgd.text())
 			if self.dbs.stateChanged == 0:
 				opcion1 = " --dbs"
 			elif self.tables.stateChanged == 0:
 				opcion1 = " --tables"
 			elif self.colums.stateChanged == 0:
 				opcion1 = " --colums"
 			elif self.all.stateChanged == 0:
 				opcion1 = " -a"
 			if self.randomagent.stateChanged == 0:
 				opcion2 = " --random-agent"
 			if self.D.stateChanged == 0:
 				opcion3 = " -D {}".format(self.DataBase.text())
 			if self.T.stateChanged == 0:
 				opcion4 = " -T {}".format(self.Tabla.text())
 			if self.C.stateChanged == 0:
 				opcion5 = " -C {}".format(self.Columna.text())
 			if self.dump.stateChanged == 0:
 				opcion8 = " --dump"
 			elif self.dumpall.stateChanged == 0:
 				opcion8 = " --dump-all"
 			if self.banner.stateChanged == 0:
 				opcion9 = " -b"
 			if self.tor.stateChanged == 0:
 				opcion10 = " --tor"
 			if self.proxy.stateChanged == 0:
 				opcion11 = " --proxy={}".format(self.proxi.text())
 			if self.cookie.stateChanged == 0:
 				opcion12 = " --cookie={}".format(self.cookies.text())
 			if os.name == "nt":
 				os.system("python2 sqlmap-master\\sqlmap.py "+opcion+opcion1+opcion2+opcion3+opcion4+opcion5+opcion6+opcion7+opcion8+opcion9+opcion10+opcion11+opcion12)
 			elif os.name == "posix":
 				os.system("python2 sqlmap-master/sqlmap.py "+opcion+opcion1+opcion2+opcion3+opcion4+opcion5+opcion6+opcion7+opcion8+opcion9+opcion10+opcion11+opcion12)


if __name__ == "__main__":
	try:
		app = QApplication(sys.argv)

		v = Options()
		ventana = Ventana()
		ventana.show()

		app.exec_() 
	except KeyboardInterrupt:
		print("Adios")
		sys.exit()