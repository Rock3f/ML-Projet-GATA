REM --------------------------------
REM ---------- Img Resize ----------
REM --------------------------------

REM --------------------------------
REM ----- Extensions supported -----
REM ------------ .jpg --------------
REM ------ Not Yet supported -------
REM ----- .png, .jpeg, other ? -----

REM GATA Project specific resize !

REM Absolute path to image folder

REM Max height
set WIDTH=300

REM Max width
set HEIGHT=400

@echo off
set "FOLDER=c:\images"
set "result_folder_1=c:\images\resized"

for %%a in ("%FOLDER%\*jpg") do (
   call scale.bat -source "%%~fa" -target "%result_folder_1%\%%~nxa" -max-height HEIGHT -max-width WIDTH -keep-ratio no -force yes
)