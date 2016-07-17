import pkg_resources

__version__ = pkg_resources.require("{{ cookiecutter.package_name }}")[0].version
__author__ = '{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>'
__all__ = []
