import Biblioteca_SQL as bsql


lista_tabela = bsql.PrintColunaSQL('banco_dos_gados','informação_da_boiada','resultado')

ordenada = sorted(lista_tabela, key=float, reverse=True)


print(ordenada)

print(ordenada[0],ordenada[1],ordenada[2])

bsql.PesquisaTabelaSQL('banco_dos_gados','nome_do_gado','informação_da_boiada','resultado',f'{ordenada[0]}')







