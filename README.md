<img src="https://cdn.jsdelivr.net/gh/verifiqueme/web@master/src/assets/icon.png" width="123px" alt="verifica.me" align="right">

# Monitoramento de Sistemas


ProjetoMonitorarBases foi criado para gerenciar correções no sistema e localizar erros de inconsistências de informações.

BackEnd e FrontEnd.
=====

* Back End: Realiza uma consulta para encontrar as rotinas a serem executadas, localizandoas e executando conforme cadastradas. Realizando o salvamento dessas informações obtidas pela rotina em uma base local. 

* Front End: Responsável por disponibilizar os formulários de cadastros, consulta, alteração e remoção das rotinas no sistema e também responsável pela apresentação dos resultados das rotinas.

***

Instalando
=====

**Executar**
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
"crie sua senha"
python manage.py runserver

Depende de:
* [Python 3](https://www.python.org/downloads/) (3+)(32bits)
* [Pip](https://pypi.org/project/pip/)
* [Django](https://www.djangoproject.com/download/) (2.1.7+)
* [SQL Server 2012](https://www.microsoft.com/pt-br/download/details.aspx?id=56042) ou (Usar o SQLite)


### Instalando dependências
Instalar as bibliotecas necessárias
```sh
pip install pyodbc
pip install cx_Oracle
```
