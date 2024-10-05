import tkinter as tk
from tkinter import colorchooser

# ////////////////////////////////////////////////////////////////////////////////// [v1.0]  //////////////////////////////////////////////////////////////////////////////////

# ► Crear la ventana
root = tk.Tk()  # Crea la base de la ventana para mostrar el programa
root.title("Rodanvas v1.1")  # Establece el título de la ventana

# ► Crear canvas
canvas = tk.Canvas(root, bg="white", width=720, height=720)  # Especificaciones del canvas | [v1.2] El tamaño pasó de 520x520 a 720x720
canvas.pack()  # Ordena que el canvas se muestre en la ventana principal del programa

# ► Variables globales
last_x, last_y = None, None
borrador = False  # Determina si el borrador está activado o desactivado
color_pincel = "black"  # Color por defecto del pincel
colores_recientes = []  # Lista que almacenará los colores recientes

# ► Función al hacer click
def al_presionar(event):  # El valor event es administrado por la librería TKinter
    global last_x, last_y  # 'Global' permite que las variables puedan ser utilizadas en cualquier parte del código
    last_x, last_y = event.x, event.y  # Guarda las coordenadas de dónde se hizo click

# ► Función al mover el mouse
def al_mover(event):
    global last_x, last_y
    if last_x and last_y:  # Verifica si las coordenadas iniciales existen
        color = 'white' if borrador else color_pincel  # <<< Actualizado: Si el modo borrador está activado dibuja en blanco, de lo contrario, en el color actual del pincel
        canvas.create_line(last_x, last_y, event.x, event.y, fill=color, width=10 if borrador else 3)  # Dibuja una línea con el color y grosor correspondiente
        last_x, last_y = event.x, event.y  # Actualiza las variables last

# ► Función al soltar el mouse
def al_soltar(event):
    global last_x, last_y
    last_x, last_y = None, None  # Vacía las variables de posición

# ► Asociar las acciones
canvas.bind("<ButtonPress-1>", al_presionar)  # Click izquierdo
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

# ► Función para limpiar el canvas
def limpiar_canvas():
    canvas.delete("all") # No uede ser más autoexplicativo

# ► Botones
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiar_canvas)
boton_limpiar.pack(side=tk.LEFT)

boton_borrador = tk.Button(root, text="Borrador", command=toggle_borrador)
boton_borrador.pack(side=tk.LEFT)

# /////////////////////////////////////////////////////////////////////////////////// [v1.2]  //////////////////////////////////////////////////////////////////////////////////

# ► Selección de colores
def seleccionar_color():
    global color_pincel
    color = colorchooser.askcolor()[1]  # Abre la ventana de selección de color y devuelve el color en formato hexadecimal y lo guarda en la variable 'color'
    if color:
        color_pincel = color # Si el color del pincel es igual a la variable 'color' (o sea siempre) lo agrega a la lista de colores
        agregar_color_reciente(color)  # Agrega el color a la lista de colores recientes

# ► Función para agregar el color a la lista de colores recientes
def agregar_color_reciente(color):
    if color not in colores_recientes:  # Evita duplicados
        if len(colores_recientes) >= 5:  # Mantiene solo los últimos 5 colores
            colores_recientes.pop(0)  # Elimina el color más antiguo
        colores_recientes.append(color)  # Agrega el nuevo color a la lista
        actualizar_colores_recientes() # Llama a la función de acá abajo :)

# ► Función para actualizar la lista de colores recientes (borra todos los botones y hace nuevos cada vez)
def actualizar_colores_recientes():
    for widget in frame_colores_recientes.winfo_children():  # Para todos los botones anteriores:
        widget.destroy() # ...borra todos
    for color in colores_recientes:  # Crea un botón para cada color reciente
        boton_color = tk.Button(frame_colores_recientes, bg=color, width=3, command=lambda c=color: usar_color_reciente(c)) # <<< De normal deberías poner 'color=', pero en este
                                                                                                                            #     caso usamos la variable 'c' como color para
                                                                                                                            #     poder usar la función de 'usar_color_reciente'
                                                                                                                            #     y así ahorrarme muchos problemas para actualziar
                                                                                                                            #     el color del botón :)
        boton_color.pack(side=tk.LEFT)
        # ^^^^^^ Pobrecito, quedo muy lejos de la función por la explicación de arriba :(

# ► Función para usar un color reciente
def usar_color_reciente(color):
    global color_pincel
    color_pincel = color # Cambia el color del pincel por el color del botón que presione (creo)

# ► Marco contenedor para el botón de seleccionar color y los colores recientes
frame_seleccion_y_colores = tk.Frame(root)
frame_seleccion_y_colores.pack(side=tk.LEFT)

# ► Botón para seleccionar color dentro del nuevo frame
boton_color = tk.Button(frame_seleccion_y_colores, text="Seleccionar color", command=seleccionar_color)
boton_color.pack(side=tk.LEFT)

# ► Marco para los colores recientes dentro del mismo frame
frame_colores_recientes = tk.Frame(frame_seleccion_y_colores)
frame_colores_recientes.pack(side=tk.LEFT)

# ///

# ► Inicia el programa
root.mainloop()

# (No puedo evitar pensar que todo el código se sostiene a base de cinta adhesiva y mucha fé, pero como funciona no me quejo)