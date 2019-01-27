from tkinter import *
from tkinter import messagebox
from tkinter import font
import os, time, zipfile
import urllib.request

ventana = Tk()
ventana.title("Menu de SQLMAP")
ventana.geometry("400x350")
def Descargar():
	try: 
		mensajito = messagebox.showwarning("Descargando", "Descargando SQLMAP Espere...")
		now = time.time()
		aD = "https://codeload.github.com/sqlmapproject/sqlmap/zip/master"
		aG = "sqlmap.zip"
		fG = urllib.request.urlopen(aD)	
		fichero = open(aG,"wb")
		fichero.write(fG.read())
		fichero.close()

		extraer = zipfile.ZipFile("sqlmap.zip")
		extraer.extractall(ubicacion)
		extraer.close()

		elapsed = time.time() - now
		if sysop == "nt":
			os.system("DEL sqlmap.zip")
		else:
			os.system("rm sqlmap.zip")
		mensajito = messagebox.showinfo("Descargado","SQLMAP Descargado con Exito\n Duracion: {}".format(elapsed))
	except:
		mensajito = messagebox.showwarning("Error", "Error al Descargar Por Favor Verifique su Conexion a Internet")
def Accept():
	opciones.quit()
def colores():
	if ColorChange.get() == "black":
		ventana.configure(bg=ColorChange.get())
		dbs.configure(bg=ColorChange.get(), fg="white")
		tables.configure(bg=ColorChange.get(), fg="white")
		colums.configure(bg=ColorChange.get(), fg="white")
		pagina.configure(bg=ColorChange.get(), fg="white")
		googleD.configure(bg=ColorChange.get(), fg="white")
		co.configure(bg=ColorChange.get(), fg="white")
		dump.configure(bg=ColorChange.get(), fg="white")
		dumpall.configure(bg=ColorChange.get(), fg="white")
		randoma.configure(bg=ColorChange.get(), fg="white")
		usera.configure(bg=ColorChange.get(), fg="white")
		Texto.configure(bg=ColorChange.get(), fg="white")
		Level.configure(bg=ColorChange.get(), fg="white")
		ries.configure(bg=ColorChange.get(), fg="white")
		ta.configure(bg=ColorChange.get(), fg="white")
		db.configure(bg=ColorChange.get(), fg="white")
	elif ColorChange.get() == "white" or "blue":
		ventana.configure(bg=ColorChange.get())
		dbs.configure(bg=ColorChange.get(), fg="black")
		tables.configure(bg=ColorChange.get(), fg="black")
		colums.configure(bg=ColorChange.get(), fg="black")
		pagina.configure(bg=ColorChange.get(), fg="black")
		googleD.configure(bg=ColorChange.get(), fg="black")
		co.configure(bg=ColorChange.get(), fg="black")
		dump.configure(bg=ColorChange.get(), fg="black")
		dumpall.configure(bg=ColorChange.get(), fg="black")
		randoma.configure(bg=ColorChange.get(), fg="black")
		usera.configure(bg=ColorChange.get(), fg="black")
		Texto.configure(bg=ColorChange.get(), fg="black")
		Level.configure(bg=ColorChange.get(), fg="black")
		ries.configure(bg=ColorChange.get(), fg="black")
		ta.configure(bg=ColorChange.get(), fg="black")
		db.configure(bg=ColorChange.get(), fg="black")

	ventana.configure(bg=ColorChange.get())
	dbs.configure(bg=ColorChange.get())
	tables.configure(bg=ColorChange.get())
	colums.configure(bg=ColorChange.get())
	pagina.configure(bg=ColorChange.get())
	googleD.configure(bg=ColorChange.get())
	co.configure(bg=ColorChange.get())
	dump.configure(bg=ColorChange.get())
	dumpall.configure(bg=ColorChange.get())
	randoma.configure(bg=ColorChange.get())
	usera.configure(bg=ColorChange.get())
	Texto.configure(bg=ColorChange.get())
	Level.configure(bg=ColorChange.get())
	ries.configure(bg=ColorChange.get())
	ta.configure(bg=ColorChange.get())
	db.configure(bg=ColorChange.get())

def options():
	global opciones
	global ColorChange
	opciones = Tk()
	opciones.geometry("300x300")
	opciones.title("Opciones")
	Aceptar = Button(opciones, text="Aceptar", command=Accept)
	bDownload = Button(opciones, text="Descargar SQLMAP", command=Descargar)
	lColor = Label(opciones,text="Color")
	ColorChange = Spinbox(opciones, values=("red","blue","black","white","gray","green"), command=colores)
	ColorChange.place(x=20,y=20)
	lColor.place(x=65,y=2)
	Aceptar.place(x=120,y=250)
	bDownload.place(x=180,y=15)
	opciones.mainloop()
def proximamente():
	messagebox.showwarning("Alerta","Esto Aun No Esta Disponible en esta Version")
def columnitas():
	columnas = Entry(ventana, textvariable=C)
	columnas.place(x=250,y=100)
def googleDork():
	google = Entry(ventana, textvariable=gugul)
	Google = Label(ventana, text="Google:")
	Google.place(x=20,y=60)
	google.place(x=70,y=60)
def pageor():
	Pagina = Label(ventana, text="Pagina:")
	Pagina.place(x=20,y=60)
	Page = Entry(ventana, textvariable=page)
	Page.place(x=70,y=60)
