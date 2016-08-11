clean:
	rm -rf build/

html:
	sphinx-build -b html source build/html
	@echo
	@echo "Build finished. Website saved to 'build/html' directory."

slides:
	sphinx-build -b slides source build/slides
	@echo "Build finished. Website saved to 'build/slides' directory."
