# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from SLFAPP import views as users_views
from SLFAPP.views import login_view, patient_dashboard, doctor_dashboard
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_views.home, name='home'),
    path('patient/signup/', users_views.patient_signup, name='patient_signup'),
    path('doctor/signup/', users_views.doctor_signup, name='doctor_signup'),
    path('login/', login_view, name='login'),
    path('patient/dashboard/<str:username>/',
         patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/<str:username>/',
         doctor_dashboard, name='doctor_dashboard'),
    path('blog/', include('blog.urls')),
    # Add other app URLs as needed
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
