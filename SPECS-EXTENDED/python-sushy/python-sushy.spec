Vendor:         Microsoft Corporation
Distribution:   Mariner
%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x5d2d1e4fb8d38e6af76c50d53d4fec30cf5ce3da
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1
%global sname sushy

%global common_desc \
Sushy is a Python library to communicate with Redfish based systems (http://redfish.dmtf.org)

%global common_desc_tests Tests for Sushy

Name: python-%{sname}
Version: 3.7.0
Release: 5%{?dist}
Summary: Sushy is a Python library to communicate with Redfish based systems
License: ASL 2.0
URL: http://launchpad.net/%{sname}/

Source0: http://tarballs.openstack.org/%{sname}/%{sname}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.openstack.org/%{sname}/%{sname}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
# Remove when updating to 3.7.1 or newer
Patch0: 001-fix-python310.patch

BuildArch: noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

%description
%{common_desc}

%package -n python3-%{sname}
Summary: Sushy is a Python library to communicate with Redfish based systems
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires: git-core
BuildRequires: python3-devel
BuildRequires: python3-pbr
BuildRequires: python3-setuptools
# For running unit tests during check phase
BuildRequires: python3-requests
BuildRequires: python3-dateutil
BuildRequires: python3-stevedore

Requires: python3-dateutil >= 2.7.0
Requires: python3-pbr >= 2.0.0
Requires: python3-requests >= 2.14.2
Requires: python3-stevedore >= 1.29.0

%description -n python3-%{sname}
%{common_desc}

%package -n python3-%{sname}-tests
Summary: Sushy tests
Requires: python3-%{sname} = %{version}-%{release}

BuildRequires: python3-oslotest
BuildRequires: python3-testrepository
BuildRequires: python3-testscenarios
BuildRequires: python3-testtools

Requires: python3-oslotest
Requires: python3-testrepository
Requires: python3-testscenarios
Requires: python3-testtools

%description -n python3-%{sname}-tests
%{common_desc_tests}

%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary: Sushy documentation

BuildRequires: python3-sphinx
BuildRequires: python3-sphinxcontrib-apidoc
BuildRequires: python3-openstackdocstheme

%description -n python-%{sname}-doc
Documentation for Sushy
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{sname}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%check
%{__python3} setup.py test

%install
%{py3_install}

%files -n python3-%{sname}
%license LICENSE
%{python3_sitelib}/%{sname}
%{python3_sitelib}/%{sname}-*.egg-info
%exclude %{python3_sitelib}/%{sname}/tests

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{sname}/tests

%if 0%{?with_doc}
%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Dmitry Tantsur <divius.inside@gmail.com> - 3.7.0-3
- Cherry-pick fix for tests on Python 3.10 from future 3.7.1 (#1969148)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.7.0-2
- Rebuilt for Python 3.10

* Wed Mar 17 2021 Joel Capitao <jcapitao@redhat.com> 3.7.0-1
- Update to upstream version 3.7.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 3.4.1-2
- Update to upstream version 3.4.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 3.2.0-1
- Update to upstream version 3.2.0

* Tue May 26 2020 Dmitry Tantsur <divius.inside@gmail.com> - 2.0.3-1
- Update to 2.0.3 (#1808722)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 2.0.0-1
- Update to upstream version 2.0.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 Dmitry Tantsur <divius.inside@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Wed Feb 06 2019 Dmitry Tantsur <divius.inside@gmail.com> - 1.3.3-1
- Update to 1.3.3 to fix the UEFI boot mode issue

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.0-7
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Aug 16 2018 Javier Peña <jpena@redhat.com> - 1.2.0-6
- Fixed Rawhide build (bz#1605933)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.7

* Thu Feb 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 14 2017 Nathaniel Potter <nathaniel.potter@intel.com> 1.2.0-1
- Update for fedora packaging.
* Mon Mar 20 2017 Lucas Alvares Gomes <lucasagomes@gmail.com> 0.1.0-1
- Initial package.
