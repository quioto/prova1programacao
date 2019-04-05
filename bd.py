# Função validar login
def get_idlogin(cursor, login, senha):
    # Executar o sql
    cursor.execute(f'select idlogin from login where login = "{login}" and senha = "{senha}"')

    # Recuperando o retorno do BD
    idlogin = cursor.fetchone()

    # Fechar o cursor
    cursor.close()

    # Retornar o idlogin
    return idlogin

# Funcao para retornar as disciplinas
def get_notas(cursor, idlogin):
    # Executar o SQL
    cursor.execute(f'select disciplinas.nome, notas.nota1, notas.nota2, notas.nota3, notas.iddisciplinas FROM notas inner join disciplinas on notas.iddisciplinas = disciplinas.iddisciplinas where idlogin = "{idlogin}"')

    # Recuperando o retorno do BD
    disciplinas = cursor.fetchall()

    print(disciplinas)

    # Fechar o cursor
    cursor.close()

    # Retornar os dados
    return disciplinas

def get_detalhes(cursor, disciplina):
    cursor.execute(f'select nome, descricao from disciplinas where iddisciplinas = "{disciplina}"')

    detalhe = cursor.fetchone()
    cursor.close()
    return detalhe

