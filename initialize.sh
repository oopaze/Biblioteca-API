pip3 install -r requirements.txt 
export SECRET_KEY="UmaChaveBemSecreta" 
export FLASK_ENV="development" 
flask db init 
flask db migrate 