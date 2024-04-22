import mysql.connector


def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Contas"
        )
        return conexao
    except mysql.connector.Error as erro:
        print("Erro ao conectar ao banco:", erro)
        return None

# Executar comandos SQL aqui
def consultar_dados(data_inicio, data_fim, tipo=None):
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()

            if tipo:
                # Se um tipo for especificado, filtrar por tipo na consulta
                cursor.execute("SELECT * FROM contas WHERE vencimento BETWEEN %s AND %s AND tipo = %s", (data_inicio, data_fim, tipo))
            else:
                # Caso contrário, executar a consulta sem filtrar por tipo
                cursor.execute("SELECT * FROM contas WHERE vencimento BETWEEN %s AND %s", (data_inicio, data_fim))

            resultados = cursor.fetchall()

            cursor.close()
            return resultados
        
        except mysql.connector.Error as erro:
            print("Erro ao executar consulta:", erro)
            return None
        
        finally:
            conexao.close()


def inserir_dados(valor,vencimento,descricao,tipo,data_sistema):
    conexao = conectar()
    if conexao:
        try:
            # Criar um cursor
            cursor = conexao.cursor()

            # Executar um comando de inserção
            cursor.execute("INSERT INTO Contas (valor,vencimento,descricao,tipo,data_sistema) VALUES (%s, %s, %s, %s, %s)", (valor, vencimento, descricao, tipo, data_sistema))

            # Confirmar a transação
            conexao.commit()

            # Fechar o cursor
            cursor.close()

        except mysql.connector.Error as erro:
            print("Erro ao inserir dados:", erro)

        finally:
            # Fechar a conexão
            conexao.close()

def consultar_saldo(tipo):
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()

            # Consulta SQL para calcular o saldo com base no tipo (pagar ou receber)
            if tipo.lower() == "pagar":
                cursor.execute("SELECT SUM(valor) FROM contas WHERE tipo = 'Pagar'")
            elif tipo.lower() == "receber":
                cursor.execute("SELECT SUM(valor) FROM contas WHERE tipo = 'Receber'")

            saldo = cursor.fetchone()[0]

            # Se o saldo for None, significa que não há registros ou o saldo é zero
            if saldo is None:
                return 0.0
            else:
                return saldo

        except mysql.connector.Error as erro:
            print("Erro ao consultar saldo:", erro)
            return None

        finally:
            conexao.close()