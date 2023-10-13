class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.seguidores = []
        self.mensajes = []

    def seguir(self, usuario):
        self.seguidores.append(usuario)

    def dejar_de_seguir(self, usuario):
        self.seguidores.remove(usuario)

    def publicar_mensaje(self, mensaje):
        self.mensajes.append(mensaje)

    def ver_mensajes(self):
        return self.mensajes

    def ver_mensajes_seguidos(self):
        mensajes = []
        for usuario in self.seguidores:
            mensajes.extend(usuario.ver_mensajes())
        return mensajes


usuario1 = Usuario("Juan")
usuario2 = Usuario("Pedro")
usuario3 = Usuario("María")

usuario1.seguir(usuario2)
usuario1.seguir(usuario3)

usuario2.publicar_mensaje("Hola, Juan!")
usuario3.publicar_mensaje("Hola, Juan!")

print(usuario1.ver_mensajes_seguidos())
