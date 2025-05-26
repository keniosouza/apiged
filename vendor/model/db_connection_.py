import pymysql


class MySQLConnection:
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host="localhost",
                database="docverse",
                user="root",
                password="root",
                cursorclass=pymysql.cursors.DictCursor,  # Retorna resultados como dicionário
                autocommit=False  # Transações gerenciadas manualmente
            )
            print("Conexão estabelecida com sucesso!")

        except pymysql.MySQLError as e:
            print(f"Erro ao conectar ao banco: {e}")
            self.connection = None

    def get_cursor(self):
        """Retorna um cursor para executar queries."""
        if self.connection:
            return self.connection.cursor()

    def commit(self):
        """Confirma a transação no banco de dados."""
        if self.connection:
            self.connection.commit()

    def rollback(self):
        """Desfaz a transação em caso de erro."""
        if self.connection:
            self.connection.rollback()

    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.connection:
            self.connection.close()
            print("Conexão fechada.")
