from django.shortcuts import render

# Create your views here.


from accounts.models import *
user1 = User.objects.create(username='Alec', first_name='Baldwin')
Author.objects.create(authorUser=user1)

user2 = User.objects.create(username='Ben', first_name='Affleck')
Author.objects.create(authorUser=user1)

Category.objects.create(name='спорт')
Category.objects.create(name='политика')
Category.objects.create(name='образование')
Category.objects.create(name='медицина')

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
c1 = Category.objects.get(name='спорт')
c2 = Category.objects.get(name='политика')
p1.postCategory.add(c1)
p2.postCategory.add(c2)
p3.postCategory.add(c2)
Comment.objects.create(com)