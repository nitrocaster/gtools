@echo off
setlocal
set exclude_dir=".[^^\.]*",bin,binaries,libraries,lib,intermediate,ipch
set exclude="*.sdf","*.VC.db",".*"
grep --binary-files=text --color=auto -rs --exclude-dir={%exclude_dir%} --exclude={%exclude%} %* .
endlocal
