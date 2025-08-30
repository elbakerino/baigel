import signal
import sys
import logging
from pathlib import Path

from apiflask import APIFlask, Schema, fields
from apispec.ext.marshmallow.field_converter import _VALID_PROPERTIES

from baigel._boot import boot
from baigel.api.api import ai_api
from baigel.config.config import AppConfig

from baigel.helper import ts
from flask import render_template, url_for
from flask_cors import CORS

# todo: https://stackoverflow.com/a/16993115/2073149
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
pil_logger = logging.getLogger('PIL')
pil_logger.setLevel(logging.INFO)

_VALID_PROPERTIES.add('widget')

s = boot()

app = APIFlask(
    __name__,
    title='baigel',
    version='0.0.1',
    docs_ui=AppConfig.API_DOCS_UI,
)
app.config['OPENAPI_VERSION'] = '3.1.0'

CORS(
    app,
    origins=AppConfig.CORS_ORIGINS,
    send_wildcard=AppConfig.CORS_SEND_WILDCARD,
)

original_sigint_handler = signal.getsignal(signal.SIGINT)


def on_signal(signal_number, frame):
    # needed for flask, calls the org. signal handler but still does not gracefully wait
    if original_sigint_handler:
        original_sigint_handler(signal_number, frame)


# signal.signal(signal.SIGKILL, on_signal)
signal.signal(signal.SIGTERM, on_signal)
signal.signal(signal.SIGINT, on_signal)

CSS_CONTENT = (Path(app.root_path) / "templates" / "main-dark.css").read_text(encoding="utf-8")


@app.route('/')
def route_home():
    links = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint == 'static':
            continue
        url = url_for(rule.endpoint, **(rule.defaults or {}))
        methods = rule.methods.copy()
        if 'HEAD' in methods:
            methods.remove('HEAD')
        if 'OPTIONS' in methods:
            methods.remove('OPTIONS')
        links.append((url, list(methods), rule.endpoint, rule.arguments, rule.defaults))

    return render_template(
        'index.html',
        version=AppConfig.APP_ENV,
        links=links,
        css=CSS_CONTENT
    )


class PingResponse(Schema):
    now = fields.String()


@app.route('/ping')
@app.output(PingResponse)
def route_ping():
    return {
        "now": ts.now_iso(micros=False),
    }


ai_api(app, s)
