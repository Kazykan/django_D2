from accounts.models import *
user1 = User.objects.create(username='Alec', first_name='Baldwin')
Author.objects.create(authorUser=user1)

user2 = User.objects.create(username='Ben', first_name='Affleck')
Author.objects.create(authorUser=user2)

Category.objects.create(name='sport')
Category.objects.create(name='politics')
Category.objects.create(name='education')
Category.objects.create(name='medicine')

Post.objects.create(choicePost='AR', headingPost='Важность спорта для детского организма',
                    textPost='С малых лет родители прививают нам любовь к спорту. Выполняй физические упражнения',
                    author=Author.objects.get(authorUser=User.objects.get(username='Ben')))

Post.objects.create(choicePost='NW', headingPost='Швейцария ввела санкции против России',
                    textPost='Швейцария присоединилась к международному санкционному режиму,',
                    author=Author.objects.get(authorUser=User.objects.get(username='Ben')))

Post.objects.create(choicePost='AR', headingPost='Идентичность России',
                    textPost='Россия была и будет суверенным, независимым государством. Это просто аксиома.',
                    author=Author.objects.get(authorUser=User.objects.get(username='Alec')))
p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(pk=2)
p3 = Post.objects.get(pk=3)
p1.postCategory.add(Category.objects.get(name='sport'))
p2.postCategory.add(Category.objects.get(name='politics'))
p3.postCategory.add(Category.objects.get(name='politics'))
Comment.objects.create(commentUser=User.objects.get(username='Alec'), commentPost=Post.objects.get(
    headingPost='Швейцария ввела санкции против России'), text='comment1')
Comment.objects.create(commentUser=User.objects.get(username='Ben'), commentPost=Post.objects.get(
    pk=3), text='comment3')
Comment.objects.create(commentUser=User.objects.get(username='Ben'), commentPost=Post.objects.get(
    pk=1), text='comment4')
Comment.objects.create(commentUser=User.objects.get(username='Alec'), commentPost=Post.objects.get(
    pk=1), text='comment5')

Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=3).dislike()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(text='comment4').dislike()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=3).dislike()
Comment.objects.get(pk=4).like()
Author.objects.get(authorUser=User.objects.get(username='Alec')).update_rating()
Author.objects.get(authorUser=User.objects.get(first_name='Affleck')).update_rating()

Author.objects.get(authorUser=User.objects.get(first_name='Affleck')).ratingAuthor
Author.objects.get(authorUser=User.objects.get(username='Alec')).ratingAuthor

Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor')[0]
aa = Post.objects.all().order_by('-ratingPost')[0]
Post.objects.all().order_by('-ratingPost').values(
    'timeInCreation', 'ratingPost', 'headingPost', 'author__authorUser__username')[0]
aa.preview()

Comment.objects.filter(commentPost__headingPost='Важность спорта для детского организма').values(
    'commentUser__username', 'text', 'timeInCreation', 'ratingComment')