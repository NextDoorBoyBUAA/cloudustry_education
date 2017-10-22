"""Hardware drive.
"""
import os
import logging


__all__ = []
__version__ = 1.0
__author__ = ['zhaozhen', 'chenjianwei']

from requests import Request


class HardwareDriver:
    """hardware driver.
    """

    def __init__(self, server: str, port: int):
        self.server = server
        self.port = port
        self.socket = None

    def execute(self, path: str) -> bool:
        return True


def test():
    """
    test function
    :return:
    """
    stl_dir = ""
    names = ["%s/%s" % (stl_dir, name) for name in os.listdir(stl_dir)]
    server, port = "", 8291
    drive = HardwareDriver(
        server=server,
        port=port
    )
    while True:
        name = names.pop()
        try:
            drive.execute(name)
        except Exception as e:
            drive = HardwareDriver(
                server=server,
                port=port,
            )
            names.append(name)  # retry


if __name__ == '__main__':
    test()