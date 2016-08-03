clean:
	rm -rf build/

html:
	sphinx-build -b html source build
	@echo
	@echo "Build finished. Website saved to `build/` directory."


slides:
	sphinx-build -b slides source slides
