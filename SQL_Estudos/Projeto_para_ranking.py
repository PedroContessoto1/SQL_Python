import Biblioteca_SQL as bsql
banco = 'banco_dos_gados'
tabela = 'informação_da_boiada'
coluna = 'namoradas'
coluna1 = 'vezes_corno'

n1 = bsql.MediaColunaSQL(banco,tabela,coluna)
n2 = bsql.MediaColunaSQL(banco,tabela,coluna1)

print(n1)
print(n2)
n3 = ((n2 / n1) * 100)
final = round(n3, 2)
print(str(final) + " % ")
