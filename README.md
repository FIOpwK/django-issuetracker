# django-issuetracker
Django(3.2.7) Issue Tracker project with testing 

&nbsp;
### `virtualenv` environment <a name="virtualenv"></a>

1. Clone the repo
```bash
git clone https://github.com/FIOpwK/django-issuetracker
```
2. `cd` into the new directory
```bash
cd django-issuetracker
```
3. Create a new virtual environment `env` in the directory
```bash
python -m virtualenv env
```
```bash
py.exe -m venv . 
```
4. Activate the new environment
```bash
source env/bin/activate
```
5. Install dependencies in new environment
```bash
pip install selenium webdriver django
```
6. Run the server locally
```bash
python manage.py runserver
```

# dependencies
- selenium webdriver
- geckodriver
- django

# testing
unit test:  `py.exe manage.py test issues`,
functional test: `py.exe manage.py test functional_tests`
