# -*- coding: utf-8 -*-


class Config(object):
    """Configuração para para todos os ambientes.
    """

    JUDGE = {
        'c++': {
            'filename': '/tmp/{problem}-{user}.cpp',
            'build': 'g++ -O2 -fno-asm -fomit-frame-pointer -lm --static'
                     ' --std=c++11 {filename} -o /tmp/runme',
            'run': '/tmp/runme'
        },
        'c': {
            'filename': '/tmp/{problem}-{user}.c',
            'build': 'gcc -O2 -fno-asm -fomit-frame-pointer -lm --static'
                     ' --std=c99 {filename} -o /tmp/runme',
            'run': '/tmp/runme'
        },
        'python': {
            'filename': '/tmp/{problem}-{user}.py',
            'build': 'mv {filename} /tmp/runme',
            'run': 'python2 /tmp/runme'
        }
    }


class DevelopmentConfig(Config):
    """Configuração do ambiente de desenvolvimento.
    """

    DEBUG = True


class ProductionConfig(Config):
    """Configuração do ambiente de produção.
    """

    DEBUG = False
