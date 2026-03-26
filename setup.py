"""Setup script."""

from setuptools import find_packages, setup  # noqa: E402

setup(
    name="flexicodec",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "funasr",
        "easydict",
        "descript-audio-codec",
        "pyyaml",
        "huggingface_hub",
        "transformers",
    ],
)
