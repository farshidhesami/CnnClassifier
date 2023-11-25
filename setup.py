import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "cnnClassifier"
AUTHOR_USER_NAME = "farshidhesami"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "farshidhesami@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package that provides a Convolutional Neural Network (CNN) classifier for image recognition tasks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", 
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    python_requires='==3.6',
)


