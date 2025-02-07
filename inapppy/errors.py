class InAppPyError(Exception):
    """ Base class for all errors """

    pass


class InAppPyValidationError(InAppPyError):
    """ Base class for all validation errors """

    raw_response = None
    message = None

    def __init__(self, message= None, raw_response= None, *args, **kwargs):
        self.raw_response = raw_response
        self.message = message

        super().__init__(message, *args, **kwargs)

    def __str__(self):
        return "{}{}{}".format(self.__class__.__name__, self.message, self.raw_response)

    def __repr__(self):
        return "{}{}{}".format(self.__class__.__name__, self.message, self.raw_response)


class GoogleError(InAppPyValidationError):
    pass
