# Honours Project

Welcome to my 4th Year honours project. This application utilizes Folium to effectively visualise and plot UK road traffic accidents which occured during 2021, implemented through a fast and responsive Django web application.

The Folium maps were generated and exported into HTML components, and will be saved in a seperate dependency as jupytr notebooks, including the original and prepared data used to generate the map components.

How to correctly install this repo:

1. Clone main branch:

```
git clone https://github.com/jonyward/honours
```

2. Have most up to date version of pip installed

3. Navigate to the dependency named "honours"

3. Open a terminal at the root directory and use command:

```
py -m pip install Django
```

4. Also run the command:

```
pip install django-bootstrap-v5
```

5. Finally, run the command:

```
py manage.py runserver
```
If any errors occur try running the command:

```
py manage.py migrate
```
