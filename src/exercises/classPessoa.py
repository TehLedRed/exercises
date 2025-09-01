class Pessoa(object):
    def __init__(
        self,
        nome: str,
        idade: int,
    ) -> None:
        self.nome = nome
        self.idade = idade

    def apresentar(self) -> None:
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


class Funcionario(Pessoa):
    def __init__(
        self,
        nome: str,
        idade: int,
        salario: float,
    ) -> None:
        super().__init__(nome, idade)
        self.salario = salario


class Gerente(Funcionario):
    def __init__(
        self,
        nome: str,
        idade: int,
        salario: float,
        departamento: str,
    ) -> None:
        super().__init__(nome, idade, salario)
        self.departamento = departamento

    def apresentar(self) -> None:
        print(f"Meu nome é {self.nome} e eu mando em você.")


Ana = Gerente("Ana", 30, 5000, "RH")
Ana.apresentar()
