from django.db import models


class GenderManager(models.Manager):

    @classmethod
    def gender_choices(cls):
        return []
        # return [pk['pk'] for pk in Gender.objects.all().values('pk')]


class Gender(models.Model):
    name = models.CharField(max_length=128)
    objects = GenderManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'genders'


class TagManager(models.Manager):

    @classmethod
    def tag_choices(cls):
        return []
        # tags = Tag.objects.all()
        # tag_choices = []
        # for tag in tags:
        #     tag_choices.append((tag.id, tag.name))
        # return tag_choices


class Tag(models.Model):
    name = models.CharField(max_length=128)
    objects = TagManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'


class InterestManager(models.Manager):

    @classmethod
    def interest_choices(cls):
        return []
        # interests = Interest.objects.all()
        # interest_choices = []
        # for interest in interests:
        #     interest_choices.append((u'%s' % interest.id, u'%s' % interest.name))
        # return interest_choices


class Interest(models.Model):
    name = models.CharField(max_length=128)
    tags = models.ManyToManyField(Tag)

    objects = InterestManager()

    def __str__(self):
        return '%s [Tags: %s]' % (self.name, ', '.join(self.tags.all().values_list('name', flat=True)))

    class Meta:
        db_table = 'interests'
