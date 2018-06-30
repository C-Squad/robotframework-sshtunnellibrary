from .SSHTunnelKeywords import SSHTunnelKeywords
from .version import VERSION

_version_ = VERSION


class SSHTunnelLibrary(SSHTunnelKeywords):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'