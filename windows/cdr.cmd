@echo off
for /f "delims=" %%a in ('git rev-parse --show-toplevel') do (
  if "%ERRORLEVEL%" neq "0" (
    goto ret
  )
  cd %%a
)
:ret
