# Pipeline_Postgres_to_Postgres
 Pipeline transferencia dados BD Postgres para BD Postgres

Desenvolvimento feito em estação de Trabalho Windows 10
Software instalados:
  	MobaXterm - Personal Edition v22.2
   PostgresSQL 15.3 (pgAdmin4 / PSQL)
   Docker  version 20.10.22
   Python	3.9.7

diretório:
	   desafio
    subdiretórios:
	       desafio\data (northwind.sql)
	      desafio\destino (northwind_pk.sql)

com MobaXterm
> docker compose up db
> docker compose up dbdestino

CMD
> extracao.bat 
Para extrair dados bat - extracao.bat

> carga.bat
para carregar dados bat - carga.bat
