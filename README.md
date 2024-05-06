# Honours Project
[![Python Version](https://img.shields.io/badge/python-3.12.1-brightgreen.svg)](https://python.org)
[![PyPI - Django Version](https://img.shields.io/pypi/djversions/djangorestframework.svg)](https://djangoproject.com)
[![PyPI - Folium Version](https://img.shields.io/pypi/v/folium.svg)](https://pypi.org/project/folium/)


Welcome to my 4th Year Honours Project. This application utilizes Folium to effectively visualise and plot UK road traffic accidents which occured during 2021, implemented through a Django web application.

## Running the project:

1. Clone main branch:

```
git clone https://github.com/jonyward/honours
```

2. Have most up to date version of pip installed

3. Open a virtual environment and activate it, as to make sure the application is using the correct dependency versions used during development

4. Navigate to the dependency named "honours", Open a terminal and use the command:

```
pip install -r requirements.txt
```

5. Run the application using the command:

```
py manage.py runserver
```

6. If there are any problems, migrate the project using the following command and attempt to run the application again:

```
py manage.py migrate
```
