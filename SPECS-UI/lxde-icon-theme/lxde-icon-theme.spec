%define debug_package %{nil}
Summary:	The LXDE Icon Theme package contains nuoveXT 2.2 Icon Theme for LXDE.
Name:		lxde-icon-theme
Version:	0.5.1
Release:	2%{?dist}
License:	LGPLv3
URL:		http://downloads.sourceforge.net/lxde
Group:		User Interface/Desktops
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
%define sha1 lxde-icon-theme=643029acac6864ee04cf409af0c825085f545cec
BuildRequires:	intltool
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

Requires:	gtk2
Requires:       gtk-update-icon-cache
%description
The LXDE Icon Theme package contains nuoveXT 2.2 Icon Theme for LXDE.
%prep
%setup -q
%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%post
gtk-update-icon-cache -qf %{_datadir}/icons/nuoveXT2 &>/dev/null
%files
%defattr(-,root,root)
%{_datadir}/*
%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 0.5.1-2
-	Mariner initial version
*	Thu May 21 2015 Alexey Makhalov <amakhalov@vmware.com> 0.5.1-1
-	initial version
