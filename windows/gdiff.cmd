@echo off
if "%1" equ "-h" (
  echo gdiff: compare modified git files with difftool
  goto ret
)
if "%1" equ "-c" (
  git difftool -y --cached %2
) else (
  git difftool -y %1
)
echo.
:ret
