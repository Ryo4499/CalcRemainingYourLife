SRC_DIR = src/

default: cryl

cryl: setup.py
	python3 setup.py build_ext --inplace && rm -fr build

clean:
	rm *.so && rm $(SRC_DIR)*.c
