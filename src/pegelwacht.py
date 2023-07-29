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
from sqlalchemy import and_
from helper.config import get_config, get_measuring_points
from helper.database import get_database_uri
from filters.convert import unix_to_hr_time, separator_conversion
from helper.time import get_time_period


config = get_config(CONFIG_FILE_PATH)
database = SQLAlchemy()
app = Flask(__name__)
app.jinja_env.filters['unix_to_hr_time'] = unix_to_hr_time
app.jinja_env.filters['separator_conversion'] = separator_conversion
app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri(config)
database.init_app(app)


def get_level_data(mp):
    timestamps = list()
    levels = list()
    begin, end = get_time_period(float(config['ui_settings']['default_time_period']))
    result = database.session.execute(database.select(mp.database_class).order_by(mp.database_class.timestamp).where(and_(mp.database_class.timestamp > begin, mp.database_class.timestamp < end)))
    for data_point in result:
        timestamps.append(unix_to_hr_time(data_point[0].timestamp))
        levels.append(data_point[0].level)
    return timestamps, levels


@app.route('/')
def home():
    measuring_points = get_measuring_points(config)
    for mp in measuring_points:
        timestamps, levels = get_level_data(mp)
        mp.set_level_data(timestamps, levels)
    return render_template('home.html', title=config['ui_settings']['title'], measuring_points=measuring_points)


@app.route('/imprint')
def imprint():
    imprint_data = config['imprint']
    return render_template('imprint.html', title=config['ui_settings']['title'], imprint_data=imprint_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
