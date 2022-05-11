run:
 	flask run
 setup: requirements.txt
 	pip install -r requirements.txt
 	set FLASK_APP=app.py
 	python app.py 
 clean:
 	rm -rf __pycache__
 	rm -rf venv
 	rm -rf .git 
