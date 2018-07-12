# coding: utf-8

import uuid

import jsonfield
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

from ins.utils import const
from ins.app.manager import AloneUserManager


class Time(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(models.Model):
    name = models.CharField(max_length=128, db_index=True)


class User(AbstractBaseUser, Time):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64, unique=True, db_index=True)
    email = models.CharField(max_length=256, db_index=True, blank=True, default='')
    phone = models.CharField(max_length=16, db_index=True, blank=True, default='')
    avatar = models.CharField(max_length=256, blank=True, default='')
    location = jsonfield.JSONField(blank=True, default={})
    sex = models.CharField(max_length=12, choices=const.SEX_TYPES, default=const.SEX_UNDEFINED)
    brief = models.CharField(max_length=512, blank=True, default='')
    followed = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    is_private = models.BooleanField(default=False)
    is_certificate = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    objects = AloneUserManager()

    def __repr__(self):
        return '{} {}'.format(self.name, self.phone)

    @property
    def is_staff(self):
        return self.is_admin

    def follow(self, target_user):
        self.followed.add(target_user)

    def unfollow(self, target_user):
        self.followed.remove(target_user)


class Ins(Time):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brief = models.CharField(max_length=512, blank=True, default='')
    type = models.CharField(max_length=16, choices=const.INS_TYPE, default=const.PICTURE_INS)
    urls = jsonfield.JSONField(default=[])
    owner = models.ForeignKey(User, related_name='post_ins')
    likes = models.ManyToManyField(User, related_name='like_ins')
    tags = models.ManyToManyField(Tag)
    enable_comment = models.BooleanField(default=True)


    def like_by(self, user):
        self.likes.add(user)

    def unlike_by(self, user):
        self.likes.remove(user)


class Comment(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=512, blank=True, default='')
    poster = models.ForeignKey(User, related_name='comments')
    ins = models.ForeignKey(Ins, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
