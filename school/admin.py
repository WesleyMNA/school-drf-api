from django.contrib import admin

from .models import Student, Course, Registration


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birthday')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20
    ordering = ('name',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'level')
    list_display_links = ('id', 'code')
    search_fields = ('code',)
    list_per_page = 20
    ordering = ('code',)


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('id', )


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Registration, RegistrationAdmin)
