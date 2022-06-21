#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define drvver  12.2
%define soname  0
%define _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d
%define _bashcompletionsdir %{_datadir}/bash-completion/completions
Name:           pulseaudio
Version:        12.2
Release:        3%{?dist}
Summary:        A Networked Sound Server
License:        GPL-2.0+ AND LGPL-2.1+
Group:          System/Sound Daemons
Vendor:		Microsoft Corporation
Distribution:	Mariner
Url:            http://pulseaudio.org
Source0:         http://www.freedesktop.org/software/pulseaudio/releases/%{name}-%{version}.tar.xz
%define sha1 pulseaudio=310a6245036a51df6585a7ebfac75b32e073aa88
Source1:        default.pa-for-gdm
Source2:        setup-pulseaudio
Source3:        sysconfig.sound-pulseaudio
Source4:        pulseaudio-server.fw
Source5:        pulseaudio.service
Source6:        disable_flat_volumes.conf
Source7:        pulseaudio.tmpfiles
# Source8:        pulseaudio-gdm-hooks.tmpfiles
Patch0:         disabled-start.diff
Patch1:         suppress-socket-error-msg.diff
Patch2:         pulseaudio-wrong-memset.patch
Patch4:         pa-set-exit-idle-time-to-0-when-we-detect-a-session.patch
Patch5:         qpaeq-shebang.patch
BuildRequires:  alsa-lib-devel
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libatomic_ops-devel
BuildRequires:  libcap-devel
BuildRequires:  openssl-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dbus-devel
BuildRequires:  GConf-devel
BuildRequires:  glib-devel
BuildRequires:  gtk3-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel
BuildRequires:  libXtst-devel
BuildRequires:  libltdl-devel
BuildRequires:  speex-devel
BuildRequires:  libsndfile-devel
BuildRequires:  doxygen
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

Requires:       zsh
Requires:       systemd
Requires:       shadow-utils
## needs the same liborc version which was used to build against
# %requires_eq    liborc-0_4-0
#Requires(post): %fillup_prereq
Recommends:     %{name}-bash-completion
# Recommends:     %{name}-lang
Recommends:     alsa-plugins-pulse
Conflicts:      kernel < 2.6.31
Obsoletes:      libpulsecore9 < 0.9.15
Provides:       libpulsecore9 = 0.9.15
Obsoletes:      libpulsecore7 < 0.9.13
Provides:       libpulsecore7 = 0.9.13


%description
pulseaudio is a networked sound server for Linux, other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

%package esound-compat
Summary:        ESOUND compatibility for PulseAudio
Group:          System/Sound Daemons
Requires:       %{name} = %{version}
Provides:       esound-daemon = 0.2.41
Obsoletes:      esound-daemon < 0.2.41

%description esound-compat
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package provides the compatibility layer for drop-in replacement
of ESOUND.

%package module-x11
Summary:        X11 module for PulseAudio
Group:          System/Sound Daemons
Requires:       %{name} = %{version}
Requires:       %{name}-utils = %{version}

%description module-x11
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package provides the components needed to automatically start
the PulseAudio sound server on X11 startup.

%package module-zeroconf
Summary:        Zeroconf module for PulseAudio
Group:          System/Sound Daemons
Requires:       %{name} = %{version}
Supplements:	packageand(pulseaudio:avahi)

%description module-zeroconf
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package provides zeroconf network support for the PulseAudio sound server

%package system-wide
Summary:        Support for running PulseAudio daemon system wide
Group:          System/Sound Daemons
Requires:       %{name}
Requires:       systemd

%description system-wide
PulseAudio daemon can be run as a system-wide instance which than can be shared
by multiple local users. We recommend running the PulseAudio daemon per-user,
just like the traditional ESD sound daemon. In some situations however, such as
embedded systems where no real notion of a user exists, it makes sense to use
the system-wide mode.

Before you now go ahead and use it please read about what is wrong with system
mode:

http://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/WhatIsWrongWithSystemWide

%package module-gconf
Summary:        GCONF module for PulseAudio
Group:          System/Sound Daemons
Requires:       %{name} = %{version}
Conflicts:      %{name}-module-gsettings

