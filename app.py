from flask import Flask, request, redirect
import mysql.connector as sql
app = Flask(__name__)

connection = sql.connect(host="127.0.0.1", user="root", password="", database="logins")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["Nome"]
        password = request.form["Senha"]
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT * FROM usuarios WHERE nome = '{username}' AND senha = '{password}'"
        )
        user = cursor.fetchall()
        connection.commit()
        cursor.close()
        if user:
            return redirect("/home")
        else:
            return redirect("/login")

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        username = request.form["Nome"]
        cpf = request.form["CPF"]
        email = request.form["Email"]
        telefone = request.form["Telefone"]
        password = request.form["Senha"]
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO usuarios (nome, senha, cpf, email, telefone) VALUES ('{username}', '{password}', '{cpf}', '{email}', '{telefone}')"
        )
        connection.commit()
        cursor.close()

@app.route('/horarios', methods=['GET'])
def horarios():
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM horarios"
    )
    horarios = cursor.fetchall()
    connection.commit()
    cursor.close()
    return horarios



@app.route('/agendar', methods=['GET','POST'])
def agendar():
        if request.method == "POST":
            data = request.get_json()
            horario = data["Horario"]
            username = data["Nome"]
            cpf = data["CPF"]
            email = data["Email"]
            
            cursor = connection.cursor()
            cursor.execute(
                f"SELECT disponivel FROM horarios WHERE horario = '{horario}'"
            )
            disponivel = cursor.fetchone()
            if disponivel and disponivel[0] == 1:
                cursor.execute(
                    f"UPDATE horarios SET disponivel = '0' WHERE horario = '{horario}'" #DESATIVAR O SAFE MODE PARA FUNCIONAR (caso contrario será retornado status 500 e os horarios não vão mudar de disponivel para indisponivel)
                )
                cursor.execute(
                    f"INSERT INTO agendamentos (horario, nome, cpf, email) VALUES ('{horario}', '{username}', '{cpf}', '{email}')"
                )
                connection.commit()
                cursor.close()
                
                return "Agendamento realizado com sucesso!", 200
            else:
                return "Horario nao disponivel", 400

@app.route('/agenda', methods=['GET'])
def agenda():
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM agendamentos"
    )
    agendamentos = cursor.fetchall()
    connection.commit()
    cursor.close()
    return agendamentos

@app.route('/editaragenda', methods=['DELETE', 'PUT'])
def editaragenda():
    if request.method == "DELETE":
        data = request.get_json()
        id = data["Id"]
        horario = data["Horario"]
        cursor = connection.cursor()
        cursor.execute(
            f"DELETE FROM agendamentos WHERE id = '{id}'"
        )
        cursor.execute(
            f"UPDATE horarios SET disponivel = '1' WHERE horario = '{horario}'"
        )
        connection.commit()
        cursor.close()
        return "Agendamento deletado com sucesso!", 200
    elif request.method == "PUT":
        data = request.get_json()
        id = data["Id"]
        horario = data["Horario"]
        nome = data["Nome"]
        cpf = data["CPF"]
        email = data["Email"]
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE agendamentos SET horario = '{horario}', nome = '{nome}', cpf = '{cpf}', email = '{email}' WHERE id = '{id}'"
        )
        cursor.execute(
            f"UPDATE horarios SET disponivel = '0' WHERE horario = '{horario}'"
        )
        connection.commit()
        cursor.close()
        return "Agendamento editado com sucesso!", 200
    
if __name__ == '__main__':
    app.run()