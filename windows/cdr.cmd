@echo off
setlocal
for /f "delims=" %%a in ('git rev-parse --show-toplevel') do set git_root=%%a
if "%ERRORLEVEL%" neq "0" (
  goto ret
)
cd %git_root%
:ret
endlocal
