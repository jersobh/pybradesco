import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybradesco",
    version="0.0.1",
    author="jersobh",
    author_email="jersobh@gmail.com",
    description="Bradesco Bank Slip API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jersobh/pybradesco",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)