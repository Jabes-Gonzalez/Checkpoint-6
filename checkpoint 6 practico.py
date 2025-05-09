class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

usuario1 = Usuario("juan123", "secreto456")

print("Nombre de usuario:", usuario1.nombre_usuario)
print("Contraseña:", usuario1.contrasena)
