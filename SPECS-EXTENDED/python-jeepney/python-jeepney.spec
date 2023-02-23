Vendor:         Microsoft Corporation
Distribution:   Mariner
## START: Set by rpmautospec
## (rpmautospec version 0.2.5)
%define autorelease(e:s:pb:) %{?-p:0.}%{lua:
    release_number = 2;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{?dist}
## END: Set by rpmautospec

%global pypi_name jeepney

Name:           python-%{pypi_name}
Version:        0.7.1
Release:        %autorelease
Summary:        Low-level, pure Python DBus protocol wrapper
License:        MIT
URL:            https://gitlab.com/takluyver/jeepney
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires: make
BuildRequires:  python3-async-timeout
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-trio
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-testpath
BuildRequires:  python3-trio

%description
This is a low-level, pure Python DBus protocol client. It has an I/O-free core,
and integration modules for different event loops.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a low-level, pure Python DBus protocol client. It has an I/O-free core,
and integration modules for different event loops.


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

make -C docs SPHINXBUILD=sphinx-build-3 html
rm -rf docs/_build/html/{.buildinfo,_sources}

%install
%py3_install

%check
%{__python3} -m pytest -v

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst examples/ docs/_build/html/
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 Göran Uddeborg <goeran@uddeborg.se> 0.7.1-1
- Upgrade to 0.7.1 (#1987023)

* Tue Aug 03 2021 Göran Uddeborg <goeran@uddeborg.se> 0.7.0-4
- Activate autorelease

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Göran Uddeborg <goeran@uddeborg.se> - 0.7.0-1
- Upgrade to 0.7.0 (#1981018)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Joel Capitao <jcapitao@redhat.com> - 0.6.0-1
- Update to 0.6.0 (#1899516)

* Sun Nov 15 2020 Göran Uddeborg <goeran@uddeborg.se> - 0.5.0-1
- Upgrade to 0.5.0 (#1896570)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-2
- Rebuilt for Python 3.9

* Wed Mar  4 2020 Göran Uddeborg <goeran@uddeborg.se> - 0.4.3-1
- Upgrade to 0.4.3 (#1809631)

* Thu Feb 13 2020 Christopher Tubbs <ctubbsii@fedoraproject.org> - 0.4.2-1
- Upgrade to 0.4.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Göran Uddeborg <goeran@uddeborg.se> - 0.4.1-1
- Upgrade to 0.4.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-1
- Initial package

