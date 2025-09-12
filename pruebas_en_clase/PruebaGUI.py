import tkinter as tk

# Función que hace la operación
def calcular(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        if op == "+":
            resultado.set(num1 + num2 + num3)
        elif op == "*":
            resultado.set(num1 * num2 * num3)
        elif op == "-":
            resultado.set(num1 - num2 - num3)
    except ValueError:
        resultado.set("Error")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora master pro")
ventana.geometry("400x400")
ventana.configure(bg="green")

# Entradas
entry1 = tk.Entry(ventana)
entry1.pack(pady=5)

entry2 = tk.Entry(ventana)
entry2.pack(pady=5)

entry3 = tk.Entry(ventana)
entry3.pack(pady=5)

# Botones
tk.Button(ventana, text="Sumar", command=lambda: calcular("+")).pack(pady=5)
tk.Button(ventana, text="Restar", command=lambda: calcular("-")).pack(pady=5)
tk.Button(ventana, text="Multiplicar", command=lambda: calcular("*")).pack(pady=5)
# Resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).pack(pady=5)

ventana.mainloop()