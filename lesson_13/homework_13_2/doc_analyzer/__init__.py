import os
import time
import pprint
import logging
from doc_analyzer.pdf_analyzer.pdf_analyzer_module import PDFAnalyzer
from doc_analyzer.link_analyzer.link_analyzer_module import LinkAnalyzer

os.makedirs(os.path.abspath(os.curdir) + os.sep + "logs", exist_ok=True)
logging.basicConfig(level=logging.DEBUG, format=u"%(filename)s[LINE:%(lineno)d]# %(levelname)-8s"
                                                u" [%(asctime)s]  %(message)s",
                    filename=os.path.abspath(os.curdir) + os.sep + "logs" + os.sep + "{}.txt".format(
                        time.strftime('%Y_%b_%d_%H_%M_%S')))

logging.info("Start of doc_analyzer program")


def print_(*args):
    for arg in args:
        pprint.pprint(arg)
        logging.info(args)
