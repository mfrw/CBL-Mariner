Summary:	The LXPanel package contains a lightweight X11 desktop panel.
Name:		lxpanel
Version:	0.10.0
Release:	1%{?dist}
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		User Interface/Desktops
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
%define sha1 lxpanel=b7fd11267b192efcb87dadd38f96bfc3a4c5f448
# Patch0:        %{name}-0.5.6-fix_alarm_redeclaration.patch
# Patch1:        lxpanel-0.7.1-X11-uint32_l.patch
# Patch2:        lxpanel-0.7.1-fix-unhiding-panel.patch
# Patch3:        lxpanel-0.9.3-batt_fix_crash.patch
BuildRequires: glibc-devel
BuildRequires: alsa-lib-devel
BuildRequires: atk-devel
BuildRequires: bzip2-devel
BuildRequires: cairo-devel
BuildRequires: expat-devel
BuildRequires: libffi-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: glib-devel
BuildRequires: graphite2-devel
BuildRequires: gtk2-devel
BuildRequires: gtk3 gtk3-immodules gtk3-immodule-xim
BuildRequires: gtk3-devel
BuildRequires: harfbuzz-devel
BuildRequires: icu-devel
BuildRequires: libiw-devel libfm-devel
BuildRequires: menu-cache-devel
BuildRequires: pango-devel
BuildRequires: libpng-devel
# BuildRequires: libpthread-stubs-devel
BuildRequires: libselinux-devel
BuildRequires: libstartup-notification-devel
BuildRequires: libstdc++-devel
BuildRequires: libwnck-devel
BuildRequires: libX11-devel
BuildRequires: libXau-devel
BuildRequires: libxcb-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXext-devel
BuildRequires: libXres-devel
BuildRequires: zlib-devel
BuildRequires: menu-cache
BuildRequires: keybinder-devel
BuildRequires: libnl3 libnl3-devel
BuildRequires: libxml2-devel
BuildRequires: gdk-pixbuf2-xlib-devel
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

Requires:      lxmenu-data wireless_tools
Requires:      alsa-plugins
Provides:      lxde-lxpanel

%description
The LXPanel package contains a lightweight X11 desktop panel.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
Requires:	gtk2-devel gtk3-devel libfm-devel libwnck-devel keybinder-devel
%description 	devel
Install this package if you want do compile applications using the pcre
library.

%prep
%setup -q
#%patch0 -p0
#%patch1 -p1
#%patch2 -p1
# patch3 -p1

%build
./configure \
    --sysconfdir=/etc \
    --prefix=/usr

#https://bugzilla.gnome.org/show_bug.cgi?id=656231
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/xdg/lxpanel
%dir %{_sysconfdir}/xdg/lxpanel/default
%{_sysconfdir}/xdg/lxpanel/default/config
%dir %{_sysconfdir}/xdg/lxpanel/default/panels
%{_sysconfdir}/xdg/lxpanel/default/panels/panel
%dir %{_sysconfdir}/xdg/lxpanel/two_panels
%{_sysconfdir}/xdg/lxpanel/two_panels/config
%dir %{_sysconfdir}/xdg/lxpanel/two_panels/panels
%{_sysconfdir}/xdg/lxpanel/two_panels/panels/bottom
%{_sysconfdir}/xdg/lxpanel/two_panels/panels/top
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%{_mandir}/man1/lxpanel.1*
%{_mandir}/man1/lxpanelctl.1*
%doc AUTHORS COPYING
%exclude %{_libdir}/debug/
%{_datadir}/locale/*

%files devel
%defattr(-,root,root)
%dir %{_includedir}/lxpanel
%{_includedir}/lxpanel/*.h
%{_libdir}/pkgconfig/*.pc
%doc ChangeLog README

%changelog
*	Fri Jun 05 2020 Andrew Phelps <anphel@microsoft.com> 0.10.0-1
-	Rename package dependencies for MM5 release.
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 0.9.3-1
-	Mariner initial version
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 0.8.1-1
-	initial version
