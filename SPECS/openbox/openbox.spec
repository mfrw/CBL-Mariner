Summary:	highly configurable desktop window manager.
Name:		openbox
Version:	3.6.1
Release:	3%{?dist}
License:	GPLv2+
URL:		http://openbox.org
Group:		User Interface/Desktops
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	http://openbox.org/dist/%{name}/%{name}-%{version}.tar.xz
%define sha1 openbox=6573516107f8cdb83842aac25a430e3f9f966bad
Patch1:		openbox-python3.patch
Patch2:		openbox-kf5menu.patch
BuildRequires:	gtk2-devel gtk3-devel pkg-config libstartup-notification-devel libstartup-notification libXcursor-devel libxml2-devel pangomm pangomm-devel pango pango-devel libXft-devel freetype-devel fontconfig-devel
Requires:	gtk2 gtk3 libXcursor libxml2 pango pkg-config libXft freetype fontconfig libstartup-notification libstartup-notification-devel
%description
Openbox is a highly configurable desktop window manager with extensive standards support. It allows you to control almost every aspect of how you interact with your desktop.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	gtk2-devel gtk3-devel libXcursor-devel libxml2-devel pango-devel pkg-config libXft-devel freetype-devel fontconfig-devel libstartup-notification-devel
%description	devel
It contains the libraries and header files to create applications
%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
./configure --prefix=%{_prefix} \
	    --sysconfdir=%{_sysconfdir} \
	    --disable-static \
	    --docdir=/usr/share/doc/%{name}-%{version}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_libexecdir}/*
%{_libdir}/*
%exclude %{_libdir}/*.la
%exclude %{_libdir}/debug
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la

%changelog
*	Fri Jun 05 2020 Andrew Phelps <anphel@microsoft.com> 3.6.1-3
-	Rename package dependencies for MM5 release.

*	Fri Jun 05 2020 Andrew Phelps <anphel@microsoft.com> 3.5.2-3
-	Rename package dependencies for MM5 release.
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 3.5.2-2
-	Mariner
*	Tue May 26 2015 Alexey Makhalov <amakhalov@vmware.com> 3.5.2-1
-	initial version
