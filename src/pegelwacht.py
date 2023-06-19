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
from CONFIG import CONFIG_FILE_PATH
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from helper.config import get_config, get_measuring_points
from helper.database import get_database_uri
from filters.convert import unix_to_hr_time


config = get_config(CONFIG_FILE_PATH)
database = SQLAlchemy()
app = Flask(__name__)
app.jinja_env.filters['unix_to_hr_time'] = unix_to_hr_time
app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri(config)
database.init_app(app)


def get_level_data(mp):
    timestamps = list()
    levels = list()
    result = database.session.execute(database.select(mp.database_class).order_by(mp.database_class.timestamp))
    for data_point in result:
        timestamps.append(data_point[0].timestamp)
        levels.append(data_point[0].level)
    return timestamps, levels


@app.route('/')
def home():
    measuring_points = get_measuring_points(config)
    for mp in measuring_points:
        timestamps, levels = get_level_data(mp)
        mp.set_level_data(timestamps, levels)
    return render_template('home.html', title=config['ui_settings']['title'], measuring_points=measuring_points)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
