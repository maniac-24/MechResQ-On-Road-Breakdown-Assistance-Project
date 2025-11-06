import ssl
from django.core.mail.backends.smtp import EmailBackend

class CustomEmailBackend(EmailBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If using SSL, set the SSL context to an unverified one
        if self.use_ssl:
            self.ssl_context = ssl._create_unverified_context()
        # If using TLS, ensure starttls also uses an unverified context
        elif self.use_tls:
            self.ssl_context = ssl._create_unverified_context()

    # The _create_connection method from the parent class will now use this ssl_context
    # when it calls smtplib.SMTP_SSL or smtplib.SMTP.starttls()
