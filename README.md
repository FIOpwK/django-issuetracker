# django-issuetracker
Django(3.2.8) Issue Tracker project with testing

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
3. Create a new virtual environment `virtualenv` in the directory
```bash
python -m venv virtualenv
```
```bash
py.exe -m venv . 
```
4. Activate the new environment
```bash
source env/bin/activate
```

```bash
.\virtualenv\Scripts\activate

```
5. Install dependencies in new environment
```bash
pip install selenium webdriver django psycopg2
```
6. Run the server locally
```bash
python manage.py runserver
```

# dependencies
- selenium webdriver (4.0.0)
- geckodriver
- django (3.2.8)
- postgresql (PostgresSQL 14)
- psycopg2 (2..9.1)

# testing
unit test:  `py.exe manage.py test issues`,
functional test: `py.exe manage.py test functional_tests`
