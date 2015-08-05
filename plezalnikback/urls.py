from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
     url(r'^plezalnik/$', 'plezalnikback.views.index', name='index'),
     url(r'^gradeletter/$', 'plezalnikback.views.gradeletter', name='gradeletter'),
     url(r'^gradenumber/$', 'plezalnikback.views.gradenumber', name='gradenumber'),
     url(r'^gradefinish/$', 'plezalnikback.views.gradefinish', name='gradefinish'),
     url(r'^speed/$', 'plezalnikback.views.speed', name='speed'),
     url(r'^login/$', 'plezalnikback.views.login', name='login'),
     url(r'^style/$', 'plezalnikback.views.style', name='style'),
     url(r'^leaderboard/$', 'plezalnikback.views.leaderboard', name='leaderboard'),
     url(r'^createachievement/$', 'plezalnikback.views.createachievement', name='createachievement'),

)

