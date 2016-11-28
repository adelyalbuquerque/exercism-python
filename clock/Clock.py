class Clock:
    def __init__(self, horas, minutos):
        self.horas = horas
        self.minutos = minutos
        self.formatar_minutos()
        self.formatar_horas()

    def __str__(self):
        self.horas = str(self.horas)
        self.minutos = str(self.minutos)
        return '{}:{}'.format(self.horas.zfill(2),self.minutos.zfill(2))

    def dimunir_minutos_maiores_sesenta(self):
        self.horas = (self.minutos / 60) + self.horas
        self.minutos = self.minutos % 60

    def manejar_minutos_negativos(self):
        self.minutos = -self.minutos
        self.horas = self.horas - (self.minutos / 60)
        self.minutos = 60 - (self.minutos % 60)
        self.horas = self.horas - 1

    def formatar_minutos(self):
        if self.minutos >= 60:
            self.dimunir_minutos_maiores_sesenta()
        elif self.minutos < 0:
            self.manejar_minutos_negativos()

    def manejar_horas_negativas(self):
        if self.horas < -24:
            self.horas = self.horas * -1
            self.horas = self.horas % 24
            self.horas = self.horas * -1
        if self.horas != 0:
            self.horas = 24 + self.horas

    def formatar_horas(self):
        if self.horas >= 24:
            self.horas = (self.horas % 24)
        elif self.horas < 0:
            self.manejar_horas_negativas()

    def add(self, minutos_adicionados):
        self.minutos = self.minutos + minutos_adicionados
        self.formatar_minutos()
        self.formatar_horas()
        return self

# str(Clock(10,0).add(3)) 1003
# str(Clock(8,0)) --- 8:00
# str(Clock(1, 160)) -- 3:40
# str(Clock(24,0)) -- 00:00
# str(Clock(25,0)) -- 01:00
# str(Clock(100,0)) --
