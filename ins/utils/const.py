# coding=utf-8

URL_REGEX = '[A-Za-z0-9-_.]+'

# model const
SEX_MALE = "MALE"
SEX_FEMALE = 'FEMALE'
SEX_UNDEFINED = "UNDEFINED"

SEX_TYPES = (
    (SEX_MALE, 'Male'),
    (SEX_FEMALE, 'Female'),
    (SEX_UNDEFINED, 'Undefined')
)


INS_TYPE_PICTURE = "PICTURE"
INS_TYPE_VIDEO = "VIDEO"

INS_TYPE = (
    (INS_TYPE_PICTURE, 'Picture'),
    (INS_TYPE_VIDEO, 'Video')
)

NOTIFY_LIKES = 'LIKE'
NOTIFY_COMMENT = 'COMMENT'
NOTIFY_FOLLOW = 'FOLLOW'
NOTIFY_BROADCAST = 'BROADCAST'

NOTIFY_TYPE = (
    (NOTIFY_LIKES, 'Like'),
    (NOTIFY_COMMENT, 'Comment'),
    (NOTIFY_FOLLOW, 'Follow'),
    (NOTIFY_BROADCAST, 'Broadcast')
)

