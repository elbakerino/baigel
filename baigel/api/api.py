from apiflask import APIFlask

from baigel._boot import Services
from baigel.api.api_models import api_models
from baigel.api.api_sentences import api_sentences
from baigel.api.api_tasks import api_tasks


def ai_api(app: APIFlask, s: Services):
    api_models(app, s)
    api_tasks(app, s)
    api_sentences(app, s)
