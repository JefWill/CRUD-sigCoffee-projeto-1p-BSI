import os
from modulos import cliente, produto, pedido, relatorio
import pickle



#####################################
#####   Projeto SIG-Coffe - V9  #####
#####################################


lista_clientes = {
 
 }

try:
    arq_clientes = open("clientes.dat", "rb")
    lista_clientes = pickle.load(arq_clientes)
except:
    arq_clientes = open("clientes.dat", "wb")
arq_clientes.close()


lista_produtos = {

 }

try:
    arq_produtos = open("produtos.dat", "rb")
    lista_produtos = pickle.load(arq_produtos)
except:
    arq_produtos = open("produtos.dat", "wb")
arq_produtos.close()



lista_pedidos = {
    
 }
try:
    arq_pedidos = open("pedidos.dat", "rb")
    lista_pedidos = pickle.load(arq_pedidos)
except:
    arq_pedidos = open("pedidos.dat", "wb")
arq_pedidos.close()


pedidos_cancelados = {
    
 }
try:
    arq_pedidos_cancelados = open("pedidos_cancelados.dat", "rb")
    pedidos_cancelados = pickle.load(arq_pedidos_cancelados)
except:
    arq_pedidos_cancelados = open("pedidos_cancelados.dat", "wb")
arq_pedidos_cancelados.close()


#############################################################
#######    P R O G R A M A   P R I N C I P A L     ##########
#############################################################

op_princ = ''
while op_princ != '0':
    os.system('clear')
    print()
    print("##############################################")
    print("#####       Projeto SIG-Coffe            #####")
    print("##############################################")
    print("#####      1 - Módulo Produto            #####")
    print("#####      2 - Módulo Cliente            #####")
    print("#####      3 - Módulo Pedido             #####")
    print("#####      4 - Módulo Relatório          #####")
    print("#####      5 - Módulo Informações        #####")
    print("#####      0 - Sair                      #####")
    op_princ = input("##### Escolha sua opção: ")
    if op_princ == '1':
        op_produto = ''
        while op_produto != '0':
            op_produto = produto.menu_produto()
            print()
            if op_produto == '1':
                produto.cadastrar_produto(lista_produtos)
            elif op_produto == '2':
                produto.exibir_produtos(lista_produtos)
            elif op_produto == '3':
                produto.alterar_produto(lista_produtos)
            elif op_produto == '4':
                produto.inativar_produto(lista_produtos)

    elif op_princ == '2':
       op_cliente = ''
       while op_cliente != '0':
          op_cliente = cliente.menu_cliente()
          print()
          if op_cliente == '1':
              cliente.cadastrar_cliente(lista_clientes)
          elif op_cliente == '2':
              cliente.exibir_cliente(lista_clientes)
          elif op_cliente == '3':
              cliente.alterar_cliente(lista_clientes)
          elif op_cliente == '4':
              cliente.inativar_cliente(lista_clientes)
    elif op_princ == '3':
        op_pedido = ''
        while op_pedido != '0':
            op_pedido = pedido.menu_pedido()
            if op_pedido == '1':
                pedido.cadastrar_pedido(lista_pedidos, lista_clientes,lista_produtos)
            elif op_pedido == '2':
              pedido.exibir_pedidos(lista_clientes, lista_produtos, lista_pedidos)
            elif op_pedido == '3':
                pedido.exibir_pedidos_cancelados(pedidos_cancelados, lista_clientes, lista_produtos)
            elif op_pedido == '4':
                pedido.cancelar_pedido(lista_pedidos, pedidos_cancelados)

    elif op_princ == '4':
        op_relatorio = ''
        while op_relatorio != '0':
            op_relatorio = relatorio.menu_relatorio()
            if op_relatorio == '1':
                produto.exibir_produtos(lista_produtos)
            elif op_relatorio == '2':
                cliente.exibir_cliente(lista_clientes)
            elif op_relatorio == '3':
                pedido.exibir_pedidos(lista_clientes, lista_produtos, lista_pedidos)
            elif op_relatorio == '4':
                relatorio.relatorio_detalhes_pedido(lista_clientes, lista_produtos, lista_pedidos)
            elif op_relatorio == '5':
                relatorio.lista_de_pedidos_por_cliente(lista_clientes, lista_produtos, lista_pedidos)
            elif op_relatorio == '6':
                produto.exibir_produtos_inativos(lista_produtos)
            elif op_relatorio == '7':
                cliente.exibir_cliente_inativo(lista_clientes)

    elif op_princ == '5':
        print()
        print("############################################")
        print("#####  Você está no Módulo Informações  ####")
        print("############################################")
        print()
        print("##### Porgrama P/ gestão de fábrica de café ####")
        print("##### Equipe de desenvolvimento:        ####")
        print("##### Jefferson willame Sena de Medeuros ####")
        print("##### SIG COFFE PROJETO DE CURSO        ####")
        print()
        input("Tecle <ENTER> para continuar...")


print("Você encerrou o programa!")
print("Até mais!")


### Gravando os dados no arquivo
os.system('clear')
print(lista_clientes)
print()
print(lista_produtos)
print()
print(lista_pedidos)
print()
print(pedidos_cancelados)

arq_produtos = open("produtos.dat", "wb")
pickle.dump(lista_produtos, arq_produtos)
arq_produtos.close()

arq_clientes = open("clientes.dat", "wb")
pickle.dump(lista_clientes, arq_clientes)
arq_clientes.close()


arq_pedidos = open("pedidos.dat", "wb")
pickle.dump(lista_pedidos, arq_pedidos)
arq_pedidos.close()


arq_pedidos_cancelados = open("pedidos_cancelados.dat", "wb")
pickle.dump(pedidos_cancelados, arq_pedidos_cancelados)
arq_pedidos_cancelados.close()