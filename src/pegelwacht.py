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
from helper.config import get_config, get_measuring_points


app = Flask(__name__)


@app.route('/')
def home():
    config = get_config(CONFIG_FILE_PATH)
    measuring_points = get_measuring_points(config)
    return render_template('home.html', title=config['ui_settings']['title'], measuring_points=measuring_points)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
