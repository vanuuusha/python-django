from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='avatars/', default=None, null=True)
    #  а как тут в поле avatar сделать так, чтоб не вылетала ошибка NOT NULL constraint failed
    #  вроде писал и blank=True, и null=True, но все равно вылетала эта ошибка, пока не удалил все записи
    #  или как другой вариант, когда через default пытался сюда передать картинку anon.jpg, тож эта ошибка вылеталa,
    #  в итоге через шаблон вставил, но это наверно неправильно удалять все поля в бд чтоб что-то добавить)

    #  для теста тут решил создать такое же поле avatar2 и оно сразу заработало, могло быть дело в том,
    #  что я сначала написал makemigrations с неправильными параметрами?
    #  и если да, то как можно менять makemigrations которые я посылаю?
    # TODO да, видимо так - ответил в ЛМС
    # avatar_2 = models.FileField(upload_to='new_avatars/', default=None, null=True)
    telephone = models.CharField(max_length=12)
