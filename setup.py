import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ReverseIP_ver_0-TruBurbank",
    version="0.001",
    author="Rayyan Hunerkar",
    author_email="ray26318@gmail.com",
    description="It's a package to find the Domains of an IP address  ",
    long_description=long_description,
    long_description_content_type="you wont read this",
    url="https://github.com/TruBurbank/ReverseIP",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
