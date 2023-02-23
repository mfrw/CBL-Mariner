Vendor:         Microsoft Corporation
Distribution:   Mariner
%?python_enable_dependency_generator
%define srcname nmstate
%define libname libnmstate

Name:           nmstate
Version:        2.0.0
Release:        1%{?dist}
Summary:        Declarative network manager API
License:        LGPLv2+
URL:            https://github.com/%{srcname}/%{srcname}
Source0:        %{url}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz.asc
Source2:        nmstate.gpg
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gnupg2
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
Requires:       python3-setuptools
Requires:       python3-%{libname} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Nmstate is a library with an accompanying command line tool that manages host
networking settings in a declarative manner and aimed to satisfy enterprise
needs to manage host networking through a northbound declarative API and multi
provider support on the southbound.


%package -n python3-%{libname}
Summary:        nmstate Python 3 API library
Requires:       NetworkManager-libnm >= 1:1.26.0
# Use Recommends for NetworkManager because only access to NM DBus is required,
# but NM could be running on a different host
Recommends:     NetworkManager
# Avoid automatically generated profiles
Recommends:     NetworkManager-config-server
Recommends:     (nmstate-plugin-ovsdb if openvswitch)
# Use Suggests for NetworkManager-ovs and NetworkManager-team since it is only
# required for OVS and team support
Suggests:       NetworkManager-ovs
Suggests:       NetworkManager-team
# FIXME: Once upstream included nispor into requirement.txt, remove below line
Requires:       python3dist(nispor)

%package -n nmstate-plugin-ovsdb
Summary:        nmstate plugin for OVS database manipulation
Requires:       python3-%{libname} = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?rhel}
# The python-openvswitch rpm package is not in the same repo with nmstate,
# require only if openvswitch is installed.
Requires:       (python3dist(ovs) if openvswitch)
Recommends:     python3dist(ovs)
%else
Requires:       python3dist(ovs)
%endif


%description -n python3-%{libname}
This package contains the Python 3 library for Nmstate.

%description -n nmstate-plugin-ovsdb
This package contains the nmstate plugin for OVS database manipulation.

%prep
gpg2 --import --import-options import-export,import-minimal %{SOURCE2} > ./gpgkey-mantainers.gpg
gpgv2 --keyring ./gpgkey-mantainers.gpg %{SOURCE1} %{SOURCE0}
%setup -q

%build
%py3_build

%install
%py3_install

%files
%doc README.md
%doc examples/
%{_mandir}/man8/nmstatectl.8*
%{_mandir}/man8/nmstate-autoconf.8*
%{python3_sitelib}/nmstatectl
%{_bindir}/nmstatectl
%{_bindir}/nmstate-autoconf

%files -n python3-%{libname}
%license LICENSE
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{srcname}-*.egg-info/
%exclude %{python3_sitelib}/%{libname}/plugins/nmstate_plugin_*
%exclude %{python3_sitelib}/%{libname}/plugins/__pycache__/nmstate_plugin_*

%files -n nmstate-plugin-ovsdb
%{python3_sitelib}/%{libname}/plugins/nmstate_plugin_ovsdb*
%{python3_sitelib}/%{libname}/plugins/__pycache__/nmstate_plugin_ovsdb*

%changelog
* Mon Feb 15 2022 Fernando Fernandez Mancera <ffmancera@riseup.net> - 2.0.0-1
- Upgrade to 2.0.0

* Tue Feb 01 2022 Fernando Fernandez Mancera <ffmancera@riseup.net> - 1.2.0-1
- Upgrade to 1.2.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Gris Ge <fge@redhat.com> - 1.1.0-2
- Add varlink service back.

* Tue Jul 27 2021 Gris Ge <fge@redhat.com> - 1.1.0-1
- Upgrade to 1.1.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.3-3
- Rebuilt for Python 3.10

* Mon Apr 19 2021 Fernando Fernandez Mancera <ferferna@redhat.com> - 1.0.3-2
- Fix installation nmstate-varlink.service

* Thu Apr 15 2021 Fernando Fernandez Mancera <ferferna@redhat.com> - 1.0.3-1
- Upgrade to 1.0.3

