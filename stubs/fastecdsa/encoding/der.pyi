# Stubs for fastecdsa.encoding.der (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Tuple

from . import SigEncoder
from .asn1 import INTEGER, SEQUENCE
from .util import bytes_to_int, int_to_bytes


class InvalidDerSignature(Exception):
    ...


class DEREncoder(SigEncoder):

    @staticmethod
    def encode_signature(r: int, s: int) -> bytes:
        ...

    @staticmethod
    def decode_signature(sig: bytes) -> Tuple[int, int]:
        ...