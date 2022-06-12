from django.contrib import admin
from apptest.models.WorkDate import WorkDate
from django.db.models.query import QuerySet
from apptest.untils.TimeTools import WorkTime


@admin.register(WorkDate)
class WorkDateAdmin(admin.ModelAdmin):
    actions = ["set_state_0", "set_state_1", "set_state_2",
               "change_time_for_long", "change_time_for_regular"]

    def set_state_0(self, req, queryset):
        rows_updated = queryset.update(state=0)
        self.message_user(req, "%s updated success" % rows_updated)

    def set_state_1(self, req, queryset):
        rows_updated = queryset.update(state=1)
        self.message_user(req, "%s updated success" % rows_updated)

    def set_state_2(self, req, queryset):
        rows_updated = queryset.update(state=2)
        self.message_user(req, "%s updated success" % rows_updated)

    def generate_work_of_week(self, req):
        pass

    def generate_work_of_day(self, req, queryset):
        print(self)

    def change_time_for_long(self, req, queryset: QuerySet):
        rows = queryset.exclude(state__exact=2)
        if not len(rows):
            self.message_user(req, "no valid data")
            return

        for row in rows:
            row: WorkDate
            _datetime = WorkTime(row.date)
            _datetime.log_time()
            if row.state == 0:
                row.in_time = _datetime.in_time
            row.out_time = _datetime.out_time
            row.save()
        self.message_user(req, "%d rows action success" % len(rows))
        return

    def change_time_for_regular(self, req, queryset):
        rows = queryset.exclude(state__exact=2)
        if not len(rows):
            self.message_user(req, "no valid data")
            return

        for row in rows:
            row: WorkDate
            _datetime = WorkTime(row.date)
            _datetime.regular_time()
            if row.state == 0:
                row.in_time = _datetime.in_time
            row.out_time = _datetime.out_time
            row.save()
        self.message_user(req, "%d rows action success" % len(rows))
        return
