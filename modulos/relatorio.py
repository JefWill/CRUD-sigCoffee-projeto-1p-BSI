import os
from modulos import cliente


#################################
###         relatorio         ###         
###############################=#
def menu_relatorio():
  os.system('clear')
  print()
  print("############################################")
  print("#####         Módulo Relatório         #####")
  print("############################################")
  print("##### 1 - Lista Geral de produtos        #####")
  print("##### 2 - Lista Geral de Clientes        #####")
  print("##### 3 - Lista Geral de pedidos         #####")
  print("##### 4 - Detalhes de um pedido          #####")
  print("##### 5 - Lista de pedidos por Cliente   #####")
  print("##### 6 - Lista de produtos inativos     #####")
  print("##### 7 - Lista de clientes inativos     #####")
  print("##### 0 - Retornar ao Menu Principal     #####")
  op_relatorio = input("##### Escolha sua opção: ")
  return op_relatorio

def relatorio_detalhes_pedido(lista_clientes, lista_produtos, lista_pedidos):
  os.system('clear')
  print()
  print("############################################")
  print("#####       Detalhes do Pedido         #####")
  print("############################################")
  print()
  id_pedido = int(input("##### Informe o ID do pedido: "))

  if id_pedido in lista_pedidos:
    pedido = lista_pedidos[id_pedido]
    cliente = lista_clientes[pedido['cpf']]
    produto = lista_produtos[pedido['id_produto']]

    print("-----------------------------------------")
    print(f"ID do Pedido:    {id_pedido}")
    print(f"Data do Pedido:  {pedido['data_criacao']}")
    print("-----------------------------------------")
    print("CLIENTE:")
    print(f"  CPF:  {pedido['cpf']}")
    print(f"  Nome: {cliente['nome']}")
    print("-----------------------------------------")
    print("PRODUTO:")
    print(f"  ID:      {pedido['id_produto']}")
    print(f"  Nome:    {produto['nome']}")
    print(f"  Qtd:     {pedido['qtd']}")
    print(f"  Valor Total: R$ {(pedido['valor'] * pedido['qtd']):.2f}")
    print("-----------------------------------------")
  else:
    print("\n##### Pedido não encontrado!")
  
  input("\n##### Tecle <ENTER> para continuar...")

def lista_de_pedidos_por_cliente(lista_clientes, lista_produtos, lista_pedidos): ##CREDITOS AO GEMINI : me ajudou com a logica deste relatorio
  os.system('clear')
  print()
  print("############################################")
  print("#####   Lista de Pedidos por Cliente   #####")
  print("############################################")
  print()
  
  cpf_cliente = cliente.ler_cpf(lista_clientes)
  
  if cpf_cliente in lista_clientes:
    pedidos_encontrados = 0
    print(f"##### Pedidos para o Cliente: {lista_clientes[cpf_cliente]['nome']} (CPF: {cpf_cliente}) #####")
    print("--------------------------------------------------")
    for id_pedido, pedido in lista_pedidos.items():
      if pedido['cpf'] == cpf_cliente:
        pedidos_encontrados = 1
        print(f"ID do Pedido: {id_pedido}")
        print(f"  Produto:      {lista_produtos[pedido['id_produto']]['nome']}")
        print(f"  Quantidade:   {pedido['qtd']}")
        print(f"  Valor Total:  R$ {pedido['valor']:.2f}")
        print(f"  Data de Criação: {pedido['data_criacao']}")
        print("--------------------------------------------------")
    
    if pedidos_encontrados == 0:
      print("##### Nenhum pedido encontrado para este cliente.")
  
  input("\n##### Tecle <ENTER> para continuar...")
