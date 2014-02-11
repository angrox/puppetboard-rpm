%global mod_name WTForms

Name:           python-wtforms
Version:        1.0.4
Release:        1%{?dist}
Summary:        Forms validation and rendering library for python

Group:          Development/Libraries
License:        BSD
URL:            http://wtforms.simplecodes.com/
Source0:        http://pypi.python.org/packages/source/W/%{mod_name}/%{mod_name}-%{version}.zip

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
With wtforms, your form field HTML can be generated for you. 
This allows you to maintain separation of code and presentation, 
and keep those messy parameters out of your python code.


%prep
%setup -q -n %{mod_name}-%{version}
sed -i "s|\r||g" docs/html/_sources/index.txt
sed -i "s|\r||g" docs/conf.py
sed -i "s|\r||g" CHANGES.txt
sed -i "s|\r||g" docs/Makefile
sed -i "s|\r||g" docs/index.rst
rm -f docs/html/.buildinfo

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

 
%files
%doc docs/ README.txt CHANGES.txt LICENSE.txt PKG-INFO
%{python_sitelib}/*.egg-info
%{python_sitelib}/wtforms/


%changelog
* Tue Feb 11 2014 Johan De Wit <johan@open-future.be> - 1.0.4-1
- Updated to version 1.0.4 - puppetboard

* Tue Aug 09 2012 Tim Flink <tflink@fedoraproject.org> - 1.0.2-1
- Upgraded to upstream 1.0.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.6.3-1
- Initial RPM release
