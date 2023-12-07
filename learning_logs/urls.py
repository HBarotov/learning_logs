from django.urls import path

from .views import (
    index,
    topics,
    topic,
    new_topic,
    new_entry,
    edit_entry,
    delete_entry,
    edit_topic,
    delete_topic,
)


app_name = "learning_logs"
urlpatterns = [
    path("", index, name="index"),
    path("new_topic/", new_topic, name="new_topic"),
    path("topics/", topics, name="topics"),
    path("topics/<int:topic_id>/", topic, name="topic"),
    path("topics/<int:topic_id>/new_entry/", new_entry, name="new_entry"),
    path("topics/<int:topic_id>/edit_topic/", edit_topic, name="edit_topic"),
    path("topics/<int:topic_id>/delete_topic/", delete_topic, name="delete_topic"),
    path("edit_entry/<int:entry_id>/", edit_entry, name="edit_entry"),
    path("delete_entry/<int:entry_id>/", delete_entry, name="delete_entry"),
]
