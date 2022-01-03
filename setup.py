from setuptools import find_packages, setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

project_urls={
    'Homepage': 'https://github.com/AkshayGhatul/input-sanitizer',
}

setup(
    name='input sanitizer',
    packages=find_packages(include=['input_sanitizer']),
    version='0.2.2',
    description='Sanitizes input data to prevent XSS i.e. cross site scripting attacks.',
    license='MIT',
    author='Akshay Ghatul',
    author_email='akshay.ghatul@trigensoft.com',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    install_requires=["bleach",],
    project_urls = project_urls,
)