Vendor:         Microsoft Corporation
Distribution:   Mariner
%global github_owner    gabrielfalcao
%global github_name     HTTPretty
%global srcname         httpretty
# define these only if actually building from a GH snapshot not a release tarball
#global github_commit   70af1f8cf925ef50cb5e72212fb0aa46e1451dc3
#global shortcommit     %%(c=%%{github_commit}; echo ${c:0:7})
#global github_date     20161011

%global run_tests 1

Name:           python-httpretty
Version:        1.1.4
# If github_date is defined, assume a post-release snapshot
Release:        3%{?github_date:.%{github_date}git%{shortcommit}}%{?dist}
Summary:        HTTP request mock tool for Python

License:        MIT
URL:            https://github.com/%{github_owner}/%{github_name}
Source0:        %{pypi_source}
# Alternative for building from a github snapshot
#Source0:        https://github.com/%%{github_owner}/%%{github_name}/archive/%%{github_commit}/%%{github_name}-%%{shortcommit}.tar.gz

# Avoid unnecessary remote access requirement (note: test only actually
# does a remote connection after PR #313)
Patch1: python-httpretty-fakesock_getpeercert_noconnect.patch

# Remote access (these tests were skipped upstream in <= 0.9.7)
Patch2: skip-test_passthrough.patch

# Remove timeout, which causes some tests to fail in Koji
#
# Fixes RHBZ#2046877
Patch3: test_response-no-within.patch

BuildArch:      noarch

%global _description\
Once upon a time a python developer wanted to use a RESTful API, everything was\
fine but until the day he needed to test the code that hits the RESTful API:\
what if the API server is down? What if its content has changed?\
Don't worry, HTTPretty is here for you.

%description %_description

%package -n python3-httpretty
Summary:        HTTP request mock tool for Python 3
Requires:       python%{python3_pkgversion}-six

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# For tests
BuildRequires:  python%{python3_pkgversion}-httplib2
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-sure
BuildRequires:  python%{python3_pkgversion}-urllib3
BuildRequires:  python%{python3_pkgversion}-tornado
BuildRequires:  python%{python3_pkgversion}-eventlet
BuildRequires:  python%{python3_pkgversion}-freezegun
BuildRequires:  python%{python3_pkgversion}-redis

%description -n python3-httpretty
Once upon a time a python developer wanted to use a RESTful API, everything was
fine but until the day he needed to test the code that hits the RESTful API:
what if the API server is down? What if its content has changed?
Don't worry, HTTPretty is here for you.


%prep
%autosetup -n httpretty-%{version} -p1

# Alternative for building from commit tarball
#autosetup -n %%{github_name}-%%{github_commit} -p1

# nose plugins we don't have yet
sed -i 's/^with-randomly = 1$//' setup.cfg
sed -i 's/^rednose = 1$//' setup.cfg

%build
%py3_build

%install
%py3_install

%check
%if %{run_tests}
%{__python3} -m nose -v
%endif

%files -n python3-httpretty
%doc README.rst
%license COPYING
%{python3_sitelib}/httpretty
%{python3_sitelib}/httpretty-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Feb 04 2022 Jiri Popelka <jpopelka@redhat.com> 1.1.4-5
- Remove timeout, which causes some tests to fail in Koji (F36)

* Fri Feb 04 2022 Jiri Popelka <jpopelka@redhat.com> 1.1.4-4
- Drop Python 2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 19 2021 Jiri Popelka <jpopelka@redhat.com> - 1.1.4-1
- 1.1.4

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Miro Hrončok <mhroncok@redhat.com>
- Fallback to WARNING when logging.getLogger().level is None

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.3-2
- Rebuilt for Python 3.10

* Tue May 25 2021 Jiri Popelka <jpopelka@redhat.com> - 1.1.3-1
- 1.1.3

* Mon May 24 2021 Jiri Popelka <jpopelka@redhat.com> - 1.1.2-1
- 1.1.2

* Thu May 13 2021 Jiri Popelka <jpopelka@redhat.com> - 1.1.0-1
- 1.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Jiri Popelka <jpopelka@redhat.com> - 1.0.5-1
- 1.0.5
- Enable tests for F34 (#1896191 has been resolved)

* Tue Oct 13 2020 Jiri Popelka <jpopelka@redhat.com> - 1.0.2-4
- Temporarily run tests on Fedora < 34 only

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-2
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Jiri Popelka <jpopelka@redhat.com> - 1.0.2-1
- 1.0.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Charalampos Stratakis <cstratak@redhat.com> - 0.9.7-1
- Update to 0.9.7 (rhbz#1759992)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.6-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.6-3
- Rebuilt for Python 3.8

* Tue Aug 06 2019 Jiri Popelka <jpopelka@redhat.com> - 0.9.6-2
- Escape macro in comment

* Tue Jul 30 2019 Jiri Popelka <jpopelka@redhat.com> - 0.9.6-1
- Update to 0.9.6
- Disable python2 subpackage on F30+

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.5-4
- Drop explicit locale setting for python3, use C.UTF-8 for python2
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-2
- Rebuilt for Python 3.7

* Wed Jun 06 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-1
- Update to 0.9.5, fix for Python 3.7 (#1580060)

* Sat May 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-1
- Update to 0.9.4 (#1572888)

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.14-8.20161011git70af1f8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-7.20161011git70af1f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 0.8.14-6.20161011git70af1f8
- Cleanup spec file conditionals

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.14-5.20161011git70af1f8
- Python 2 binary package renamed to python2-httpretty
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-4.20161011git70af1f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-3.20161011git70af1f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Adam Williamson <awilliam@redhat.com> - 0.8.14-2.20161011git70af1f8
- Backport PR #317 (call reset from setUp / tearDown) - thanks gholms

* Fri Jan 06 2017 Adam Williamson <awilliam@redhat.com> - 0.8.14-1.20161011git70af1f8
- Update to current git master (as a 0.8.14 post-release snapshot)
- Backport PR #313 (fix with recent OpenSSL, requests and urllib3)
- Backport PR #314 (fix a test with Python 3)
- Backport PR #315 (fix some issues with urllib 1.10, as found in RHEL 6)
- Avoid an unnecessary remote roundtrip in one of the tests
- Replace dependency 'un-pinning' patch with some sed commands in the spec
- Replace ASCII patch by running setup.py with a UTF-8 LANG
- Enable the tests, with necessary buildrequires

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.8.3-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Jamie Lennox <jamielennox@redhat.com> - 0.8.3-3
- Added conditional __python2 macros for building on RHEL 6.

* Tue Feb 24 2015 Jamie Lennox <jamielennox@redhat.com> - 0.8.3-2
- Added with_python3 build flags to enable building on EPEL.

* Mon Jul 28 2014 Jamie Lennox <jamielennox@redhat.com> - 0.8.3-1
- Updated to new version.
- Removed check, there are simply too many problems upstream.

* Mon Mar 10 2014 Jamie Lennox <jamielennox@redhat.com> - 0.8.0-1
- Initial package.

