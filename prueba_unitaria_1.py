import unittest


# Función que simula el registro de usuarios en el sistema
def registrar_usuario(nombre_usuario):
    usuarios_registrados = ["usuario1", "usuario2", "usuario3"]

    if nombre_usuario in usuarios_registrados:
        return "El usuario ya está registrado"
    else:
        usuarios_registrados.append(nombre_usuario)
        return "Registro exitoso"


# Clase de prueba que hereda de unittest.TestCase
class TestRegistroUsuarios(unittest.TestCase):

    # Método de prueba para el primer caso de prueba
    def test_registro_exitoso(self):
        resultado = registrar_usuario("nuevo_usuario")
        self.assertEqual(resultado, "Registro exitoso")

    # Método de prueba para el segundo caso de prueba
    def test_usuario_existente(self):
        resultado = registrar_usuario("usuario1")
        self.assertEqual(resultado, "El usuario ya está registrado")


if __name__ == '__main__':
    unittest.main()
