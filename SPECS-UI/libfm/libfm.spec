Summary:	The libfm package contains a library used to develop file managers providing some file management utilities.
Name:		libfm
Version:	1.2.3
Release:	1%{?dist}
License:	LGPLv2+
URL:		http://downloads.sourceforge.net/pcmanfm
Group:		User Interface/Desktops
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	http://downloads.sourceforge.net/pcmanfm/%{name}-%{version}.tar.xz
%define sha1 libfm=c3f2f34086761d89d6aba549883610084ba00750
Patch0:		host2guest_dnd_support.patch
BuildRequires:	gtk2-devel menu-cache-devel
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

Requires:	gtk2 menu-cache
%description
The libfm package contains a library used to develop file managers providing some file management utilities.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
Requires:	gtk2-devel menu-cache-devel
%description 	devel
Install this package if you want do compile applications using the pcre
library.
%prep
%setup -q
%patch0 -p1
%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} \
	    --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install

rm -rf %{buildroot}%{_libdir}/%{name}-extra.so.4.0.3

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/*.la
%exclude %{_libdir}/debug
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 1.2.3-1
-	Mariner initial version
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 0.5.1-1
-	initial version

