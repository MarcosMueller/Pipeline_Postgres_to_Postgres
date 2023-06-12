@echo off
set diretorio=origem%date:~6,4%%date:~3,2%%date:~0,2%
python extrai_tabela.py categories %diretorio%
python extrai_tabela.py customers %diretorio%
python extrai_tabela.py customer_customer_demo %diretorio%
python extrai_tabela.py customer_demographics %diretorio% 
python extrai_tabela.py employees %diretorio%
python extrai_tabela.py employee_territories %diretorio%
python extrai_tabela.py orders %diretorio%
python extrai_tabela.py products %diretorio%
python extrai_tabela.py region %diretorio%
python extrai_tabela.py shippers %diretorio%
python extrai_tabela.py suppliers %diretorio%
python extrai_tabela.py territories %diretorio%
python extrai_tabela.py us_states %diretorio%
echo "==>>> Copiando OrderDetails.txt"
copy OrderDetailsCSV.txt %diretorio%\order_details.txt
