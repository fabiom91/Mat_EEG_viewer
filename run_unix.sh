#!/bin/bash

VIRTUAL_ENV="mat_visualizer_env"

read_mat () {
    source mat_visualizer_env/bin/activate
    pip install -r app_files/requirements.txt
    python3 -c "import sys; sys.path.insert(1,'app_files'); from main import visualize_mat_eeg; visualize_mat_eeg($1)"
}

if [[ -f "$VIRTUAL_ENV/bin/activate" ]]; then
    read_mat
else
    pip install virtualenv
    python3 -m venv mat_visualizer_env
    read_mat
fi