* Sun Feb 21 2021 Fernando Fernandez Mancera <ferferna@redhat.com> - 1.0.2-1
- Upgrade to 1.0.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Fernando Fernandez Mancera <ferferna@redhat.com> - 1.0.1-1
- Upgrade to 1.0.1

* Tue Dec 08 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 1.0.0-1
- Upgrade to 1.0.0

* Thu Oct 22 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.4.1-1
- Upgrade to 0.4.1

* Tue Oct 13 2020 Gris Ge <fge@redhat.com> - 0.4.0-2
- Fix the ELN build by put ovs stuff as soft requirement.

* Sun Sep 20 2020 Gris Ge <fge@redhat.com> - 0.4.0-1
- Upgrade to 0.4.0

* Mon Aug 31 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.3.5-1
- Update to 0.3.5

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.3.4-1
- Update to 0.3.4
- Sync. with upstream specfile

* Thu Jul 02 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.3.3-1
- Update to 0.3.3

* Tue Jun 16 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.3.2-1
- Update to 0.3.2
- Sync with upstream specfile

* Tue Jun 09 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.3.1-1
- Update to 0.3.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Rebuilt for Python 3.9

* Fri May 08 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.3.0-4
- Fix source path

* Fri May 08 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.3.0-3
- Fix signature verification

* Fri May 08 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.3.0-2
- Update signature verification

* Fri May 08 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.3.0-1
- Update to 0.3.0
- Sync with upstream specfile

* Tue Apr 21 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.2.10-1
- Update to 0.2.10

* Thu Mar 26 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.2.9-1
- Update to 0.2.9

* Fri Mar 13 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.2.8-1
- Update to 0.2.8

* Wed Mar 04 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.2.7-1
- Update to 0.2.7

* Mon Feb 24 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.2.6-1
- Update to 0.2.6

* Wed Feb 19 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.2.5-1
- Update to 0.2.5
- Sync with upstream specfile

* Wed Feb 12 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.2.4-1
- Update to 0.2.4

* Wed Feb 05 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.2.3-1
- Update to 0.2.3

* Tue Feb 04 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.2.2-1
- Update to 0.2.2
- Sync with upstream specfile

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.2.1-2
- Fix changelog

* Tue Jan 14 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Tue Dec 03 2019 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.2.0-2
- Fix changelog

* Tue Dec 03 2019 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.2.0-1
- Update to 0.2.0

* Mon Dec 02 2019 Till Maas <opensource@till.name> - 0.1.1-1
- Update to 0.1.1
- Sync with upstream specfile

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.8-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.8-2
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Gris Ge <fge@redhat.com> - 0.0.8-1
- Upgrade to 0.0.8.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Gris Ge <fge@redhat.com> - 0.0.7-2
- Workaround broken dbus-python packaging:
   https://bugzilla.redhat.com/show_bug.cgi?id=1654774

* Fri Jun 14 2019 Gris Ge <fge@redhat.com> - 0.0.7-1
- Upgrade to 0.0.7

* Sun May 05 2019 Gris Ge <fge@redhat.com> - 0.0.6-1
- Upgrade to 0.0.6

* Fri Apr 12 2019 Gris Ge <fge@redhat.com - 0.0.5-2
- Add missing runtime requirement: python3-dbus

* Tue Mar 12 2019 Gris Ge <fge@redhat.com> - 0.0.5-1
- Upgrade to 0.0.5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Till Maas <opensource@till.name> - 0.0.4-2
- Sync with upstream spec
- Use Recommends for NetworkManager
- Add Suggests for NetworkManager-ovs
- package examples as doc

* Thu Jan 24 2019 Gris Ge <fge@redhat.com> - 0.0.4-1
- Upgrade to 0.0.4.

* Mon Jan 21 2019 Gris Ge <fge@redhat.com> - 0.0.3-3
- Add missing runtime dependency for nmstatectl.

* Wed Jan 02 2019 Gris Ge <fge@redhat.com> - 0.0.3-2
- Add source file PGP verification.

* Thu Dec 20 2018 Gris Ge <fge@redhat.com> - 0.0.3-1
- Upgrade to 0.0.3.

* Mon Dec 03 2018 Gris Ge <fge@redhat.com> - 0.0.2-2
- Trival RPM SPEC fix.

* Wed Nov 28 2018 Gris Ge <fge@redhat.com> - 0.0.2-1
- Initial release.
