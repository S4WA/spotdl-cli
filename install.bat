@echo off
@echo Before you run this batch file, check this prerequisites: https://spotdl.readthedocs.io/en/latest/#prerequisites
TIMEOUT /T 15
@echo.
pip install -r requirements.txt
@echo.
spotdl --download-ffmpeg
@echo.
@echo Install completed.
@echo.
pause