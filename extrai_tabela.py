# Extracao dados banco de dados Northwind

# Imports
import datetime
import os
import sys
import psycopg2

def duplica_aspas(texto, n):
    novotexto = ""
    while n > 0:
        i = texto.find("'")
        novotexto = novotexto + texto[0:i+1] + "'"
        texto = texto[i+1:len(texto)]
        n -= 1
    novotexto = novotexto + texto
    return novotexto

def extrai_tabela(tabela,diretorio):
    # conectar com banco de dados
    conn = psycopg2.connect(
        host="localhost",
        database="northwind",
        user="northwind_user",
        password="thewindisblowing",
        port=5432)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    nlinhas = 0

    # abre arquivo para escrita
    nomearquivo= diretorio + "/" + tabela + ".txt"
    arquivo = open(nomearquivo, 'wt', encoding='UTF-8')

    # colunas da query
    if tabela == 'categories':
        linha = 'category_id,category_name,description,picture'
    elif tabela == 'customer_customer_demo':
        linha = 'customer_id,customer_type_id'
    elif tabela == 'customer_demographics':
        linha = 'customer_type_id,customer_desc'
    elif tabela == 'customers':
        linha = "customer_id,company_name,contact_name,contact_title,address,city,region,postal_code,country," \
                "phone,fax"
    elif tabela == 'employee_territories':
        linha = 'employee_id,territory_id'
    elif tabela == 'employees':
        linha = "employee_id,last_name,first_name,title,title_of_courtesy,birth_date,hire_date,address,city," \
                "region,postal_code,country,home_phone,extension,photo,notes,reports_to,photo_path"
    elif tabela == "orders":
        linha = "order_id,customer_id,employee_id,order_date,required_date,shipped_date,ship_via,freight," \
                "ship_name,ship_address,ship_city,ship_region,ship_postal_code,ship_country"
    elif tabela == 'products':
        linha = "product_id,product_name,supplier_id,category_id,quantity_per_unit," \
                "unit_price,units_in_stock,units_on_order,reorder_level,discontinued"
    elif tabela == "region":
        linha = 'region_id,region_description'
    elif tabela =='shippers':
        linha = "shipper_id,company_name,phone"
    elif tabela == 'suppliers':
        linha = "supplier_id,company_name,contact_name,contact_title,address,city,region,postal_code,country," \
                "phone,fax,homepage"
    elif tabela == "territories":
        linha = "territory_id,territory_description,region_id"
    elif tabela == 'us_states':
        linha = 'state_id,state_name,state_abbr,state_region'
    else:
        print("tabela: {tabela} desconhecida")
        return

    # colunas da tabela para arquivo CSV
    if imprime:
        print(linha)
    arquivo.write(linha+"\n")

    # Execute a query
    if tabela == 'employees':
        linha = "employee_id,last_name,first_name,title,title_of_courtesy,TO_CHAR(birth_date,'YYYY-MM-DD')," \
            "TO_CHAR(hire_date, 'YYYY-MM-DD'),address,city,region,postal_code,country,home_phone," \
            "extension,photo,notes,reports_to,photo_path"
        if imprime:
            print(f"linha de select para employees: {linha}")
    elif tabela == 'order':
        linha = "order_id, customer_id, employee_id, TO_CHAR(order_date,'YYYY-MM-DD'), " \
                "TO_CHAR(required_date,'YYYY-MM-DD'), TO_CHAR(shipped_date,'YYYY-MM-DD'), " \
                "ship_via,freight, ship_name, ship_address, ship_city, ship_region, ship_postal_code, " \
                "ship_country"
        if imprime:
            print(f"linha de select para orders: {linha}")

    sql_comand = f"SELECT {linha} FROM public.{tabela}"

    if imprime:
        print(sql_comand)

    cur.execute(sql_comand)

    # Retrieve query results
    records = cur.fetchall()

    print(f'==>>> Extração Tabela - {tabela}')

    for linha in records:
        if imprime:
            print(linha)
        i = 0
        colunas = ""
        for item in linha:
            if i != 0:
                colunas = colunas + ","
            i = i + 1
            if imprime:
                print(f'coluna: {i} tipo {type(item)}valor {item}')
            if type(item) == int or type(item) == float or type(item) == complex:
                colunas = colunas + str(item)
            elif type(item) == memoryview:
                colunas = colunas + "''"
            elif type(item) == str:
                qtd = item.count("'")
                if qtd != 0:
                    item = duplica_aspas(item, qtd)
                if item == 'None':
                    colunas = colunas + 'null'
                else:
                    colunas = colunas + "'" + item + "'"
            elif type(item) == datetime.date:
                colunas = colunas + "'" + str(item) + "'"
            else:
                if tabela == 'employees' or tabela == 'customers' \
                        or tabela == 'orders' or tabela == 'suppliers':
                    colunas = colunas + 'null'
                else:
                    colunas = colunas + str(item)
        arquivo.write(colunas+'\n')
        if imprime:
            print(colunas)
            if nlinhas == 10:
                return

        nlinhas += 1

    print(f'==>>> Total de {nlinhas} linhas no arquivo {nomearquivo}')

# Bloco main
if __name__ == "__main__":

    imprime = False

    if len(sys.argv) == 3:
        tabela=str(sys.argv[1])
        diretorio=(sys.argv[2])
        if not(os.path.exists(diretorio)):
            os.mkdir(diretorio)
        extrai_tabela(tabela,diretorio)
    else:
        if len(sys.argv) < 2:
            print('Erro: Informe nome da tabela')
        else:
            print('Erro: Informe nome do diretorio')
