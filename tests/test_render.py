import flask

from flask.ext.simplemde import SimpleMDE

TEMPLATE = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Flask-SimpleMDE example</title>
    {{ simplemde.css }}
    {{ simplemde.js }}
  </head>
  <body>
    {{ simplemde.load }}
    {{ simplemde.load_id("editor") }}
  </body>
</html>
"""

STATIC_CSS = '/static/simplemde/simplemde.min.css'
STATIC_JS = '/static/simplemde/simplemde.min.js'


def create_client(use_cdn=None):
    app = flask.Flask(__name__)

    app.config['TESTING'] = True
    if use_cdn is not None:
        app.config['SIMPLEMDE_USE_CDN'] = use_cdn

    SimpleMDE(app)

    @app.route('/')
    def index():
        return flask.render_template_string(TEMPLATE)

    return app.test_client()


def test_serve_static_simplemde_css_file():
    client = create_client()
    response = client.get(STATIC_CSS)
    assert response.status_code == 200


def test_serve_static_simplemde_js_file():
    client = create_client()
    response = client.get(STATIC_JS)
    assert response.status_code == 200


def test_use_cdn_by_default():
    client = create_client()
    html = client.get('/').data.decode()
    assert STATIC_CSS not in html
    assert STATIC_JS not in html


def test_use_cdn_turn_off():
    client = create_client(use_cdn=False)
    html = client.get('/').data.decode()
    assert STATIC_CSS in html
    assert STATIC_JS in html
