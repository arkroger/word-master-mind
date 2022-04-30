#Create an environment
python3 -m venv venv

#Activate the environment

#Activate the environment
pip install Flask

export FLASK_ENV=development
export FLASK_APP=wordmastermind


#console
clear && python -c 'from app import console; console()'

#gunicorn
gunicorn -w 4 wordmastermind:app


#generate requirements.txt
pip3 freeze > requirements.txt

docker run --network host -e WORKERS=2 -e THREADS=10 -e DB_CONNECTION_STRING=postgresql://postgres:123123@localhost/postgres --cpus="1" -m=1024mi teste-python:latest

docker build -t teste-python:gevent -f Dockerfilegevent .


#Database
create table word (
	word varchar primary key
);
create table daily_word (
	date date primary key,
	word varchar not null,
	foreign key (word) references word(word)
)
