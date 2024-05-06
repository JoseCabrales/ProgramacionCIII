import tkinter as tk


class VentanaLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de Sesión")
        self.geometry("800x500")  

        self.marco_izquierdo = tk.Frame(self, width=400, height=500)  
        self.marco_izquierdo.grid(row=0, column=0, sticky="nsew")

        self.logo = tk.Label(self.marco_izquierdo, text="Logo", font=("Arial", 18))
        self.logo.grid(row=0, column=0, padx=20, pady=200, sticky="nsew")
        

        self.marco_derecho = tk.Frame(self, width=400, height=500)  
        self.marco_derecho.grid(row=0, column=1, sticky="nsew")

        self.etiqueta_titulo = tk.Label(self.marco_derecho, text="Inicio de sesión")
        self.etiqueta_titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

        self.etiqueta_usuario = tk.Label(self.marco_derecho, text="Usuario:")
        self.etiqueta_usuario.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.entrada_usuario = tk.Entry(self.marco_derecho)
        self.entrada_usuario.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        self.etiqueta_clave = tk.Label(self.marco_derecho, text="Clave:")
        self.etiqueta_clave.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        self.entrada_clave = tk.Entry(self.marco_derecho, show="*")
        self.entrada_clave.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

        self.boton_ingresar = tk.Button(self.marco_derecho, text="Ingresar")
        self.boton_ingresar.grid(row=3, column=0, columnspan=2, padx=20, pady=200, sticky="nsew")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.resizable(False, False) 


ventana_login = VentanaLogin()
ventana_login.mainloop()


