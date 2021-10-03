### Django


Django_create_adminuser:
	cd budgetproject;.  env/bin/activate; python manage.py createsuperuser

Django_admin_delete_datas:
	python3 manage.py flush
	# Removes all data from the database and re-executes any post-synchronization handlers. The table of which migrations have been applied is not cleared.

Django_new_app:
	cd budgetproject;.  env/bin/activate; python manage.py startapp session_auth;

Django_migrate_with_name:
	cd budgetproject;.  env/bin/activate; python manage.py makemigrations sessions;

make_migrations_all:
	pwd;.  env/bin/activate;cd budgetproject; python manage.py makemigrations

migrate_all:
	pwd;.  env/bin/activate;cd budgetproject; python manage.py migrate;

MM:
	.  env/bin/activate;cd budgetproject ; python manage.py makemigrations; python manage.py migrate;

1RUN:
	.  env/bin/activate;cd budgetproject; python manage.py runserver;

fake_migration:
	cd budgetproject;.  env/bin/activate; python manage.py migrate --fake-initial

migrate:
	cd budgetproject;.  env/bin/activate; python manage.py makemigrations; python manage.py migrate

#__________________________

####Running Tests
Test_the_folder:
	.  env/bin/activate;cd budgetproject; python manage.py test

Test_the_budget:
	.  env/bin/activate;cd budgetproject; python manage.py test budget


