from django.db                                      import models
from django_countries.fields                        import CountryField


class AuditFields(models.Model):

    datetime_created    = models.DateTimeField('DATE CREATED',  auto_now_add=True)
    datetime_updated    = models.DateTimeField('DATE UPDATED',  auto_now=True)
    last_updated_by     = models.CharField('LAST UPDATED BY',   max_length=50,    blank=True,         null=True)
    bool_deleted        = models.BooleanField('IS DELETED?',    default=False)

    class Meta:
        abstract = True


class AddressFields(models.Model):

    street_name     = models.CharField('Street Name', max_length=200,           blank=True,         null=True)
    house_number    = models.PositiveSmallIntegerField('Number',                blank=True,         null=True)
    post_code       = models.CharField('Postal Code', max_length=50,            blank=True,         null=True)
    area            = models.CharField('Area',        max_length=100,           blank=True,         null=True)
    city            = models.CharField('City',        max_length=100,           blank=True,         null=True)
    region          = models.CharField('Region',      max_length=100,           blank=True,         null=True)
    country         = CountryField('Country',                                                       null=True)

    class Meta:
        abstract = True


# class AccountsFields(models.Model):
#
#     code_currency   = models.CharField('Currency', choices=CURRENCIES, max_length=3)
#     exchange_rate   = models.DecimalField(decimal_places=5, max_digits=9, default=1)
#     date_cancelled  = models.DateTimeField('Date Cancelled',                    blank=True,         null=True)
#     comment         = models.CharField(max_length=200,                          blank=True,         null=True)
#     cancel_note     = models.CharField(max_length=200,                          blank=True,         null=True)
#
#     class Meta:
#         abstract = True


class EmailFields(models.Model):

    email1          = models.EmailField('Admin. Email',                         blank=True,         null=True)
    email2          = models.EmailField('Account Email',                        blank=True,         null=True)
    email3          = models.EmailField('Branch Email',                         blank=True,         null=True)
    email4          = models.EmailField('Legal Email',                          blank=True,         null=True)

    class Meta:
        abstract = True


class PhoneFields(models.Model):

    phone1 = models.CharField('Phone 1', max_length=30, unique=True, blank=False, null=False)
    phone2 = models.CharField('Phone 2', max_length=30, unique=True, blank=True,  null=True)
    phone3 = models.CharField('Phone 3', max_length=30, unique=True, blank=True,  null=True)
    phone4 = models.CharField('Phone 4', max_length=30, unique=True, blank=True,  null=True)

    class Meta:
        abstract = True
