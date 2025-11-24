VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
STREAMLIT=$(VENV)/bin/streamlit

install: 
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run:
	$(STREAMLIT) run app.py