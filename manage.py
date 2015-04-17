#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager
from dojudge import create_app
from dojudge.config import DevelopmentConfig


app = create_app(DevelopmentConfig())
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
