from django.conf.urls import patterns, url
from bincom_test import views


urlpatterns = [
	url(r'^$',  views.indexView,  name='index'),
	url(r'^polling-unit-results/$',  views.puResultsView,  name='unit-results'),
	url(r'^results/polling-unit-summary/$',  views.lgaSummaryView,  name='unit-summary'),
	url(r'^lga-summary/$',           views.addNewScoreView,  name='add-new-result'),
	]