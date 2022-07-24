%{!?_unitdir: %global _unitdir %{_prefix}/lib/systemd/system/}

Summary:	Lightweight display manager
Name:		lxdm
Version:	0.5.3
Release:	6%{?dist}
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		System Environment/Libraries
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
%define sha1 lxdm=8c4f7439fa7b56a97e8b19dc62af02a88ae12b45
Source1:	lxdm.conf
Source2:	azuremariner.png
Source3:	greeter.ui
Source4:	lxdm.service
Source5:	azuremariner-default.jpg
BuildRequires:	gtk3 gtk3-immodules gtk3-immodule-xim gtk2-devel gtk3-devel librsvg-devel pam pam-devel systemd pkg-config dbus-glib-devel intltool automake libtool iso-codes-devel iso-codes desktop-file-utils libX11-devel
#BuildRequires:	gtk3 gtk3-immodules gtk3-immodule-xim gtk2-devel gtk3-devel librsvg-devel consolekit-devel pam systemd pkg-config dbus-glib-devel intltool automake libtool iso-codes-devel iso-codes desktop-file-utils libX11-devel
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

#Requires:	gtk2 gtk3 librsvg consolekit pam systemd libxcb which pkg-config dbus-glib intltool automake libtool iso-codes libX11 gtk2-engines
Requires:	gtk2 gtk3 librsvg pam systemd libxcb which pkg-config dbus-glib intltool automake libtool iso-codes libX11 gtk2-engines

%description
The LXDM is a lightweight Display Manager for the LXDE desktop. It can also be used as an alternative to other Display Managers such as GNOME's GDM or KDE's KDM.

%prep

%setup -q

%build
cat > pam/lxdm << "EOF"
# Begin /etc/pam.d/lxdm

auth     requisite      pam_nologin.so
auth     required       pam_env.so
auth     include        system-auth

account  include        system-account

password include        system-password

session  required       pam_limits.so
session  include        system-session

# End /etc/pam.d/lxdm
EOF

sed -i 's:sysconfig/i18n:profile.d/i18n.sh:g' data/lxdm.in &&
sed -i 's:/etc/xprofile:/etc/profile:g' data/Xsession &&
sed -e 's/^bg/#&/'        \
    -e '/reset=1/ s/# //' \
    -e 's/logou$/logout/' \
    -e "/arg=/a arg=$XORG_PREFIX/bin/X" \
    -i data/lxdm.conf.in

./configure --prefix=%{_prefix}     \
            --sysconfdir=/etc \
            --with-pam        \
			--disable-silent-rules \
			--disable-consolekit \
            --with-systemdsystemunitdir=no

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/lxdm/
install -d $RPM_BUILD_ROOT/usr/share/backgrounds
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/usr/share/backgrounds/
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT/usr/share/lxdm/themes/Industrial/
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT/usr/share/backgrounds/

install -Dpm 644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}.service

cat >> $RPM_BUILD_ROOT/etc/lxdm/PostLogout << "EOF"
# Workaround: --exit-with-session doesn't work.
# dbus-daemon --session is started in /etc/skel/.xinitrc and terminated here.
for p in `ps ax | grep "dbus-daemon" | grep "session" | awk '{print $1}'` ; do
    kill $p
done
EOF

sed -i 's/ --exit-with-session//' %{buildroot}/etc/lxdm/Xsession


%post
systemctl enable lxdm
%systemd_post %{name}.service


%preun
systemctl disable lxdm
%systemd_preun %{name}.service


%files
%defattr(-,root,root)
%{_bindir}/*
%{_sysconfdir}/*
# /lib/*
%{_libexecdir}/*
%{_sbindir}/*
%{_datadir}/*
%{_unitdir}/lxdm.service

%changelog
*   Sat May 14 2022 Bala <balakumaran.kannan@microsoft.com> 0.5.3-2
-   Reverted Harish Udaiya Kumar's change. Using Industrial theme
*	Fri Jun 05 2020 Andrew Phelps <anphel@microsoft.com> 0.5.3-2
-	Rename package dependencies for MM5 release.
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 0.5.3-1
-	Mariner initial version
*	Fri Jun 12 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.5.0-2
-	Excluded the Industrial theme and added our custom theme as a dependency. 
*	Fri Jun 12 2015 Alexey Makhalov <amakhalov@vmware.com> 0.5.0-1
-	initial version
