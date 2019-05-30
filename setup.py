import setuptools

setuptools.setup(
    name="tq-bsq-utils",
    version="0.0.1",
    url="https://github.com/quorum/tq-bsq-utils",
    author="Arnau Panosa",
    author_email="apanosa@yahoo.com",
    description="Utilities to parse and generate BSQ raster cubes",
    long_description=open("README.md").read(),
    packages=["tq", "tq.hdr"],
    install_requires=["numpy"],
)