-# El archivo de Python se subirá como Release. El README será siemre este mismo archivo pero se irá actualizando.

# Rodanvas

## Contexto
El proposito del proyceto es de crear un programa que genere una interfaz en la que se podrá dibujar
similar a como funciona Microsoft Paint o Ibis Studio.

El proposito de crear la aplicación es poder tener una herramienta de dibujo ligera sin necesidad de instalar
nada (considerando que ya se tiene el archivo .py) además de que considero que es un buen reto para poner
aprueba mis capacidades como principiante en la programación.

## Algoritmo
### Puntos técnicos:
Como funcionará el código será primero que nada importando la librería de TKinker la cuál agrega funciones
basadas en interfases de usuario sobretodo para proyectos similares a éste.

Después se tendrá que crear el lienzo (canva) el cuál será un espacio blanco en el que el usuario podrá dibujar
al hacer click (o tocar en dispositivos móviles) mediante el proceso de identificar la posición del puntero en
el mometo en el que se interactuó e ir creando una línea hasta que se suelte el click.

#### ► Entradas:

• Pocición del mouse al hacer click

• Pocición del mouse al soltar click

#### ► Proceso:

• Guarda la ubicación del mouse cuando se hace click
• Traza una línea que una las ubicaciones donde pasó el mouse
• Guarda la ubicación del mouse al soltar click
• Deja de trazar la línea al soltar el click

#### ► Salidas

• Línea del rastro del mouse

### Usuario:
El usuario al ejectutar el archivo .py verá un espacio en blanco. Al hacer click en cualquier parte del canva una línea negra se irá generando en los lugares por los que pase el mouse hasta que se suuelte el click.

## Información adicional
El programa contará con diversas funciones agrupadas en botones tales como un borrador, el botón de limpiar canvas o en el futuro cambiar el color del pincel o un botón que muestre indicaciones de cómo usar el programa.

Con respecto a las dos últimas futuras funciones, en la primera de ellas posiblemente se pueda hacer uso de listas para almacenar los colores utilizados recientemente para que sea más fácil acceder a los colores que habrías usado anteriormente. Ahora, con respecto al botón de ayuda, podemos usar un archivo .txt que muestre una serie de instrucciones básicas sobre cómo usar el programa, posiblemente explicando qué hace cada botón.
