class Endereco :
  def __init__ (self, rua, bairro, cidade, numero):
    self.rua= rua
    self.bairro= bairro
    self.cidade= cidade
    self.numero= numero
    
  def informar_Endereco(self):
    self.rua= ( input('\n ' "Forneça sua rua: "))
    self.bairro= (input(" Forneça seu bairro: "))
    self.cidade= (input(" Forneça sua cidade: "))
    self.numero= (input(" Forneça o numero da casa: "))
    print("\n Endereço Cadastrado")

  