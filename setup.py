from setuptools import setup, find_packages

setup(
    name="rtsmappingdl",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "rasterio",
        "numpy",
        "pandas",
        "google-cloud-storage",
    ],
    author="Yili Yang",
    author_email="yyang@woodwellclimate.org",
    description="RTSmappingDL: Mapping retrogressive thaw slumps using deep learning",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/whrc/RTSmappingDL",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)