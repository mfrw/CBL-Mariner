Vendor:         Microsoft Corporation
Distribution:   Mariner
%global modname eventlet
%global bundle_dns 0
%{?python_enable_dependency_generator}

Name:           python-%{modname}
Version:        0.33.0
Release:        2%{?dist}
Summary:        Highly concurrent networking library
%if %bundle_dns
License:        MIT and ISC
%else
License:        MIT
%endif

URL:            http://eventlet.net
Source0:        https://github.com/eventlet/%{modname}/archive/v%{version}.zip
Source1:        %{pypi_source dnspython 1.16.0 zip}
Patch0:         switch_to_python_cryptography.patch

# Since Python 3.10 MutableMapping is available in collections.abc instead of collections.
# This is already fixed in dnspython 2.0.0+, but eventlet still uses old 1.16.0.
Patch1:         0001-import-MutableMapping-from-collections.abc.patch

BuildArch:      noarch

%description
Eventlet is a networking library written in Python. It achieves high
scalability by using non-blocking io while at the same time retaining
high programmer usability by using coroutines to make the non-blocking
io operations appear blocking at the source code level.

%package -n python3-%{modname}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(greenlet) >= 0.3
BuildRequires:  python3dist(monotonic) >= 1.4
BuildRequires:  python3dist(six) >= 1.10
BuildRequires:  python3-nose
BuildRequires:  python3-pyOpenSSL

%if %bundle_dns
Provides:       bundled(python3dist(dnspython)) = 1.16.0
BuildRequires:  python3-cryptography
Recommends:     python3-cryptography
%else
BuildRequires:  python3dist(dnspython) >= 1.15
BuildRequires:  python3dist(dnspython) < 3
%endif

%{?python_provide:%python_provide python3-%{modname}}


%description -n python3-%{modname}
Eventlet is a networking library written in Python. It achieves high
scalability by using non-blocking io while at the same time retaining
high programmer usability by using coroutines to make the non-blocking
io operations appear blocking at the source code level.

%package -n python3-%{modname}-doc
Summary:        Documentation for python3-%{modname}
BuildRequires:  python3-sphinx
BuildRequires:  python3-zmq

%description -n python3-%{modname}-doc
%{summary}.

%prep
%if %bundle_dns
%setup -n %{modname}-%{version} -q -a1
%else
%setup -n %{modname}-%{version} -q
%endif
# Remove dependency on enum-compat from setup.py
# enum-compat is not needed for Python 3
sed -i "/'enum-compat',/d" setup.py
%if %bundle_dns
# We bundle last version of dns1 as eventlet does not support yet dns2
pushd dnspython-1.16.0
%patch -P 0 -p1
%patch -P 1 -p1
grep -lRZ "dns\." dns | xargs -0 -l sed -i -e 's/\([^[a-zA-Z]\)dns\./\1eventlet\.dns\./g'
grep -lRZ "^import dns$" dns | xargs -0 -l sed -i -e 's/^import\ dns$/import\ eventlet\.dns/'
popd
mv dnspython-1.16.0/dns eventlet
sed -i '/dnspython >= 1.15.0, < 2.0.0/d' setup.py
sed -i "s/import_patched('dns/import_patched('eventlet\.dns/g" eventlet/support/greendns.py
cp -a dnspython-1.16.0/LICENSE LICENSE.dns
rm -vrf dnspython-1.16.0
%endif
rm -vrf *.egg-info

%build
%py3_build

# Disable setting up dns (we have no /etc/resolv.conf in mock
export EVENTLET_NO_GREENDNS=yes
export PYTHONPATH=$(pwd)
sphinx-build-%{python3_version} -b html -d doctrees doc html-3

%install
%py3_install
rm -vrf %{buildroot}%{python3_sitelib}/tests

%check
# Disable setting up dns (we have no /etc/resolv.conf in mock
export EVENTLET_NO_GREENDNS=yes
# Tests are written only for Python 3
nosetests-%{python3_version} -v -e greendns_test -e socket_test -e test_patcher_existing_locks_locked -e test_017_ssl_zeroreturnerror

%files -n python3-%{modname}
%doc README.rst AUTHORS LICENSE NEWS
%license LICENSE
%if %bundle_dns
%license LICENSE.dns
%endif
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-*.egg-info/

%files -n python3-%{modname}-doc
%license LICENSE
%doc html-3

%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Kevin Fenzi <kevin@scrye.com> - 0.33.0-1
- Update to 0.33.0. Fixes rhbz#2023953

* Tue Oct 05 2021 Lumír Balhar <lbalhar@redhat.com> - 0.32.0-2
- Unbundle dnspython

* Sat Sep 25 2021 Kevin Fenzi <kevin@scrye.com> - 0.32.0-1
- Update to 0.32.0. Fixes rhbz#2000093

* Fri Jul 30 2021 Kevin Fenzi <kevin@scrye.com> - 0.31.1-1
- Update to 0.31.1. Fixes rhbz#1981430
- Fix FTBFS rhbz#1981320

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Tomas Hrnciar <thrnciar@redhat.com> - 0.31.0-3
- Backport upstream patch to add compatibility of Eventlet with Python 3.10
- Fixes: rhbz#1913291

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.31.0-2
- Rebuilt for Python 3.10

* Sun May 16 2021 Kevin Fenzi <kevin@scrye.com> - 0.31.0-1
- Update to 0.31.0. Fixes rhbz#1957249
- Mitigates CVE-2021-21419

* Sun Mar 07 2021 Kevin Fenzi <kevin@scrye.com> - 0.30.2-1
- Update to 0.30.2. Fixes rhbz#1934511

