from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.db.models import Sum


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь один к одному
    ratingAuthor = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.all().aggregate(postRating=Sum('ratingPost'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.all().aggregate(commentRating=Sum('ratingComment'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Post(models.Model):
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )
    choicePost = models.CharField(max_length=2,
                                  choices=CATEGORY_CHOICES,
                                  default=NEWS)  # поле с выбором — «статья» или «новость»
    headingPost = models.CharField(max_length=128)  # заголовок статьи/новости
    textPost = models.TextField()  # текст статьи/новости
    ratingPost = models.SmallIntegerField(default=0)
    timeInCreation = models.DateTimeField(auto_now_add=True)  # Автоматическое добавление даты создания сайта

    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Связь один ко многим
    postCategory = models.ManyToManyField(Category, through='PostCategory')

    def preview(self):
        return self.textPost[0:123]+'...'

    def like(self):
        self.ratingPost += 1
        self.save()

    def dislike(self):
        self.ratingPost -= 1
        self.save()


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timeInCreation = models.DateTimeField(auto_now_add=True)  # Автоматическое добавление даты создания комментария
    ratingComment = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.commentUser.username

    def like(self):
        self.ratingComment += 1
        self.save()

    def dislike(self):
        self.ratingComment -= 1
        self.save()


Comment.objects.create(commentUser=User.objects)


