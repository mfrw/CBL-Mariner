Vendor:         Microsoft Corporation
Distribution:   Mariner
## START: Set by rpmautospec
## (rpmautospec version 0.2.5)
%define autorelease(e:s:pb:) %{?-p:0.}%{lua:
    release_number = 7;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{?dist}
## END: Set by rpmautospec

# Enable tests everywhere except EPEL 9, where python-httpretty is not backported.
%if 0%{?rhel} >= 9
%bcond_with    tests
%else
%bcond_without tests
%endif


%global         srcname     adal
%global         forgeurl    https://github.com/AzureAD/azure-activedirectory-library-for-python
Version:        1.2.7
%global         tag         %{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Microsoft Azure Active Directory Authentication Library (ADAL) for Python

License:        MIT
URL:            %forgeurl
Source0:        %forgesource
# Fix tests with httpretty >= 0.9.0
Patch0:         %{name}-1.2.0-tests.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(httpretty)
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
Microsoft Azure Active Directory Authentication Library (ADAL) for Python.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%if %{with tests}
%check
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
* Wed May 04 2022 Stephen Gallagher <sgallagh@redhat.com> 1.2.7-7
- Use %rhel macro instead of %el9 and %centos

* Mon Apr 25 2022 Major Hayden <major@mhtx.net> 1.2.7-6
- Clean up spec file with pyproject-rpm-macros

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> 1.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> 1.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 06 2021 Major Hayden <major@mhtx.net> 1.2.7-3
- Fix lato font build requirement

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> 1.2.7-2
- Rebuilt for Python 3.10

* Thu Apr 22 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> 1.2.7-1
- Update to 1.2.7

* Mon Feb 15 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> 1.2.6-1
- Update to 1.2.6

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Tom Stellard <tstellar@redhat.com> 1.2.4-3
- Add BuildRequires: make

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> 1.2.4-1
- Update to 1.2.4 + spec cleanup

* Tue May 26 2020 Miro Hrončok <miro@hroncok.cz> 1.2.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <miro@hroncok.cz> 1.2.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <miro@hroncok.cz> 1.2.2-4
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Charalampos Stratakis <cstratak@redhat.com> 1.2.2-2
- Add sphinx_rtd_theme build dependency for docs generation (fix by
  Charalampos Stratakis)

* Fri Aug 09 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> 1.2.2-1
- Update to 1.2.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> 1.2.1-2
- RPMAUTOSPEC: unresolvable merge
