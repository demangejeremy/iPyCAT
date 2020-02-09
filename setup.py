import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='iPyCat',  
     version='0.0.04',
     scripts=['ipycat'] ,
     author="Jérémy DEMANGE",
     author_email="jeremy.demange.mail@gmail.com",
     description="Interface Python en ligne de commande pour les Analyses Multidimensionnelles de Textes.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/demangejeremy/iPyCAT",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)