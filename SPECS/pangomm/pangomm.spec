Summary:	The Pangomm package provides a C++ interface to Pango.
Name:		pangomm
Version:	2.40.2
Release:	2%{?dist}
License:	LGPLv2+
URL:		http://www.pango.org
Group:		System Environment/Libraries
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pangomm/2.40/%{name}-%{version}.tar.xz
%define sha1 pangomm=2a26466ee907ca944b9a5d72dda1c6c9abda9328
BuildRequires:	pango-devel glibmm24-devel cairomm-devel libXft-devel
Requires:	cairomm pango  glibmm24 libXft
%description
The Pangomm package provides a C++ interface to Pango.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	pango-devel glibmm24-devel cairomm-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%setup -q
%build
./configure --prefix=%{_prefix} &&
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%post
pango-querymodules --update-cache
%files
%defattr(-,root,root)
#%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/*.la
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%{_datadir}/*

%changelog
*	Fri Jun 05 2020 Andrew Phelps <anphel@microsoft.com> 2.40.2-2
-	Rename package dependencies for MM5 release.
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 2.40.2-1
-	Mariner initial version
*	Sun Jun 14 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.36.0-1
-	initial version
