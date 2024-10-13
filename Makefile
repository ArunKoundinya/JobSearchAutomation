install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

systemdep:
	
	## Uncomment below for Ubuntu Environment
	#sudo apt-get update
	#sudo apt-get install chromium-browser
	#sudo apt-get install chromium-chromedriver
	
	## Uncomment below for Mac Environment
	#brew install chromedriver chromium

test:
	#Yet to create test cases
	#python -m pytest -vv test_main.py

format:
	black *.py Scraping/*.py WebApp/*.py

lint:
	pylint --disable=R,C,W070,W1510,W0702 main.py Scraping/*.py WebApp/*.py

all: systemdep install lint format test
