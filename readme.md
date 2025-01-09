pip install -r requirements.txt
set FLASK_APP=run.py
#database codes database is in instance folder
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
flask run 