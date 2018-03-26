FILES-TO-CLEAN = $(shell find . -name "*.pyc")

main: clean exec

clean:
	@rm -f $(FILES-TO-CLEAN)	

exec:
	@echo 'Executing..'
	@python main.py
