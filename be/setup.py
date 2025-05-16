from setuptools import setup, find_packages

setup(
    name="ai-judge",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.104.1",
        "uvicorn==0.24.0",
        "pydantic==2.4.2",
        "python-dotenv==1.0.0",
        "PyGithub==2.1.1",
        "sqlalchemy==2.0.23",
        "alembic==1.12.1",
    ],
) 