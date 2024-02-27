from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import psycopg2
import pandas as pd
import API.models.user as user

config = {
	"dialect":"postgresql",
	"driver":"psycopg2",
	"username":"isla",
	"password":"password",
	"host":"172.32.0.2",
	"port":"5432",
	"database":"postgres"
}

db_url = None
engine = None


def init():
	global engine
	# Informations de connexion à la base de données PostgreSQL
	db_url = "{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}".format(**config)

	# Création du moteur SQLAlchemy
	engine = create_engine(db_url)

	if ("token" in checkTableExists()["tablename"].to_list() and
		"users" in checkTableExists()["tablename"].to_list()):
		print("PostgreSQL tables already created !")
	else :
		create_table()


def query(query):
	with engine.begin() as conn:
		query = text(query)
		return pd.read_sql(query, conn)


def checkTableExists():
	return query("SELECT tablename FROM pg_catalog.pg_tables WHERE tablename NOT LIKE 'pg_%' AND tablename NOT LIKE 'sql_%'")


def create_table():
	print("Creating PostgreSQL tables...")
	with engine.begin() as conn:
		query = text("CREATE TABLE token (id varchar(36), user_id varchar(36), expire_date timestamp)")
		conn.execute(query)

		query = text("CREATE TABLE users (user_id varchar(36), first_name varchar(64), last_name varchar(64), password varchar(64), email varchar(64), username varchar(64), credit integer)")
		conn.execute(query)


def insert_user(user_data):
	Session = sessionmaker(bind=engine)
	session = Session()

	new_user = user.UserBase(**user_data)
	session.add(new_user)
	session.commit()

def add_token(user_id, nb_token):
	Session = sessionmaker(bind=engine)
	session = Session()
	session.query(user.UserBase).filter(user.UserBase.user_id == user_id).update({user.UserBase.credit: user.UserBase.credit + nb_token})
	session.commit()