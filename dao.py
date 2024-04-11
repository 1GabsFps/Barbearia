import mysql.connector as sql


class UsuarioDAO:
    @classmethod
    def autenticar(cls, nome, senha):
        connection = sql.connect(
            host="127.0.0.1", user="root", password="", database="frioli_hair"
        )
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT * FROM usuarios WHERE nome = '{nome}' AND senha = '{senha}'"
        )
        user = cursor.fetchall()
        connection.commit()
        cursor.close()
        return user[0][2] if user else False

    @classmethod
    def cadastrar(cls, nome, senha, cpf, email, telefone):
        connection = sql.connect(
            host="127.0.0.1", user="root", password="", database="frioli_hair"
        )
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO usuarios (nome, senha, cpf, email, telefone) VALUES ('{nome}', '{senha}', '{cpf}', '{email}', '{telefone}')"
        )
        connection.commit()
        cursor.close()


class HorarioDAO:
    @classmethod
    def buscar_todos(cls):
        connection = sql.connect(
            host="127.0.0.1", user="root", password="", database="frioli_hair"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM horarios")
        horarios = cursor.fetchall()
        connection.commit()
        cursor.close()
        return horarios

    @classmethod
    def salvar(cls, horario, disponivel):
        connection = sql.connect(
            host="127.0.0.1", user="root", password="", database="frioli_hair"
        )
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO horarios (horario, disponivel) VALUES ('{horario}', '{disponivel}')"
        )
        connection.commit()
        cursor.close()


class AgendamentoDAO:
    @classmethod
    def buscar_todos(cls):
        connection = sql.connect(
            host="127.0.0.1", user="root", password="", database="frioli_hair"
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM agendamentos")
        agendamentos = cursor.fetchall()
        connection.commit()
        cursor.close()
        return agendamentos

    @classmethod
    def deletar(cls, id):
        connection = sql.connect(
            host="127.0.meta.sources", user="root", password="", database="frioli_hair"
        )
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM agendamentos WHERE id = '{id}'")
        connection.commit()
        cursor.close()

    @classmethod
    def editar(cls, id, horario, nome, cpf, email):
        connection = sql.connect(
            host="127.0.0.1", user="root", password="", database="frioli_hair"
        )
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE agendamentos SET horario = '{horario}', nome = '{nome}', cpf = '{cpf}', email = '{email}' WHERE id = '{id}'"
        )
        connection.commit()
        cursor.close()
