# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)			# 설문조사 질문
    pub_date = models.DateTimeField('date published')	# 생성일시

    # HERE 
    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)						# Poll과 연결
    choice_text = models.CharField(max_length=200)		# 설문조사의 선택지
    votes = models.IntegerField(default=0)				# 투표수

    # AND HERE
    def __str__(self):
        return self.choice_text