%global upstream_name puppetboard

Name:           python-%{upstream_name}
Version:        0.0.4
Release:        1%{?dist}
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
Requires: python-jinja2-27 = 2.7
Requires: python-markupsafe = 0.18
Requires: python-wtforms = 1.0.4
Requires: python-werkzeug = 0.9.3
Requires: python-itsdangerous = 0.22
Requires: python-pypuppetdb = 0.1.0
Requires: python-requests = 1.2.3

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

%files
%doc LICENSE CHANGELOG.rst README.rst MANIFEST.in
%{python_sitelib}/%{upstream_name}/
%{python_sitelib}/%{upstream_name}*.egg-info

%changelog
* Tue Feb 11 2014 Johan De Wit <johan@open-future.be> - 0.0.4-1
- initial rpm package 0.0.4 
