from django.db import models
from django.contrib.auth.models import User
from enum import Enum


class Interviewee(User):
    courses = models.ManyToManyField('Course')


class Interviewer(User):
    post = models.CharField(max_length=25)


class Course(models.Model):
    course_name = models.CharField(max_length=25)


class Slot(models.Model):
    slot_name = models.CharField(max_length=25)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    title = models.CharField(max_length=25)


class InterviewerSlot(models.Model):
    interviewer_id = models.ForeignKey('Interviewer', on_delete=models.CASCADE)
    slot_id = models.ForeignKey('Slot', on_delete=models.CASCADE)
    interviewee_id = models.ForeignKey('Interviewee', on_delete=models.CASCADE)
    date = models.DateField()
    instructions = models.CharField(max_length=255)
    meeting_link = models.CharField(max_length=255)
    interviewee_attended = models.BooleanField()
    interviewer_attended = models.BooleanField()
    status = models.IntegerField()
    feedback = models.TextField(max_length=500)
    rating = models.IntegerField()
