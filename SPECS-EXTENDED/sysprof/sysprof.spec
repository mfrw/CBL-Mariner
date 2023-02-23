Vendor:         Microsoft Corporation
Distribution:   Mariner
%global glib2_version 2.67.4

Name:           sysprof
Version:        3.44.0
Release:        1%{?dist}
Summary:        A system-wide Linux profiler

License:        GPLv3+
URL:            http://www.sysprof.com
Source0:        https://download.gnome.org/sources/sysprof/3.44/sysprof-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libdazzle-1.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libunwind-generic)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       hicolor-icon-theme
Requires:       %{name}-cli%{?_isa} = %{version}-%{release}
Requires:       libsysprof-ui%{?_isa} = %{version}-%{release}

%description
Sysprof is a sampling CPU profiler for Linux that collects accurate,
high-precision data and provides efficient access to the sampled
calltrees.


%package        cli
Summary:        Sysprof command line utility
# sysprofd needs turbostat
Requires:       kernel-tools
Requires:       libsysprof%{?_isa} = %{version}-%{release}

%description    cli
The %{name}-cli package contains the sysprof-cli command line utility.


%package     -n libsysprof
Summary:        Sysprof libraries

%description -n libsysprof
The libsysprof package contains the Sysprof libraries.


%package     -n libsysprof-ui
Summary:        Sysprof UI library

%description -n libsysprof-ui
The libsysprof-ui package contains the Sysprof UI library.


%package        capture-devel
Summary:        Development files for sysprof-capture static library
License:        BSD-2-Clause-Patent
Provides:       sysprof-capture-static = %{version}-%{release}
# Split out in F34
Conflicts:      %{name}-devel < 3.39.94-1

%description    capture-devel
The %{name}-capture-devel package contains the sysprof-capture static library and header files.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-capture-devel%{?_isa} = %{version}-%{release}
Requires:       libsysprof%{?_isa} = %{version}-%{release}
Requires:       libsysprof-ui%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING
%doc NEWS README.md AUTHORS
%{_bindir}/sysprof
%{_datadir}/applications/org.gnome.Sysprof3.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.sysprof3.gschema.xml
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/org.gnome.Sysprof3.appdata.xml
%{_datadir}/mime/packages/sysprof-mime.xml

%files cli -f %{name}.lang
%license COPYING
%{_bindir}/sysprof-cli
%{_libexecdir}/sysprofd
%{_datadir}/dbus-1/system.d/org.gnome.Sysprof2.conf
%{_datadir}/dbus-1/system.d/org.gnome.Sysprof3.conf
%{_datadir}/dbus-1/system-services/org.gnome.Sysprof2.service
%{_datadir}/dbus-1/system-services/org.gnome.Sysprof3.service
%{_datadir}/polkit-1/actions/org.gnome.sysprof3.policy
%{_unitdir}/sysprof2.service
%{_unitdir}/sysprof3.service

%files -n libsysprof
%license COPYING
%{_libdir}/libsysprof-4.so
%{_libdir}/libsysprof-memory-4.so
%{_libdir}/libsysprof-speedtrack-4.so

%files -n libsysprof-ui
%license COPYING
%{_libdir}/libsysprof-ui-4.so

%files capture-devel
%license src/libsysprof-capture/COPYING
%dir %{_includedir}/sysprof-4
%{_includedir}/sysprof-4/sysprof-address.h
%{_includedir}/sysprof-4/sysprof-capture-condition.h
%{_includedir}/sysprof-4/sysprof-capture-cursor.h
%{_includedir}/sysprof-4/sysprof-capture.h
%{_includedir}/sysprof-4/sysprof-capture-reader.h
%{_includedir}/sysprof-4/sysprof-capture-types.h
%{_includedir}/sysprof-4/sysprof-capture-writer.h
%{_includedir}/sysprof-4/sysprof-clock.h
%{_includedir}/sysprof-4/sysprof-collector.h
%{_includedir}/sysprof-4/sysprof-macros.h
%{_includedir}/sysprof-4/sysprof-platform.h
%{_includedir}/sysprof-4/sysprof-version.h
%{_includedir}/sysprof-4/sysprof-version-macros.h
%{_libdir}/libsysprof-capture-4.a
%{_libdir}/pkgconfig/sysprof-capture-4.pc

