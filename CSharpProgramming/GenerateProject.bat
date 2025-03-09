@echo off

SET PROJECT_NAME=%1
SET PYTHON_EXE=python.exe
SET PYTHON_SCRIPT_PATH=%~dp0\Script\GenerateProject.py
SET PYTHON_ARGS=--project_name=%PROJECT_NAME% --root_directory=%~dp0

%PYTHON_EXE% %PYTHON_SCRIPT_PATH% %PYTHON_ARGS%