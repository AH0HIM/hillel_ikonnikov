# !/usr/bin/env python
import io

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def main():
    setup(
        name='hillel-package',
        version='1.0',
        description='My Hillel Package Description',
        long_description="long_description",
        long_description_content_type="text/markdown",
        url="",
        author='Ikonnikov Ilya',
        author_email='i666943097@gmail.com',
        packages=[
            'hillel_package',
            'hillel_package.creator',
            'hillel_package.manager'
        ],
        install_requires=['requests>=2.21.0'],
        include_package_data=True,
        keywords="mypackage for product test"
    )


if __name__ == '__main__':
    main()
