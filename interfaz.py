#Estos son los requerimientos
import tkinter as front
from tkinter import filedialog
from collections import Counter
import time 

#Frontend
def contarCaracteres(file_path):
        with open(file_path, 'r') as file:
            archivo = file.read()
            contador = Counter(archivo)

            print("Frecuencia de caracteres:")
            for Letra, Veces in contador.items():
                print(f"{Letra}: {Veces}")


def abrirArchivo():
    file_path = filedialog.askopenfilename()
    print(file_path)
    if file_path:
        contarCaracteres(file_path)

#Backend
def comprimir():
    print("Esta es la función de comprimir")
    botonComprimir.config(text='clicked!')

def descomprimir():
    botonDescomprimir.config(text='clicked!')
    print("Esta va a ser la función de descomprimir")


#Main
if __name__ == "__main__":
    root = front.Tk()
    root.title("File Analyzer")
    root.config(bg='darkgreen')
    root.title("Clock")
    root.maxsize(320, 200)
    root.geometry('180x160')
    root.resizable(0,1)
    root.title("Programa Comprimir")
    frm = front.Frame(root)
    testo = front.Label(frm, text="Hello World!")

# Botones
botonAgarrar = front.Button(root, text="Examinar", command=abrirArchivo, fg="white", bg="black")
botonAgarrar.pack(pady=3)

botonComprimir = front.Button(root, text="Comprimir", command=comprimir, fg="white", bg="black")
botonComprimir.pack(pady=1)

botonDescomprimir = front.Button(root, text="Descomprimir", command=descomprimir, fg="white", bg="black")
botonDescomprimir.pack(pady=3)


root.mainloop()