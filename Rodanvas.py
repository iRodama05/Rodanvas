import tkinter as tk

# ////////////////////////////////////////////////////////////////////////////////// [v1.0]  //////////////////////////////////////////////////////////////////////////////////

# ► Crear la ventana
root = tk.Tk() # Crea la bsse de la ventana para mostrar el programa
root.title("Rodanvas v1.1") # Establece el título de la ventana

# ► Crear canvas
canvas = tk.Canvas(root, bg="white", width=520, height=520) # Especificaciones del canvas
canvas.pack() # Ordena que canvas se muestre en la ventana principal del programa

# ► Variables globales
last_x, last_y = None, None
borrador = False # Determina si el borrador está activado o desactivado

# ► Función al hacer click
def al_presionar(event): # El valor event es administrado por la librería TKinter
    global last_x, last_y # 'Global' permite que las variables puedan ser utilizadas en cualquier parte del código
    last_x, last_y = event.x, event.y # Guarda las coordenadas de dónde se hizo click

# ► Función al mover el mouse
def al_mover(event):
    global last_x, last_y
    if last_x and last_y: # [POR INVESTIGAR]
        color = 'white' if borrador else 'black' # <<< [v1.1] | Si el modo borrador está activado dibuja en blanco, de lo contrario dibuja en negro
        canvas.create_line(last_x, last_y, event.x, event.y, fill=color, width=10 if borrador else 3) # Desde donde se hizo el click (variables last) hasta donde se encuentra
                                                                                                      # actualmente el mouse (event) dibuja una línea del color correspondiente
                                                                                                      # con la anchura correspondiente en pixeles
        last_x, last_y = event.x, event.y # Actualiza las variables last

# ► Función al soltar el mouse
def al_soltar(event):
    global last_x, last_y
    last_x, last_y = None, None # Vacia las variables de posición

# ► Asociar las acciones
canvas.bind("<ButtonPress-1>", al_presionar) # En ButtonPress o similares, -1 es el click izquierdo
canvas.bind("<B1-Motion>", al_mover)
canvas.bind("<ButtonRelease-1>", al_soltar)

# /////////////////////////////////////////////////////////////////////////////////// [v1.1]  //////////////////////////////////////////////////////////////////////////////////

# ► Función de borrador
def toggle_borrador():
    global borrador
    borrador = not borrador
    if borrador:
        boton_borrador.config(text="Pincel")
    else:
        boton_borrador.config(text="Borrador")

# ► Función limpiar canvas
def limpiar_canvas():
    canvas.delete("all")

# ► Botones
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiar_canvas)
boton_limpiar.pack(side=tk.LEFT)

boton_borrador = tk.Button(root, text="Borrador", command=toggle_borrador)
boton_borrador.pack(side=tk.LEFT)

# ///

# ► Inicia el programa
root.mainloop()