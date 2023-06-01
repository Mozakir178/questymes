from django.db import models


class Availability(models.Model):
    availability_id = models.IntegerField(primary_key=True)
    day = models.CharField(max_length=100)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    recurringMeeting = models.ForeignKey('RecurringMeeting', on_delete=models.CASCADE)


class Batch(models.Model):
    batch_id = models.IntegerField(primary_key=True)
    batch_name = models.CharField(max_length=100)


class Interviews(models.Model):
    interview_id = models.AutoField(primary_key=True)
    interviewer_id = models.IntegerField()
    interviewee_id = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    students_notes = models.CharField(max_length=255)
    admin_feedback = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    instructions = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    meeting_link = models.CharField(max_length=255)
    meeting_status = models.CharField(max_length=1)
    batch = models.CharField(max_length=255)
    reminder_sent = models.BooleanField()

    def __str__(self):
        return self.title


class InterviewsOM(models.Model):
    interview_id = models.AutoField(primary_key=True)
    interviewer_id = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    students_notes = models.CharField(max_length=255)
    admin_feedback = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    instructions = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    meeting_link = models.CharField(max_length=255)
    meeting_status = models.CharField(max_length=1)
    batch = models.CharField(max_length=255)
    reminder_sent = models.BooleanField()

    def __str__(self):
        return self.title


class OneOnOne(models.Model):
    title = models.CharField(max_length=255)
    instruction = models.CharField(max_length=255)
    admin_id = models.IntegerField()
    meeting_link = models.CharField(max_length=255)
    date = models.DateField()
    slot_time = models.ManyToManyField('SlotTiming')
    duration = models.IntegerField()
    type = models.CharField(max_length=255)
    admin_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class RecurringMeeting(models.Model):
    recurring_id = models.AutoField(primary_key=True)
    admin_id = models.IntegerField()
    title = models.CharField(max_length=255)
    meeting_link = models.CharField(max_length=255)
    instruction = models.CharField(max_length=255)
    duration = models.IntegerField()
    type = models.CharField(max_length=255)
    availabilities = models.ManyToManyField('Availability')

    def __str__(self):
        return self.title


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Slot(models.Model):

    slot_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    instruction = models.TextField()
    admin_id = models.IntegerField()
    meeting_link = models.CharField(max_length=255)
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    day = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=1)
    user_id = models.IntegerField()
    recurring_id = models.IntegerField()


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    roles = models.ManyToManyField('Role')

    def __str__(self):
        return self.email


class SlotTiming(models.Model):

    startTime = models.TimeField()
    endTime = models.TimeField()

