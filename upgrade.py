from pip._internal.utils.misc import get_installed_distributions
from subprocess import call

for i in get_installed_distributions():
    call("pip install --upgrade " + i.project_name, shell=True)
