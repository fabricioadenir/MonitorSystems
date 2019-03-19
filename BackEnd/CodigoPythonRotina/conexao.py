import pyodbc
import cx_Oracle
import getpass
from datetime import datetime


class ConexaoBanco():
    # Dados para conexão com o sistema MSAJ
    def conexaosistema(self):
        self.driver = '{SQL Server}'
        self.server = 'soft020-742\msaj'
        self.database = 'dbmsaj'
        self.database = 'dbsitemsaj'
        self.usuario = 'adminmsaj'
        self.password = '.zxcsdr#123'
        self.conexaosist = ('DRIVER='+ self.driver + ';SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.usuario + ';PWD=' + self.password)
    
        # Tratamento de erro de coneão com o MSAJ
        try:
            #print('#################      CONECTANDO...     #################\n')

            self.conectarsist = pyodbc.connect(self.conexaosist, autocommit=True)
            
            #print('#################  CONECTADO AO SISTEMA  ##################\n')
            
            self.cursorsist = self.conectarsist.cursor()
            
        # Fazer criação de arquivo de log    
        except pyodbc.Error as ErroAcessarSistema:
            
            #print('\n########################################################### \n'
            #         '#########       OCORREU UM ERRO DE CONEXÃO       ##########\n'
            #         '###########################################################\n')
            
            self.erroconexao = ErroAcessarSistema.args[1]
            
            #print(self.erroconexao)
            
            exit()

    def conexaoclient(self, driver, server, database, usuario, password):
        if driver == 'sql server':
            self.conexao = ('DRIVER='+ driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + usuario + ';PWD=' + password)
            self.conectar = pyodbc.connect(self.conexao, autocommit=False)
            self.cursorcliente = self.conectar.cursor()  


        if driver == 'oracle':
            self.conexao = (usuario + '/' + password + '@' + server + '/' + database)
            self.conectar = cx_Oracle.connect(self.conexao)
            self.cursorcliente = self.conectar.cursor()  

        #self.conexao = ('DRIVER='+ driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + usuario + ';PWD=' + password)
        #self.conectar = pyodbc.connect(self.conexao, autocommit=False) 
        #print('CONEXÃO REALIZADA '+ str(datetime.now()) + ' COM SUCESSO! ')
        

'''
        # Conexão usando o Driver SQL:
        if driver == 'SQL SERVER':
            self.conexao = ('DRIVER='+ driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + usuario + ';PWD=' + password)
            print('conectou')
            self.conectar = pyodbc.connect(self.conexao, autocommit=False) 
            print('CONEXÃO REALIZADA '+ str(datetime.now()) + ' COM SUCESSO! ')
            self.cursorcliente = self.conectar.cursor()

        # Conexão usando o drive Oracle:
        elif driver == 'ORACLE':
            self.conexao = ('{}/{}}@{}}').format(usuario,password,database)
            self.conectar = pyodbc.connect(self.conexao)
            print('CONEXÃO REALIZADA '+ str(datetime.now()) + ' COM SUCESSO! ')   
            self.cursorcliente = self.conectar.cursor()

'''