import os


class AppConfig:
    APP_ENV = os.getenv('APP_ENV')
    SERVICE_NAME = os.getenv('SERVICE_NAME', "unnamed-service")
    SERVICE_NAMESPACE = os.getenv('SERVICE_NAMESPACE', "unknown")

    API_DOCS_UI = os.getenv('API_DOCS_UI', 'swagger-ui')
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')
    CORS_SEND_WILDCARD = os.getenv('CORS_SEND_WILDCARD') in ['true', 'True', '1', 'yes']

    MODEL_DIR = os.getenv('MODEL_DIR', '/app/model-assets')
    SHARED_DIR = os.getenv('SHARED_DIR', '/app/shared-assets')
    MODELS = {key[len('MODEL__'):]: os.environ[key] for key in os.environ.keys() if key.startswith('MODEL__')}
