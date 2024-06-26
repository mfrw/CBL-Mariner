%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

%bcond_without check
%define pkgname cherrypy
%define pypiname CherryPy

Summary:        A pythonic, object-oriented HTTP framework
Name:           python-%{pkgname}
Version:        18.6.1
Release:        1%{?dist}
License:        BSD
Url:            https://cherrypy.org/
Vendor:         Microsoft Corporation
Distribution:   Mariner
Source0:        https://pypi.io/packages/source/C/%{pypiname}/%{pypiname}-%{version}.tar.gz
BuildArch:      noarch

%global _description %{expand:
CherryPy allows developers to build web applications in much the same way they would
build any other object-oriented Python program. This results in smaller source code 
developed in less time.

CherryPy is now more than ten years old and it is has proven to be fast and reliable.
It is being used in production by many sites, from the simplest to the most demanding.}

%description %_description

%package -n python3-%{pkgname}
Summary:        A pythonic, object-oriented HTTP framework

BuildRequires:  python3-devel
BuildRequires:  python3-xml
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
Requires:       python3
Requires:       python3-libs
%if 0%{with check}
BuildRequires:  python3-pip
%endif

%description -n python3-%{pkgname}  %_description

%prep
%setup -q -n %{pypiname}-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot}

%if 0%{with check}
%check
pip3 install tox
tox -e py39
%endif

%files -n python3-%{pkgname}
%license LICENSE.md
%doc README.rst docs/
%{python3_sitelib}/*
%{_bindir}/cherryd

%changelog
* Tue Feb 08 2022 Muhammad Falak <mwani@microsoft.com> - 18.6.1-1
- Bump version to 18.6.1
- Use 'py39' as tox environment to enable ptest

* Fri Aug 21 2020 Thomas Crain <thcrain@microsoft.com> - 18.6.0-1
- Original version for CBL-Mariner
- License verified
