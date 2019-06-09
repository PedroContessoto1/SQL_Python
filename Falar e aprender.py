import Biblioteca_SQL as bsql

banco = "botpythonfala"
tabela1 = "lista_bot"
tabela2 = "cadastro"
certificado = 0
cadastro = 0
mensagem = 1
bugnomepersonagem = 0

nome = input("Digite seu nome : ").upper()

lista_de_nome = bsql.PrintColunaSQL(banco,tabela2,"nome")

for i in lista_de_nome:
    if i == nome:           #Verifica se existe o nome no banco
        cadastro = 1

if cadastro == 1:
    nome_do_personagem = bsql.PesquisaTabelaSQL(banco,"nome_personagem",tabela2,"nome",nome)
    nome_do_personagem = nome_do_personagem[0]    #Chama o nome do personagem

else:
    nome_personagem_novo = input("Digite o nome do seu bot : ")
    bsql.ComandosSQL(banco, f"INSERT INTO {tabela2} (nome, nome_personagem) "f"VALUES ('{nome}','{nome_personagem_novo}')")
    bugnomepersonagem = 1;



pergunta = input(f"[{mensagem}] {nome} : ").upper()

while pergunta != "SAIR":
    certificado = 0

    if bugnomepersonagem == 1:
        nome_do_personagem = nome_personagem_novo
        bugnomepersonagem = 0

    if mensagem > 1:
        pergunta = input(f"[{mensagem}] {nome} : ").upper()
    mensagem += 1



    if pergunta == "TROCA":
        pergunta_troca = input("Qual pergunta você gostaria de trocar a resposta ? : ")
        troca = input("Digite a nova resposta : ")
        bsql.AlterarValorColunaSQL(banco,tabela1,"resposta","pergunta",troca,pergunta_troca)
        certificado = 3



    lista_pergunta = bsql.PrintColunaSQL(banco,tabela1,"pergunta")

    for i in lista_pergunta:
        existe = pergunta in lista_pergunta
        if existe == True:
            resposta = bsql.PesquisaTabelaSQL(banco,"resposta",tabela1,"pergunta",pergunta)
            certificado = 1

    if certificado == 1:
        print(f"[{mensagem}] {nome_do_personagem} : {resposta[0]}")

    if certificado == 0:
        nova_resposta = input("Digite uma resposta para essa pergunta : ")
        bsql.ComandosSQL(banco, f"INSERT INTO {tabela1} (id, pergunta, resposta, colaborador) "f"VALUES (default,'{pergunta}','{nova_resposta}','{nome}')")

