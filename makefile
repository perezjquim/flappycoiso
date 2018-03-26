FILES-TO-CLEAN = $(shell find . -name "*.pyc")

main: exec
exec:
	@rm -f $(FILES-TO-CLEAN)
	@echo 'Executing..'
	@python main.py
