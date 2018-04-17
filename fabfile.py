from fabric.api import local, settings, abort
from fabric.contrib.console import confirm
from fabpolish import polish, sniff, local, info
from fabpolish.contrib import find_merge_conflict_leftovers

@sniff(severity='major', timing='fast')
def composer_security_check_npm():
    """Requires nsp in package"""
    info('Running security check for python dependencies...')
    return local("safety check -r requirements.txt")
    
