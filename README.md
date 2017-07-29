# HiSchool! Project

Requirements
---

Under an APT-based system, just run as `root`:

```
apt install python3 python3-pip virtualenv
```

Setup
---

- Clone this repository and move to the project directory
- Create a virtual environment: `virtualenv -p $(which python3) venv`
- Source the virtual environment: `source venv/bin/activate`
- Install the required packages: `pip install -r requirements.txt`

Your application now has its required dependencies, in order to create the
database, simply run `python manage.py migrate`. You can also create a new
super user with `python manage.py createsuperuser`.

Finally, run the server: `python manage.py runserver`

