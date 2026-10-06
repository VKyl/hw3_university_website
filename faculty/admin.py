from django.contrib import admin
from .models import IndexPage, ContactEmail, Program, Subject, Department, Tutor, ExchangeProgram

admin.site.register(IndexPage)
admin.site.register(ContactEmail)
admin.site.register(Program)
admin.site.register(Subject)
admin.site.register(Department)
admin.site.register(Tutor)
admin.site.register(ExchangeProgram)
