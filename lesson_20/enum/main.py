from enum import Enum
from http import HTTPStatus


class StatusEnum(Enum):

    def __init__(self, status, description):
        self.status = status
        self.description = description

    initial = (0, 'status_initial')
    processing = (1, 'status_processing')
    returned = (2, 'status_returned')


print(StatusEnum.initial.status)
#
# print(HTTPStatus.OK == 200)
# print(HTTPStatus.CREATED.description)


for status in StatusEnum:
    print(status.value)
    print(status.description)