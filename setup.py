import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME = "Galaxy-classification-project"
AUTHOR_USER_NAME = "SourajaKundu"
SRC_REPO = "galaxyclassification"
AUTHOR_EMAIL = "sourajaakundu@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author=AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for galaxy-star classification"
)