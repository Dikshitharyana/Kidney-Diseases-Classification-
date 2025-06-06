import setuptools

with open("Readme.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classification-"
AUTHOR_USER_NAME = "Dikshitharyana"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "dikshitkumar951@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author= AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
)