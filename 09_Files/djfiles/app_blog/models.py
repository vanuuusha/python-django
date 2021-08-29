from django.db import models


class Blog(models.Model):
    author = models.CharField(max_length=25)
    title = models.CharField(verbose_name='название новости', max_length=100)
    content = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blog'


class FileForBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='files')
    file_field = models.FileField(upload_to='img/')