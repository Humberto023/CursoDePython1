class contaBancaria:
    def __init__ (self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.historico = []

    def depositar(self, valor):
        self.saldo += valor
        self.historico.append(f'O valor depositado foi de R$ {valor}')
        print(f'Depositado foi de R$ {valor}')

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.append(f'O valor sacado foi de R$ {valor}')
            print(f'Saque de R$ {valor} realizado com sucesso')
        else:
            print(f'Saldo insuficiente, tente novamente, valor em conta de R${self.saldo}')

    def ver_saldo(self):
        print(f'Saldo atual: {self.saldo}')

    def ver_historico(self):
        for h in self.historico:
            print('-', h)

conta = contaBancaria('Beto', 100)

conta.depositar(100)
conta.sacar(100)
conta.ver_saldo()
conta.ver_historico()