%description module-gconf
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package provides gconf storage of PulseAudio sound server settings.

%package module-gsettings
Summary:        GSettings module for PulseAudio
Group:          System/Sound Daemons
Requires:       %{name} = %{version}
Conflicts:      %{name}-module-gconf

%description module-gsettings
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package provides GSettings storage of PulseAudio sound server settings.

%package -n libpulse%{soname}
Summary:        Client interface to PulseAudio
Group:          System/Libraries
Provides:       pulseaudio-libs = %{version}
Obsoletes:      pulseaudio-libs < %{version}

%description -n libpulse%{soname}
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package contains the system libraries for clients of pulseaudio
sound server.

%package -n libpulse-mainloop-glib%{soname}
Summary:        GLIB 2.0 Main Loop wrapper for PulseAudio
Group:          System/Sound Daemons
Provides:       pulseaudio-libs-glib2 = %{version}
Obsoletes:      pulseaudio-libs-glib2 < %{version}

%description -n libpulse-mainloop-glib%{soname}
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package contains the GLIB Main Loop bindings for the PulseAudio
sound server.

%package -n libpulse-devel
Summary:        Development package for the pulseaudio library
Group:          Development/Libraries/C and C++
Requires:       libpulse%{soname} = %{version}
Requires:       libpulse-mainloop-glib%{soname} = %{version}
Requires:       pkg-config
Requires:       glib-devel
Provides:       pulseaudio-devel = %{version}
Obsoletes:      pulseaudio-devel < %{version}

%description -n libpulse-devel
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package contains the files needed to compile programs that use the
pulseaudio library.

%package utils
Summary:        PulseAudio utilities
Group:          System/Sound Daemons
Requires:       %{name} = %{version}
Requires:       libpulse%{soname} = %{version}
Requires:       libpulse-mainloop-glib%{soname} = %{version}

%description utils
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package provides utilies for making use of the PulseAudio sound
server.


%package bash-completion
Summary:        PulseAudio Bash completion
Group:          System/Shells

%description bash-completion
Optional dependency offering bash completion for various PulseAudio utilities

%package zsh-completion
Summary:        PulseAudio zsh completion
Group:          System/Shells
Requires:       zsh

%description zsh-completion
Optional dependency offering zsh completion for various PulseAudio utilities

# %lang_package

%prep
%setup -q -T -b0
%patch0
%patch1 -p1
%patch2
%patch4 -p1
%patch5

%build
NOCONFIGURE=1 ./bootstrap.sh
echo 'HTML_TIMESTAMP=NO' >> doxygen/doxygen.conf.in
export LDFLAGS="-pie"
export CFLAGS="%{optflags} -fPIE"
%configure \
        --disable-static \
        --disable-rpath \
%ifarch armv5tel armv6hl
        --disable-neon-opt \
%endif
        --with-system-user=pulse \
        --with-system-group=pulse \
        --with-access-group=pulse-access \
        --disable-hal-compat \
        --disable-bluez4 \
        --disable-webrtc-aec \
        --enable-adrian-aec \
        --enable-gconf \
        --enable-gsettings \
        --with-udev-rules-dir=%{_udevrulesdir} \
        --with-pulsedsp-location='%{_prefix}/\\$$LIB/pulseaudio'

make %{?_smp_mflags} V=1
make %{?_smp_mflags} doxygen

