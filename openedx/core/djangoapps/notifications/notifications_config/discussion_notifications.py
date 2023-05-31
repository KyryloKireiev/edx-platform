"""
Configuration for Discussions Notifications.
"""

from openedx.core.djangoapps.notifications.notifications_config.base_notification import (
    NotificationApp,
    NotificationType,
)


class DiscussionNotificationApp(NotificationApp):
    """
    Discussion notification app
    """
    name = 'discussion'

    core_web = True
    core_email = True
    core_push = True
    core_info = 'comment on post and response on comment'


class NewCommentNotificationType(NotificationType):
    """
    New comment on post notification type
    """
    notification_app = 'discussion'
    name = 'new_comment_on_post'

    web = True
    email = True
    push = True
    info = 'Comment on post'
    is_core = False
    non_editable_channels = ['push']

    content_context = {
        'content': 'New comment on post.',
        'post_title': 'Post title',
        'comment_text': 'Comment text',
        'post_url': 'Post URL',
    }


class NewResponseNotificationType(NotificationType):
    """
    New response on post notification type
    """
    notification_app = 'discussion'
    name = 'new_response_on_post'

    web = True
    email = True
    push = True
    info = 'New Response on Post'
    is_core = False
    non_editable_channels = ['web']

    content_context = {
        'content': 'New response on post.',
        'post_title': 'Post title',
        'comment_text': 'Comment text',
        'post_url': 'Post URL',
    }


class NewResponseOnCommentNotificationType(NotificationType):
    """
    New response on comment on post notification type
    """
    notification_app = 'discussion'
    name = 'new_response_on_comment'

    web = True
    email = True
    push = True
    info = 'Response on comment'
    is_core = False
    non_editable_channels = ['web', 'push']

    content_context = {
        'content': 'New response on comment.',
        'comment_text': 'Comment text',
        'response_text': 'Response text',
        'comment_url': 'Comment URL',
    }
