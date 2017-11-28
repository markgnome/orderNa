create virtual environment
    'python3 -m venv virtualEnv/foodtasker'

activate virtual environment  
    'source virtualEnv/foodtasker/bin/activate'

install Pillow
    'python3 -m pip install Pillow'

check versions
    'python3 -m pip freeze'


run server
    'python3 manage.py runserver'

create django project
    'django-admin startproject foodtasker'

make migrations command (model)
    'python3 manage.py makemigrations'

apply all migrations
    'python3 manage.py migrate'
    Apply all migrations: admin, auth, contenttypes, foodtaskerapp, sessions

