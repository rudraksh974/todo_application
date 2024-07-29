from django.apps import AppConfig


class TodoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo_app'


    
# class Profile(models.Model):
#     profile=models.CharField(max_length=100)
#     image=models.ImageField(upload_to="profile_pic/")
