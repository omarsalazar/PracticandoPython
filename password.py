import uuid


class Password:
    contrasena = None

    def _init_(self, contrasena):
        self.contrasena = contrasena

    def generar_password(self):
        self.contrasena = uuid.uuid1()

    def get_password(self):
        print(self.contrasena)

    def es_fuerte(self):
        print("La contrasena es fuerte, contiene: ",
        sum(1 for c in str(self.contrasena) if c.islower()),
        " letras minusculas")


kquita = Password()
kquita.generar_password()
kquita.get_password()
kquita.es_fuerte()
