from setuptools import setup, find_packages

setup(
    name="spanish_lottery",
    version="0.1",
    packages=find_packages(),
    install_requires=["typer", "trogon"],
    entry_points={
        "console_scripts": [
            "spanish_lottery=spanish_lottery.lottery:lottery",
        ],
    },
    author="Gero Zayas",
    author_email="gerozayas@gmail.com",
    description="CLI app that generates random bets for famous Spanish Lottery Games",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/GeroZayas/Spanish-Lottery-CLI",  # Optional
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",  # Specify Python version requirements
)
