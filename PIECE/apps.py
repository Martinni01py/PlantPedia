from django.apps import AppConfig


class PieceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PIECE'
    
    def ready(self):
        import PIECE.signals  # Importe o arquivo signals.py