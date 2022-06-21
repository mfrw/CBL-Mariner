Summary:	Extra libraries and files for menu-cache-gen.
Name:		libfm-extra
Version:	1.2.3
Release:	1%{?dist}
License:	LGPLv2+
URL:		http://downloads.sourceforge.net/pcmanfm
Group:		User Interface/Desktops
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	http://downloads.sourceforge.net/pcmanfm/libfm-%{version}.tar.xz
%define sha1 libfm=c3f2f34086761d89d6aba549883610084ba00750
BuildRequires:	intltool glib-devel
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

Requires:	glib
%description
The libfm package contains a library and other files required by menu-cache-gen libexec of menu-cache-1.0.0.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
Requires:	intltool glib-devel
%description 	devel
Install this package if you want do compile applications using the pcre
library.
%prep
%setup -q -n libfm-%{version}
%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} \
            --with-extra-only \
	    --with-gtk=no     \
	    --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%exclude %{_libdir}/debug
%exclude %{_libdir}/debug/
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 1.2.3-1
-	Mariner initial version
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 0.5.1-1
-	initial version

