# -*- coding: utf-8 -*-

import subprocess


class Judge(object):
    """Juiz.

    Responsável por compilar e julgar os problemas.
    """

    def __init__(self, config):
        self.config = config

    def set_time_limit(self, seconds):
        self.time_limit = seconds

    def set_memory_limit(self, memory):
        pass

    def run(self, user, problem, source):
        """Compila, executa o código e faz uma solicitação de análise da saída.
        """

        filename = self.save_source_file(user, problem, source)

        build_status, stdout, stderr = self.build(filename)
        if build_status != 0:
            return {
                'error': 'Compilation Error',
                'stdout': stdout,
                'stderr': stderr
            }

        run_status, stdout, stderr = self.execute()

        if run_status == 124:
            return {
                'error': 'Timeout Error',
                'stdout': stdout,
                'stderr': stderr
            }

        if run_status != 0:
            return {
                'error': 'Runtime Error',
                'stdout': stdout,
                'stderr': stderr
            }

        return self.check_code(user, problem, stdout)

    def save_source_file(self, user, problem, source):
        filename = self.config['filename'].format(user=user, problem=problem)

        with open(filename, 'w') as source_file:
            source_file.write(source)

        return filename

    def build(self, filename):
        build_command = self.config['build'].format(filename=filename)
        return self._run_process(build_command)

    def execute(self):
        run_command = self.config['run']
        return self._run_process(run_command)

    def check_code(self, user, problem, stdout):
        return {
            'success': 'OK'
        }

    def _run_process(self, command):
        if self.time_limit:
            command = 'timeout {0} {1}'.format(self.time_limit, command)

        p = subprocess.Popen(command,
                             stdout=subprocess.PIPE,
                             shell=True)

        (stdout, stderr) = p.communicate()
        return_code = p.wait()

        return return_code, stdout, stderr
