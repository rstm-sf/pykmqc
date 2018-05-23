from kmqc import api
from kmqc import base
from kmqc import gates
from kmqc import program

from kmqc.api import Connection
from kmqc.base import Qubit
from kmqc.gates import DEFINITE_GATES
from kmqc.program import Program


__all__ = [
    'connect', 'Connection',
    'Qubit'
    'DEFINITE_GATES',
    'Program',
]

__version__ = "alpha"


def connect(*args, **kwargs):
    return Connection(*args, **kwargs)


connect.__doc__ = Connection.__init__.__doc__
