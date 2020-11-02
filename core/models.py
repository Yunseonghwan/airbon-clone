from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(
        auto_now_add=True
    )  # auto_now_add=True현재 시간을 자동으로 넣어주는 기능
    updated = models.DateTimeField(auto_now=True)  # auto_now=True 저장할때마다 시간을 넣어줌

    class Meta:
        abstract = True  # abstract model 은 데이터베이스에 안나타는 모델
