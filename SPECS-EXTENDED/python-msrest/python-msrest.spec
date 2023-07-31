Vendor:         Microsoft Corporation
Distribution:   Mariner
## START: Set by rpmautospec
## (rpmautospec version 0.3.1)
## RPMAUTOSPEC: autorelease, autochangelog
%define autorelease(e:s:pb:n) %{?-p:0.}%{lua:
    release_number = 1;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{!?-n:%{?dist}}
## END: Set by rpmautospec

# tests are enabled by default
%bcond_without  tests

%global         srcname     msrest
%global         forgeurl    https://github.com/Azure/msrest-for-python
Version:        0.7.1
# MSFT isn't making tags any longer in this repo for some reason.
%global         commit      2d8fd04f68a124d0f3df7b81584accc3270b1afc
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        The runtime library "msrest" for AutoRest generated Python clients
License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-packaging
BuildRequires:  python3-wheel

%if %{with tests}
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(trio)
%endif

%global _description %{expand:
The runtime library "msrest" for AutoRest generated Python clients}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import

%if %{with tests}
# Some tests require network connectivity, so they are skipped here.
%pytest \
    --ignore=tests/asynctests/test_pipeline.py \
    --ignore=tests/asynctests/test_universal_http.py \
    --ignore=tests/test_runtime.py
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
* Wed Mar 1 2023 Lakshmi Satya Sai Sindhu Karri <lakarri@microsoft.com> - 0.7.1-1
- Initial CBL-Mariner import from Fedora 37 (license: MIT)
- Added BR: python3-pip, python3-wheel and python3-packaging

* Fri Oct 14 2022 Major Hayden <major@redhat.com> - 0.7.1-1
- Update to 0.7.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 05 2022 Major Hayden <major@redhat.com> - 0.7.0-1
- Update to 0.7.0

* Wed Jun 22 2022 Major Hayden <major@redhat.com> - 0.6.21-10
- Add import check

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.6.21-9
- Rebuilt for Python 3.11

* Sat Apr 23 2022 Major Hayden <major@mhtx.net> - 0.6.21-8
- Disable HTTP tests that rely on httpretty

* Fri Apr 22 2022 Major Hayden <major@mhtx.net> - 0.6.21-6
- Overhaul with pyproject-rpm-macros/rpmautospec

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 06 2021 Major Hayden <major@mhtx.net> - 0.6.21-3
- Fix lato font requirement

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.21-2
- Rebuilt for Python 3.10

* Mon Feb 15 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.21-1
- Update to 0.6.21

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 09 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.19-1
- Update to 0.6.19

* Wed Jul 29 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.18-1
- Update to 0.6.18

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.17-1
- Update to 0.6.17

* Tue May 26 2020 Miro Hrončok <miro@hroncok.cz> - 0.6.13-2
- Rebuilt for Python 3.9

* Fri Apr 17 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.13-1
- Update to 0.6.13

* Fri Jan 31 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.11-1
- Update to 0.6.11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.10-1
- Update to 0.6.10

* Mon Aug 19 2019 Miro Hrončok <miro@hroncok.cz> - 0.6.9-2
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.9-1
- Update to 0.6.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.6-1
- Update to 0.6.6

* Mon Feb 04 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Tue Nov 13 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.1-7
- Fix typo in Requires for python-isodate

* Sun Nov 11 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.1-6
- Fix Requires for Fedora <= 27

* Sun Nov 11 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.1-5
- Fix comments

* Sat Nov 10 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.1-4
- Build doc & fix BuildRequires for Fedora <= 27

* Sat Nov 10 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.1-3
- Fix typo

* Sat Nov 10 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.1-2
- Enable dependency on python3-trio for Fedora >= 29 only

* Sat Nov 10 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Sun Aug 05 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.5.4-3
- Update patch for EPEL7

* Sun Aug 05 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.5.4-2
- Add missing dependencies

* Sun Aug 05 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.5.4-1
- Update to 0.5.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Mohamed El Morabity <melmorabity@fedoraproject.com> - 0.4.29-1
- Revert "Update to 0.5.0"

* Wed Jun 20 2018 Mohamed El Morabity <melmorabity@fedoraproject.com> - 0.5.0-1
- Update to 0.5.0

* Tue Jun 19 2018 Miro Hrončok <miro@hroncok.cz> - 0.4.29-2
- Rebuilt for Python 3.7

* Mon May 28 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.29-1
- Update to 0.4.29

* Tue Mar 20 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.27-1
- Update to 0.4.27

* Tue Feb 27 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 0.4.25-3
- Update Python 2 dependency declarations to new packaging standards

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.25-1
- Update to 0.4.25

* Fri Nov 10 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.18-1
- Update to 0.4.18

* Tue Oct 17 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.17-1
- Update to 0.4.17

* Fri Oct 06 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.16-1
- Update to 0.4.16

* Wed Aug 30 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.14-1
- Update to 0.4.14 - Use python2- prefix for Fedora dependencies if
  possible

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.11-1
- Update to 0.4.11

* Fri Jun 09 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.9-1
- Update to 0.4.9

* Tue May 30 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.8-2
- Disable version check on certifi in setup.py

* Tue May 30 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.8-1
- Update to 0.4.8

* Wed Apr 05 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.7-1
- Update to 0.4.7

* Tue Mar 07 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.6-2
- Update build patch for new release

* Tue Mar 07 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.6-1
- Update to 0.4.6

* Tue Feb 14 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.5-1
- First import
