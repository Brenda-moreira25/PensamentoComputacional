from .Veiculos import Veiculos      

class Proprietarios():
    def __init__(self, nome: str, cpf: str, telefone: str) -> None:
        """Construtor da classe Proprietario"""
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__veiculos = []    

    def __str__(self):
        """Retorna uma string com as informações do proprietario"""
        infos =  f"Nome: {self.__nome}\n"
        infos += f"CPF: {self.__cpf}\n"
        infos += f"Telefone: {self.__telefone}\n"
        infos += "Veículos:\n"
        for veiculo in self.__veiculos:
            infos += str(veiculo) + "\n"
        return infos
    
    def __vaalidarcpf(self, cpf: str ) -> bool:
        """Método privado para validar o CPF"""
        # Exemplo simples: verificar se o CPF tem 11 dígitos
        return len(cpf) == 11 and cpf.isdigit()
    
    def adicionar_veiculo(self, veiculo: Veiculos) -> bool:
        """Método para adicionar um veículo ao proprietário"""
        if isinstance(veiculo, Veiculos):
            self.__veiculos.append(veiculo)
            return True
        return False
    def remover_veiculo(self, placa: str) -> bool: 
        """Método para remover um veículo do proprietário pelo número da placa"""
        for veiculo in self.__veiculos:
            if veiculo.getPlaca() == placa:
                self.__veiculos.remove(veiculo)
                return True
        return False
    
    def get_nome(self) -> str:
        """Método para obter o nome do proprietário"""
        return self.__nome
    
    def set_nome(self, nome: str) -> None:  
        """Método para definir o nome do proprietário"""
        self.__nome = nome  

    def get_cpf(self) -> str:
        """Método para obter o CPF do proprietário"""
        return self.__cpf   
    def set_cpf(self, cpf: str) -> None:    
        """Método para definir o CPF do proprietário"""
        if self.__vaalidarcpf(cpf):
            self.__cpf = cpf
        else:
            raise ValueError("CPF inválido")
    
    def get_telefone(self) -> str:  
        """Método para obter o telefone do proprietário"""
        return self.__telefone
    def set_telefone(self, telefone: str) -> None:
        """Método para definir o telefone do proprietário"""
        self.__telefone = telefone
    def get_veiculos(self) -> list:
        """Método para obter a lista de veículos do proprietário"""
        return self.__veiculos
    def set_veiculos(self, veiculos: list) -> None:
        """Método para definir a lista de veículos do proprietário"""
        if isinstance(veiculos, list):
            self.__veiculos = veiculos
        else:
            raise ValueError("Veículos devem ser uma lista")
    def calcular_consumo(self, distancia: float) -> float:

        """Método para calcular o consumo de combustível dos veículos do proprietário"""
        total_consumo = 0
        for veiculo in self.__veiculos:
            if hasattr(veiculo, 'calcular_consumo'):
                total_consumo += veiculo.calcular_consumo(distancia)
        return total_consumo
    def listar_veiculos(self) -> str:
        """Método para listar os veículos do proprietário"""
        if not self.__veiculos:
            return "Nenhum veículo cadastrado."
        lista = "Veículos do Proprietário:\n"
        for veiculo in self.__veiculos:
            lista += str(veiculo) + "\n"
        return lista
    def buscar_veiculo_por_placa(self, placa: str) -> Veiculos:
        """Método para buscar um veículo pelo número da placa"""
        for veiculo in self.__veiculos:
            if veiculo.getPlaca() == placa:
                return veiculo
        return None         
    def buscar_veiculo_por_modelo(self, modelo: str) -> list:
        """Método para buscar veículos pelo modelo"""
        veiculos_encontrados = []
        for veiculo in self.__veiculos:
            if veiculo.getModelo() == modelo:
                veiculos_encontrados.append(veiculo)
        return veiculos_encontrados
    def buscar_veiculo_por_marca(self, marca: str) -> list:
        """Método para buscar veículos pela marca"""
        veiculos_encontrados = []
        for veiculo in self.__veiculos:
            if veiculo.getMarca() == marca:
                veiculos_encontrados.append(veiculo)
        return veiculos_encontrados
    def buscar_veiculo_por_ano(self, ano: int) -> list:
        """Método para buscar veículos pelo ano"""
        veiculos_encontrados = []
        for veiculo in self.__veiculos:
            if veiculo.getAno() == ano:
                veiculos_encontrados.append(veiculo)
        return veiculos_encontrados
    def buscar_veiculo_por_cor(self, cor: str) -> list:
        """Método para buscar veículos pela cor"""
        veiculos_encontrados = []
        for veiculo in self.__veiculos:
            if veiculo.getCor() == cor:
                veiculos_encontrados.append(veiculo)
        return veiculos_encontrados 