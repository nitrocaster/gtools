@echo off
if "%1" equ "-h" (
  goto print_usage
)
if "%1" equ "-c" (
  git difftool -y --cached %2
  goto ret
)
if "%1" equ "-p" (
  if "%2" neq "" (
    git difftool -y %2~1 %2
    goto ret
  )
  goto print_usage
)
git difftool -y %1
echo.
goto ret

:print_usage
echo gdiff: compare modified git files with difftool
echo     -h        : show this message
echo     -c [file] : diff cached (staged) changes
echo     -p ^<sha^>  : diff exact commit
:ret
