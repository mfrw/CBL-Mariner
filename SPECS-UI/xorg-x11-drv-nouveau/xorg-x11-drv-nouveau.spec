%define tarball xf86-video-nouveau
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir %{moduledir}/drivers
#define gitdate 20151008

%undefine _hardened_build

Summary:   Xorg X11 nouveau video driver for NVIDIA graphics chipsets
Name:      xorg-x11-drv-nouveau
# need to set an epoch to get version number in sync with upstream
Epoch:     1
Version:   1.0.17
Release:   2%{?dist}
URL:       http://www.x.org
License:   MIT

# Fedora specific snapshot no upstream release
%if 0%{?gitdate}
Source0: xf86-video-nouveau-%{gitdate}.tar.xz
%else
Source0: http://xorg.freedesktop.org/archive/individual/driver/xf86-video-nouveau-%{version}.tar.bz2
%endif
Source1: make-git-snapshot.sh

Patch1: remove-sarea.h.patch

ExcludeArch: s390 s390x

BuildRequires: make
BuildRequires: libtool automake autoconf
BuildRequires: xorg-x11-server-devel >= 1.14.2-8
BuildRequires: libdrm-devel >= 2.4.24-0.1.20110106
BuildRequires: mesa-libGL-devel
%if 0%{?fedora} > 17 || 0%{?rhel} > 6
BuildRequires: systemd-devel
%else
BuildRequires: libudev-devel
%endif

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)
Requires:  libdrm >= 2.4.33-0.1

%description 
X.Org X11 nouveau video driver.

%if 0%{?gitdate}
%define dirsuffix %{gitdate}
%else
%define dirsuffix %{version}
%endif

%prep
%setup -q -n xf86-video-nouveau-%{dirsuffix}
%patch1 -p1

%build
autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%files
%{driverdir}/nouveau_drv.so
%{_mandir}/man4/nouveau.4*

%changelog
* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 06 2021 Lyude Paul <lyude@redhat.com> - 1:1.0.17-1
- Update to 1.0.17
- Add patch to workaround build error until 1.0.18 release

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 10:11:29 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 1:1.0.15-11
- Add BuildRequires for make

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Adam Jackson <ajax@redhat.com> - 1:1.0.15-5
- Rebuild for xserver 1.20

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 1 2017 Ben Skeggs <bskeggs@redhat.com> 1.0.15-1
- Update to 1.0.15

* Thu Apr 13 2017 Ben Skeggs <bskeggs@redhat.com> 1.0.14-1
- Update to 1.0.14

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 29 2016 Hans de Goede <hdegoede@redhat.com> 1.0.13-1
- Update to 1.0.13
- Rebuild against xserver-1.19
- Prune changelog

* Fri Jun 17 2016 Hans de Goede <hdegoede@redhat.com> - 1.0.12-4
- Fix the crtc not being turned off, causing the dgpu to not suspend,
  after using a dgpu attached output

* Mon Feb 15 2016 Dave Airlie <airlied@redhat.com> 1.0.12-3
- pull reverse prime fix in from master.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Ben Skeggs <bskeggs@redhat.com> 1.0.12-1
- 1.0.12

