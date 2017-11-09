from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'images'
    verboste_name = 'Image bookmarks'

    def ready(self):
        import images.signals
