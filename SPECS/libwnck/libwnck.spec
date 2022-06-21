Summary:	Window Navigator Construction Kit.
Name:		libwnck
Version:	2.30.7
Release:	2%{?dist}
License:	LGPLv2+
URL:		http://www.gnome.org
Group:		User Interface/Desktops
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.30/%{name}-%{version}.tar.xz
%define sha1 libwnck=9283c0efe0c5c44135c9015cfbfd518a877e4d2e
BuildRequires:	gtk2-devel intltool
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

Requires:	gtk2
%description
The libwnck package contains a Window Navigator Construction Kit.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
Requires:	gtk2-devel
%description 	devel
Install this package if you want do compile applications using the pcre
library.
%prep
%setup -q
%build
%configure --prefix=%{_prefix} \
            --disable-static \
	    --program-suffix=-1
make %{?_smp_mflags} GETTEXT_PACKAGE=libwnck-1
%install
make DESTDIR=%{buildroot} GETTEXT_PACKAGE=libwnck-1 install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 2.30.7-2
-	Mariner initial version
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 2.30.7-1
-	initial version

