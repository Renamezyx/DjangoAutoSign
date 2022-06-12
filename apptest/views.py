from django.shortcuts import render
from apptest.models.WorkDate import WorkDate
import datetime
from MyScripts.sign import SignPlan

# Create your views here.
from django.http import JsonResponse


def sign_srv(req):
    work_date_filter_set = WorkDate.objects.filter(date__exact=datetime.date.today())
    work_date = work_date_filter_set[0]
    sign_plan = SignPlan(work_date.date, work_date.in_time, work_date.out_time, work_date.state)
    stated = sign_plan.do_sign()
    work_date.state = stated
    work_date.save()
    res = {
        "data": work_date.date,
        "stated": stated,
        "message": "success"
    }

    return JsonResponse(res)
