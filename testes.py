from Cliente import Cliente
from Profissional import Profissional
from Endereco import Endereco
from servico import Servico
from Especialidades import Especialidades
from horario import Horario 
from pagamento import Pagamento

class Teste:

  def teste_cadastro_cliente():
    nome = "Usuario teste"
    cpf = "111.111.111-11"
    email = "usuario@teste.com"
    genero = "outro"

    cliente = Cliente()
    cliente_cadastrado = cliente.cadastrarCliente(nome, cpf, email, genero)

    assert cliente_cadastrado == (
      '\n'
      f'Nome= {nome}, cpf= {cpf}, email={email}, genero= {genero} ')

  def teste_cadastro_profissional ():
    nome = "Ana Maria"
    cpf = "222.222.222-22"
    email = "profissional@teste.com"
    genero= "feminino" 
    especialidade = "manicure"

    profissional = Profissional()
    profissional_cadastrado= profissional.cadastrarProfissional(nome, cpf, email, genero, especialidade)

    assert profissional_cadastrado == (
      '\n'
      f'Nome= {nome}, cpf= {cpf}, email={email}, genero= {genero} , especialidade = {especialidade}')

    def teste_informar_endereco ():
      rua = "Avenida Dias"
      bairro = "Centro"
      cidade = "Cajazeiras"
      numero = "07"

      endereco = Endereco()
      endereco_informado= endereco.informarEndereco(rua, bairro, cidade, numero)

      assert endereco_informado== (
      '\n'
      f'rua= {rua}, bairro= {bairro}, cidade={cidade}, numero {numero} ')

    def teste_cadastar_Servico():
      nomeServico = "Algum serviço"
      descricao = "Otimo Serviço"
      valor= 'preco do serviço'

      servico = Servico()
      servico_cadastrado= servico.cadastrarServico(nomeServico, descricao, valor)

      assert servico_cadastrado== (
       '\n'
       f'nomeServico= {nomeServico}, descricao= {descricao}, valor={valor}')

    def teste_escolher_Especialidades ():
      nomeEspecialidades = "Cabeleira"
      preco = "99"
      
      especialidades = Especialidades()
      especialidades_escolhida = especialidades.escolherEspecialidades(nomeEspecialidades, preco)
      
      assert especialidades_escolhida == (
       '\n'
        f'nomeEspecialidades= {nomeEspecialidades}, preco= {preco}')

    def teste_marcar_horario():
      data ="22/12"

      horario = Horario ()
      horario_marcado = horario.marcar.Horario(data)

      assert horario_marcado == (
       '\n'
        f'data= {data}')

    def teste_escolher_pagamento():
      TPagamento= 'Cartão de Crédito'

      pagamento = Pagamento ()
      pagamento_feito = pagamento.escolher.Pagamento(TPagamento)

      assert pagamento_feito == (
       '\n'
        f'TPagamento= {TPagamento}')

      
      
      

      
    