* Thu Oct 08 2015 Dave Airlie <airlied@redhat.com> 1.0.12-0.3
- bump to latest upstream git snapshot (#1269709)

* Wed Sep 16 2015 Dave Airlie <airlied@redhat.com> - 1:1.0.12-0.2
- 1.18 ABI rebuild

* Wed Jul 29 2015 Dave Airlie <airlied@redhat.com> 1.0.12-0.1
- bump to latest git for ABI changes.

* Wed Jul 29 2015 Dave Airlie <airlied@redhat.com> - 1:1.0.11-5
- 1.15 ABI rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Dave Airlie <airlied@redhat.com> 1.0.11-3
- force hardened build off.

* Wed Feb 11 2015 Hans de Goede <hdegoede@redhat.com> - 1:1.0.11-2
- xserver 1.17 ABI rebuild

* Fri Sep 05 2014 Ben Skeggs <bskeggs@redhat.com> 1.0.11-1
- add upstream 1.0.11 release

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Hans de Goede <hdegoede@redhat.com> - 1:1.0.10-5
- xserver 1.15.99.903 ABI rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Hans de Goede <hdegoede@redhat.com> - 1:1.0.10-3
- xserver 1.15.99-20140428 git snapshot ABI rebuild

* Thu Apr 17 2014 Hans de Goede <hdegoede@redhat.com> - 1.0.10-2
- Add patches for server managed fd support
- Rebuild for xserver 1.15.99.902

* Sun Mar 02 2014 Ben Skeggs <bskeggs@redhat.com> 1.0.10-1
- add upstream 1.0.10 release

* Mon Jan 13 2014 Adam Jackson <ajax@redhat.com> - 1:1.0.9-7
- 1.15 ABI rebuild

* Tue Dec 17 2013 Adam Jackson <ajax@redhat.com> - 1:1.0.9-6
- 1.15RC4 ABI rebuild

* Wed Nov 20 2013 Adam Jackson <ajax@redhat.com> - 1:1.0.9-5
- 1.15RC2 ABI rebuild

* Wed Nov 06 2013 Adam Jackson <ajax@redhat.com> - 1:1.0.9-4
- 1.15RC1 ABI rebuild

* Fri Oct 25 2013 Adam Jackson <ajax@redhat.com> - 1:1.0.9-3
- ABI rebuild

* Tue Oct 22 2013 Kyle McMartin <kyle@fedoraproject.org> 1.0.9-3
- Remove artificial kernel-drm-nouveau Requires, which dates from when
  nouveau.ko was out of tree.

* Wed Jul 31 2013 Dave Airlie <airlied@redhat.com> 1.0.9-2
- fix powerpc build - fix name collisions in randr

* Tue Jul 30 2013 Dave Airlie <airlied@redhat.com> 1.0.9-1
- add upstream 1.0.9 release - fixes dual head offload + nvf0 support

* Fri Apr 12 2013 Dave Airlie <airlied@redhat.com> 1.0.7-1
- add upstream 1.0.7 release

* Tue Mar 19 2013 Adam Jackson <ajax@redhat.com> 1.0.6-7
- Less RHEL customization

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1:1.0.6-6
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1:1.0.6-5
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1:1.0.6-4
- ABI rebuild

* Thu Jan 10 2013 Adam Jackson <ajax@redhat.com> 1.0.6-3
- Obsoletes: nv in F19 and up

* Thu Jan 10 2013 Adam Jackson <ajax@redhat.com> - 1:1.0.6-2
- ABI rebuild

* Mon Jan 07 2013 Ben Skeggs <bskeggs@redhat.com> 1.0.6-1
- nouveau 1.0.6

* Fri Nov 09 2012 Ben Skeggs <bskeggs@redhat.com> 1.0.4-1
- nouveau 1.0.4

* Thu Oct 25 2012 Dave Airlie <airlied@redhat.com> 1.0.3-1
- nouveau 1.0.3 - fix shadowfb crash

* Wed Sep 12 2012 Adam Jackson <ajax@redhat.com> 1.0.2-1
- nouveau 1.0.2

* Fri Aug 17 2012 Dave Airlie <airlied@redhat.com> 1.0.1-6
- fix dri2 tfp rendering since prime support broke it.

* Thu Aug 16 2012 Dave Airlie <airlied@redhat.com> 1.0.1-5
- upstream snapshot + prime support

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 18 2012 Dave Airlie <airlied@redhat.com> - 1:1.0.1-3
- ABI rebuild

* Mon Jul 02 2012 Karsten Hopp <karsten@redhat.com> 1.0.1-2
- we don't have vbe.h and xf86int10.h in xorg-x11-server-devel for ppc(64)

* Tue Jun 19 2012 Ben Skeggs <bskeggs@redhat.com> 1.0.1-1
- nouveau 1.0.1

* Mon Jun 18 2012 Ben Skeggs <bskeggs@redhat.com> 1.0.0-1
- nouveau 1.0.0

* Thu Jun 14 2012 Ben Skeggs <bskeggs@redhat.com> 0.0.16-39.20120426git174f170
- Drop explicit Requires on libudev

* Tue Jun 05 2012 Adam Jackson <ajax@redhat.com> 0.0.16-38.20120426git174f170
- Rebuild for new libudev
- Conditional BuildReqs for {libudev,systemd}-devel

* Thu Apr 26 2012 Dave Airlie <airlied@redhat.com> 1:0.0.16-37.20120426git174f170
- rebase to master

* Thu Apr 05 2012 Adam Jackson <ajax@redhat.com> - 1:0.0.16-36.20120306gitf5d1cd2
- RHEL arch exclude updates

* Tue Mar 06 2012 Ben Skeggs <bskeggs@redhat.com> - 1:0.0.16-35.20120306gitf5d1cd2
- pull in latest upstream code

* Sat Feb 11 2012 Peter Hutterer <peter.hutterer@redhat.com> - 1:0.0.16-34.20110720gitb806e3f
- ABI rebuild

* Fri Feb 10 2012 Peter Hutterer <peter.hutterer@redhat.com> - 1:0.0.16-33.20110720gitb806e3f
- ABI rebuild

* Tue Jan 24 2012 Peter Hutterer <peter.hutterer@redhat.com> - 1:0.0.16-32.20110720gitb806e3f
- ABI rebuild

* Tue Jan 03 2012 Peter Hutterer <peter.hutterer@redhat.com> - 1:0.0.16-31.20110720gitb806e3f
- Rebuild for server 1.12
