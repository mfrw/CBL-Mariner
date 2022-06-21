%define majver %(echo %version | cut -d. -f1-2)
%define debug_package %{nil}

Name:          lxde-common
Version:       0.99.1
Release:       3%{?dist}
Summary:       LXDE Common, the default settings configuration file for integrating the different components of LXDE.
Group:         Graphical Desktop/Applications/Environment
Vendor:		Microsoft Corporation
Distribution:	Mariner
URL:           http://www.lxde.org/
Source0:        http://downloads.sourceforge.net/project/lxde/lxde-common%20%28default%20config%29/lxde-common%20%{majver}/lxde-common-%{version}.tar.xz
%define sha1 lxde-common=6dda860cc0c96a3d0d444325ac9f4ee6c3a7b946
Source1:       marineros_background-default.jpg
Source2:       lxde-common-icon-mariner.png
# Source3:       lxde-common-lxbrowser.desktop
Source5:       logout-banner.png
Source6:       marineros_wallpaper1.jpg
Source7:       marineros_wallpaper2.jpg
Source8:       marineros_wallpaper3.jpg
Source9:       marineros_wallpaper4.jpg
Source10:       marineros_wallpaper5.jpg
Source11:       marineros_wallpaper6.jpg
Source12:       marineros_wallpaper7.jpg
Source13:       marineros_wallpaper8.jpg
Source14:       marineros_wallpaper9.jpg
Source15:       marineros_wallpaper10.jpg
Source16:	install_microsoft_edge.sh

# Mariner Desktop default wallpaper
Source100:      background-default.jpg

Patch2:        %{name}-0.5.0-matchbox-keyboard.patch
Patch4:        lxde-common-0.5.5-mariner-default-panel.patch
Patch5:        lxde-common-0.99.0-startlxde.patch
Patch7:        lxde-common-0.5.6-fix-lxde-logout.patch
License:       GPL

BuildRequires: glib-devel
BuildRequires: glibc-devel gtk3 gtk3-immodules gtk3-immodule-xim
BuildRequires: atk-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: glib-devel
BuildRequires: pango-devel
BuildRequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: libXft-devel
BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: libunique-devel
BuildRequires: intltool
BuildRequires: gnome-menus-devel
BuildRequires: libstdc++-devel
BuildRequires: libwnck-devel
BuildRequires: libX11-devel
BuildRequires: libXau-devel
BuildRequires: libxcb-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXext-devel
BuildRequires: libXres-devel
BuildRequires: alsa-lib-devel
BuildRequires: speex-devel
BuildRequires: libpulse-devel
BuildRequires:  systemd-devel
BuildRequires:  dbus-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libXtst-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libXi-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXvMC-devel
BuildRequires:  libXv-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-vulkan-devel
BuildRequires:  xorg-x11-drv-libinput-devel
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

Requires:  mesa-libGL
Requires:  mesa-libEGL
Requires:  mesa-libGL
Requires:  mesa-libGLES
Requires:  mesa-vulkan-drivers
Requires:  mesa-libEGL
Requires:  mesa-dri-drivers
Requires:  pulseaudio pulseaudio-utils
Requires:  pulseaudio-module-gsettings
Requires:  pulseaudio-module-x11 pulseaudio-system-wide
Requires:  alsa-lib-devel alsa-utils alsa-lib
Requires:  libpulse-devel

Requires:  xorg-x11-drv-libinput xorg-x11-drv-intel xorg-x11-drv-vesa xf86-input-synaptics
Requires:  xorg-x11-drv-fbdev xorg-x11-drv-ati xorg-x11-drv-nouveau xf86-input-evdev xf86-input-keyboard xf86-input-mouse

Requires:  libX11 libinput systemd pixman twm xclock xterm libdrm libfontenc libupnp13
#Requires:  liberation-fonts liberation-fonts-common liberation-mono-fonts liberation-sans-fonts liberation-serif-fonts
Requires:      gnome-menus >= 3.36.0-5
Requires:      gsettings-desktop-schemas
Requires:      xrdp gnome-icon-theme

Requires:      openbox
Requires:      polkit-gnome
Requires:      dbus
Requires:      lxde-icon-theme
Requires:      lxpanel
Requires:      lxsession
Requires:      pcmanfm
Requires:      lxtask
Requires:      lxappearance
Requires:     xorg-x11-xinit
Requires:     xorg-x11-fonts-base
Requires:     xorg-x11-server-common
Requires:     imsettings
Requires:     xorg-x11-fonts-100dpi
Requires:     xorg-x11-fonts-75dpi
Requires:     xorg-x11-fonts-cyrillic
Requires:     xorg-x11-fonts-ethiopic
Requires:     xorg-x11-fonts-ISO8859-1-100dpi
Requires:     xorg-x11-fonts-ISO8859-1-75dpi
Requires:     xorg-x11-fonts-ISO8859-14-100dpi
Requires:     xorg-x11-fonts-ISO8859-14-75dpi
Requires:     xorg-x11-fonts-ISO8859-15-100dpi
Requires:     xorg-x11-fonts-ISO8859-15-75dpi
Requires:     xorg-x11-fonts-ISO8859-2-100dpi
Requires:     xorg-x11-fonts-ISO8859-2-75dpi
Requires:     xorg-x11-fonts-ISO8859-9-100dpi
Requires:     xorg-x11-fonts-ISO8859-9-75dpi
Requires:     xorg-x11-fonts-misc
Requires:     xorg-x11-fonts-Type1
#Requires:     cascadia-fonts-all
Requires:     gtk-update-icon-cache

