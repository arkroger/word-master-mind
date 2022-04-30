import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from psycogreen.gevent import patch_psycopg
patch_psycopg()  

engine = create_engine(os.environ.get('DB_CONNECTION_STRING'), pool_size=5)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()