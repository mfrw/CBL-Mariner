%global security_hardening nonow
Summary:	Generic Linux input driver for the Xorg X server.
Name:		xf86-input-evdev
Version:	2.10.5
Release:	1%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		Development/Libraries
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	http://ftp.x.org/pub/individual/driver/%{name}-%{version}.tar.bz2
%define sha1 xf86-input-evdev=1f599c8f95f7d39af83aa2a59039432f35ab8c55
BuildRequires:	libevdev-devel pixman-devel libpciaccess-devel systemd-devel libmtdev-devel
BuildRequires:       xorg-x11-server-devel
BuildRequires:       xorg-x11-server-Xorg
BuildRequires:       xorg-x11-server-Xwayland
BuildRequires:       xorg-x11-server-Xvfb

Requires:       xorg-x11-server-Xorg
Requires:       xorg-x11-server-Xwayland
Requires:       xorg-x11-server-Xvfb

Requires:	libevdev pixman libpciaccess systemd libmtdev
%description
The Xorg Evdev Driver package contains Generic Linux input driver for the Xorg X server. It handles keyboard, mouse, touchpads and wacom devices, though for touchpad and wacom advanced handling, additional drivers are required.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	libevdev-devel xorg-x11-server-devel pixman-devel libpciaccess-devel systemd-devel libmtdev-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%setup -q
%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install


%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/evdev_drv.la
%{_libdir}/xorg/modules/input/evdev_drv.so
%{_includedir}/xorg/evdev-properties.h
%{_libdir}/pkgconfig/xorg-evdev.pc
%{_datadir}/X11/xorg.conf.d/10-evdev.conf
%{_mandir}/man4/evdev.4*

%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 2.10.5-1
-	Mariner initial version
*	Wed May 20 2015 Alexey Makhalov <amakhalov@vmware.com> 2.9.2-1
-	initial version
