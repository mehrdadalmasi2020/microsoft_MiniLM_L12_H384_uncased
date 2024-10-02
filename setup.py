from setuptools import setup, find_packages

# Read the content of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="microsoft_MiniLM_L12_H384_uncased", 
    version="0.1.1",  # version number
    author="Mehrdad ALMASI, Demival VASQUES FILHO",
    author_email="mehrdad.al.2023@gmail.com, demival.vasques@uni.lu",
    description="A library that leverages the pre-trained microsoft_MiniLM-L12-H384-uncased model for efficient and lightweight text classification tasks, with a focus on English. The library offers easy-to-use fine-tuning capabilities, making it suitable for rapid deployment in resource-constrained environments.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mehrdadalmasi2020/microsoft_MiniLM_L12_H384_uncased", 
    packages=find_packages(),
    include_package_data=True,  # Include non-Python files in the package distribution
    install_requires=[
        "transformers>=4.20.0,<5.0.0",  # Update transformers version to avoid compatibility issues
        'tokenizers>=0.10.0,<0.14.0',   # Update tokenizers, matching transformers compatibility
        "torch>=1.7.0,<2.0.0",          # PyTorch version pinned to avoid conflicts
        "pandas>=1.1.0",                # Keep pandas as it is
        "scikit-learn>=1.0",            # Keep scikit-learn as it is
        "numpy>=1.19.0,<1.24.0",        # Pin numpy to avoid breaking changes with latest versions
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

