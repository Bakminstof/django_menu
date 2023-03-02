function set_variables() {
  export "$(grep -v '^#' .env | xargs)"

}

function start() {
  set_variables

  docker-compose -f docker-compose.yaml up --build --remove-orphans -d

  docker exec django_mysite_menu python manage.py flush --no-input
  docker exec django_mysite_menu python manage.py migrate --noinput
  docker exec django_mysite_menu python manage.py loaddata db.json
  docker exec django_mysite_menu python manage.py collectstatic --no-input --clear

  docker exec -ti django_mysite_menu python manage.py createsuperuser

}

start
