import io

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with io.open("requirements.txt") as f:
    required = f.read().splitlines()

with io.open("Readme.md", encoding="utf-8") as f:
    long_description = f.read()


def main():
    setup(
        name='pdf-analyzer-package',
        version='1.0',
        description='PDF Analyzer Tool Package',
        long_description=open('README.md').read(),
        long_description_content_type="text/markdown",
        url="https://github.com/AH0HIM/doc_analyzer_package",
        author='Ikonnikov Ilya',
        author_email='i666943097@gmail.com',
        packages=[
            'doc_analyzer',
            'doc_analyzer.pdf_analyzer',
            'doc_analyzer.link_analyzer'],
        install_requires=['requests>=2.21.0', 'pdfminer', 'pdfx~=1.4.1'],
        include_package_data=True,
        keywords="PDF Analyzer Tool Package"
    )


if __name__ == '__main__':
    main()
