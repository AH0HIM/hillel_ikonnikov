from doc_analyzer import PDFAnalyzer


class MainApp:
    def __init__(self, path):
        self.path = path

    def run(self):
        pdf = PDFAnalyzer(self.path)
        pdf.link_analyzer.collect_links()
        pdf.link_analyzer.review_link(pdf.link[0])
        pdf.link_analyzer.review_links(pdf.link[2:9])
        pdf.link_analyzer.make_report()
        pdf.link_analyzer.clean()


if __name__ == "__main__":
    print("Start...")
    pdf = MainApp('../example_pdf/example.pdf')
    pdf.run()
    print("Finish!")
