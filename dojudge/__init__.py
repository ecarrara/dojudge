# -*- coding: utf-8 -*


from flask import Flask, request, current_app, jsonify
from dojudge.config import ProductionConfig
from dojudge.judge import Judge


def create_app(config=None):

    app = Flask(__name__)

    if config is None:
        config = ProductionConfig()

    app.config.from_object(config)
    app.config.from_envvar('DOJudge_CONFIG', silent=True)

    @app.route('/', methods=['POST'])
    def service():
        """View responsável por receber as requisições e encaminhar para o
        juiz.

        Devem ser informados nos cabeçalhos HTTP:

          :X-Judge-USER: Identificador do usuário que enviou o solicitação.
          :X-Judge-LANG: Linguagem de programação usada no código.
          :X-Judge-PROBLEM: Identificador do problema.
          :X-Judge-TIMELIMIT: limite do tempo de execuçao (opcional).
          :X-Judge-MEMORYLIMIT: limite de memória da execução (opcional).

        O corpo da requisição deve conter um código fonte.
        """

        source_code = request.get_data()

        user = request.headers.get('X-Judge-User', 'nobody')
        lang = request.headers.get('X-Judge-Lang', 'c++')
        problem = request.headers.get('X-Judge-Problem', None)
        time_limit = request.headers.get('X-Judge-TimeLimit', None)
        memory_limit = request.headers.get('X-Judge-MemoryLimit', None)

        judge = Judge(current_app.config['JUDGE'][lang])
        judge.set_time_limit(time_limit)
        judge.set_memory_limit(memory_limit)

        result = judge.run(user, problem, source_code)

        if 'success' in result:
            return jsonify(result), 202

        return jsonify(result), 400

    return app
