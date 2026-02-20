class Cliente:
    def __init__(self, nombre, email, saldo):
        self.nombre = nombre
        self.email = email
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
        else:
            raise ValueError("El monto debe ser positivo.")

    def __str__(self):
        return f"👤 [Normal] {self.nombre} | Email: {self.email} | Saldo: ${self.__saldo:.2f}"