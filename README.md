# Google DevFest

## Executing the scripts

### Mining the data

For generating the `csv` file -
```
python scrape.py
```
**output_file.csv** will be generated.

For extracting specific columns from the `csv` file -
```
python read-csv.py
```

### Functional tests
```
python3 manage.py test functional_tests
```

### Unit tests
```
python3 manage.py test lists
```

## Directory Structure
```
├── data_mining
│   ├── output_file.csv
│   ├── read-csv.py
│   └── scrape.py
├── functional_tests.py
├── README.md
└── superlists
    ├── db.sqlite3
    ├── lists
    │   ├── admin.py
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_item_text.py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       ├── 0001_initial.cpython-34.pyc
    │   │       ├── 0002_item_text.cpython-34.pyc
    │   │       └── __init__.cpython-34.pyc
    │   ├── models.py
    │   ├── models.pyc
    │   ├── __pycache__
    │   │   ├── admin.cpython-34.pyc
    │   │   ├── __init__.cpython-34.pyc
    │   │   ├── models.cpython-34.pyc
    │   │   ├── tests.cpython-34.pyc
    │   │   └── views.cpython-34.pyc
    │   ├── templates
    │   │   └── home.html
    │   ├── tests.py
    │   ├── views.py
    │   └── views.pyc
    ├── manage.py
    └── superlists
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-34.pyc
        │   ├── settings.cpython-34.pyc
        │   ├── urls.cpython-34.pyc
        │   └── wsgi.cpython-34.pyc
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```
