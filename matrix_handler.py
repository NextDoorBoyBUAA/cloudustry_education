"""Matrix main handler.
"""
from typing import Callable

__all__ = []
__version__ = 1.0
__author__ = 'chenjianwei'

from ce_thrift_gen.matrix.ttypes import RetrievalRequest, RetrievalReponse
from ce_thrift_gen.matrix.matrix import Iface


class MatrixRecommender(Iface):
    """web app will use this serve.
    """

    def __init__(self):
        pass

    def retrieval(self, request: RetrievalRequest) -> RetrievalReponse:
        """
        :type request: List[RetrievalRequest]
        :rtype: RetrievalRequest
        :param request:
        :return:
        """
        pass


if __name__ == '__main__':
    app = MatrixRecommender()
    req = RetrievalRequest()
    print(req)