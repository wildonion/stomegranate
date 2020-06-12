clean:
	rm -rf cranv

.PHONY: run

venv:
	test -d cranv || virtualenv -p $(shell which python3) cranv --system-site-packages
	cranv/bin/pip install -r requirements.txt;

run: venv
	source cranv/bin/activate;
	python app.py & python api/server/__init__.py