Vendor:         Microsoft Corporation
Distribution:   Mariner
%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x5d2d1e4fb8d38e6af76c50d53d4fec30cf5ce3da

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name oslo.serialization
%global pkg_name oslo-serialization
%global with_doc 1

%global common_desc \
An OpenStack library for representing objects in transmittable and \
storable formats.

Name:           python-%{pkg_name}
Version:        4.1.0
Release:        4%{?dist}
Summary:        OpenStack oslo.serialization library

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

# Upstream patch to add compatibility with Python 3.10
Patch1:         https://github.com/openstack/oslo.serialization/commit/967a36fdbed5fc68e307fefc385ab2b8509a91e2.patch

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

%description
%{common_desc}

%package -n python3-%{pkg_name}
Summary:        OpenStack oslo.serialization library
%{?python_provide:%python_provide python3-%{pkg_name}}

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
# test requirements
BuildRequires:  python3-mock
BuildRequires:  python3-oslotest
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-stestr
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-msgpack >= 0.5.2
BuildRequires:  python3-netaddr
BuildRequires:  python3-simplejson

Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-msgpack >= 0.5.2
Requires:       python3-pytz
Requires:       python3-pbr >= 2.0.0

%description -n python3-%{pkg_name}
%{common_desc}


%package -n python3-%{pkg_name}-tests
Summary:   Tests for OpenStack Oslo serialization library
%{?python_provide:%python_provide python2-%{pkg_name}}

Requires:  python3-%{pkg_name} = %{version}-%{release}
Requires:  python3-mock
Requires:  python3-oslotest
Requires:  python3-oslo-i18n
Requires:  python3-stestr
Requires:  python3-netaddr
Requires:  python3-simplejson

%description -n python3-%{pkg_name}-tests
Tests for OpenStack Oslo serialization library

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo serialization library

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme

Requires:  python3-%{pkg_name} = %{version}-%{release}

%description -n python-%{pkg_name}-doc
Documentation for the Oslo serialization library.
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Let RPM handle the dependencies
rm -f requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# doc
sphinx-build-3 -W -b html doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%check
export OS_TEST_PATH="./oslo_serialization/tests"
PYTHON=python3 stestr-3 --test-path $OS_TEST_PATH run

%files -n python3-%{pkg_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/oslo_serialization
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/oslo_serialization/tests

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_serialization/tests

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.10

* Tue Mar 16 2021 Joel Capitao <jcapitao@redhat.com> 4.1.0-1
- Update to upstream version 4.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 4.0.1-2
- Update to upstream version 4.0.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 3.1.1-1
- Update to upstream version 3.1.1

* Mon Jun 01 2020 Alfredo Moralejo <amoralej@redhat.com> - 2.29.2-5
- Remove hacking as build requirement

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.29.2-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.29.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 2.29.2-2
- Update to upstream version 2.29.2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.28.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.28.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 RDO <dev@lists.rdoproject.org> 2.28.2-1
- Update to 2.28.2

