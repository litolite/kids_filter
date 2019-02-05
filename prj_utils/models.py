import argparse
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from prj_utils.db_session import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer(), primary_key=True)
    username = sa.Column(sa.String(100), nullable=False)
    password = sa.Column(sa.String(250), nullable=False)
    first_name = sa.Column(sa.String(100), nullable=True)
    is_admin = sa.Column(sa.Boolean(), default=True)
    processes = relationship("Process")

    def __repr__(self):
        return f"{self.username} ({self.first_name})"


class Process(Base):
    __tablename__ = 'process'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(100))
    username = sa.Column(sa.String(100))
    is_allowed = sa.Column(sa.Boolean, default=True)
    owner = sa.Column(sa.Integer, sa.ForeignKey('users.id'))

    def __repr__(self):
        return f"{self.username} : {self.name}"


class Timer(Base):
    __tablename__ = 'timers'

    id = sa.Column(sa.Integer(), primary_key=True)
    start_time = sa.Column(sa.Time(), nullable=False)
    end_time = sa.Column(sa.Time(), nullable=False)
    day = relationship("DayOfWeek")


class DayOfWeek(Base):
    __tablename__ = 'week_day'

    id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.String(15))
    time = sa.Column(sa.Integer, sa.ForeignKey('timers.id'))


class FirstRun(Base):
    __tablename__ = 'first_run'
    key = sa.Column(sa.String(length=15), primary_key=True)
    value = sa.Column(sa.Boolean, default=True)

    def __repr__(self):
        return f"{self.key} : {self.value}"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--add_table", help="Table name needed")
    args = parser.parse_args()
    if args.add_table:
        Base.metadata.tables[args.add_table].create(bind=engine)
    else:
        Base.metadata.create_all(engine)
