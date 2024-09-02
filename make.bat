@ECHO OFF

REM Command file for Sphinx documentation

setlocal

pushd %~dp0

if "%PYTHON%" == "" (
	set PYTHON=py -3
)

set BUILDDIR=_build
set SPHINXOPTS=--fail-on-warning --keep-going
set _ALL_SPHINX_OPTS=%SPHINXOPTS%

if "%1" == "check" goto check

if "%1" == "" goto help
if "%1" == "help" (
	:help
	echo.Please use `make ^<target^>` where ^<target^> is one of
	echo.  html       to make standalone HTML files
	echo.  htmlview   to open the index page built by the html target in your browser
	echo.  dirhtml    to make HTML files named index.html in directories
	echo.  singlehtml to make a single large HTML file
	echo.  pickle     to make pickle files
	echo.  json       to make JSON files
	echo.  htmlhelp   to make HTML files and a HTML help project
	echo.  qthelp     to make HTML files and a qthelp project
	echo.  devhelp    to make HTML files and a Devhelp project
	echo.  epub       to make an epub
	echo.  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter
	echo.  text       to make text files
	echo.  man        to make manual pages
	echo.  changes    to make an overview over all changed/added/deprecated items
	echo.  linkcheck  to check all external links for integrity
	echo.  doctest    to run all doctests embedded in the documentation if enabled
	echo.  check      to check for stylistic and formal issues using sphinx-lint
	goto end
)

if "%1" == "clean" (
	for /d %%i in (%BUILDDIR%\*) do rmdir /q /s %%i
	del /q /s %BUILDDIR%\*
	goto end
)

if "%1" == "versions" (
	%PYTHON% _tools/generate_release_cycle.py
	if errorlevel 1 exit /b 1
	echo.
	echo Release cycle data generated.
	goto end
)

rem Targets other than "clean", "check", "help", or "" need the
rem Sphinx build command, which the user may define via SPHINXBUILD.

if not defined SPHINXBUILD (
	rem If it is not defined, we build in a virtual environment
	if not exist venv (
		echo.    Setting up the virtual environment
		%PYTHON% -m venv venv
		echo.    Installing requirements
		venv\Scripts\python -m pip install -r requirements.txt
	)
	set PYTHON=venv\Scripts\python
	set SPHINXBUILD=venv\Scripts\sphinx-build
	set SPHINXAUTOBUILD=venv\Scripts\sphinx-autobuild
)

if "%1" == "htmlview" (
	cmd /C %this% html

	if EXIST "%BUILDDIR%\html\index.html" (
		echo.Opening "%BUILDDIR%\html\index.html" in the default web browser...
		start "" "%BUILDDIR%\html\index.html"
	)

	goto end
)

if "%1" == "htmllive" (
    %SPHINXAUTOBUILD% --re-ignore="/\.idea/|/venv/" --open-browser --delay 0 --port 55301 . %BUILDDIR%/html
    if errorlevel 1 exit /b 1
    goto end
)

%SPHINXBUILD% -M %1 "." %BUILDDIR% %_ALL_SPHINX_OPTS%
goto end

:check
if not defined SPHINXLINT (
	rem If it is not defined, we build in a virtual environment
	if not exist venv (
		echo.    Setting up the virtual environment
		%PYTHON% -m venv venv
		echo.    Installing requirements
		venv\Scripts\python -m pip install -r requirements.txt
	)
	set PYTHON=venv\Scripts\python
	set SPHINXLINT=%PYTHON% -m sphinxlint
)

rem Ignore the tools and venv dirs and check that the default role is not used.
cmd /S /C "%SPHINXLINT% -i tools -i venv --enable default-role"
goto end

:end
popd
endlocal
