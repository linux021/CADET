#!/bin/bash

#export FLASK_APP="cadetapi:create_app()"
export FLASK_APP="cadetapi/__init__.py"
export FLASK_DEBUG=1
python3 -m flask run
