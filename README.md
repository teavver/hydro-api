# Setup repository

1. `git clone https://github.com/teavver/hydro-api && cd hydro-api`
2. `python3 -m venv venv`
3. `. venv/bin/activate` (`. venv/Scripts/activate` on Windows)
4. Double check if the `activate` command successfully sourced the `venv` shell
5. `pip install -r requirements.txt`
6. `docker-compose up -d`

# Running tests

Test an app with: `docker-compose exec web python manage.py test <app>`. Replace `<app>` with the app's name, e.g: `users_api` to run the tests inside [users_api/tests.py](hydro/users_api/tests.py)
