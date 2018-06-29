from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^takeleave_list$', views.takeleave_list, name="takeleave_list"),
    url(r'^takeleave_audit_list$', views.takeleave_audit_list, name="takeleave_audit_list"),
    url(r'^apply_takeleave$', views.apply_takeleave, name="apply_takeleave"),
    url(r'^takeleave_audit$', views.takeleave_audit, name="takeleave_audit"),
    url(r'^cancel_takeleave$', views.cancel_takeleave, name="cancel_takeleave"),
]
