puppetboard-rpm
===============

Spec files to build all required packages to install pupeptboard form rpm

This is a first attemp to get all python-packages into an rpm.  Most specs are taken from the epel (6.5) or centos base (6.5) src.rpms, and updated to the 'requirements.txt' form the [puppetboard github page] (https://github.com/nedap/puppetboard).

Only the python-flacs is taken from the fc20 repos.  This spec file has support for both current versions of fedora and RHEL and deriviates.https://github.com/nedap/puppetboardhttps://github.com/nedap/puppetboard)

Building the packaged is best done using a clean centos6.5 vagrant box.  There is a specific order and build requirements.  I still have some conflicting versions  ... 


