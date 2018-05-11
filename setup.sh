#!/bin/bash

# switch to virtual env
# $VENV='virtualenv ENV'
# $INIT='source ENV/bin/activate'

# install dependencies
PIP='which pip'
DEP='install requirements.txt'

$PIP $DEP