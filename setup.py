import re
from setuptools import setup
from setuptools import find_packages

def version():
    Filename = "Quartny/__init__.py"
    with open(Filename) as co:
        match = re.search(r"""^__version__ = ['"]([^'"]*)['"]""", co.read(), re.M)
    if not match:
        raise RuntimeError("{} doesn't contain __version__".format(Filename))
    version = match.groups()[0]
    return version
with open("README.md", encoding="utf8") as readme:
    long_desc = readme.read()


setup(
    name="Quartny",
    version=version(),
    author="Quartny | Quartny",
    author_email="quartny@proton.me",
    description="PyOpen-Api Hub | QuartnyAPI",
    long_description_content_type="text/markdown",
    long_description=long_desc,
    packages=find_packages(),
    license="MIT",
    url="https://github.com/Quartny/QuartnyAPI",
    download_url="https://github.com/Quartny/QuartnyAPI/blob/main/README.md",
    install_requires=["pytz>=2023.3","requests-html","pillow"],
    keywords=['python', "QuartnyAPI","FastAPI"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    
    project_urls={
        "Tracker": "https://github.com/Quartny/QuartnyAPI/issues",
        "Community": "https://telegram.me/Quartny",
        "Source": "https://github.com/Quartny/QuartnyAPI",
    },
    python_requires="~=3.7",
)
