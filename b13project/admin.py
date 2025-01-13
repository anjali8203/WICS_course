from django.contrib import admin
from .models import UploadedFile, UserProfile, Project, Vote, Message, JoinRequest

admin.site.register(UploadedFile)
admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Vote)
admin.site.register(Message)
admin.site.register(JoinRequest)