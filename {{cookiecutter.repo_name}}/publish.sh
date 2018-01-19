#!/bin/sh

VERSION=$(<VERSION)

package() {
    python setup.py bdist_wheel
}

upload() {
    twine upload dist/"{{cookiecutter.package_name}}-$VERSION-py3-none-any.whl"
}

package
upload
