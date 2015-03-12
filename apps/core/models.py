from django.db import models
from django.db.models.signals import post_save, post_delete


class BaseModel(models.Model):
    number = models.IntegerField(default=0)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Base(BaseModel):
     def __unicode__(self):
        return self.text


class Log(BaseModel):
    STATUS_CHOICES = (('1', 'Alterado'), ('2', 'Deletado'))

    status = models.CharField(max_length=3, choices=STATUS_CHOICES)

    def __unicode__(self):
        return self.text


def update_log(sender, instance, **kwargs):
    if kwargs['created'] == False:
        log = Log()
        log.text = instance.text
        log.number = instance.number
        log.status = '1'
        log.save()

post_save.connect(update_log, sender=Base, )


def delete_log(sender, instance, **kwargs):
    log = Log()
    log.text = instance.text
    log.number = instance.number
    log.status = '2'
    log.save()

post_delete.connect(delete_log, sender=Base, )