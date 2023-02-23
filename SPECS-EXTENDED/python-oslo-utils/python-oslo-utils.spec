Vendor:         Microsoft Corporation
Distribution:   Mariner
%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x5d2d1e4fb8d38e6af76c50d53d4fec30cf5ce3da
%global pypi_name oslo.utils
%global pkg_name oslo-utils
%global with_doc 1

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
The OpenStack Oslo Utility library. \
* Documentation: http://docs.openstack.org/developer/oslo.utils \
* Source: http://git.openstack.org/cgit/openstack/oslo.utils \
* Bugs: http://bugs.launchpad.net/oslo

%global common_desc_tests Tests for the Oslo Utility library.

Name:           python-oslo-utils
Version:        4.8.0
Release:        4%{?dist}
Summary:        OpenStack Oslo Utility library

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
Patch001:       0001-Switch_to_collections_abc.patch
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core

%description
%{common_desc}

%package -n python3-%{pkg_name}
Summary:    OpenStack Oslo Utility library
%{?python_provide:%python_provide python3-%{pkg_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-iso8601
BuildRequires:  python3-debtcollector
# test requirements
BuildRequires:  python3-eventlet
BuildRequires:  python3-hacking
BuildRequires:  python3-fixtures
BuildRequires:  python3-oslotest
BuildRequires:  python3-testtools
BuildRequires:  python3-ddt
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-pyparsing
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testrepository
BuildRequires:  python3-netaddr
BuildRequires:  python3-packaging
BuildRequires:  python3-yaml
# Required to compile translation files
BuildRequires:  python3-babel
BuildRequires:  python3-netifaces
BuildRequires:  python3-pytz

Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-iso8601
Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-pyparsing
Requires:       python3-netaddr >= 0.7.18
Requires:       python3-pytz
Requires:       python3-netifaces >= 0.10.4
Requires:       python3-packaging >= 20.4
Requires:       python-%{pkg_name}-lang = %{version}-%{release}
Requires:       python3-pbr >= 2.0.0

%description -n python3-%{pkg_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo Utility library

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-%{pkg_name}-doc
Documentation for the Oslo Utility library.
%endif

%package -n python3-%{pkg_name}-tests
Summary:    Tests for the Oslo Utility library

Requires: python3-%{pkg_name} = %{version}-%{release}
Requires: python3-eventlet
Requires: python3-hacking
Requires: python3-fixtures
Requires: python3-oslotest
Requires: python3-testtools
Requires: python3-ddt
Requires: python3-testscenarios
Requires: python3-testrepository

%description -n python3-%{pkg_name}-tests
%{common_desc_tests}

%package  -n python-%{pkg_name}-lang
Summary:   Translation files for Oslo utils library

%description -n python-%{pkg_name}-lang
Translation files for Oslo utils library

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# Let RPM handle the dependencies
rm -rf *requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 -W -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

# Generate i18n files
python3 setup.py compile_catalog -d build/lib/oslo_utils/locale --domain oslo_utils

%install
%{py3_install}

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{python3_sitelib}/oslo_utils/locale/*/LC_*/oslo_utils*po
rm -f %{buildroot}%{python3_sitelib}/oslo_utils/locale/*pot
mv %{buildroot}%{python3_sitelib}/oslo_utils/locale %{buildroot}%{_datadir}/locale

# Find language files
%find_lang oslo_utils --all-name

%check
python3 setup.py test

%files -n python3-%{pkg_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/oslo_utils
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/oslo_utils/tests

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_utils/tests

%files -n python-%{pkg_name}-lang -f oslo_utils.lang
%license LICENSE

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.8.0-2
- Rebuilt for Python 3.10

* Mon Mar 22 2021 Joel Capitao <jcapitao@redhat.com> 4.8.0-1
- Update to upstream version 4.8.0

* Wed Feb 10 2021 Charalampos Stratakis <cstratak@redhat.com> - 4.6.0-4
- Remove redundant python-funcsigs depdendency

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 21 2020 Joel Capitao <jcapitao@redhat.com> 4.6.0-2
- Enable sources tarball validation using GPG signature.

* Thu Sep 17 2020 RDO <dev@lists.rdoproject.org> 4.6.0-1
- Update to 4.6.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Joel Capitao <jcapitao@redhat.com> 4.1.1-1
- Update to upstream version 4.1.1

* Mon Jun 01 2020 Javier Peña <jpena@redhat.com> - 3.41.1-5
- Remove python-hacking from requirements, it is not actually needed for the build

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.41.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.41.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Alfredo Moralejo <amoralej@redhat.com> 3.41.1-2
- Update to upstream version 3.41.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.40.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Alfredo Moralejo <amoralej@redhat.com> 3.40.3-4
- Add digestmod when using hmac - Resolves rhbz#1743899
- Disabled failing unit test with python 3.8.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.40.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 RDO <dev@lists.rdoproject.org> 3.40.3-1
- Update to 3.40.3

