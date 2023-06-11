'''
    PegelWacht
    Copyright (C) 2023 Peter Weidenbach

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import sys
import logging

from sqlalchemy import orm, engine, Column, Integer, Float
from sqlalchemy.exc import IntegrityError


class Base(orm.DeclarativeBase):
    pass


class MeasuringPoint_1(Base):
    __tablename__ = 'MeasuringPoint_1'
    timestamp = Column(Integer, primary_key=True)
    level = Column(Float)

    def __repr__(self) -> str:
        return '{} -> timestamp: {}; level: {}'.format(self.__tablename__, self.timestamp, self.level)


class MeasuringPoint_2():
    __tablename__ = 'MeasuringPoint_2'
    timestamp = Column(Integer, primary_key=True)
    level = Column(Float)

    def __repr__(self) -> str:
        return '{} -> timestamp: {}; level: {}'.format(self.__tablename__, self.timestamp, self.level)


class MeasuringPoint_3():
    __tablename__ = 'MeasuringPoint_3'
    timestamp = Column(Integer, primary_key=True)
    level = Column(Float)

    def __repr__(self) -> str:
        return '{} -> timestamp: {}; level: {}'.format(self.__tablename__, self.timestamp, self.level)


class MeasuringPoint_4():
    __tablename__ = 'MeasuringPoint_4'
    timestamp = Column(Integer, primary_key=True)
    level = Column(Float)

    def __repr__(self) -> str:
        return '{} -> timestamp: {}; level: {}'.format(self.__tablename__, self.timestamp, self.level)


class DbConnection:

    def __init__(self, provider, user=None, password=None, database=None, hostname=None, port=None):
        self.base = Base

        if provider == 'sqlite':
            self.engine = engine.create_engine('sqlite:///{}'.format(database))
            logging.debug('SqLite file: {}'.format(database))
        elif provider == 'mysql':
            self.engine = engine.create_engine('mysql://{}:{}@{}:{}/{}'.format(user, password, hostname, port, database))
        else:
            sys.exit('databse provider not supported: {}'.format(provider))

        self.Session = orm.sessionmaker(bind=self.engine)

    def create_tables(self):
        self.base.metadata.create_all(self.engine)

    def add_entry(self, dataset):
        session = self.Session()
        session.add(dataset)
        try:
            session.commit()
        except IntegrityError:
            logging.debug('{} already present'.format(dataset))

    def add_entries(self, datasets):
        for dataset in datasets:
            self.add_entry(dataset)
