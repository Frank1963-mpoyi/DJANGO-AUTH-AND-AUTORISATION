import uuid

from django.contrib.auth                         import get_user_model
#from django.conf                                import AUTH_USER_MODEL
from django.db                                          import models

from common.global_choices                       import ISSUE_TYPE, LANGUAGES, STATUS_TYPE
from core.model_mixins                           import AuditFields
from core.utils                                  import randcode_gen

User = get_user_model()


# Create your models here.
class Issue(AuditFields):

    uuid_code       = models.UUIDField('UUID CODE', primary_key=True, default=uuid.uuid4, editable=False)

    token_key       = models.UUIDField('TOKEN', default=uuid.uuid4, editable=False,     blank=True, null=True)
    code            = models.CharField('CODE',          max_length=100,                 blank=False, default=randcode_gen)

    assigned_to     = models.ForeignKey(User, on_delete=models.PROTECT, related_name='assigned_to', null=True)
    assigned_by     = models.ForeignKey(User, on_delete=models.PROTECT, related_name='assigned_by', null=True)

    title           = models.CharField('TITLE',             max_length=250,               blank=True, null=True)
    description     = models.TextField('DESCRIPTION',       blank=True, null=True)
    dev_note        = models.TextField('DEVELOPER NOTE',    blank=True, null=True)
    language        = models.CharField('LANGUAGE',          max_length=3,               choices=LANGUAGES, default='FR')

    type            = models.PositiveSmallIntegerField('TYPE',          default=1,  choices=ISSUE_TYPE)
    status          = models.PositiveSmallIntegerField('STATUS',                    choices=STATUS_TYPE, blank=True, null=True)

    class Meta:

        app_label   = 'blog'# django  dont know to which app it belong to 
        db_table    = 'issue'
        verbose_name_plural = 'issues'

    def __str__(self):
        return self.title

