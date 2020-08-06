import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gsct", # Replace with your own username
    version="0.0.1",
    author="Eric & Allie Baur",
    author_email="baurfamily@gmail.com",
    description="A tracker for Girl Scout cookie booth sales",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/baurfamily/cookie-pi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pytest',
    ],
    # scripts=['gs-cookie-tracker'],
    python_requires='>=3.7',
)