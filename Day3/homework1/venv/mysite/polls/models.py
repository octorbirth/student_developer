import datetime

from django.db import models
from django.utils import timezone


#git이 꼬여서 지금 단계는 벌써 2번째 단계까지 진행한 단계라서
#commit만 더하겠습니다.
#양해부탁드려요~~





class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text