%description
LXDE Common, the default settings configuration file for integrating the different components of LXDE. LXDE Common manages the system behavior and functions to integrate icons and artwork.

%prep
%setup -q
%patch2 -p1
sed -i "s|lxde_blue.jpg|marineros.jpg|" pcmanfm/pcmanfm.conf.in
# %patch4 -p1
# %patch5 -p1
# %patch7 -p1

%build
autoreconf
./configure --prefix=%{_prefix} \
	    --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

install -D -m0644 lxde-logout.desktop %{buildroot}%{_datadir}/applications/lxde-logout.desktop
install -D -m0644 %{SOURCE100} %{buildroot}%{_datadir}/lxde/wallpapers/marineros.jpg
install -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/lxde/wallpapers/marineros_default_wallpaper.jpg
# install -D -m0644 %{SOURCE100} %{buildroot}%{_datadir}/backgrounds/background-default.jpg
install -D -m0644 %{SOURCE2} %{buildroot}%{_datadir}/lxde/images/lxde-icon.png
# install -D -m0644 %{SOURCE3} %{buildroot}%{_datadir}/applications/lxbrowser.desktop
install -D -m0644 %{SOURCE5} %{buildroot}%{_datadir}/lxde/images/logout-banner.png
install -D -m0644 %{SOURCE6} %{buildroot}%{_datadir}/backgrounds/marineros_wallpaper1.jpg
install -D -m0644 %{SOURCE7} %{buildroot}%{_datadir}/backgrounds/marineros_wallpaper2.jpg
install -D -m0644 %{SOURCE8} %{buildroot}%{_datadir}/backgrounds/marineros_wallpaper3.jpg
install -D -m0644 %{SOURCE9} %{buildroot}%{_datadir}/backgrounds/marineros_wallpaper4.jpg
install -D -m0644 %{SOURCE10} %{buildroot}%{_datadir}/backgrounds/marineros_wallpaper5.jpg
install -D -m0644 %{SOURCE11} %{buildroot}%{_datadir}/backgrounds/marineros_wallpape6.jpg
install -D -m0644 %{SOURCE12} %{buildroot}%{_datadir}/backgrounds/marineros_wallpaper7.jpg
install -D -m0644 %{SOURCE13} %{buildroot}%{_datadir}/backgrounds/marineros_wallpaper8.jpg
install -D -m0644 %{SOURCE14} %{buildroot}%{_datadir}/backgrounds/marineros_wallpaper9.jpg
install -D -m0644 %{SOURCE15} %{buildroot}%{_datadir}/backgrounds/marineros_wallpaper10.jpg

echo "@xcompmgr" >> %{buildroot}/etc/xdg/lxsession/LXDE/autostart
echo "@openbox-session &" >> %{buildroot}/etc/xdg/lxsession/LXDE/autostart
echo "@pulseaudio" >> %{buildroot}/etc/xdg/lxsession/LXDE/autostart


install -d %{buildroot}/etc/skel/
cat > %{buildroot}/etc/skel/.xinitrc << "EOF"
ck-launch-session startlxde
EOF

%post
update-mime-database /usr/share/mime &&
gtk-update-icon-cache -qf /usr/share/icons/hicolor &&
update-desktop-database -q
cp /etc/skel/.xinitrc /root

%files
%defattr(-,root,root)
%{_sysconfdir}/xdg/lxpanel/LXDE/config
%{_sysconfdir}/xdg/lxpanel/LXDE/panels/panel
%{_sysconfdir}/xdg/lxsession/LXDE/autostart
%{_sysconfdir}/xdg/lxsession/LXDE/desktop.conf
%{_sysconfdir}/xdg/openbox/LXDE/menu.xml
%{_sysconfdir}/xdg/openbox/LXDE/rc.xml
%{_sysconfdir}/xdg/pcmanfm/LXDE/pcmanfm.conf
%{_sysconfdir}/skel/.xinitrc
%{_bindir}/lxde-logout
%{_bindir}/openbox-lxde
%{_bindir}/startlxde
# %{_datadir}/applications/lxbrowser.desktop
%{_datadir}/applications/lxde-screenlock.desktop
%{_datadir}/applications/lxde-logout.desktop
%{_datadir}/lxde/images/logout-banner.png
%{_datadir}/lxde/images/lxde-icon.png
%{_datadir}/lxde/wallpapers/marineros.jpg
%{_datadir}/lxde/wallpapers/marineros_default_wallpaper.jpg
%{_datadir}/xsessions/LXDE.desktop
%{_mandir}/man?/lxde-logout.1*
%{_mandir}/man?/openbox-lxde.1*
%{_mandir}/man?/startlxde.1*
%doc AUTHORS COPYING
%{_datadir}/lxde/wallpapers/lxde_blue.jpg
%{_datadir}/lxde/wallpapers/lxde_green.jpg
%{_datadir}/lxde/wallpapers/lxde_red.jpg
%{_datadir}/backgrounds/*.jpg

%changelog
*	Fri Jun 05 2020 Andrew Phelps <anphel@microsoft.com> 0.99.1-2
-	Rename package dependencies for MM5 release.
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 0.99.1-1
-	Mariner initial version
*	Tue May 26 2015 Alexey Makhalov <amakhalov@vmware.com> 0.99.0-1
-	initial version
