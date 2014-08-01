%global upstream_name puppetboard

Name:           python-%{upstream_name}
Version:        0.0.4
Release:        3%{?dist}
Summary:        Puppetboard is a web interface to PuppetDB aiming to replace the reporting functionality of Puppet Dashboard. 
License:        Apache v2.0 License
URL:            https://github.com/nedap/puppetboard
Source0:        http://pypi.python.org/packages/source/p/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

# taken from the requirements.txt
Requires: python-flask = 1:0.10.1
Requires: python-flask-wtf = 0.8.4
Requires: python-jinja2 = 2.7
Requires: python-markupsafe = 0.18
Requires: python-wtforms = 1.0.4
Requires: python-werkzeug = 0.9.6
Requires: python-itsdangerous = 0.24
Requires: python-pypuppetdb = 0.1.0
Requires: python-requests >= 2.3.0-PB
# to get it running with apache
Requires: httpd
Requires: mod_wsgi

%description
Puppetboard is a web interface to PuppetDB aiming to replace the reporting
functionality of Puppet Dashboard.
Puppetboard relies on the pypuppetdb library to fetch data from PuppetDB and
is built with the help of the Flask microframework.
Because this project is powered by Flask we are restricted to: pythin 2.x

%prep
%setup -q -n %{upstream_name}-%{version}
rm -r *.egg-info

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
# /var/www/puppetboard
mkdir -p %{buildroot}/var/www/%{upstream_name}/
cp %{buildroot}/%{python_sitelib}/%{upstream_name}/default_settings.py %{buildroot}/var/www/%{upstream_name}/settings.py
cat << EOF > %{buildroot}/var/www/puppetboard/wsgi.py
from __future__ import absolute_import
import os

# Needed if a settings.py file exists
os.environ['PUPPETBOARD_SETTINGS'] = '/var/www/puppetboard/settings.py'
from puppetboard.app import app as application
EOF

mkdir -p %{buildroot}/etc/httpd/conf.d
cat << EOFF > %{buildroot}/etc/httpd/conf.d/puppetboard.conf
DocumentRoot /var/www/puppetboard
WSGIDaemonProcess puppetboard user=apache group=apache threads=5
WSGIScriptAlias / /var/www/puppetboard/wsgi.py
Alias /static /usr/lib/python2.6/site-packages/puppetboard/static

<Directory /usr/lib/python2.6/site-packages/puppetboard>
    WSGIProcessGroup puppetboard
    WSGIApplicationGroup %{GLOBAL}
    Order deny,allow
    Allow from all
</Directory>
EOFF

%files
%doc LICENSE CHANGELOG.rst README.rst MANIFEST.in
%{python_sitelib}/%{upstream_name}/
%{python_sitelib}/%{upstream_name}*.egg-info
%config /etc/httpd/conf.d/puppetboard.conf
%config /var/www/puppetboard/wsgi.py
%ghost /var/www/puppetboard/wsgi.py[co]
%config /var/www/puppetboard/settings.py
%ghost /var/www/puppetboard/settings.py[co]

%changelog

* Fri Aug 01 2014 Martin Zehetmayer <angrox@idle.at>  - 0.0.4-3
- Added configuration files and requirements for apache webserver
- Added puppetboard directory and configuration files in /var/www/puppetboard

* Tue Feb 19 2014 Johan De Wit <johan@open-future.be> - 0.0.4-2
- Adjustment of the deplist.  Troubles with some python packages

* Tue Feb 11 2014 Johan De Wit <johan@open-future.be> - 0.0.4-1
- initial rpm package 0.0.4 
