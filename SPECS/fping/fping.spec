Summary:        Utility to send ICMP echo probes to network hosts
Name:           fping
Version:        5.0
Release:        1%{?dist}
License:        BSD
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Productivity/Networking/Diagnostic
URL:            https://www.fping.org/
Source0:        https://github.com/schweikert/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake

%description
fping is a ping like program which uses the Internet Control Message Protocol
(ICMP) echo request to determine if a target host is responding.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
ln -sf fping %{buildroot}%{_sbindir}/fping6
rm -rf %{buildroot}%{_infodir}

%files
%defattr(-, root, root)
%{_sbindir}/fping
%{_sbindir}/fping6
%license COPYING
%doc CHANGELOG.md
%doc %{_mandir}/man8/fping.8*

%changelog
* Wed Feb 02 2022 Cameron Baird <cameronbaird@microsoft.com> - 5.0-1
- Update to 5.0

* Thu Dec 16 2021 Pawel Winogrodzki <pawelwi@microsoft.com> - 4.2-3
- Removing the explicit %%clean stage.
- License verified.

* Sat May 09 2020 Nick Samson <nisamson@microsoft.com> - 4.2-2
- Added %%license line automatically

*   Mon Mar 16 2020 Henry Beberman <henry.beberman@microsoft.com> 4.2-1
-   Updated to 4.2. Updated License.

*   Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 4.1-2
-   Initial CBL-Mariner import from Photon (license: Apache2).

* Wed Jan 23 2019 Dweep Advani <dadvani@vmware.com> 4.1-1
- Added fping package to Photon 2.0
