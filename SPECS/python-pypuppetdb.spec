%global upstream_name pypuppetdb

Name:           python-%{upstream_name}
Version:        0.1.0
Release:        1%{?dist}
Summary:        pypuppetdtb is a library to work with PuppetDB's REST AP
License:        Apache v2.0 License
URL:            https://github.com/nedap/pypuppetdb
Source0:        http://pypi.python.org/packages/source/p/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
pypuppetdtb is a library to work with PuppetDB's REST API. It is implemented using the requests library.

This library is a thin wrapper around the REST API providing some convinience functions and objects to
request and hold data from PuppetDB.

%prep
%setup -q -n %{upstream_name}-%{version}
rm -r *.egg-info

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc CHANGELOG.rst LICENSE MANIFEST.in PKG-INFO README.rst
%{python_sitelib}/%{upstream_name}
%{python_sitelib}/%{upstream_name}*.egg-info

%changelog
* Tue Feb 11 2014 Johan De Wit <johan@open-future.be> - 1.0.1-1
- initial rpm package 1.0.1 - puppetboard 
