Vendor:         Microsoft Corporation
Distribution:   Mariner
# Created by pyp2rpm-1.1.1
%global pypi_name mox3

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
Mox3 is a mock object framework for Python 3 and 2.7. \
Mox3 is an unofficial port of the Google mox framework to Python 3. It was \
meant to be as compatible with mox as possible, but small enhancements have \
been made.

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        5%{?dist}
Summary:        Mock object framework for Python

License:        ASL 2.0
URL:            http://git.openstack.org/cgit/openstack/mox3
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch


%description
%{common_desc}

%package -n     python3-%{pypi_name}
Summary:        Mock object framework for Python
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:  python3-pbr
Requires:  python3-fixtures
Requires:  python3-six >= 1.9.0
Requires:  python3-testtools

BuildRequires:  python3-devel
BuildRequires:  python3-pbr

# test requires
BuildRequires:  python3-fixtures
BuildRequires:  python3-stestr
BuildRequires:  python3-subunit
BuildRequires:  python3-testtools
BuildRequires:  python3-six >= 1.9.0

%description -n python3-%{pypi_name}
%{common_desc}

%prep
%autosetup -p1 -n %{pypi_name}-%{upstream_version}

# let RPM handle deps
rm -rf *requirements.txt

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root %{buildroot}

%check
PYTHON=python3 stestr-3 run

%files -n python3-%{pypi_name}
%doc README.rst
%license COPYING.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*.egg-info

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Alfredo Moralejo <amoralej@redhat.com> 1.1.0-1
- Update to upstream version 1.1.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 1.0.0-1
- Update to upstream version 1.0.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.28.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 0.28.0-2
- Update to upstream version 0.28.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.27.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.27.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 RDO <dev@lists.rdoproject.org> 0.27.0-1
- Update to 0.27.0

