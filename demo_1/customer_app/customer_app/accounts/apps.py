from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer_app.accounts'

    def ready(self):
        import customer_app.accounts.signals
