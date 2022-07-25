import os
import time
import pprint
import logging
from lesson_13.classwork_13_1.hillel_package.manager.manager_module import Manager

os.makedirs(os.path.abspath(os.curdir) + os.sep + "logs", exist_ok=True)
logging.basicConfig(level=logging.DEBUG, format=u"%(filename)s[LINE:%(lineno)d]# %(levelname)-8s"
                                                u" [%(asctime)s]  %(message)s",
                    filename=os.path.abspath(os.curdir) + os.sep + "logs" + os.sep + "{}.txt".format(
                        time.strftime('%Y_%b_%d_%H_%M_%S')))

logging.info("Start of Hillel program")


def print(*args):
    for arg in args:
        pprint.pprint(arg)
        logging.info(args)
