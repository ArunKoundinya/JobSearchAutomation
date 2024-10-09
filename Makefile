install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

systemdep:
	#sudo apt-get install chromium chromium-driver
	#brew install chromedriver chromium

test:
	#python -m pytest -vv test_main.py

format:
	black *.py Scrapping/*.py

lint:
	pylint --disable=R,C,W0702 main.py Scrapping/*.py

all: install lint format
