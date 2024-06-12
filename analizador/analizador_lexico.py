import re
import tkinter as tk

# Estructura de datos para la tabla de símbolos
tabla_simbolos = []

# Definición de expresiones regulares para los tokens
tokens = {
    'IDENTIFICADOR': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'ENTERO': r'\d+',
    'REAL': r'\d+\.\d+',
    'ASIGNACION': r'=',
    'SUMA': r'\+',
    'RESTA': r'-',
    'MULTIPLICACION': r'\*',
    'DIVISION': r'/',
}

# Función para analizar una línea y encontrar tokens
def analizar_linea(linea):
    # Eliminar comentarios de una línea
    linea = re.sub(r'//.*', '', linea)
    # Eliminar comentarios de una línea
    linea = re.sub(r'^\s*#\s*.*$', '', linea)
    # Eliminar comentarios multilínea entre /* y */
    linea = re.sub(r'/\*.*?\*/', '', linea, flags=re.DOTALL)
    # Eliminar comentarios multilínea entre """ y """
    linea = re.sub(r'""".*?"""', '', linea, flags=re.DOTALL)
    # Encontrar tokens en la línea y escribir en la tabla de símbolos
    for nombre, patron in tokens.items():
        for token in re.finditer(patron, linea):
            tabla_simbolos.append((token.group(), nombre))

# Función para manejar el evento de clic en el botón "Analizar"
def analizar_codigo():
    # Obtener el código fuente del widget de texto
    codigo_fuente = texto.get("1.0", tk.END)
    # Analizar el código fuente
    analizar_codigo_fuente(codigo_fuente)

# Función para analizar el código fuente
def analizar_codigo_fuente(codigo_fuente):
    # Limpiar la tabla de símbolos antes de analizar el nuevo código fuente
    tabla_simbolos.clear()
    # Analizar cada línea del código fuente
    lineas = codigo_fuente.split("\n")
    for linea in lineas:
        analizar_linea(linea)

# Función para mostrar la tabla de símbolos en una nueva ventana
def mostrar_tabla_simbolos():
    # Llamar a la función para analizar el código fuente
    analizar_codigo_fuente(texto.get("1.0", tk.END))
    
    # Crear una nueva ventana
    ventana_tabla_simbolos = tk.Toplevel(ventana)
    ventana_tabla_simbolos.title("Tabla de Símbolos")

    # Crear un widget de texto para mostrar la tabla de símbolos
    texto_tabla_simbolos = tk.Text(ventana_tabla_simbolos, wrap="word", width=50, height=20)
    texto_tabla_simbolos.pack(padx=10, pady=10)

    # Imprimir la tabla de símbolos en el widget de texto
    for token, tipo in tabla_simbolos:
        texto_tabla_simbolos.insert(tk.END, f"Token: {token}, Tipo: {tipo}\n")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Editor de Código Fuente")

# Crear un widget de texto para ingresar el código fuente
texto = tk.Text(ventana, wrap="word", width=50, height=20)
texto.pack(padx=10, pady=10)

# Crear un botón para analizar el código fuente
boton_analizar = tk.Button(ventana, text="Analizar", command=analizar_codigo)
boton_analizar.pack(pady=5)

# Crear un botón para mostrar la tabla de símbolos
boton_mostrar_tabla = tk.Button(ventana, text="Mostrar Tabla de Símbolos", command=mostrar_tabla_simbolos)
boton_mostrar_tabla.pack(pady=5)

# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()

