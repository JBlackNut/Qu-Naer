#!/usr/bin/env python
__author__ = 'gong'
__create_time__ = '10/03/2014'

from django.db import models
from django.forms.models import model_to_dict


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    book_id = models.BigIntegerField(blank=True, null=True)
    place_id = models.BigIntegerField(blank=True, null=True)
    post_content = models.BinaryField(blank=True, null=True)
    post_image = models.CharField(max_length=32, blank=True)
    post_source = models.SmallIntegerField(blank=True, null=True)
    post_type = models.SmallIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    post_status = models.SmallIntegerField(blank=True, null=True)
    post_audit = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'rdb_post'
        managed = True

    def canonical(self):
        """
        return the object as a tuple
        """
        fields = model_to_dict(self, fields=('id', 'user_id', 'book_id', 'place_id', 'post_content', 'post_image',
                                             'post_source', 'post_type', 'create_time', 'update_time',
                                             'post_status', 'post_audit', 'post_image_meta'))
        return fields




class SharedPost(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.BigIntegerField(blank=True, null=False)
    user_id = models.BigIntegerField(blank=True, null=False)
    create_time = models.DateTimeField(blank=True, null=False)

    class Meta:
        db_table = 'rdb_shard_post'
        managed = True

