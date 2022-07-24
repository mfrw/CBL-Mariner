%define majversion %(echo %version | cut -d. -f 1-2)
%define pkgname startup-notification

Name:          libstartup-notification
Version:       0.12
Release:       2%{?dist}
Summary:       A mechanism allowing a desktop environment to track application startup
Group:         System/Libraries
Vendor:		Microsoft Corporation
Distribution:	Mariner
URL:           http://www.gnome.org
#Source0:        ftp://ftp.gnome.org/pub/GNOME/sources/startup-notification/%{majversion}/%{pkgname}-%{version}.tar.bz2
Source0:        http://freedesktop.org/software/startup-notification/releases/%{pkgname}-%{version}.tar.gz
%define sha1 %{pkgname}=4198bce2808d03160454a2940d989f3a5dc96dbb
License:       LGPL
BuildRequires: glibc-devel
BuildRequires: libX11-devel
BuildRequires: libxcb-devel
BuildRequires: xcb-util-devel
BuildRequires: pkg-config
Provides:	   %{pkgname}

%description
A mechanism allowing a desktop environment to track application startup, to provide user feedback and other features.

%package devel
Summary:       Devel package for %{name}
Group:         Development/Libraries

%description devel
A mechanism allowing a desktop environment to track application startup, to
provide user feedback and other features.

This package contains static libraries and header files need for development.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libstartup-notification-1.so.*
%doc AUTHORS COPYING

%files devel
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.la
%dir %{_includedir}/startup-notification-?.?
%{_includedir}/startup-notification-?.?/*
%{_libdir}/pkgconfig/libstartup-notification-?.?.pc
%doc ChangeLog NEWS README

%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 0.12-1
-	Mariner initial version
