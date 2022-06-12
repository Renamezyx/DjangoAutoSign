import datetime
import os

from django.db import models
from apptest.models.BaseModel import BaseModel


class WorkDate(BaseModel):
    date = models.DateField(primary_key=True)
    in_time = models.DateTimeField(null=False)
    out_time = models.DateTimeField(null=False)
    state = models.IntegerField(default=0)

    def __str__(self):
        return "date: %s | inTime: %s | outTime: %s | state: %d" % (
            self.date, self.in_time.strftime("%H:%M:%S"),
            self.out_time.strftime("%H:%M:%S"), self.state)