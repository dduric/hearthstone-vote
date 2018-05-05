from django.apps import AppConfig

class AppConfigWithSignals(AppConfig):
    name ='data'
    def ready(self):
        from data import signals

default_app_config='data.AppConfigWithSignals'
