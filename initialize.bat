pip3 install -r requirements.txt
set SECRET_KEY="UmaChaveBemSecreta"
set FLASK_ENV="development"
flask db init
flask db migrate
flask db upgrade