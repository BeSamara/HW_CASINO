from envparse import  env
import os
env.read_envfile('settings.env')
money = int(os.environ.get('MY_MONEY'))
