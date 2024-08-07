import tkinter as tk # import module for windows creation
import webbrowser # import module to hypertext link
from tkinter import filedialog
import pygame #import for playing the audio

def searchFile1():
    global file1
    file1 = filedialog.askopenfilename(
        title="file select",
        filetypes=(("Archivos de audio", "*.wav *.mp3"), ("Todos los archivos", "*.*"))
    )
    if file1:
        print(f"File selected: {file1}")

def searchFile2():
    global file2
    file2 = filedialog.askopenfilename(
        title="file select",
        filetypes=(("Archivos de audio", "*.wav *.mp3"), ("Todos los archivos", "*.*"))
    )
    if file2:
        print(f"File selected: {file2}")

def searchFile3():
    global file3
    file3 = filedialog.askopenfilename(
        title="file select",
        filetypes=(("Archivos de audio", "*.wav *.mp3"), ("Todos los archivos", "*.*"))
    )
    if file3:
        print(f"File selected: {file3}")

def playSound1():
    if file1:
        pygame.mixer.init()
        pygame.mixer.music.load(file1)
        pygame.mixer.music.play()

def playSound2():
    if file2:
        pygame.mixer.init()
        pygame.mixer.music.load(file2)
        pygame.mixer.music.play()

def playSound3():
    if file1:
        pygame.mixer.init()
        pygame.mixer.music.load(file3)
        pygame.mixer.music.play()

def weblink1(): # Link whom open my website ;)
    
    webbrowser.open("https://rogeliovr.github.io/Roge.pro/")

def main():

    global file
    archivo = None

    # Tkinter windows
    windows = tk.Tk()
    windows.title("SD - V 0.1")
    windows.geometry("800x600")

    # Configurar la grilla
    for i in range(4):
        windows.grid_columnconfigure(i, weight=1)

    title_label = tk.Label(windows, text="SoundDesk RyP", font=("Helvetica", 24, "bold"))
    credits_label = tk.Label(windows, text="https://rogeliovr.github.io/Roge.pro/", font=("Helvetica", 12), fg="blue", cursor="hand2")
    credits_label.bind("<Button-1>", lambda e: weblink1())

    title_label.grid(row=0, column=0, columnspan=4, pady=20)
    credits_label.grid(row=1, column=0, columnspan=4, pady=0)

    # Crear el botón para buscar archivo
    boton_buscar = tk.Button(windows, text="Search File", command=searchFile1)
    boton_buscar.grid(row=2, column=0, columnspan=4, pady=20)

    # Crear el botón para reproducir sonido
    boton_reproducir = tk.Button(windows, text="Search File", command=playSound1)
    boton_reproducir.grid(row=3, column=0, columnspan=4, pady=20)

    # Crear el botón para buscar archivo
    boton_buscar = tk.Button(windows, text="Buscar Archivo", command=searchFile2)
    boton_buscar.grid(row=4, column=0, columnspan=4, pady=20)

    # Crear el botón para reproducir sonido
    boton_reproducir = tk.Button(windows, text="Sonido 2", command=playSound2)
    boton_reproducir.grid(row=5, column=0, columnspan=4, pady=20)

        # Crear el botón para buscar archivo
    boton_buscar = tk.Button(windows, text="Buscar Archivo", command=searchFile3)
    boton_buscar.grid(row=6, column=0, columnspan=4, pady=20)

    # Crear el botón para reproducir sonido
    boton_reproducir = tk.Button(windows, text="Sonido 3", command=playSound3)
    boton_reproducir.grid(row=7, column=0, columnspan=4, pady=20)

    # Tkinter windows execution
    windows.mainloop()

if __name__ == "__main__":
    main()
