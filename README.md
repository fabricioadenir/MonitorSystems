<img src="https://cdn.jsdelivr.net/gh/verifiqueme/web@master/src/assets/icon.png" width="123px" alt="verifica.me" align="right">

# Monitoramento de Sistemas
MonitorSystems foi criado para gerenciar correções nos sistemas e localizar erros de inconsistências de dados.

BackEnd e FrontEnd.
=====
* Back End: Realiza uma consulta para encontrar as rotinas a serem executadas, localizando-as e executando conforme cadastradas. Realizando o salvamento dessas informações obtidas pela rotina em uma base local. 

* Front End: Responsável por disponibilizar os formulários de cadastros, consulta, alteração e remoção das rotinas no sistema e também responsável pela apresentação dos resultados das rotinas.

***
Depende de:
* [Python 3](https://www.python.org/downloads/) (3+)

Instalando Dependências
=====
```
pip  install -r requirements.txt
```
Executar os comandos:
```
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser --email admin@example.com --username admin

python manage.py runserver
```
## Contato
Em caso de dúvidas ou encontrou um erro, entre em contato conosco através do e-mail ou abra uma issue no projeto:

[Fabricio Silva](mailto:fabricioadenir@gmail.com)