%files devel
%{_includedir}/sysprof-4/
%{_libdir}/pkgconfig/sysprof-4.pc
%{_libdir}/pkgconfig/sysprof-ui-4.pc
%{_datadir}/dbus-1/interfaces/org.gnome.Sysprof2.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Sysprof3.Profiler.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Sysprof3.Service.xml


%changelog
* Sat Mar 19 2022 David King <amigadave@amigadave.com> - 3.44.0-1
- Update to 3.44.0

* Wed Mar 09 2022 David King <amigadave@amigadave.com> - 3.43.90-1
- Update to 3.43.90

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.42.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 05 2021 Kalev Lember <klember@redhat.com> - 3.42.1-1
- Update to 3.42.1
- Build with libunwind support

* Tue Sep 21 2021 Kalev Lember <klember@redhat.com> - 3.42.0-1
- Update to 3.42.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 23 2021 Kalev Lember <klember@redhat.com> - 3.40.1-1
- Update to 3.40.1

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 3.40.0-1
- Update to 3.40.0

* Tue Mar 16 2021 Kalev Lember <klember@redhat.com> - 3.39.94-2
- Add explicit conflicts to help with upgrades

* Thu Feb 25 2021 Kalev Lember <klember@redhat.com> - 3.39.94-1
- Update to 3.39.94

* Wed Feb 24 2021 Kalev Lember <klember@redhat.com> - 3.39.92-2
- Split sysprof-capture library and header files out to sysprof-capture-devel
- Update minimum required glib2 version

* Wed Feb 24 2021 Kalev Lember <klember@redhat.com> - 3.39.92-1
- Update to 3.39.92

* Mon Feb 22 2021 Kalev Lember <klember@redhat.com> - 3.39.90-2
- Specify pic for static libsysprof-capture

* Thu Feb 18 2021 Kalev Lember <klember@redhat.com> - 3.39.90-1
- Update to 3.39.90

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 20 2020 Kalev Lember <klember@redhat.com> - 3.38.1-2
- Rebuild

* Fri Oct 16 2020 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Sun Sep 20 2020 Kalev Lember <klember@redhat.com> - 3.38.0-2
- Split out a separate libsysprof package and avoid -devel subpackage depending
  on the GUI app

* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Mon Sep 07 2020 Kalev Lember <klember@redhat.com> - 3.37.92-1
- Update to 3.37.92

* Mon Aug 17 2020 Kalev Lember <klember@redhat.com> - 3.37.90-1
- Update to 3.37.90

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 07 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Mon Mar 02 2020 Kalev Lember <klember@redhat.com> - 3.35.92-1
- Update to 3.35.92

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Kalev Lember <klember@redhat.com> - 3.35.3-1
- Update to 3.35.3

* Wed Dec 11 2019 Adam Williamson <awilliam@redhat.com> - 3.35.2-1
- Update to 3.35.2

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Tue Sep 10 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Thu Sep 05 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92
- Set minimum required glib2 version

* Tue Aug 27 2019 Kalev Lember <klember@redhat.com> - 3.33.90-2
- Add kernel-tools runtime dep for turbostat

* Mon Aug 26 2019 Kalev Lember <klember@redhat.com> - 3.33.90-1
- Update to 3.33.90

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Kalev Lember <klember@redhat.com> - 3.33.3-1
- Update to 3.33.3

* Wed Mar 13 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Thu Feb 07 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Kalev Lember <klember@redhat.com> - 3.31.1-2
- Backport new API for gnome-builder

* Tue Oct 09 2018 Kalev Lember <klember@redhat.com> - 3.31.1-1
- Update to 3.31.1

