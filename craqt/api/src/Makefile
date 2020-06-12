

venv = /home/wildonion/Desktop/stomegranate/app/desktop/craqt/cranv
api = /home/wildonion/Desktop/stomegranate/app/desktop/craqt/api
pe = /home/wildonion/Desktop/stomegranate/app/desktop/novacrash/PE

.PHONY: compile clean

compile:
	source ${venv}/bin/activate;
	python setup.py build_ext --inplace

generate: clean
	mv *.so ${api}

clean: compile
	mv $(abspath build/temp.*/*.o) ${pe} 
	rm -rf build
	rm -f *.c
	rm -f *.cpp