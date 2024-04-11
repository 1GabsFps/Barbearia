from flask import Flask, jsonify, request
from Model import Usuario, Horario, Agendamento
from dao import UsuarioDAO, HorarioDAO, AgendamentoDAO

app = Flask(__name__)


@app.route("/cadastrar", methods=["POST"])
def cadastrar_usuario():
    data = request.get_json()
    usuario = Usuario(
        data["nome"], data["senha"], data["cpf"], data["email"], data["telefone"]
    )
    UsuarioDAO.cadastrar(
        usuario.nome, usuario.senha, usuario.cpf, usuario.email, usuario.telefone
    )
    return jsonify(usuario.__dict__), 201


@app.route("/login", methods=["POST"])
def autenticar_usuario():
    data = request.get_json()
    usuario = UsuarioDAO.autenticar(data["nome"], data["senha"])
    return (
        ("Login efetuado com sucesso", 200)
        if usuario
        else ("Usuário não encontrado", 404)
    )


@app.route("/horarios", methods=["POST"])
def criar_horario():
    data = request.get_json()
    horario = Horario(data["horario"], data["disponivel"])
    HorarioDAO.salvar(horario.horario, horario.disponivel)
    return jsonify(horario.__dict__), 201


@app.route("/horarios", methods=["GET"])
def buscar_horario():
    horario = HorarioDAO.buscar_todos()
    return jsonify(horario) if horario else ("Nenhum horario encontrado", 404)


@app.route("/agendamentos", methods=["POST"])
def criar_agendamento():
    data = request.get_json()
    agendamento = Agendamento(data["horario"], data["nome"], data["cpf"], data["email"])
    AgendamentoDAO.salvar(
        agendamento.horario, agendamento.nome, agendamento.cpf, agendamento.email
    )
    return jsonify(agendamento.__dict__), 20


@app.route("/agendamentos", methods=["GET"])
def buscar_agendamento():
    agendamento = AgendamentoDAO.buscar_todos()
    return (
        jsonify(agendamento.__dict__)
        if agendamento
        else ("Nenhum agendamento encontrado", 404)
    )


@app.route("/agendamentos/<int:id>", methods=["DELETE"])
def deletar_agendamento(id):
    AgendamentoDAO.deletar(id)
    return "Agendamento deletado com sucesso", 200


@app.route("/agendamentos/<int:id>", methods=["PUT"])
def editar_agendamento(id):
    data = request.get_json()
    agendamento = Agendamento(data["horario"], data["nome"], data["cpf"], data["email"])
    AgendamentoDAO.editar(
        id, agendamento.horario, agendamento.nome, agendamento.cpf, agendamento.email
    )
    return jsonify(agendamento.__dict__), 200


if __name__ == "__main__":
    app.run()
