%define _unpackaged_files_terminate_build 0
Summary:	CSS2 parsing and manipulation library.
Name:		libcroco
Version:	0.6.12
Release:	1%{?dist}
License:	LGPLv2
URL:		http://www.gnome.org/
Group:		System Environment/Libraries
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.6/%{name}-%{version}.tar.xz
%define sha1 libcroco=f34287280cbf44d6c9628d15fa8a16347753a1d5
Patch0:         libcroco-fix-CVE-2017-7960.patch
Patch1:         libcroco-fix-CVE-2017-7961.patch
BuildRequires:	glib-devel libxml2-devel
Requires:	glib libxml2
%description
The libcroco package contains a standalone CSS2 parsing and manipulation library.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	glib-devel libxml2-devel

%description	devel
It contains the libraries and header files to create applications

%prep
%setup -q
%build
./configure --prefix=%{_prefix} \
            --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%files devel
%defattr(-,root,root)
%{_datadir}/*
%{_includedir}/*

%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 0.6.12-1
-	Mariner initial version
*	Wed May 27 2015 Alexey Makhalov <amakhalov@vmware.com> 0.6.8-1
-	initial version

