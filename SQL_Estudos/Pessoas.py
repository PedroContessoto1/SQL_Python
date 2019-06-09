import pymysql as sql

conexao = sql.connect(db='cadastro', user='root', passwd='')

cursor = conexao.cursor()

nome = input("Nome : ")
nacimento = input("Nacimento : ")
sexo = input("sexo : ")
peso = input("peso : ")
altura = input("altura : ")
nacionalidade = input("nacionalidade : ")

cursor.execute("INSERT INTO gafanhotos (nome, nacimento, sexo, peso, altura, nacionalidade) "
               "VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(nome, nacimento, sexo, peso, altura, nacionalidade))

conexao.commit()
conexao.close()