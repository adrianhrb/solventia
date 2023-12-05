runserver:
    python manage.py runserver
    
shell:
    python manage.py shell

migrate:
    python manage.py migrate


startapp app:
    python manage.py startapp {{ app }}

makemigrations app:
    python manage.py makemigrations {{ app }}

super:
    python manage.py createsuperuser

debug:
    python manage.py debugsqlshell
