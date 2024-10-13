import tkinter as tk
from tkinter import colorchooser
import random
from tkinter import filedialog
from PIL import Image, ImageDraw

# ////////////////////////////////////////////////////////////////////////////////// [v1.0]  //////////////////////////////////////////////////////////////////////////////////

# ► Crear la ventana
root = tk.Tk()  # Crea la base de la ventana para mostrar el programa
root.title("Rodanvas v1.3")  # Establece el título de la ventana

# ► Crear canvas
canvas = tk.Canvas(root, bg="white", width=720, height=720)  # Especificaciones del canvas | [v1.2] El tamaño pasó de 520x520 a 720x720
canvas.pack()  # Ordena que el canvas se muestre en la ventana principal del programa

# ► Variables globales
last_x, last_y = None, None
borrador = False  # Determina si el borrador está activado o desactivado
color_pincel = "black"  # Color por defecto del pincel
colores_recientes = []  # Lista que almacenará los colores recientes
tamaño_pincel = 3  # Tamaño inicial del pincel

# ► Configuración de imagen para guardar
image = Image.new("RGB", (720, 720), "white")
draw = ImageDraw.Draw(image)

# ► Función al hacer click
def al_presionar(event):  # El valor event es administrado por la librería TKinter
    global last_x, last_y  # 'Global' permite que las variables puedan ser utilizadas en cualquier parte del código
    last_x, last_y = event.x, event.y  # Guarda las coordenadas de dónde se hizo click

# ► Función al mover el mouse
def al_mover(event):
    global last_x, last_y
    if last_x and last_y:  # Verifica si las coordenadas iniciales existen
        color = 'white' if borrador else color_pincel  # <<< Actualizado: Si el modo borrador está activado dibuja en blanco, de lo contrario, en el color actual del pincel
        canvas.create_line(last_x, last_y, event.x, event.y, fill=color, width=10 if borrador else tamaño_pincel)  # Dibuja una línea con el color y grosor correspondiente
        draw.line([last_x, last_y, event.x, event.y], fill=color, width=10 if borrador else tamaño_pincel)  # Dibuja también en la imagen para guardar
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
    draw.rectangle([0, 0, 720, 720], fill="white")  # Limpia también la imagen guardada

# ► Botones
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiar_canvas)
boton_limpiar.pack(side=tk.LEFT)

boton_borrador = tk.Button(root, text="Borrador", command=toggle_borrador)
boton_borrador.pack(side=tk.LEFT)

# /////////////////////////////////////////////////////////////////////////////////// [v1.2]  //////////////////////////////////////////////////////////////////////////////////

# ► Función para aumentar el tamaño del pincel
def aumentar_pincel():
    global tamaño_pincel
    tamaño_pincel += 1
    actualizar_tamaño_pincel()

# ► Función para disminuir el tamaño del pincel
def disminuir_pincel():
    global tamaño_pincel
    if tamaño_pincel > 1:  # Evitar que el tamaño del pincel sea menor que 1
        tamaño_pincel -= 1
    actualizar_tamaño_pincel()

# ► Función "prueba" para cambiar colores y dibujar algo
def prueba():
    for i in range(7):  # Coloca colores aleatorios en los recientes
        color_aleatorio = "#%06x" % random.randint(0, 0xFFFFFF)
        agregar_color_reciente(color_aleatorio)
    # Dibuja algo aleatorio en el canvas
    for _ in range(10):  # Dibuja 10 líneas aleatorias
        x1, y1 = random.randint(0, 720), random.randint(0, 720)
        x2, y2 = random.randint(0, 720), random.randint(0, 720)
        canvas.create_line(x1, y1, x2, y2, fill=random.choice(colores_recientes), width=random.randint(1, 10))

# ► Función para actualizar la etiqueta con el tamaño del pincel
def actualizar_tamaño_pincel():
    etiqueta_tamaño.config(text=f"Tamaño del pincel: {tamaño_pincel}")

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
        if len(colores_recientes) >= 7:  # Mantiene solo los últimos 5 colores
            colores_recientes.pop(0)  # Elimina el color más antiguo
        colores_recientes.append(color)  # Agrega el nuevo color a la lista
        actualizar_colores_recientes() # Llama a la función de acá abajo :)

# ► Función para actualizar la lista de colores recientes (borra todos los botones y hace nuevos cada vez)
def actualizar_colores_recientes():
    for widget in frame_colores_recientes.winfo_children():  # Para todos los botones anteriores:
        widget.destroy() # ...borra todos
    for color in colores_recientes:  # Crea un botón para cada color reciente
        boton_color = tk.Button(frame_colores_recientes, bg=color, width=3, command=lambda c=color: usar_color_reciente(c))
        boton_color.pack(side=tk.LEFT)

# ► Función para usar un color reciente
def usar_color_reciente(color):
    global color_pincel
    color_pincel = color # Cambia el color del pincel por el color del botón que presione

# ► Función para guardar la imagen creada
def guardar_imagen():
    archivo = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if archivo:
        image.save(archivo)

# ► Marco contenedor para el botón de seleccionar color y los colores recientes
frame_seleccion_y_colores = tk.Frame(root)
frame_seleccion_y_colores.pack(side=tk.LEFT)

# ► Botón para seleccionar color dentro del nuevo frame
boton_color = tk.Button(frame_seleccion_y_colores, text="Seleccionar color", command=seleccionar_color)
boton_color.pack(side=tk.LEFT)

# ► Marco para los colores recientes dentro del mismo frame
frame_colores_recientes = tk.Frame(frame_seleccion_y_colores)
frame_colores_recientes.pack(side=tk.LEFT)

# Botón prueba()
boton_prueba = tk.Button(root, text="prueba()", command=prueba)
boton_prueba.pack(side=tk.LEFT)

# ► Botón para guardar la imagen creada
boton_guardar = tk.Button(root, text="Guardar imagen", command=guardar_imagen)
boton_guardar.pack(side=tk.LEFT)

# ► Marco para los botones de tamaño de pincel y la etiqueta
frame_tamaño_pincel = tk.Frame(root)
frame_tamaño_pincel.pack(side=tk.RIGHT)

# ► Etiqueta que muestra el tamaño del pincel actual
etiqueta_tamaño = tk.Label(frame_tamaño_pincel, text=f"Tamaño del pincel: {tamaño_pincel}")
etiqueta_tamaño.pack(side=tk.LEFT)

# ► Botones para aumentar y disminuir el tamaño del pincel
boton_aumentar = tk.Button(frame_tamaño_pincel, text="  +  ", command=aumentar_pincel)
boton_aumentar.pack(side=tk.RIGHT)

boton_disminuir = tk.Button(frame_tamaño_pincel, text="  -  ", command=disminuir_pincel)
boton_disminuir.pack(side=tk.RIGHT)

# ///

root.mainloop()  # Hace que la ventana de TKinter se mantenga ejecutándose