def credits():
	credits = Tk()
	credits.geometry("200x200")
	credits.title("Acerca de")
	Creditos = Label(credits, text="Menu Creado por F3D3")
	version = Label(credits, text="Version: 0.2")
	version.place(x=70,y=70)
	Creditos.place(x=40,y=50)
	credits.mainloop()
def tabla():
	tablitas = Entry(ventana,textvariable=T)
	tablitas.place(x=250,y=80)
def database():
	Database = Entry(ventana, textvariable=D)
	Database.place(x=250,y=60)
def Atacar():
	messagebox.showinfo("Advertencia","Revisar Terminal")
	#Variables
	option = ""
	option1 = ""
	option2 = ""
	option3 = ""
	option4 = " --level={}".format(valor.get())
	option5 = " --risk={}".format(valor1.get())
	option6 = ""
	option7 = ""
	option8 = ""
	if dbc.get() == 1:
		option1 = " --dbs"
	elif dbc.get() == 2:
		option1 = " --tables"
	elif dbc.get() == 3:
		option1 = " --colums"
	if Db.get() == 1:
		option2 = " -D {}".format(D.get())
	if tablas.get() == 1:
		option3 = " -T {}".format(T.get())
	if paog.get() == 1:
		option = "-u {}".format(page.get())
	elif paog.get() == 2:
		option = "-g {}".format(gugul.get())
	if Columns.get() == 1:
		option6 = " -C {}".format(C.get())
	if Dump.get() == 1:
		option7 = " --dump" 
	elif Dump.get() == 2:
		option7 = " --dump-all"
	if agent.get() == 1:
		option8 = " --random-agent"
	if sysop == "posix":
		os.system("python2 sqlmap-master/sqlmap.py "+option+option1+option2+option3+option4+option5+option6+option7+option8)
	elif sysop == "nt":	
		os.system("python2 sqlmap-master\sqlmap.py "+option+option1+option2+option3+option4+option5+option6+option7+option8)
def reset():
	dbc.set(0)
	paog.set(0)
	agent.set(0)
	Db.set(0)
	tablas.set(0)
	Columns.set(0)
	Dump.set(0)
	gugul.set("")
	page.set("")
	valor.set("1")
	valor1.set("1")
	D.set("")
	T.set("")
	C.set("")
#Variables
agent = IntVar()
gugul = StringVar()
paog = IntVar()
page = StringVar()
dbc = IntVar()
tablas = IntVar()
valor = StringVar()
valor1 = StringVar()
Columns = IntVar()
Dump = IntVar()
Db = IntVar()
D = StringVar()
T = StringVar()
C = StringVar()
sysop = os.name
ubicacion = os.getcwd()

#Fuentes
Fuente = font.Font(family="Fixedsys", size=15)
#Textos
Texto = Label(ventana, text="Opciones para Injection", font=Fuente)
Level = Label(ventana, text="Level")
ries = Label(ventana, text="Risk")


#Botones Redondos
dbs = Radiobutton(ventana, text="Ver DBS",value=1, variable=dbc)
tables = Radiobutton(ventana, text="Ver Tablas",value=2, variable=dbc)
colums = Radiobutton(ventana,text="Ver Columnas",value=3, variable=dbc)
db = Radiobutton(ventana,text="D", value=1, variable=Db, command=database)
ta = Radiobutton(ventana,text="T ",value=1, variable=tablas, command=tabla)
pagina = Radiobutton(ventana,text="Pagina",value=1,variable=paog,command=pageor)
googleD = Radiobutton(ventana,text="Google Dork",value=2,variable=paog,command=googleDork)
co = Radiobutton(ventana, text="C",value=1,variable=Columns,command=columnitas)
dump = Radiobutton(ventana,text="Dump",value=1,variable=Dump)
dumpall = Radiobutton(ventana,text="Dump All",value=2,variable=Dump)
randoma = Radiobutton(ventana,text="Random Agent", value=1, variable=agent) 
usera = Radiobutton(ventana, text="User Agent", value=2, variable=agent, command=proximamente)

#SpinBox
Risk = Spinbox(ventana, from_=1, to=3, textvariable=valor1)
nivel = Spinbox(ventana, from_=1, to=5, textvariable=valor)

#Botones
aceptar = Button(ventana, text="Atacar", command=Atacar)
creditos = Button(ventana, text="Acerca De", command=credits)
resetear = Button(ventana, text="Reset All", command=reset)
opciones = Button(ventana, text="Opciones", command=options)

#Ubicacion SpinBox
nivel.place(x=20,y=190)
Risk.place(x=20, y=240)

#Ubicacion Textos
ries.place(x=75,y=220)
Level.place(x=70,y=170)
Texto.place(x=110,y=10)


#Ubicacion Botones Redondos
usera.place(x=200,y=170)
randoma.place(x=200,y=150)
dump.place(x=200, y=200)
dumpall.place(x=260,y=200)
co.place(x=200, y=100)
googleD.place(x=75,y=30)
pagina.place(x=10,y=30)
dbs.place(x=20, y=100)
tables.place(x=20, y=120)
colums.place(x=20,y=140)
db.place(x=200, y=60)
ta.place(x=200, y=80)

#Ubicacion Botones
opciones.place(x=20,y=300)
resetear.place(x=150,y=300)
aceptar.place(x=220,y=300)
creditos.place(x=325,y=300)


ventana.mainloop()