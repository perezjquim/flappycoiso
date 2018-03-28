main: clean update repackage

clean:
	@rm -rf flappycoiso-deb/opt/flappycoiso/*

update:
	@cd flappycoiso > /dev/null && make clean > /dev/null && cd - > /dev/null
	@echo "@Updating files...@"
	@cp -R flappycoiso/* flappycoiso-deb/opt/flappycoiso/
	@echo "@Files updated!@"

repackage:
	@echo "@Repackaging...@"
	@dpkg-deb --build flappycoiso-deb flappycoiso.deb > /dev/null
	@echo "@Repackaged!@"
