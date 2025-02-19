#!/usr/bin/env python3
#
# License: BSD
#   https://raw.github.com/robotics-in-py/rocon_app_platform/master/rocon_app_manager/LICENSE
#
##############################################################################
# Imports
##############################################################################

##############################################################################
# Exceptions
##############################################################################


class RappException(Exception):
    """
     Rapp Exception
    """
    pass


class NotFoundException(RappException):
    """
      Resource Not Found Exception
    """
    pass


class InvalidRappException(RappException):
    '''
      Raised if the app definition is invalid.
    '''


class MissingCapabilitiesException(Exception):
    '''
      Raised if one or more required capabilities are missing.
    '''
    def __init__(self, missing_caps):
        self.missing_caps = missing_caps


class GatewayNotFoundException(RappException):
    '''
      Raised if the gateway was not found.
    '''