%install
%make_install
rm -rf \
    "%{buildroot}%{_libdir}"/*.la \
    "%{buildroot}%{_libdir}/pulse-%{drvver}/modules"/*.la \
    "%{buildroot}%{_libdir}/pulseaudio"/*.la

# configure --disable-static had no effect; delete manually.
rm -rf "%{buildroot}%{_libdir}"/*.a

install -D -m 0644 %{SOURCE5} %{buildroot}%{_libexecdir}/systemd/system/%{name}.service
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# some HW may get undetected without this (check pulseaudio 6.0RC1 announce)
ln -s default.conf %{buildroot}%{_datadir}/pulseaudio/alsa-mixer/profile-sets/extra-hdmi.conf

# %find_lang %{name}
install %{SOURCE2} %{buildroot}%{_bindir}
chmod 755 %{buildroot}%{_bindir}/setup-pulseaudio
install -d %{buildroot}%{_fillupdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
touch %{buildroot}%{_sysconfdir}/profile.d/pulseaudio.sh
touch %{buildroot}%{_sysconfdir}/profile.d/pulseaudio.csh
mkdir -p %{buildroot}%{_prefix}/lib/tmpfiles.d
install -m 644 %{SOURCE7} %{buildroot}%{_prefix}/lib/tmpfiles.d/pulseaudio.conf
# install -m 644 %{SOURCE8} %{buildroot}%{_prefix}/lib/tmpfiles.d/pulseaudio-gdm-hooks.conf
# mkdir -p %{buildroot}%{_prefix}/share/factory/var/lib/gdm/.pulse
# install -m 644 %{SOURCE1} %{buildroot}%{_prefix}/share/factory/var/lib/gdm/.pulse/default.pa
# mkdir -p %{buildroot}%{_localstatedir}/lib/gdm
ln -s esdcompat %{buildroot}%{_bindir}/esd
# install firewall rule
# create .d conf dirs (since 8.0)
mkdir -p %{buildroot}%{_sysconfdir}/pulse/client.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/pulse/daemon.conf.d
# Install disable_flat_volumes.conf
install -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/pulse/daemon.conf.d
# created by setup-pulseaudio script
touch %{buildroot}%{_sysconfdir}/pulse/client.conf.d/50-system.conf


%post   -n libpulse%{soname} -p /sbin/ldconfig
%postun -n libpulse%{soname} -p /sbin/ldconfig
%post   -n libpulse-mainloop-glib%{soname} -p /sbin/ldconfig
%postun -n libpulse-mainloop-glib%{soname} -p /sbin/ldconfig
%post
/sbin/ldconfig
%tmpfiles_create pulseaudio.conf
%{fillup_only -an sound}
# Update the /etc/profile.d/pulseaudio.* files
setup-pulseaudio --auto > /dev/null

%postun -p /sbin/ldconfig
#%pre system-wide
#%service_add_pre pulseaudio.service
#exit 0

%post system-wide
getent group pulse >/dev/null || groupadd -r pulse
getent passwd pulse >/dev/null || useradd -r -g pulse -d %{_localstatedir}/lib/pulseaudio -s /sbin/nologin -c "PulseAudio daemon" pulse
getent group pulse-access >/dev/null || groupadd -r pulse-access
getent group audio | grep pulse >/dev/null || usermod -a -G audio pulse

%systemd_post pulseaudio.service
exit 0

%preun system-wide
%systemd_preun pulseaudio.service
exit 0

%postun system-wide
%systemd_postun_with_restart pulseaudio.service
exit 0

%files
%doc README
%license LICENSE GPL LGPL
%{_bindir}/pulseaudio
%{_bindir}/setup-pulseaudio
# %{_bindir}/qpaeq
%dir %{_datadir}/pulseaudio
%{_datadir}/pulseaudio/alsa-mixer
%{_fillupdir}/sysconfig.sound-pulseaudio
%dir %{_libdir}/pulseaudio
%{_libdir}/pulseaudio/libpulsecore-%{drvver}.so
%dir %{_libdir}/pulse-%{drvver}/
%dir %{_libdir}/pulse-%{drvver}/modules/
%{_libdir}/pulse-%{drvver}/modules/libalsa-util.so
%{_libdir}/pulse-%{drvver}/modules/libcli.so
%{_libdir}/pulse-%{drvver}/modules/liboss-util.so
%{_libdir}/pulse-%{drvver}/modules/libprotocol-cli.so
%{_libdir}/pulse-%{drvver}/modules/libprotocol-esound.so
%{_libdir}/pulse-%{drvver}/modules/libprotocol-http.so
%{_libdir}/pulse-%{drvver}/modules/libprotocol-native.so
%{_libdir}/pulse-%{drvver}/modules/libprotocol-simple.so
%{_libdir}/pulse-%{drvver}/modules/librtp.so
# %{_libdir}/pulse-%{drvver}/modules/libwebrtc-util.so
%{_libdir}/pulse-%{drvver}/modules/module-alsa-card.so
%{_libdir}/pulse-%{drvver}/modules/module-alsa-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-alsa-source.so
%{_libdir}/pulse-%{drvver}/modules/module-always-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-always-source.so
%{_libdir}/pulse-%{drvver}/modules/module-allow-passthrough.so
%{_libdir}/pulse-%{drvver}/modules/module-augment-properties.so
%{_libdir}/pulse-%{drvver}/modules/module-card-restore.so
%{_libdir}/pulse-%{drvver}/modules/module-cli.so
%{_libdir}/pulse-%{drvver}/modules/module-cli-protocol-tcp.so
%{_libdir}/pulse-%{drvver}/modules/module-cli-protocol-unix.so
%{_libdir}/pulse-%{drvver}/modules/module-combine.so
%{_libdir}/pulse-%{drvver}/modules/module-combine-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-console-kit.so
%{_libdir}/pulse-%{drvver}/modules/module-dbus-protocol.so
%{_libdir}/pulse-%{drvver}/modules/module-default-device-restore.so
%{_libdir}/pulse-%{drvver}/modules/module-detect.so
%{_libdir}/pulse-%{drvver}/modules/module-device-manager.so
%{_libdir}/pulse-%{drvver}/modules/module-device-restore.so
%{_libdir}/pulse-%{drvver}/modules/module-echo-cancel.so
%{_libdir}/pulse-%{drvver}/modules/module-esound-compat-spawnfd.so
%{_libdir}/pulse-%{drvver}/modules/module-esound-compat-spawnpid.so
%{_libdir}/pulse-%{drvver}/modules/module-esound-protocol-tcp.so
%{_libdir}/pulse-%{drvver}/modules/module-esound-protocol-unix.so
%{_libdir}/pulse-%{drvver}/modules/module-esound-sink.so
# %{_libdir}/pulse-%{drvver}/modules/module-equalizer-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-filter-apply.so
%{_libdir}/pulse-%{drvver}/modules/module-filter-heuristics.so
%{_libdir}/pulse-%{drvver}/modules/module-http-protocol-tcp.so
%{_libdir}/pulse-%{drvver}/modules/module-http-protocol-unix.so
%{_libdir}/pulse-%{drvver}/modules/module-intended-roles.so
%{_libdir}/pulse-%{drvver}/modules/module-ladspa-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-loopback.so
%{_libdir}/pulse-%{drvver}/modules/module-match.so
%{_libdir}/pulse-%{drvver}/modules/module-mmkbd-evdev.so
%{_libdir}/pulse-%{drvver}/modules/module-native-protocol-fd.so
%{_libdir}/pulse-%{drvver}/modules/module-native-protocol-tcp.so
%{_libdir}/pulse-%{drvver}/modules/module-native-protocol-unix.so
%{_libdir}/pulse-%{drvver}/modules/module-null-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-null-source.so
%{_libdir}/pulse-%{drvver}/modules/module-oss.so
%{_libdir}/pulse-%{drvver}/modules/module-pipe-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-pipe-source.so
%{_libdir}/pulse-%{drvver}/modules/module-position-event-sounds.so
%{_libdir}/pulse-%{drvver}/modules/module-remap-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-rescue-streams.so
%{_libdir}/pulse-%{drvver}/modules/module-role-cork.so
%{_libdir}/pulse-%{drvver}/modules/module-rtp-recv.so
%{_libdir}/pulse-%{drvver}/modules/module-rtp-send.so
%{_libdir}/pulse-%{drvver}/modules/module-rygel-media-server.so
%{_libdir}/pulse-%{drvver}/modules/module-simple-protocol-tcp.so
%{_libdir}/pulse-%{drvver}/modules/module-simple-protocol-unix.so
%{_libdir}/pulse-%{drvver}/modules/module-sine.so
%{_libdir}/pulse-%{drvver}/modules/module-sine-source.so
%{_libdir}/pulse-%{drvver}/modules/module-stream-restore.so
%{_libdir}/pulse-%{drvver}/modules/module-suspend-on-idle.so
%{_libdir}/pulse-%{drvver}/modules/module-switch-on-connect.so
%{_libdir}/pulse-%{drvver}/modules/module-switch-on-port-available.so

%{_libdir}/pulse-%{drvver}/modules/module-systemd-login.so

%{_libdir}/pulse-%{drvver}/modules/module-tunnel-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-tunnel-sink-new.so
%{_libdir}/pulse-%{drvver}/modules/module-tunnel-source.so
%{_libdir}/pulse-%{drvver}/modules/module-tunnel-source-new.so
%{_libdir}/pulse-%{drvver}/modules/module-udev-detect.so
%{_libdir}/pulse-%{drvver}/modules/module-virtual-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-virtual-source.so
%{_libdir}/pulse-%{drvver}/modules/module-virtual-surround-sink.so
%{_libdir}/pulse-%{drvver}/modules/module-volume-restore.so
%{_libdir}/pulse-%{drvver}/modules/module-remap-source.so
%{_libdir}/pulse-%{drvver}/modules/module-role-ducking.so
%{_udevrulesdir}/90-pulseaudio.rules
%{_mandir}/man1/pulseaudio.1*
%{_mandir}/man5/default.pa.5*
%{_mandir}/man5/pulse-client.conf.5*
%{_mandir}/man5/pulse-daemon.conf.5*
%{_mandir}/man5/pulse-cli-syntax.5*
%dir %{_sysconfdir}/pulse/
%dir %{_sysconfdir}/pulse/daemon.conf.d
%config(noreplace) %{_sysconfdir}/pulse/daemon.conf.d/disable_flat_volumes.conf
%config(noreplace) %{_sysconfdir}/pulse/daemon.conf
%config(noreplace) %{_sysconfdir}/pulse/default.pa
%config(noreplace) %{_sysconfdir}/pulse/system.pa
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/pulseaudio-system.conf
# init
%dir %{_libdir}/systemd
%dir %{_libdir}/systemd/user
%{_libdir}/systemd/user/%{name}.service
%{_libdir}/systemd/user/%{name}.socket
%{_prefix}/lib/tmpfiles.d/pulseaudio.conf

%{_datadir}/locale/*

# created by setup-pulseaudio script
%ghost %{_sysconfdir}/profile.d/pulseaudio.sh
%ghost %{_sysconfdir}/profile.d/pulseaudio.csh
%ghost %{_sysconfdir}/pulse/client.conf.d/50-system.conf

%files esound-compat
%{_bindir}/esdcompat
%{_bindir}/esd
%{_mandir}/man1/esdcompat.1*

%files -n libpulse%{soname}
%doc README LICENSE GPL LGPL
%dir %{_sysconfdir}/pulse/
%dir %{_sysconfdir}/pulse/client.conf.d
%config(noreplace) %{_sysconfdir}/pulse/client.conf
%{_libdir}/libpulse.so.%{soname}
%{_libdir}/libpulse.so.%{soname}.*
%{_libdir}/libpulse-simple.so.*
%dir %{_libdir}/pulseaudio
%{_libdir}/pulseaudio/libpulsecommon-%{drvver}.so

%files -n libpulse-devel
%doc doxygen/html
%{_includedir}/pulse/
%{_libdir}/libpulse.so
%{_libdir}/libpulse-mainloop-glib.so
%{_libdir}/libpulse-simple.so
%{_libdir}/pkgconfig/libpulse*.pc
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/PulseAudio
%{_libdir}/cmake/PulseAudio/PulseAudio*.cmake
%{_datadir}/vala

%files -n libpulse-mainloop-glib%{soname}
%{_libdir}/libpulse-mainloop-glib.so.%{soname}
%{_libdir}/libpulse-mainloop-glib.so.%{soname}.*
%{_datadir}/glib-2.0/schemas/org.freedesktop.pulseaudio.gschema.xml


%files module-gconf
%dir %{_libexecdir}/pulse
%dir %{_libdir}/pulse-%{drvver}
%dir %{_libdir}/pulse-%{drvver}/modules
%{_libdir}/pulse-%{drvver}/modules/module-gconf.so
%{_libexecdir}/pulse/gconf-helper

%files module-gsettings
%dir %{_libexecdir}/pulse
%dir %{_libdir}/pulse-%{drvver}
%dir %{_libdir}/pulse-%{drvver}/modules
%dir %{_datarootdir}/GConf
%dir %{_datarootdir}/GConf/gsettings
%{_libdir}/pulse-%{drvver}/modules/module-gsettings.so
%{_libexecdir}/pulse/gsettings-helper
%{_datadir}/GConf/gsettings/pulseaudio.convert


%files module-x11
%dir %{_libdir}/pulse-%{drvver}
%dir %{_libdir}/pulse-%{drvver}/modules
%{_sysconfdir}/xdg/autostart/pulseaudio.desktop
%{_bindir}/start-pulseaudio-x11
%{_libdir}/pulse-%{drvver}/modules/module-x11-bell.so
%{_libdir}/pulse-%{drvver}/modules/module-x11-cork-request.so
%{_libdir}/pulse-%{drvver}/modules/module-x11-publish.so
%{_libdir}/pulse-%{drvver}/modules/module-x11-xsmp.so
%{_mandir}/man1/start-pulseaudio-x11.1*

%files module-zeroconf
%dir %{_libdir}/pulse-%{drvver}
%dir %{_libdir}/pulse-%{drvver}/modules
# %{_libdir}/pulse-%{drvver}/modules/libavahi-wrap.so
%{_libdir}/pulse-%{drvver}/modules/libraop.so
# %{_libdir}/pulse-%{drvver}/modules/module-raop-discover.so
%{_libdir}/pulse-%{drvver}/modules/module-raop-sink.so
# %{_libdir}/pulse-%{drvver}/modules/module-zeroconf-discover.so
# %{_libdir}/pulse-%{drvver}/modules/module-zeroconf-publish.so

%files utils
%{_bindir}/pacat
%{_bindir}/pacmd
%{_bindir}/pactl
%{_bindir}/paplay
%{_bindir}/parec
%{_bindir}/pamon
%{_bindir}/parecord
%{_bindir}/pax11publish
%{_bindir}/padsp
%{_bindir}/pasuspender
%dir %{_libdir}/pulseaudio
%{_libdir}/pulseaudio/libpulsedsp.so
%{_mandir}/man1/pacat.1*
%{_mandir}/man1/pacmd.1*
%{_mandir}/man1/pactl.1*
%{_mandir}/man1/paplay.1*
%{_mandir}/man1/pasuspender.1*
%{_mandir}/man1/padsp.1*
%{_mandir}/man1/pax11publish.1*
%{_mandir}/man1/pamon.1*
%{_mandir}/man1/parec.1*
%{_mandir}/man1/parecord.1*

# %files lang -f %{name}.lang

%files system-wide
%{_sbindir}/rc%{name}
%dir %{_libexecdir}/systemd/system
%{_libexecdir}/systemd/system/%{name}.service

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_bashcompletionsdir}/pulseaudio
%{_bashcompletionsdir}/pacat
%{_bashcompletionsdir}/pacmd
%{_bashcompletionsdir}/pactl
%{_bashcompletionsdir}/padsp
%{_bashcompletionsdir}/paplay
%{_bashcompletionsdir}/parec
%{_bashcompletionsdir}/parecord
%{_bashcompletionsdir}/pasuspender

%files zsh-completion
%dir %{_datarootdir}/zsh
%dir %{_datarootdir}/zsh/site-functions/
%{_datarootdir}/zsh/site-functions/_pulseaudio

%changelog
*	Fri Jun 05 2020 Andrew Phelps <anphel@microsoft.com> 12.2-3
-	Rename package dependencies for MM5 release.
*	Wed Apr 08 2020 Daniel McIlvaney <damcilva@microsoft.com> 12.2-2
-	Remove unavailable %systemd_requires macro
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 12.2-1
-	Mariner initial version
