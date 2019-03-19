from conexao import ConexaoBanco
import getpass
import pyodbc
from datetime import datetime

class IniciaSistema():
    def conexaonosistema(self):
        self.conectar = ConexaoBanco()
        self.conectar.conexaosistema()
        
        self.conectar.cursorsist.execute('''
        SELECT
        C.chave_consulta,
        C.max_consulta,
        C.nome_consulta,
        C.sql_qtd_consulta,
        C.sql_valores_consulta,
        CL.nome_cliente,
        S.nome_sistema,
        B.alias,
        B.driver,
        B.server_instancia,
        B.usuario,
        B.password
        FROM dbo.SiteMonitoramentoMSAJ_Consulta C
        JOIN dbo.SiteMonitoramentoMSAJ_Cliente CL ON C.nome_cliente_id = CL.chave_cliente
        JOIN dbo.SiteMonitoramentoMSAJ_Sistema S ON C.nome_sistema_id = S.chave_sistema
        JOIN dbo.SiteMonitoramentoMSAJ_BaseDeDados B ON C.nome_base_id = B.alias
        WHERE 
        C.consulta_ativa = 1 AND
        C.data_inicio <= GETDATE() AND
        C.data_fim >= GETDATE()
        '''
        )
        self.consultascarregadas = tuple(self.conectar.cursorsist.fetchall())
        #print('SEGUE ABAIXO AS CONSULTAS CADASTRADAS PARA SEREM RODADAS: \n \n'
         #     'CONSULTAS ATIVAS PARA SER REALIZADAS: ')
        for self.consulta in self.consultascarregadas:
            #print(consulta)
            #print('\n',self.consulta.nome_consulta,'\n',self.consulta.nome_cliente,'\n',self.consulta.nome_sistema,'\n',self.consulta.alias)
            #rodar = input('DESEJA REALIZAR AS CONSULTAS SE "SIM" TECLE "ENTER" SE "NÃO" DIGITE "N":\n ').upper
            
            rodar = 'S'
            if rodar == 'N':
                exit()
            else:
                self.conectarl = ConexaoBanco()
                #fo self.consulta in self.consultascarregadas:
                self.conectarl.conexaoclient(self.consulta.driver, self.consulta.server_instancia, self.consulta.alias, self.consulta.usuario, self.consulta.password)
                self.conectarl.cursorcliente.execute("select * from epadscriptrodado where descript like '%SAJ/PG5%' order by dtexecucao desc")
                self.versao = self.conectarl.cursorcliente.fetchone()
                #print(self.versao)
                print('\nCONSULTA: ', self.consulta.nome_consulta, '\nBASE: ',self.consulta.server_instancia, ':',self.consulta.alias, '\nDRIVE:',self.consulta.driver)
                self.conectarl.cursorcliente.execute(self.consulta.sql_qtd_consulta)
                self.qtd = self.conectarl.cursorcliente.fetchone()
                #print(self.qtd[0])
                if int(self.qtd[0]) < 20000 and int(self.qtd[0]) < self.consulta.max_consulta:
                    #print('\n ########## CONSULTA SERÁ EXECUTADA ############')
                    self.conectarl.cursorcliente.execute(self.consulta.sql_valores_consulta)
                    self.resultadoconsulta = self.conectarl.cursorcliente.fetchall()
                    if self.qtd[0] == 0:
                        self.resultadoconsulta = ('Não Encontrou erros. ')

                    self.conectar.cursorsist.execute('select max(nuseqexecucao) as quantidade from dbo.SiteMonitoramentoMSAJ_resultadoconsulta where consulta_chave_id = ' + str(self.consulta.chave_consulta))
                    nuseq = self.conectar.cursorsist.fetchone()
                    #print(nuseq[0])
                    
                    #for self.result in self.resultadoconsulta:
                    
                    if nuseq[0] == None:
                        
                        data_atual = datetime.now()
                        data_hora_str = data_atual.strftime('%d/%m/%Y %H:%M:%S')   
                        comando = ('''
                        INSERT INTO
                        dbo.SiteMonitoramentoMSAJ_resultadoconsulta (
                        consulta_chave_id,
                        NUSEQEXECUCAO,
                        DTEXECUCAO,
                        DEVERSAO,
                        QTDVALORES,
                        valores_consulta
                        )
                        VALUES(
                        {},
                        {},
                        convert(datetime, '{}', 105),
                        "{}",
                        {}, 
                        "{}")
                        ''' ).format(self.consulta.chave_consulta, 1, data_hora_str, self.versao, self.qtd[0], self.resultadoconsulta)
                    else:
                    
                        data_atual = datetime.now()
                        data_hora_str = data_atual.strftime('%d/%m/%Y %H:%M:%S')   
                        seq = ('(select max(nuseqexecucao) +1 from dbo.SiteMonitoramentoMSAJ_resultadoconsulta where consulta_chave_id =' + str(self.consulta.chave_consulta)+')')
                        comando = ('''
                        INSERT INTO
                        dbo.SiteMonitoramentoMSAJ_resultadoconsulta (
                        consulta_chave_id,
                        NUSEQEXECUCAO,
                        DTEXECUCAO,
                        DEVERSAO,
                        QTDVALORES,
                        valores_consulta
                        )
                        VALUES(
                        {},
                        {},
                        convert(datetime, '{}', 105),
                        "{}",
                        {}, 
                        "{}")
                        ''' ).format(self.consulta.chave_consulta,seq, data_hora_str, self.versao, self.qtd[0], self.resultadoconsulta)
                    self.conectar.cursorsist.execute('BEGIN TRANSACTION')
                    self.conectar.cursorsist.execute('SET QUOTED_IDENTIFIER OFF')
                    self.conectar.cursorsist.execute(comando)
                    self.conectar.cursorsist.execute('COMMIT')
                    
                else:
                    print('CONSULTA COM VALORES ACIMA DO DEFINIDO NO LIMITE! ')
                    
ligar = IniciaSistema()
ligar.conexaonosistema()
