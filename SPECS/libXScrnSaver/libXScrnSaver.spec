Summary:	X11 Screen Saver runtime library.
Name:		libXScrnSaver
Version:	1.2.2
Release:	2%{?dist}
License:	MIT
URL:		http://www.x.org/
Group:		System Environment/Libraries
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%define sha1 libXScrnSaver=7b8298eec371c33a71232e3653370a98f03c6c88
BuildRequires:	xorg-x11-proto-devel libXext-devel
Requires:	libXext xorg-x11-proto-devel
%description
The X11 Screen Saver runtime library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	xorg-x11-proto-devel libXext-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%setup -q
%build
%configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_datadir}/*
%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 1.2.2-2
-	Mariner initial version
*	Tue May 19 2015 Alexey Makhalov <amakhalov@vmware.com> 1.2.2-1
-	initial version

