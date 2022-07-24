Summary:	Lightweight task manager
Name:		lxtask
Version:	0.1.8
Release:	2%{?dist}
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		System Environment/Libraries
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
%define sha1 lxtask=ad089ceb3cb467e021862c6804ae50f1993919f4
BuildRequires: glibc-devel
BuildRequires: atk-devel gtk3 gtk3-immodules gtk3-immodule-xim
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: glib-devel
BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: pango-devel
BuildRequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

%description
The LXTask package contains a lightweight and desktop-independent task manager.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*

%changelog
*	Fri Jun 05 2020 Andrew Phelps <anphel@microsoft.com> 0.1.8-2
-	Rename package dependencies for MM5 release.
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 0.1.8-1
-	Mariner initial version
*	Mon Jun 1 2015 Alexey Makhalov <amakhalov@vmware.com> 0.1.6-1
-	initial version
