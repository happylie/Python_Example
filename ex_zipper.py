# -*- coding: utf-8 -*-
import sys
import os
import glob
import subprocess


class Zipper:
    def __init__(self):
        pass

    def _cmd_exists(self, cmd):
        """
        Check
        :param cmd: Command Line
        :return: True or False
        """
        return any(
            os.access(os.path.join(path, cmd), os.X_OK)
            for path in os.environ["PATH"].split(os.pathsep)
        )

    def zip_file(self, src, dst="", password=""):
        """
        File Zipper
        :param src: SRC Path
        :param dst: DST Path (Optional)
        :param password: Zip Password (Optional)
        :return: True or False
        """
        if not self._cmd_exists('zip'):
            return False
        if not dst:
            dst = src + ".zip"
        src = os.path.realpath(src)
        command = ['zip', '-j']
        if password:
            command += ['-P', password]
        command += [dst] + [src]
        try:
            ret = subprocess.call(command)
        except Exception, e:
            sys.stderr.write("exception dir_zip function : %s\n", str(e))
            return False
        else:
            if ret != 0:
                return False
            return True
        pass

    def zip_dir(self, src, dst="", password=""):
        """
        Directory Zipper
        :param src: SRC Path
        :param dst: DST Path (Optional)
        :param password: Zip Password (Optional)
        :return: True or False
        """
        if not self._cmd_exists('zip'):
            return False
        if not dst:
            dst = src + ".zip"
        src = os.path.realpath(src)
        command = ['zip', '-j']
        if password:
            command += ['-P', password]
        command += [dst] + glob.glob(src + "/*")
        try:
            ret = subprocess.call(command)
        except Exception, e:
            sys.stderr.write("exception dir_zip function : %s\n", str(e))
            return False
        else:
            if ret != 0:
                return False
            return True
        pass


if __name__ == '__main__':
    zipper = Zipper()
    zipper.zip_file('/test/test.txt', password='1234')
    zipper.zip_dir('/test/tmp', password='1234')
