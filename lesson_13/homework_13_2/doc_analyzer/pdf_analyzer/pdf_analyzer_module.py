import pdfx
from ..link_analyzer.link_analyzer_module import LinkAnalyzer


class PDFAnalyzer:

    def __init__(self, path):
        self.path = path
        self.dict_url = self.read()
        self.link = self.dict_url['url']
        self.link_analyzer = LinkAnalyzer(self.dict_url)

    def read(self):
        pdf = pdfx.PDFx(self.path)
        return pdf.get_references_as_dict()
