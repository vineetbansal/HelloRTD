call activate base
cd docs
sphinx-apidoc -f -M -o . ../mypackage
sphinx-build -b html . _build
pause