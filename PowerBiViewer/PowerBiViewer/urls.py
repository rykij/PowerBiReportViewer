"""
Definition of urls for PowerBiViewer.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.views

urlpatterns = [

    url(r'^$', app.views.home, name='home'),
   
]
