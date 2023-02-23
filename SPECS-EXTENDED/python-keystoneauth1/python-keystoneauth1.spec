Vendor:         Microsoft Corporation
Distribution:   Mariner
%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x5d2d1e4fb8d38e6af76c50d53d4fec30cf5ce3da
%global pypi_name keystoneauth1

%global common_desc \
Keystoneauth provides a standard way to do authentication and service requests \
within the OpenStack ecosystem. It is designed for use in conjunction with \
the existing OpenStack clients and for simplifying the process of writing \
new clients.

%global with_doc 1

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:       python-%{pypi_name}
Version:    4.3.1
Release:    4%{?dist}
Summary:    Authentication Library for OpenStack Clients
License:    ASL 2.0
URL:        https://pypi.io/pypi/%{pypi_name}
Source0:    https://tarballs.openstack.org/keystoneauth/keystoneauth1-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/keystoneauth/keystoneauth1-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

%description
%{common_desc}

%package -n     python3-%{pypi_name}
Summary:        Authentication Libarary for OpenStack Identity
%{?python_provide:%python_provide python3-%{pypi_name}}
%{?python_provide:%python_provide python3-keystoneauth}

BuildRequires: git-core
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-six
BuildRequires: python3-pbr >= 2.0.0

# test requires
BuildRequires: python3-betamax >= 0.7.0
BuildRequires: python3-fixtures >= 1.3.1
BuildRequires: python3-mock
BuildRequires: python3-oslotest
BuildRequires: python3-oslo-config
BuildRequires: python3-oslo-utils
BuildRequires: python3-stestr
BuildRequires: python3-oauthlib
BuildRequires: python3-requests
BuildRequires: python3-os-service-types
BuildRequires: python3-stevedore
BuildRequires: python3-iso8601
BuildRequires: python3-requests-mock >= 1.1

BuildRequires: python3-PyYAML
BuildRequires: python3-lxml
BuildRequires: python3-requests-kerberos

Requires:      python3-iso8601 >= 0.1.11
Requires:      python3-os-service-types >= 1.2.0
Requires:      python3-pbr >= 2.0.0
Requires:      python3-requests >= 2.14.2
Requires:      python3-six => 1.10.0
Requires:      python3-stevedore >= 1.20.0

%description -n python3-%{pypi_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:    Documentation for OpenStack Identity Authentication Library

BuildRequires: python3-sphinx
BuildRequires: python3-sphinxcontrib-apidoc
BuildRequires: python3-openstackdocstheme
BuildRequires: python3-mox3

%description -n python-%{pypi_name}-doc
Documentation for OpenStack Identity Authentication Library
%endif


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git

sed -i '/sphinx.ext.intersphinx.*$/d'  doc/source/conf.py

# Let RPM handle the dependencies
rm -rf {test-,}requirements.txt
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# remove syntax tests
rm keystoneauth1/tests/unit/test_hacking_checks.py

%build
%{py3_build}

%install
%{py3_install}

%if 0%{?with_doc}
# generate html docs
export PYTHONPATH=.
# Disabling warning-is-error because of issue with python2 giving a warning:
# "The config value `apidoc_module_dir' has type `unicode', expected to ['str']."
sphinx-build-3 -b html -d doc/build/doctrees doc/source doc/build/html
rm -rf doc/build/html/.buildinfo
%endif

%check
PYTHON=%{__python3} stestr-3 run

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/*.egg-info

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc doc/build/html
%endif

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.3.1-2
- Rebuilt for Python 3.10

* Wed Mar 17 2021 Joel Capitao <jcapitao@redhat.com> 4.3.1-1
- Update to upstream version 4.3.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 4.2.1-2
- Update to upstream version 4.2.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 4.0.0-1
- Update to upstream version 4.0.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.17.2-2
- Rebuilt for Python 3.9

* Mon May 04 2020 Javier Peña <jpena@redhat.com> - 3.17.2-1
- Update to upstream version 3.17.2 (bz#1830974)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Alfredo Moralejo <amoralej@redhat.com> 3.17.1-2
- Update to upstream version 3.17.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.13.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.13.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 RDO <dev@lists.rdoproject.org> 3.13.1-1
- Update to 3.13.1

