Summary:        Query Language for JSON
Name:           python-jmespath
Version:        0.9.3
Release:        6%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/jmespath
Source0:        https://pypi.python.org/packages/e5/21/795b7549397735e911b032f255cff5fb0de58f96da794274660bca4f58ef/jmespath-%{version}.tar.gz
BuildArch:      noarch

%description
JMESPath (pronounced “james path”) allows you to declaratively specify how to extract elements from a JSON document.

%package -n     python3-jmespath
Summary:        Query Language for JSON
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
%if %{with_check}
BuildRequires:  python3-pip
BuildRequires:  curl-devel
BuildRequires:  openssl-devel
%endif
Requires:       python3
Requires:       python3-libs

%description -n python3-jmespath
JMESPath (pronounced “james path”) allows you to declaratively specify how to extract elements from a JSON document.

%prep
%autosetup -n jmespath-%{version}

%build
%py3_build

%install
%{py3_install "--single-version-externally-managed"}
ln -sfv jp.py %{buildroot}%{_bindir}/jp.py-%{python3_version}

%check
pip3 install nose
%python3 setup.py test

%files -n python3-jmespath
%defattr(-,root,root)
%license LICENSE.txt
%{python3_sitelib}/*
%{_bindir}/jp.py
%{_bindir}/jp.py-%{python3_version}

%changelog
* Fri Dec 03 2021 Thomas Crain <thcrain@microsoft.com> - 0.9.3-6
- Replace easy_install usage with pip in %%check sections

* Wed Oct 20 2021 Thomas Crain <thcrain@microsoft.com> - 0.9.3-5
- Add license to python3 package
- Remove python2 package,
- Lint spec
- License verified

* Sat May 09 2020 Nick Samson <nisamson@microsoft.com> - 0.9.3-4
- Added %%license line automatically

* Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> - 0.9.3-3
- Initial CBL-Mariner import from Photon (license: Apache2).

* Wed Nov 28 2018 Tapas Kundu <tkundu@vmware.com> - 0.9.3-2
- Fix make check
- moved the build requires from subpackages

* Sun Jan 07 2018 Kumar Kaushik <kaushikk@vmware.com> - 0.9.3-1
- Initial packaging for photon.
