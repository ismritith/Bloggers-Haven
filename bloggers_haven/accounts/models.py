from django.db import models


from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]

class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)
