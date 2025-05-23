from django.utils.translation import gettext_lazy as _


CLASSIFICATION_LIST = (('protocollo', _('Protocol')),
                       ('decreto_rettorale', _('Rector\'s Decree (R.D.)')),
                       ('decreto_direttore_generale', _('General Director\'s Decree (G.D.D.)')),
                       ('decreto_dirigente_struttura', _('Department Director or Structure Manager\'s Decree')),
                       ('decreto_direttore_cr', _('Residential Center Director\'s Decree (R.C.D.)')),
                       ('decreto_prorettore', _('Pro-Rector\'s Decree (Residential Center)')),
                       ('delibera_dipartimento_facolta', _('Department/Faculty Resolution')),
                       ('delibera_senato', _('Senate Resolution')),
                       ('delibera_cda', _('Board of Directors Resolution')))

# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_UPLOAD_SIZE = 214958080

PDF_FILETYPE = ('application/pdf',)
DATA_FILETYPE = ('text/csv', 'application/json',
                 'application/vnd.ms-excel',
                 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                 'application/vnd.oasis.opendocument.spreadsheet',
                 'application/wps-office.xls',
                 )
TEXT_FILETYPE = ('text/plain',
                 'application/vnd.oasis.opendocument.text',
                 'application/msword',
                 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                )
VIDEO_FILETYPE = ('video/mp4', 'video/avi', 'video/mov', 'video/wmv', 'video/flv', 'video/webm', 'video/mkv')
IMG_FILETYPE = ('image/jpeg', 'image/png', 'image/gif', 'image/x-ms-bmp')
P7M_FILETYPE = ('application/pkcs7-mime',)
SIGNED_FILETYPE = PDF_FILETYPE + P7M_FILETYPE
PERMITTED_UPLOAD_FILETYPE = TEXT_FILETYPE + DATA_FILETYPE + SIGNED_FILETYPE + IMG_FILETYPE + VIDEO_FILETYPE

# maximum permitted filename lengh in attachments, uploads
ATTACH_NAME_MAX_LEN = 255

ATTACHMENTS_DICT_PREFIX = "allegati"

# attachments validation messages
WRONG_TYPE = _("Please upload only files "
               "in {}. "
               "Currently this is '{}'")
WRONG_SIZE = _("Please keep the file size within {}. "
               "Currently this is {}")
WRONG_LENGTH = _("Please use an attachment name length "
                 "less than {}. Currently you have entered a name of {} characters")

# formset special words
FORMSET_REGEX = "^(?P<field_name>{})-(?P<index>[0-9]+)-(?P<name>[a-zA-ZÀ-ÿ0-9_°^\-\'\"]+)$"
FORMSET_FULL_REGEX = FORMSET_REGEX.format("[a-zA-ZÀ-ÿ0-9_°^\-\'\"]+")

FORMSET_TEMPLATE_NAMEID = 'NNNNN'
MANAGEMENT_FORMSET_STRINGS = [FORMSET_TEMPLATE_NAMEID,
                              '-TOTAL_FORMS', '-INITIAL_FORMS',
                              '-MAX_NUM_FORMS','-MIN_NUM_FORMS']

CAPTCHA_DEFAULT_LANG = 'es'
CAPTCHA_EXPIRATION_TIME = 120000 # milliseconds
CUSTOM_WIDGETS_IN_FORMSETS = True

LANGUAGE_CODE = "es"
