class Cachorro:
    def emitir_som(self):
        print('AuAu')


class Gato:
    def emitir_som(self):
        print('Miau')

animais = [Cachorro(), Gato()]

for a in animais:
    a.emitir_som()