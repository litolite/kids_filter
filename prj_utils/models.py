import argparse
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from db_session import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer(), primary_key=True)
    username = sa.Column(sa.String(100))
    password = sa.Column(sa.String(100))
    first_name = sa.Column(sa.String(100), nullable=True)
    last_name = sa.Column(sa.String(100), nullable=True)
    is_admin = sa.Column(sa.Boolean(), default=True)

    def __repr__(self):
        return f"{self.username} ({self.first_name}, {self.last_name})"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--add_table", help="Table name needed")
    args = parser.parse_args()
    if args.add_table:
        Base.metadata.tables[args.add_table].create(bind=engine)
    else:
        Base.metadata.create_all(engine)
