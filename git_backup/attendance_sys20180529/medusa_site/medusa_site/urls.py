from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import main.urls
import attendance.urls

urlpatterns = [
    url(r'^', include(main.urls)),
    url(r'^attendance/', include(attendance.urls)),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
