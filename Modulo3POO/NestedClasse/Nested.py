#Criar classe Main

class Computador:
    def __init__(self,modelo,gpu_nome,gpu_memoria,cpu_nome, cpu_core, cpu_clock ):   #Construtor
        self.modelo = modelo
        self.gpu = self.GPU(gpu_nome, gpu_memoria)
        self.cpu = self.CPU(cpu_nome, cpu_core, cpu_clock)


    def mostrar_configuracao(self):                #Função de mostrar configuração onde precisa mostrar tanto a GPu quanto CPU
        print(f'Computador: {self.modelo}')
        self.gpu.mostrar_gpu()
        self.cpu.mostrar_cpu()


    class GPU: #Nested class
        def __init__(self,nome, memoria_gb):
            self.nome = nome
            self.memoria_gb = memoria_gb

        def mostrar_gpu(self):
            print(f'GPU: {self.nome} - {self.memoria_gb}')

    class CPU:
        def __init__(self,nome ,cores,clocks_ghz_):
            self.nome = nome
            self.cores = cores
            self.clocks_ghz_ = clocks_ghz_

        def mostrar_cpu(self):
            print(f'CPU: {self.nome} - {self.cores} nucleos - {self.clocks_ghz_}GHz')

#Utilização

pc1 = Computador('Dell g15','RTX4050',6, 'Intel Core i7', 8, 4.6)
pc1.mostrar_configuracao()
