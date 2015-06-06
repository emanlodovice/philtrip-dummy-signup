import time
import json
from datetime import datetime

from social.backends.facebook import FacebookOAuth2

from dummysignup.models import UserProfile


def login(backend, uid, user, details, is_new, response, *args, **kwargs):
    print response
    # if not is_new:
    #     return
    create_new_user(user, details)
    create_profile(user, response)


def create_new_user(user, details):
    user.first_name = details['first_name']
    user.last_name = details['last_name']
    user.save()


def create_profile(user, response):
    works = []
    for work in response['work']:
        position = work['position']['name']
        works.append(position)
    work = json.dumps(works)
    location = ''
    if 'name' in response['location']:
        location = response['location']['name']
    d = time.strptime(response['birthday'], '%m/%d/%Y')
    d = datetime.fromtimestamp(time.mktime(d))
    profile = UserProfile(user=user, work=work, location=location, birthday=d)
    profile.save()
