from models.cliente import Cliente

class ClienteNormal(Cliente):
    def __init__(self, nombre, email, saldo):
        super().__init__(nombre, email, saldo)

    def __str__(self):
        return f"👤 [Normal] {self.nombre} | Email: {self.email} | Saldo: ${self.saldo:.2f}"

class ClienteVIP(Cliente):
    def __init__(self, nombre, email, saldo, descuento=0.10):
        super().__init__(nombre, email, saldo) 
        self.descuento = descuento

    def __str__(self):
        return f"⭐ [VIP] {self.nombre} | Email: {self.email} | Saldo: ${self.saldo:.2f} (Desc: {self.descuento*100}%)"

class ClienteCorporativo(Cliente):
    def __init__(self, nombre, email, saldo, rut_empresa):
        super().__init__(nombre, email, saldo) 
        self.rut_empresa = rut_empresa

    def __str__(self):
        return f"🏢 [CORP] {self.nombre} | RUT: {self.rut_empresa} | Saldo: ${self.saldo:.2f}"