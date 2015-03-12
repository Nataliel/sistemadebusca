import json
from random import randint
import urllib2
from celery.task import task
from apps.core.models import Base

__author__ = 'Nataliel Vasconcelos'


def get_object_api():
    url_api = 'http://api.randomuser.me/'
    open_url = urllib2.urlopen(url_api).read()

    objects = json.loads(open_url)

    return objects['results'][0]


@task
def add_object():
    object_api = get_object_api()

    object = Base()
    object.text = '%s %s' % (object_api['user']['name']['first'], object_api['user']['name']['last'])
    object.number = randint(0,10000)
    object.save()

@task
def add_objects():
    for i in range(1000):
        add_object.apply_async()