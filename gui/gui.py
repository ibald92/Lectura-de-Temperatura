# Importamos las librerías necesarias
import tkinter as tk                # Tkinter para la interfaz gráfica
import serial                       # pyserial para la comunicación con Arduino
import serial.tools.list_ports      # para listar los puertos disponibles
from tkinter import messagebox

# Modificación Borrador
# Próximo paso: implementar lectura serial y login como modulos separados

# Datos de acceso (puedes cambiarlos o cargarlos desde otro sitio)
# --- Funciones ---

# def listar_puertos():
#     """Busca los puertos seriales disponibles y los muestra en el menú desplegable."""
#     puertos = [p.device for p in serial.tools.list_ports.comports()]  # Lista de dispositivos detectados
#     menu_puertos["menu"].delete(0, "end")  # Limpia el menú desplegable
#     for p in puertos:  # Agrega cada puerto como opción
#         menu_puertos["menu"].add_command(label=p, command=lambda v=p: puerto_var.set(v))
#     if puertos:  # Si hay puertos disponibles, selecciona el primero por defecto
#         puerto_var.set(puertos[0])

def conectar():
    """Intenta abrir la conexión serial con el puerto y baudrate seleccionados."""
    global ser  # usamos la variable global 'ser'
    try:
        # Abrimos el puerto serial con los parámetros elegidos
        ser = serial.Serial(puerto_var.get(), int(baud_var.get()), timeout=0)
        mostrar_datos()              # empezamos a leer datos
        estado.set("Conectado")      # cambiamos el estado
    except Exception as e:           # si algo falla, mostramos el error
        estado.set(f"Error: {e}")

def mostrar_datos():
    """Lee los datos del Arduino y los coloca en la caja de texto."""
    if ser and ser.is_open:                      # Verifica que el puerto esté abierto
        data = ser.read(ser.in_waiting or 1)     # Lee datos disponibles (o 1 byte si no hay nada)
        if data:                                 # Si hay datos recibidos
            texto.insert("end", data.decode(errors="ignore"))  # Los escribe en el área de texto
            texto.see("end")                     # Desplaza la vista hacia abajo
        root.after(100, mostrar_datos)           # Llama de nuevo a esta función cada 100 ms


# --- Interfaz gráfica ---
#Logeo

#Interfaz Serial
def iniciar_interfaz_principal():
    global root, puerto_var, baud_var, estado, ser, texto, menu_puertos 
    root = tk.Tk()                    # Crea la ventana principal
    root.title("Arduino Serial Viewer")  # Título de la ventana

    puerto_var = tk.StringVar()       # Variable para guardar el puerto seleccionado
    baud_var = tk.StringVar(value="9600")  # Variable para guardar el baudrate (por defecto 9600)
    estado = tk.StringVar(value="Desconectado")  # Variable para mostrar el estado
    ser = None                        # Variable global para el objeto Serial

    # Botón para actualizar la lista de puertos
    # tk.Button(root, text="Actualizar puertos", command=listar_puertos).pack()

    # Menú desplegable para seleccionar puerto
    # menu_puertos = tk.OptionMenu(root, puerto_var, "")
    # menu_puertos.pack()

    menu_puertos=tk.Entry(root, textvariable=puerto_var).pack()


    # Caja de texto para ingresar el baudrate
    tk.Entry(root, textvariable=baud_var).pack()

    # Botón para conectar
    tk.Button(root, text="Conectar", command=conectar).pack()

    # Caja de texto donde se mostrarán los datos recibidos
    texto = tk.Text(root, height=15, width=60)
    texto.pack()

    # Etiqueta que muestra el estado (desconectado/conectado/error)
    tk.Label(root, textvariable=estado).pack()

    # Llenamos la lista de puertos al inicio
    # listar_puertos()

    # Bucle principal de la interfaz
    root.mainloop()

# Datos de acceso
USUARIO_CORRECTO = "admin"
CONTRASEÑA_CORRECTA = "1234"

# -------------------
# FUNCIONES DE LOGIN
# -------------------

def verificar_usuario(usuario, contraseña):
    """Verifica las credenciales del usuario y la contraseña."""
    if usuario == USUARIO_CORRECTO and contraseña == CONTRASEÑA_CORRECTA:
        return True
    else:
        return False

def verificar_login(entry_usuario, entry_contraseña, login_window):
    """Verifica las credenciales e inicia la interfaz principal si es correcto."""
    usuario = entry_usuario.get()        # Obtener el valor del campo de usuario
    contraseña = entry_contraseña.get()   # Obtener el valor del campo de contraseña

    if verificar_usuario(usuario, contraseña):
        login_window.destroy()  # Cerrar la ventana de login si las credenciales son correctas
        iniciar_interfaz_principal()  # Llamamos a la función que inicia la interfaz principal
    else:
        messagebox.showerror("Login incorrecto", "Usuario o contraseña incorrectos.")
        entry_usuario.delete(0, tk.END)  # Limpiar el campo de usuario
        entry_contraseña.delete(0, tk.END)  # Limpiar el campo de contraseña
        entry_usuario.focus()  # Volver el foco al campo de usuario

def crear_login():
    """Crea la ventana de login y permite verificar las credenciales."""
    global login_window, entry_usuario, entry_contraseña

    login_window = tk.Tk()  # Crear la ventana de login
    login_window.title("Login")
    login_window.geometry("300x150")

    # Campos de texto para usuario y contraseña
    tk.Label(login_window, text="Usuario:").pack(pady=(10, 0))
    entry_usuario = tk.Entry(login_window)
    entry_usuario.pack()

    tk.Label(login_window, text="Contraseña:").pack(pady=(10, 0))
    entry_contraseña = tk.Entry(login_window, show="*")
    entry_contraseña.pack()

    # Botón para intentar login
    tk.Button(login_window, text="Entrar", command=lambda: verificar_login(entry_usuario, entry_contraseña, login_window)).pack(pady=10)

    entry_usuario.focus()  # Foco en el campo de usuario

    # Mostrar la ventana de login
    login_window.mainloop()

crear_login()  # Iniciar el proceso de login