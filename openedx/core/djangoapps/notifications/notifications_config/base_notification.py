"""
Base setup for Notification Apps and Types.
"""
from typing import List


class NotificationType:
    """
    This is the base class for all notification types.
    """
    notification_app: str = None
    name: str = None

    # notification preferences
    web: bool = False
    email: bool = False
    push: bool = False
    info: str = None
    is_core: bool = False
    non_editable_channels: List[str] = []

    # notification content
    content_context: dict = {}
    email_template: str = None

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__().encode('utf-8')

    def get_preferences(self):
        """
        Returns preferences for the given notification type.
        """
        return {
            self.name: {
                'email': self.email,
                'push': self.push,
                'web': self.web,
                'info': self.info,
            },
        }

    def compile_content(self):
        """
        Method to compile content based on content_context
        """

    def send_email(self):
        """
        Method to send email.
        """


class NotificationTypeManager:
    """
    Manager for notification types
    """
    notification_types: List[NotificationType]

    def __init__(self):
        self.notification_types = NotificationType.__subclasses__()

    def get_notification_types_by_app(self, notification_app):
        """
        Returns notification types for the given notification app.
        """
        return [
            notification_type for notification_type in self.notification_types
            if notification_type.notification_app == notification_app
        ]


class NotificationApp:
    """
    This is base class for all notification apps.
    """
    name: str
    enabled: bool = True

    core_web: bool = False
    core_email: bool = False
    core_push: bool = False
    core_info: str = ''

    core_notification_types: List[NotificationType] = []
    notification_types: List[NotificationType] = []
    non_editable_notification_types: List[NotificationType] = []

    def get_app_notification_types(self):
        """
        Returns notification types for the given notification app.
        """
        return NotificationTypeManager().get_notification_types_by_app(self.name)

    def get_core_notification_types(self, notification_types):
        """
        Returns core notification types for the given notification app.
        """
        return [notification_type for notification_type in notification_types if notification_type.is_core]

    def get_non_editable_notification_types(self, notification_types):
        """
        Returns non-editable notification types notification app.
        """
        non_editable_notification_types = {}
        for notification_type in notification_types:
            non_editable_channels = notification_type.non_editable_channels
            if non_editable_channels:
                non_editable_notification_types[notification_type.name] = non_editable_channels
        return non_editable_notification_types

    def __init__(self):
        app_notification_types = self.get_app_notification_types()
        self.notification_types = app_notification_types
        self.core_notification_types = self.get_core_notification_types(app_notification_types)
        self.non_editable_notification_types = self.get_non_editable_notification_types(app_notification_types)

    def get_core_notification_preferences(self):
        """
        Returns core notification preferences for notification app.
        """
        return {
            'email': self.core_email,
            'push': self.core_push,
            'web': self.core_web,
            'info': self.core_info,
        }

    def get_notification_type_preferences(self):
        """
        Returns notification type preferences for notification app.
        """
        notification_type_preferences = {}
        non_core_notification_type = list(set(self.notification_types) - set(self.core_notification_types))
        for notification_type in non_core_notification_type:
            notification_type_preference = notification_type().get_preferences()
            notification_type_preferences.update(notification_type_preference)

        notification_type_preferences['core'] = self.get_core_notification_preferences()

        return notification_type_preferences

    def get_core_notification_type_names(self):
        """
        Returns core notification type names for notification app.
        """
        return [core_notification_type.name for core_notification_type in self.core_notification_types]

    def get_notification_app_preferences(self):
        """
        Returns notification preference for notification app.
        """
        return {
            'enabled': self.enabled,
            'not_editable': self.non_editable_notification_types,
            'notification_types': self.get_notification_type_preferences(),
            'core_notification_types': self.get_core_notification_type_names(),
        }

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__().encode('utf-8')


class NotificationAppManager:
    """
    Notification app manager
    """
    notification_apps: List[NotificationApp] = []

    def __init__(self):
        self.notification_apps = NotificationApp.__subclasses__()

    def get_notification_app(self, name):
        """
        Returns notification app for the given name.
        """
        for notification_app in self.notification_apps:
            if notification_app.name == name:
                return notification_app
        return None

    def get_notification_app_preferences(self, name):
        """
        Returns notification app preferences for the given name.
        """
        notification_app = self.get_notification_app(name)
        if notification_app:
            return notification_app().get_notification_app_preferences()
        return None

    def get_app_notifications(self, app_name):
        """
        Returns notification types for the given app name.
        """
        notification_app = self.get_notification_app(app_name)
        if notification_app:
            return notification_app().get_app_notification_types()
        return None

    def get_app_core_notifications(self, app_name):
        """
        Returns core notification types for the given app name.
        """
        app_notification = self.get_app_notifications(app_name)
        return [notification_type for notification_type in app_notification if notification_type.is_core]
