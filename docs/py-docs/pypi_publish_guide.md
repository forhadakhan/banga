
# Guide: Republish Python Package (PyPI)

Follow these steps to update and republish your Python package after making new changes.

## 1. Update Version in setup.py:

Open `py-package/setup.py` and increment the version number. Update the "version" field:

```python
# py-package/setup.py

from setuptools import setup, find_packages

setup(
    name='banga',
    version='X.Y.Z',  # Increment version number
    # ... other fields ...
)
```

## 2. Create a Source Distribution:
In the py-package directory, run:

```bash
python setup.py sdist
```
This will create a source distribution tarball in the dist directory.

## 3. Upload to PyPI using Twine:
Upload the new version to PyPI using Twine:

```bash
twine upload dist/*
```
During this step, you might be prompted to enter your PyPI API token. 
```bash
twine upload --username __token__ --password <your-api-token> dist/*
```

Now, your updated Python package is published on PyPI with the new version.

Remember to update any projects using this package to the latest version.






