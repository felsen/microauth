from setuptools import setup, find_packages

setup(
    name="microauth",
    version='0.1',
    packages=["microauth", "microauth.resources"],
    zip_safe=False,
    install_requires=[
        "Flask-RESTful",
        "Flask-SQLAlchemy",
        "bcrypt",
        "requests",
        "pyopenssl",
    ]
)
