import unittest


# Función que simula el proceso de reserva de una habitación
def reservar_habitacion(info_pago):
    if info_pago:
        # Verificar si la información de pago es válida (solo como ejemplo)
        if info_pago == "informacion_valida":
            return "La reserva se procesa correctamente, y se muestra una confirmación de reserva."
        else:
            return "La información de pago es inválida."
    else:
        return "Se requiere información de pago."


# Clase de prueba que hereda de unittest.TestCase
class TestReservaHabitacion(unittest.TestCase):

    # Método de prueba para el primer caso de prueba
    def test_reserva_correcta(self):
        resultado = reservar_habitacion("informacion_valida")
        self.assertEqual(resultado, "La reserva se procesa correctamente, y se muestra una confirmación de reserva.")

    # Método de prueba para el segundo caso de prueba
    def test_sin_informacion_pago(self):
        resultado = reservar_habitacion(None)
        self.assertEqual(resultado, "Se requiere información de pago.")

    # Método de prueba para el tercer caso de prueba
    def test_informacion_pago_invalida(self):
        resultado = reservar_habitacion("informacion_invalida")
        self.assertEqual(resultado, "La información de pago es inválida.")


if __name__ == '__main__':
    unittest.main()