* Wed Sep 26 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0
- Drop ldconfig scriptlets

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 3.28.1-3
- Rebuild with fixed binutils

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Wed Mar 14 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Sat Mar 03 2018 Kalev Lember <klember@redhat.com> - 3.27.91-1
- Update to 3.27.91
- Switch to the meson build system

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.1-3
- Switch to %%ldconfig_scriptlets

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.1-2
- Remove obsolete scriptlets

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Sat Sep 16 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Thu Sep 07 2017 Kalev Lember <klember@redhat.com> - 3.25.92-1
- Update to 3.25.92

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 11 2017 Kalev Lember <klember@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Mon Mar 20 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Thu Mar 16 2017 Kalev Lember <klember@redhat.com> - 3.23.92-1
- Update to 3.23.92

* Wed Mar 01 2017 Kalev Lember <klember@redhat.com> - 3.23.91-1
- Update to 3.23.91
- Add appdata validation

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 29 2016 Kalev Lember <klember@redhat.com> - 3.22.3-1
- Update to 3.22.3

* Wed Nov 02 2016 Kalev Lember <klember@redhat.com> - 3.22.2-1
- Update to 3.22.2

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1
- Don't use -Werror for builds

* Wed Sep 21 2016 Kalev Lember <klember@redhat.com> - 3.22.0-2
- Split out sysprof-cli and libsysprof-ui subpackages

* Wed Sep 21 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Mon Sep  5 2016 Peter Robinson <pbrobinson@fedoraproject.org> 3.21.91-2
- Build on all arches now generic atomics supported

* Fri Sep 02 2016 Kalev Lember <klember@redhat.com> - 3.21.91-1
- Update to 3.21.91

* Tue Aug 23 2016 Kalev Lember <klember@redhat.com> - 3.21.90-2
- Enable building for arm architectures

* Tue Aug 23 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90

* Mon Aug 08 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0
- Modernize spec file

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Gianluca Sforna <giallu@gmail.com> 1.2.0-3
- fix udev rule path (#979545)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep 15 2012 Gianluca Sforna <giallu@gmail.com> 1.2.0-1
- New upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Adam Jackson <ajax@redhat.com> 1.1.8-2
- Rebuild to break bogus libpng dependency

* Thu Jul 28 2011 Gianluca Sforna <giallu@gmail.com> 1.1.8-1
- New upstream release

* Fri Jun 24 2011 Gianluca Sforna <giallu@gmail.com> 1.1.6-3
- Fix missing icon (#558089)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun  8 2010 Gianluca Sforna <giallu gmail com> - 1.1.6-1
- New upstream release

* Sun Sep 27 2009 Gianluca Sforna <giallu gmail com> - 1.1.2-3
- Incorporate suggestions from package review
- Require kernel 2.6.31
- Updated description

* Sat Sep 26 2009 Gianluca Sforna <giallu gmail com> - 1.1.2-1
- New upstream release

* Wed Apr  9 2008 Gianluca Sforna <giallu gmail com> - 1.0.9-1
- version update to 1.0.9

* Tue Aug 28 2007 Gianluca Sforna <giallu gmail com> 1.0.8-2
- update License field

* Thu Dec 21 2006 Gianluca Sforna <giallu gmail com> 1.0.8-1
- version update to 1.0.8

* Tue Nov 21 2006 Gianluca Sforna <giallu gmail com> 1.0.7-1
- version update to 1.0.7

* Wed Nov  1 2006 Gianluca Sforna <giallu gmail com> 1.0.5-1
- version update

* Sun Oct  8 2006 Gianluca Sforna <giallu gmail com> 1.0.3-6
- better to use ExclusiveArch %%{ix86} (thanks Ville)

* Thu Oct  5 2006 Gianluca Sforna <giallu gmail com> 1.0.3-5
- add ExclusiveArch to match sysprof-kmod supported archs

* Mon Oct  2 2006 Gianluca Sforna <giallu gmail com> 1.0.3-4
- add .desktop file

* Sat Sep 30 2006 Gianluca Sforna <giallu gmail com> 1.0.3-3
- versioned Provides
- add BR: binutils-devel

* Fri Sep 29 2006 Gianluca Sforna <giallu gmail com> 1.0.3-2
- own sysprof directory

* Thu Jun 22 2006 Gianluca Sforna <giallu gmail com> 1.0.3-1
- version update
- use standard %%configure macro

* Sun May 14 2006 Gianluca Sforna <giallu gmail com> 1.0.2-1
- Initial Version
