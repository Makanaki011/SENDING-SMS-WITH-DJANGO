from django.db import models
from twilio.rest import Client

# Create your models here.

class Score(models.Model):
    result = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        if self.result < 70:

            account_sid = 'ACe56284d4c60784dd71cbe47865c37f0a'
            auth_token = 'afc9f3c43ec1e4056cf973eed5a7d80d'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f'The current result is bad - {self.result}',
                from_='+16292764823',
                to='+2348061461955',
                )


            print(message.sid)



        return super().save(*args, **kwargs)
