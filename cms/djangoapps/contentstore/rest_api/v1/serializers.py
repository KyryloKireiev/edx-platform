"""
API Serializers for Contentstore
"""

from rest_framework import serializers

from xmodule.course_block import get_available_providers


class ProctoredExamSettingsSerializer(serializers.Serializer):
    """ Serializer for edX Staff proctored exam settings. """
    enable_proctored_exams = serializers.BooleanField()
    allow_proctoring_opt_out = serializers.BooleanField()
    proctoring_provider = serializers.CharField()
    proctoring_escalation_email = serializers.CharField(required=False, allow_null=True)
    create_zendesk_tickets = serializers.BooleanField()


class LimitedProctoredExamSettingsSerializer(serializers.Serializer):
    """Serializer for non edX Staff for proctored exam settings"""
    enable_proctored_exams = serializers.BooleanField()
    proctoring_provider = serializers.CharField()
    proctoring_escalation_email = serializers.CharField(allow_blank=True)
    create_zendesk_tickets = serializers.BooleanField()


class ProctoredExamConfigurationSerializer(serializers.Serializer):
    """ Serializer for various metadata associated with proctored exam settings. """
    proctored_exam_settings = ProctoredExamSettingsSerializer()
    available_proctoring_providers = serializers.ChoiceField(get_available_providers())
    course_start_date = serializers.DateTimeField()


class ProctoringErrorModelSerializer(serializers.Serializer):
    """
    Serializer for proctoring error model item.
    """
    deprecated = serializers.BooleanField()
    display_name = serializers.CharField()
    help = serializers.CharField()
    hide_on_enabled_publisher = serializers.BooleanField()
    value = serializers.CharField()


class ProctoringErrorListSerializer(serializers.Serializer):
    """
    Serializer for proctoring error list.
    """
    key = serializers.CharField()
    message = serializers.CharField()
    model = ProctoringErrorModelSerializer()


class ProctoringErrorsSerializer(serializers.Serializer):
    """
    Serializer for proctoring errors with url to proctored exam settings.
    """
    mfe_proctored_exam_settings_url = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    proctoring_errors = ProctoringErrorListSerializer(many=True)
