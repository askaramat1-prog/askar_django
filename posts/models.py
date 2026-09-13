from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(null=True, upload_to="posts")
    views = models.IntegerField(default=0)


class Comment(models.Model):
    authoer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)