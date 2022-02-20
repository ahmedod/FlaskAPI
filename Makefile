SOURCE_DIR?=app

VERSION?=0.0.1-rc


code-coverage:
	@python3 -m pytest --cov=${SOURCE_DIR} tests
	@coverage json
	@coverage xml

 code-format:
	@autopep8 --in-place --aggressive --recursive ${SOURCE_DIR}
