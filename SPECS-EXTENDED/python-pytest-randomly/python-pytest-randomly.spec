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

%global upstream_name pytest-randomly

Name:           python-%{upstream_name}
Version:        3.11.0
Release:        %autorelease
Summary:        Pytest plugin to randomly order tests and control random.seed
License:        MIT
URL:            https://github.com/pytest-dev/pytest-randomly
Source0:        %{url}/archive/%{version}/%{upstream_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# Required for tests
BuildRequires:  python3dist(factory-boy)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pytest-forked)
BuildRequires:  python3dist(pytest-xdist)

%description
%{summary}.

%package -n     python3-%{upstream_name}
Summary:        %{summary}

%description -n python3-%{upstream_name}
%{summary}.

%prep
%autosetup -n %{upstream_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_randomly

%check
%pytest -p no:randomly -k 'not test_it_runs_before_stepwise'

%files -n python3-%{upstream_name} -f %{pyproject_files}
%doc README.rst HISTORY.rst
%license LICENSE

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Mikel Olasagasti Uranga <mikel@olasagasti.info> 3.11.0-1
- Update to 3.11.0 - Closes rhbz#2038996

* Sat Nov 06 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 3.10.1-1
- Update to 3.10.1
- Switch to pyproject-rpm-macros

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 3.5.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 12 2020 Dan Callaghan <djc@djc.id.au> - 3.5.0-1
- new upstream release 3.5.0, including license change to MIT:
  https://github.com/pytest-dev/pytest-randomly/blob/3.5.0/HISTORY.rst

* Thu Aug 20 2020 Merlin Mathesius <mmathesi@redhat.com> - 3.4.1-4
- Fix Rawhide FTBFS error by pulling in upstream patch
- Fix ELN FTBFS error by making minor conditional fixes

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Dan Callaghan <djc@djc.id.au> - 3.4.1-2
- skip tests for optional faker integration when it is not available

* Wed Jul 15 2020 Dan Callaghan <djc@djc.id.au> - 3.4.1-1
- new upstream release 3.4.1:
  https://github.com/pytest-dev/pytest-randomly/blob/3.4.1/HISTORY.rst

* Sat Jun 13 2020 Dan Callaghan <djc@djc.id.au> - 3.4.0-1
- new upstream release 3.4.0:
  https://github.com/pytest-dev/pytest-randomly/blob/3.4.0/HISTORY.rst

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Dan Callaghan <dan.callaghan@opengear.com> - 3.3.1-1
- new upstream release 3.3.1:
  https://github.com/pytest-dev/pytest-randomly/blob/3.3.1/HISTORY.rst

* Thu Jan 30 2020 Dan Callaghan <dan.callaghan@opengear.com> - 3.2.1-1
- new upstream release 3.2.1

* Mon Dec 30 2019 Dan Callaghan <dan.callaghan@opengear.com> - 1.2.3-2
- re-enabled tests, suppress pytest bytecode

* Mon Dec 31 2018 Dan Callaghan <dan.callaghan@opengear.com> - 1.2.3-1
- initial version

