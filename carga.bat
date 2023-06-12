@echo off
set diretorio=origem%date:~6,4%%date:~3,2%%date:~0,2%
python carrega_tabela.py categories %diretorio%  
python carrega_tabela.py customers %diretorio%  
python carrega_tabela.py customer_customer_demo %diretorio%  
python carrega_tabela.py customer_demographics %diretorio%  
python carrega_tabela.py employees %diretorio%  
python carrega_tabela.py employee_territories %diretorio%  
python carrega_tabela.py orders %diretorio%  
python carrega_tabela.py order_details %diretorio%  
python carrega_tabela.py products %diretorio%  
python carrega_tabela.py region %diretorio%  
python carrega_tabela.py shippers %diretorio%  
python carrega_tabela.py suppliers %diretorio%  
python carrega_tabela.py territories %diretorio%  
python carrega_tabela.py us_states %diretorio%  

