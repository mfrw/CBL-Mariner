Vendor:         Microsoft Corporation
Distribution:   Mariner
%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%global pypi_name oslotest
%global repo_bootstrap 1

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?repo_bootstrap} == 0
%global with_doc 1
%else
%global with_doc 0
%endif

%global common_desc OpenStack test framework and test fixtures.

Name:           python-%{pypi_name}
Version:        4.4.1
Release:        6%{?dist}
Summary:        OpenStack test framework

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:        OpenStack test framework
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools


# test requires
BuildRequires:  python3-six
BuildRequires:  python3-stestr
%if 0%{?repo_bootstrap} == 0
BuildRequires:  python3-oslo-config
%endif

Requires: python3-fixtures
Requires: python3-six
Requires: python3-subunit
Requires: python3-testtools
Requires: python3-mock


%description -n python3-%{pypi_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        Documentation for the OpenStack test framework

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-%{pypi_name}-doc
%{common_desc} Documentation
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# let RPM handle deps
rm -rf {test-,}requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%check
%if 0%{?repo_bootstrap} == 0
python3 setup.py test
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%{_bindir}/oslo_run_cross_tests
%{_bindir}/oslo_run_pre_release_tests
%{_bindir}/oslo_debug_helper
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*.egg-info

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc doc/build/html
%doc README.rst
%endif

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.4.1-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 4.4.1-2
- Update to upstream version 4.4.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 4.2.0-1
- Update to upstream version 4.2.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.8.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 3.8.1-2
- Update to upstream version 3.8.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.7.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.7.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 RDO <dev@lists.rdoproject.org> 3.7.1-1
- Update to 3.7.1

