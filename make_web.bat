@ECHO off

call make clean
call make html

echo %~dp0
set html="%~dp0_build\html"
for %%f in (%html%\*.html) do (
    python "%~dp0code_tools\swap_html.py" "%%f" -c "%~dp0html_config.json" -m perform

)
