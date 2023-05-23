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

from sqlalchemy import orm, engine, Column, Integer, Float


class Base(orm.DeclarativeBase):
    pass


class MeasuringDataSet(Base):
    timestamp = Column(Integer, primary_key=True)
    level = Column(Float)

    def __repr__(self) -> str:
        return 'timestamp: {}; level: {}'.format(self.timestamp, self.level)


class MeasuringPoint_1(MeasuringDataSet):
    __table_name__ = 'MeasuringPoint_1'


class MeasuringPoint_2(MeasuringDataSet):
    __talbe_name__ = 'MeasuringPoint_2'


class DbConnection:

    def __init__(self, provider, user=None, password=None, database=None, hostname=None, port=None):
        self.base = Base

        if provider == 'sqlite':
            self.engine = engine.create_engine('sqlite://{}'.format(database))
        elif provider == 'mysql':
            self.engine = engine.create_engine('mysql://{}:{}@{}:{}/{}'.format(user, password, hostname, port, database))
        else:
            sys.exit('databse provider not supported: {}'.format(provider))

        self.session_maker = orm.sessionmaker(bind=self.engine)

    def create_tables(self):
        self.base.metadata.create_all(self.engine)

    def add_entry_mp1(self, timestamp, level):
        pass
