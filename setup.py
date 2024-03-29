from setuptools import setup, find_packages
setup(
    name='DeltacodeProject',
    version='0.7.32.0',
    author='daisseur',
    author_email='daisseur@gmail.com',
    packages=find_packages(),
    url='https://github.com/daisseur/Deltacode_project',
    description="Encoder et décoder du texte à l'aide de plusieurs types d'encodages",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    license=open('LICENSE', 'r').read(),
    keywords=['python', 'deltacode', 'code', 'coding', 'encoding', 'DayEncoding', 'ROT', 'Cesar', 'DeltacodeProject', 'project', 'delta'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ]
)