* Sun Feb 07 2021 Kevin Fenzi <kevin@scrye.com> - 0.30.1-1
- Update to 0.30.1. Fixes rhbz#1923933

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Kevin Fenzi <kevin@scrye.com> - 0.30.0-1
- Update to 0.30.0. (rhbz#1907221)

* Mon Nov 30 2020 Joel Capitao <jcapitao@redhat.com> - 0.29.1-2.20201102git087ba743
- Bundle dns1 (rhbz#1896191)

* Fri Nov 06 2020 Joel Capitao <jcapitao@redhat.com> - 0.29.1-1.20201102git087ba743
- Update to 0.29.1.20201102git087ba743. (rhbz#1862178)

* Sat Oct 10 2020 Kevin Fenzi <kevin@scrye.com> - 0.26.0-1
- Update to 0.26.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.25.2-2
- Rebuilt for Python 3.9

* Sat Apr 18 2020 Kevin Fenzi <kevin@scrye.com> - 0.25.2-1
- Update to 0.25.2. Fixes bug #1822602

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Miro Hrončok <mhroncok@redhat.com> - 0.25.1-2
- Subpackage python2-eventlet has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Aug 22 2019 Kevin Fenzi <kevin@scrye.com> - 0.25.1-1
- Update to 0.25.1. Fixes bug #1744357

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.25.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Kevin Fenzi <kevin@scrye.com> - 0.25.0-1
- Update to 0.25.0. Fixes bug #1713639

* Sat Mar 09 2019 Kevin Fenzi <kevin@scrye.com> - 0.24.1-4
- Drop python2-eventlet-doc subpackage as python2-sphinx is going away.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.24.1-2
- use python dependency generator

* Sun Oct 14 2018 Kevin Fenzi <kevin@scrye.com> - 0.24.1-1
- Update to 0.24.1. Fixes bug #1611023

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Miro Hrončok <mhroncok@redhat.com> - 0.23.0-1
- Update to 0.23.0 (#1575434)
- Add patch for Python 3.7 (#1594248)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.22.1-2
- Rebuilt for Python 3.7

* Sun Feb 18 2018 Kevin Fenzi <kevin@scrye.com> - 0.22.1-1
- Update to 0.22.1. Fixes bug #1546471

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.0-1
- Update to 0.22.0

* Tue Oct  3 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.21.0-3
- Fix upstream #401
- Fix compat with PyOpenSSL 17.3.0
- Cleanup BR

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Lumír Balhar <lbalhar@redhat.com> - 0.21.0-1
- Upstream 0.21.0
- Fix issue with enum-compat dependency for dependent packages
- Enable tests
- Fix tracebacks during docs generating by install python[23]-zmq

* Tue Apr 25 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.20.1-1
- Upstream 0.20.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.18.4-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.4-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 25 2016 Kevin Fenzi <kevin@scrye.com> - 0.18.4-1
- Update to 0.18.4. Fixes bug #1329993

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.4-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 19 2015 Jon Schlueter <jschluet@redhat.com> 0.17.4-4
- greenio: send() was running empty loop on ENOTCONN rhbz#1268351

* Thu Sep 03 2015 Pádraig Brady <pbrady@redhat.com> - 0.17.4-3
- Tighten up Provides: and Obsoletes: for previous change

* Tue Sep 01 2015 Chandan Kumar <chkumar246@gmail.com> - 0.17.4-2
- Added python3 support

* Wed Jul 22 2015 Pádraig Brady <pbrady@redhat.com> - 0.17.4-1
- Latest upstream

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Pádraig Brady <pbrady@redhat.com> - 0.17.3-1
- Latest upstream

* Tue Mar 31 2015 Pádraig Brady <pbrady@redhat.com> - 0.17.1-1
- Latest upstream

* Tue Sep 02 2014 Pádraig Brady <pbrady@redhat.com> - 0.15.2-1
- Latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 28 2013 Alan Pevec <apevec@redhat.com> - 0.14.0-1
- Update to 0.14.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 20 2013 Pádraig Brady <P@draigBrady.com - 0.12.0-1
- Update to 0.12.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Pádraig Brady <P@draigBrady.com - 0.9.17-2
- fix waitpid() override to not return immediately

* Fri Aug 03 2012 Pádraig Brady <P@draigBrady.com - 0.9.17-1
- Update to 0.9.17

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 27 2012 Pádraig Brady <P@draigBrady.com - 0.9.16-6
- Update patch to avoid leak of _DummyThread objects

* Mon Mar  5 2012 Pádraig Brady <P@draigBrady.com - 0.9.16-5
- Fix patch to avoid leak of _DummyThread objects

* Wed Feb 29 2012 Pádraig Brady <P@draigBrady.com - 0.9.16-4
- Apply a patch to avoid leak of _DummyThread objects

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Pádraig Brady <P@draigBrady.com - 0.9.16-2
- Apply a patch to support subprocess.Popen implementations
  that accept the timeout parameter, which is the case on RHEL >= 6.1

* Sat Aug 27 2011 Kevin Fenzi <kevin@scrye.com> - 0.9.16-1
- Update to 0.9.16

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 08 2010 Lev Shamardin <shamardin@gmail.com> - 0.9.12-1
- Updated to version 0.9.12.

* Wed Jul 28 2010 Lev Shamardin <shamardin@gmail.com> - 0.9.9-1
- Updated to version 0.9.9.

* Wed Apr 14 2010 Lev Shamardin <shamardin@gmail.com> - 0.9.7-1
- Initial package version.
