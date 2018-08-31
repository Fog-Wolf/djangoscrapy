import sys
import os
import django

sys.path.append('../../../djangoscrapy') # 具体路径
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoscrapy.settings'
django.setup()