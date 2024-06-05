import os

from flask import Flask, request, render_template, g
from flask4fun.modules.pokeapi import PokeApi


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/healthz')
    def health_check():
        return 'Hello world'
    
    # Homepage
    @app.route('/home')
    def home():
        return render_template("base.html")
    
    # pokemon
    @app.route('/pokemon')
    def pokemon():
        api = PokeApi()
        params = request.args
        if params['limit'] is None:
            params['limit'] = 20
        if params['offset'] is None:
            params['offset'] = 0
        data = api.get_items(int(params['limit']), int(params['offset']))
        # for item in data['results']:
        #     item['sprite'] = item['url'].replace(api.baseUrl, 'https://pokeapi.co/api/v2/', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/')
        return render_template("pokemon/search.html", data=data)
    
    @app.errorhandler(404)
    def not_found(error):
        app.logger.error(error)
        return render_template('error.html',  error=error), error.code

    return app