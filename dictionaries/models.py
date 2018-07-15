from django.db import models


class InitcapField(models.CharField):

    def get_prep_value(self, value):
        return str(value).capitalize()


class Gender(models.Model):
    name = InitcapField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'genders'
        unique_together = ('name',)


class Tag(models.Model):
    name = InitcapField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'
        unique_together = ('name',)


class Interest(models.Model):
    name = models.CharField(max_length=128)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return '%s [Tags: %s]' % (self.name, ', '.join(self.tags.all().values_list('name', flat=True)))

    class Meta:
        db_table = 'interests'
        unique_together = ('name',)
