Summary:        Applying JSON Patches in Python
Name:           python-jsonpointer
Version:        2.0
Release:        4%{?dist}
License:        BSD
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages/Python
URL:            https://pypi.org/project/jsonpointer/
Source0:        https://pypi.python.org/packages/source/j/jsonpointer/jsonpointer-%{version}.tar.gz
BuildArch:      noarch

%description
Library to apply JSON Patches according to RFC 6902.

%package -n     python3-jsonpointer
Summary:        Applying JSON Patches in Python
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
Requires:       python3

%description -n python3-jsonpointer
Library to apply JSON Patches according to RFC 6902.

%prep
%autosetup -n jsonpointer-%{version}

%build
%py3_build

%install
%py3_install
ln -s jsonpointer %{buildroot}%{_bindir}/jsonpointer3

%check
%python3 tests.py

%files -n python3-jsonpointer
%defattr(-,root,root,-)
%license LICENSE.txt
%{python3_sitelib}/*
%{_bindir}/jsonpointer
%{_bindir}/jsonpointer3

%changelog
* Wed Oct 20 2021 Thomas Crain <thcrain@microsoft.com> - 2.0-4
- Add license to python3 package
- Remove python2 package
- Lint spec

* Sat May 09 2020 Nick Samson <nisamson@microsoft.com> - 2.0-3
- Added %%license line automatically

* Fri Apr 24 2020 Andrew Phelps <anphel@microsoft.com> - 2.0-2
- Initial CBL-Mariner import from Photon (license: Apache2).
- Updated Source0 and URL. Remove sha1 definition. Verified license.

* Sun Sep 09 2018 Tapas Kundu <tkundu@vmware.com> - 2.0-1
- Update to version 2.0

* Wed Jun 07 2017 Xiaolin Li <xiaolinl@vmware.com> - 1.10-6
- Add python3-setuptools and python3-xml to python3 sub package Buildrequires.

* Wed Apr 26 2017 Sarah Choi <sarahc@vmware.com> - 1.10-5
- Rename jsonpointer for python3

* Thu Apr 06 2017 Sarah Choi <sarahc@vmware.com> - 1.10-4
- support python3

* Tue Oct 04 2016 ChangLee <changlee@vmware.com> - 1.10-3
- Modified %check

* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> - 1.10-2
- GA - Bump release of all rpms

* Tue Feb 23 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> - 1.10-1
- Updated to version 1.10

* Wed Mar 04 2015 Mahmoud Bassiouny <mbassiouny@vmware.com>
- Initial packaging for Photon
