# Personagem: classe mae
# HEroi: Controlado pelo usuario
# Inimigo: Adversario do usuario

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
    
    # Getters retorna o valor do atributo encapsulado
    def get_nome(self):  
        return self.__nome
    def get_vida(self):  
        return self.__vida
    def get_nivel(self):  
        return self.__nivel
    def exibir_detalhes(self):
        return f'\nNome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}'
    
    def atacar(self, alvo):
        dano = self.__nivel * 2
        alvo.receber_ataque(dano)
        print(f'{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano')
    def receber_ataque(self,dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida == 0

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
    def get_habilidade(self):
        return self.__habilidade
    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}'

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    def get_tipo(self):
        return self.__tipo
    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n'


class jogo:
    """Classe orquestradora do jogo"""
    def __init__(self):
        self.heroi = Heroi("Mauro", 100, 5, "Super soco")
        self.inimigo = Inimigo("morcego", 50, 3, "Fogo") 

    def iniciar_batalha(self):
        """Gestao de batalha"""
        print("Iniciando batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("Detalhes dos personagens")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input("Escolha ([1]. Ataque normal, [2]. Ataque Especial): ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            else:
                print("comando invalido")
        if self.heroi.get_vida() > 0:
            print(f"\nParabens, voce derrotou [{self.inimigo.get_nome()}]")
        else:
            print("\nVoce foi derrotado")




# Criando as instancias para inicio de combate
game = jogo()
game.iniciar_batalha()
