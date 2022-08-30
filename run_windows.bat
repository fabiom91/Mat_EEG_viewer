set "VIRTUAL_ENV=mat_visualizer_env"

:read_mat
%VIRTUAL_ENV%\Scripts\activate.bat
pip install -r app_files\requirements.txt
python -c "import sys; sys.path.insert(1,'app_files'); from main import visualize_mat_eeg; visualize_mat_eeg('%1')"
pause
EXIT /B 0

IF EXIST "%VIRTUAL_ENV%\Scripts\activate.bat" (
    CALL :read_mat
) ELSE (
    pip install virtualenv
    python -m venv mat_visualizer_env
    CALL :read_mat
)