# Honours Project

My 4th Year honours project which uses Folium to effectively visualise and plot UK road traffic accidents during 2021, implemented through a fast and responsive Django web application

The Folium maps were generated and exported into HTML components, and will be saved in a seperate dependency as jupytr notebooks, including the original and prepared data used to generate the map components

How to correctly install this repo:

1. Clone main branch
2. Open a terminal at the root directory and use command "py -m pip install Django"
3. Navigate to the dependency in the project called "crash_vis"
4. Run command "py manage.py runserver" and view the website on local port 8080

(If any errors occur, run command "py manage.py migrate" in the "crash_vis" dependency)