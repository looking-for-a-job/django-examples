all:
	find "$(CURDIR)" -name "tests.py" -print0 | xargs -0 -L 1 -I{} sh -c 'set "$$(dirname "$$0")"/Makefile; echo .EXPORT_ALL_VARIABLES: > "$$1"; echo DJANGO_SETTINGS_MODULE= >> "$$1"; echo "all:" >> "$$1"; echo "	@django-app-test ." >> "$$1";echo $$1' {}
