""" Exceptions module"""


class NotFoundException(Exception):
    """ Not found exception"""
    pass


class ExceptionModel(Exception):
    """ Models exception"""
    pass


class XmlException(Exception):
    """ Xml exception"""
    pass


class RespironicsException(Exception):
    """ Respironics exception"""
    pass


class ResmedException(Exception):
    """ Resmed exception"""
    pass


class ConnectionException(Exception):
    """ Connection DB exception"""
    pass


class WorkerException(Exception):
    """ workers exception"""
    pass




