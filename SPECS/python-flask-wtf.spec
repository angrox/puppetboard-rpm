%global mod_name Flask-WTF

Name:           python-flask-wtf
Version:        0.8.4
Release:        1%{?dist}
Summary:        Simple integration of Flask and WTForms

Group:          Development/Libraries
License:        BSD
URL:            http://bitbucket.org/danjac/flask-wtf
Source0:        http://pypi.python.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-wtforms > 1.0
BuildRequires:  python-setuptools

Requires:   python-wtforms > 1.0
%description
Flask-WTF offers simple integration with WTForms. This integration 
includes optional CSRF handling for greater security.


%prep
%setup -q -n %{mod_name}-%{version}
rm -f docs/index.rst.orig

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc docs/ LICENSE PKG-INFO README 

%{python_sitelib}/*.egg-info/
%{python_sitelib}/flask_wtf/

%changelog
* Tue Feb 11 2014 Johan De Wit <johan@open-future.be> - 0.8.4-1
- Updated to version 0.8.4 - puppetboard

* Tue Oct 09 2012 Tim Flink <tflink@fedoraproject.org> - 0.8-1
- Upgrade to upstream 0.8

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 4 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.5.2-3
- Added python-wtforms as requires.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.5.2-1
- Initial RPM release
