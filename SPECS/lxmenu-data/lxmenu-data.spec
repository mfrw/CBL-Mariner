%define debug_package %{nil}
Summary:	The LXMenu Data package provides files required to build freedesktop.org menu spec-compliant desktop menus for LXDE.
Name:		lxmenu-data
Version:	0.1.5
Release:	1%{?dist}
License:	LGPLv3
URL:		http://downloads.sourceforge.net/lxde
Group:		User Interface/Desktops
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
%define sha1 lxmenu-data=5c3cba7d2061a490ad62c1e9c3f6120343df7712
BuildRequires:	intltool
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

%description
The LXMenu Data package provides files required to build freedesktop.org menu spec-compliant desktop menus for LXDE.
%prep
%setup -q
%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_datadir}/*
%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 0.1.5-1
-	Mariner initial version
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 0.1.4-1
-	initial version
