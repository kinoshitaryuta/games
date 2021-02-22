from django.db import models
from accounts.models import User



CHOICES =(
    ("10","アプリの不具合"),
    ("20","スパムと迷惑行為について"),
    ("30","要注意コンテンツ"),
    ("40","サービスの改善について"),
    ("50","その他"),
)


class Contact(models.Model):
    username=models.CharField(max_length=30, null=True, blank=True)
    contact_us=models.CharField(max_length=20,choices=CHOICES)
    email=models.EmailField(max_length=100,null=False, blank=True)
    message=models.TextField(max_length=1000,null=False, blank=True)

    def __str__(self):
        return self.message
