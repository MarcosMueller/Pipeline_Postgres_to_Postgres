# Carga dados banco de dados Northwind

# Imports
import sys
import os
import csv
import psycopg2

def carrega_tabela(tabela,diretorio):

    # conectar com banco de dados
    conn = psycopg2.connect(
        host="localhost",
        database="northwind",
        user="northwind_user",
        password="estaventando",
        port=5433)

    cur = conn.cursor()
    truncatecommand = f'TRUNCATE public.{tabela}'
    cur.execute(truncatecommand)
    nomearquivo = diretorio + "/" + tabela + ".txt"
    # Inicializa o contador
    nlinhas = 0

    print(f'==>>> Carga Tabela - {tabela}')

    with open(nomearquivo, newline='', encoding='UTF-8') as arquivo:
        csv_reader = csv.reader(arquivo, delimiter=',')

        for row in csv_reader:
            if nlinhas == 0:
                comand_columns = f'INSERT INTO public.{tabela} ({",".join(row)})'
            else:
                comand_values= f' VALUES ({",".join(row)});'
                sql_insere = comand_columns + " " + comand_values
                if imprime:
                    print(sql_insere)
                cur.execute(sql_insere)

            # Incrementa o contador
            nlinhas += 1

    conn.commit()
    cur.close()
    conn.close()
    nlinhas -= 1

    print(f'==>>> Total de {nlinhas} linhas carregadas na tabela {tabela}')

# Bloco main
if __name__ == "__main__":

    imprime = False

    if len(sys.argv) == 3:
        tabela=str(sys.argv[1])
        diretorio=(sys.argv[2])
        if not(os.path.exists(diretorio)):
            os.mkdir(diretorio)
        carrega_tabela(tabela,diretorio)
    else:
        if len(sys.argv) < 2:
            print('Erro: Informe nome da tabela')
        else:
            print('Erro: Informe nome do diretorio')

