@echo off

SET NAME=%1
SET PYTHON_EXE=python.exe
SET PYTHON_SCRIPT_PATH=%~dp0\Script\GenerateProject.py

%PYTHON_EXE% %PYTHON_SCRIPT_PATH%