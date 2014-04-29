from django.conf.urls import patterns, url


# Note that these patterns are all under /api/,
# due to the way they've been included into main/urls.py
urlpatterns = patterns(__package__ + '.api_views',
    # For user management
    url(r'^move_to_group$', 'move_to_group', {}, 'move_to_group'),
    url(r'^delete_users$', 'delete_users', {}, 'delete_users'),

    url(r'^facility_delete$', 'facility_delete', {}, 'facility_delete'),
    url(r'^facility_delete/(?P<facility_id>\w+)$', 'facility_delete', {}, 'facility_delete'),
)

