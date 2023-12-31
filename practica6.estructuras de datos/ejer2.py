class Usuario:
    def __init__(self, nombre, correo, contraseña):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.sesion_iniciada = False

    def iniciar_sesion(self, correo, contraseña):
        if self.correo == correo and self.contraseña == contraseña:
            self.sesion_iniciada = True
            print(f"Bienvenida, {self.nombre}!")
        else:
            print("Correo o contraseña incorrectos.")

    def cerrar_sesion(self):
        self.sesion_iniciada = False
        print("Sesion cerrada.")

    def cambiar_contraseña(self, nueva_contraseña):
        self.contraseña = nueva_contraseña
        print("Contraseña cambiada exitosamente.")


cuenta = Usuario("Raquel Mejia", "raquel.mejia@gmail.com", "password.RMFLORES")
cuenta.iniciar_sesion("raquel.mejia@gmail.com", "password.RMFLORES")
cuenta.cambiar_contraseña("newpassworMEJIA")
cuenta.cerrar_sesion()
