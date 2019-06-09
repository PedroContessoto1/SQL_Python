
def PrintColunaSQL(banco, tabela, coluna):
    import pymysql as sql

    n = []

    conexao = sql.connect(db=f'{banco}', user='root', passwd='')

    cursor = conexao.cursor()

    cursor.execute(f"SELECT {coluna} FROM {tabela}")

    resultado = cursor.fetchall()

    for linha in resultado:
        for i in linha:
            n.append(i)
    return n

    conexao.close()

def ComandosSQL(banco,comando):

    import pymysql as sql

    conexao = sql.connect(db=f'{banco}', user='root', passwd='')

    cursor = conexao.cursor()

    cursor.execute(comando)

    conexao.commit()

    conexao.close()

def PesquisaTabelaSQL(banco,coluna_do_resultado,tabela,coluna_de_procurar,procura):

    import pymysql as sql

    conexao = sql.connect(db=f'{banco}', user='root', passwd='')

    cursor = conexao.cursor()

    cursor.execute(f"SELECT {coluna_do_resultado} FROM {tabela} WHERE {coluna_de_procurar} = '{procura}'")

    resultado = cursor.fetchall()

    for linha in resultado:
        linha
    return linha

    conexao.close()


def RankingSQL(banco,tabela,coluna_nome,coluna_resultado):

    lista_tabela = PrintColunaSQL(f'{banco}', f'{tabela}', f'{coluna_resultado}')

    ordenada = sorted(lista_tabela, key=float, reverse=True)

    print(f"Ranking 1 # {PesquisaTabelaSQL(f'{banco}', f'{coluna_nome}', f'{tabela}', f'{coluna_resultado}',f'{ordenada[0]}')} com {ordenada[0]} pontos \n")

    print(f"Ranking 2 # {PesquisaTabelaSQL(f'{banco}', f'{coluna_nome}', f'{tabela}', f'{coluna_resultado}',f'{ordenada[1]}')} com {ordenada[1]} pontos \n")

    print(f"Ranking 3 # {PesquisaTabelaSQL(f'{banco}', f'{coluna_nome}', f'{tabela}', f'{coluna_resultado}',f'{ordenada[2]}')} com {ordenada[2]} pontos \n")

def MediaColunaSQL(banco,tabela,coluna):
    lista = PrintColunaSQL(banco,tabela,coluna)
    n = 0
    n1 = 0
    for i in lista:
        float(i)
        n = n + 1
        n1 = n1 + i
        media = n1 / n
        final = round(media, 2)
    return final

def AlterarValorColunaSQL(banco,tabela,coluna_trocada,coluna_referencia,valor_subistituto,valor_referencia):
    ComandosSQL(banco,f"update {tabela}\nset {coluna_trocada} = '{valor_subistituto}'\nwhere {coluna_referencia} = '{valor_referencia}';")















