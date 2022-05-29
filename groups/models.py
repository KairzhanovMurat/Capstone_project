from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse
# import misaka
register=template.Library()
User=get_user_model()

# Create your models here.

class Group(models.Model):
    name=models.CharField(unique=True,max_length=100)
    slug=models.SlugField(unique=True,allow_unicode=True)
    description=models.TextField(blank=True,default='')
    description_html=models.TextField(blank=True,default='',editable=False)
    members=models.ManyToManyField(User,through='GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        # self.description_html=misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})

    class Meta:
        ordering=['name']




class GroupMember(models.Model):
    group=models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.user.name

    class Meta:
        unique_together = ('group', 'user')
