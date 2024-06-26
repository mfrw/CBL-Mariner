Summary:        Console-based network traffic monitor
Name:           vnstat
Version:        2.7
Release:        1%{?dist}
License:        GPLv2
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Applications/System
URL:            https://humdi.net/vnstat/
Source0:        https://github.com/vergoh/vnstat/archive/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd

%description
vnStat is a console-based network traffic monitor that uses the network
interface statistics provided by the kernel as information source. This
means that vnStat wont actually be sniffing any traffic and also ensures
light use of system resources regardless of network traffic rate.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
mkdir -p %{buildroot}%{_unitdir}/
%make_install
%{__install} -p -m 644 examples/systemd/vnstat.service %{buildroot}%{_unitdir}/

%post
%systemd_post vnstat.service

%preun
%systemd_preun vnstat.service

%files
%license COPYING
%doc README
%{_unitdir}/vnstat.service
%{_sysconfdir}/vnstat.conf
%{_bindir}/vnstat
%{_sbindir}/vnstatd
%{_mandir}/*

%changelog
* Tue Jan 04 2022 Neha Agarwal <nehaagarwal@microsoft.com> - 2.7-1
- Update to version 2.7

* Fri Feb 05 2021 Henry Beberman <henry.beberman@microsoft.com> 2.6-1
- Add vnstat spec
- License verified
- Original version for CBL-Mariner
