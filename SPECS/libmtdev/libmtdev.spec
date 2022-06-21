Name:          libmtdev
Version:       1.1.5
Release:       1%{?dist}
Summary:       Multitouch Protocol Translation Library
Group:         System/Libraries
Vendor:        Microsoft Corporation
Distribution:  Mariner
URL:           http://bitmath.org/code/mtdev/
Source0:       http://bitmath.org/code/mtdev/mtdev-%{version}.tar.bz2
%define sha1 mtdev=15267fbde0ed466f8474db1bbdf2d6989846f415
License:       MIT
BuildRequires:	pixman-devel libpciaccess-devel pkg-config
BuildRequires: glibc-devel systemd-devel
BuildRequires:       xorg-x11-server-devel
BuildRequires:       xorg-x11-server-Xorg
BuildRequires:       xorg-x11-server-Xwayland
BuildRequires:       xorg-x11-server-Xvfb

Requires:       xorg-x11-server-Xorg
Requires:       xorg-x11-server-Xwayland
Requires:       xorg-x11-server-Xvfb

Requires:	pixman libpciaccess pkg-config systemd

%description
The mtdev is a stand-alone library which transforms all variants of kernel MT events
to the slotted type B protocol. The events put into mtdev may be from any MT device,
specifically type A without contact tracking, type A with contact tracking, or type B
with contact tracking. See the kernel documentation for further details.

%package devel
Group:         Development/Libraries
Summary:       Development files for %{name}
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}
## note: you can add this requirement if .pc files are provided by this package
Requires:      pkg-config

%description devel
This package contains libraries and header files for developing applications that use %{name}.

%prep
%setup -q -n mtdev-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libmtdev.so.*
%doc COPYING

%files devel
%defattr(-,root,root)
%{_bindir}/mtdev-test
%{_includedir}/mtdev-mapping.h
%{_includedir}/mtdev-plumbing.h
%{_includedir}/mtdev.h
%{_libdir}/libmtdev.a
%{_libdir}/libmtdev.la
%{_libdir}/libmtdev.so
%{_libdir}/pkgconfig/mtdev.pc

%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 1.1.5-1
-	Mariner initial version

