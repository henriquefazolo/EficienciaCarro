'''
A medida de eficiência de um carro é medida em km/l (quantos km o carro anda com 1 litro de combustível).
Faça um algoritmo que calcule a eficiência de um carro tendo como entrada a distância percorrida e
a quantidade de combustível gasta em litros.
'''


class EficienciaVeiculo:
    def __init__(self, distancia_percorrida, litros_gastos):
        self.distancia_percorrida = distancia_percorrida
        self.litros_gastos = litros_gastos

    def eficiencia(self):
        resultado_eficiencia = f'Distância percorrida = {self.distancia_percorrida:.2f} Km. \n' \
                               f'Quantidade gasta = {self.litros_gastos:.2f} litros. \n' \
                               f'Eficiência: {self.distancia_percorrida / self.litros_gastos:.2f}.\n'

        return resultado_eficiencia


class EficienciaVeiculoCombustivel:
    
    def __init__(self, eficiencia_gasolina, eficiencia_etanol, preco_gasolina, preco_etanol):
        """
        Recebe valores de eficiencias de diferentes combustiveis e seus valores.

        :param eficiencia_gasolina: float
        :param eficiencia_etanol: float
        :param preco_gasolina: float
        :param preco_etanol: float
        """
        self.eficiencia_gasolina = eficiencia_gasolina
        self.eficiencia_etanol = eficiencia_etanol
        self.preco_gasolina = preco_gasolina
        self.preco_etanol = preco_etanol

    def eficiencia(self):
        """

        :return: Retorna a eficiencia do veiculo em diferentes combustiveis e preços.
        """
        resultado_eficiencia = f'Eficiência com gasolina: {self.eficiencia_gasolina:.2f} \n' \
                               f'Preço da gasolina: R$ {self.preco_gasolina:.2f} \n' \
                               f'Valor do km rodado com gasolina: R$ {self.preco_gasolina / self.eficiencia_gasolina:.2f} \n' \
                               f'\n' \
                               f'Eficiência com gasolina: {self.eficiencia_etanol:.2f} \n' \
                               f'Preço da gasolina: R$ {self.preco_etanol:.2f} \n' \
                               f'Valor do km rodado com gasolina: R$ {self.preco_etanol / self.eficiencia_etanol:.2f} \n' \

        return resultado_eficiencia


carro = EficienciaVeiculo(300, 20)
print(carro.eficiencia())

carro2 = EficienciaVeiculoCombustivel(15, 10, 4.3, 3.5)
print(carro2.eficiencia())

