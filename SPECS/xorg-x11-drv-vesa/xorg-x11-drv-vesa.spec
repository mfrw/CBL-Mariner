%global tarball xf86-video-vesa
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir	%{moduledir}/drivers

%undefine _hardened_build

Summary:   Xorg X11 vesa video driver
Name:      xorg-x11-drv-vesa
Version:   2.4.0
Release:   12%{?dist}
URL:       https://www.x.org
Source0:   https://xorg.freedesktop.org/releases/individual/driver/%{tarball}-%{version}.tar.bz2
License: MIT

Patch1:     0001-Disable-shadow-by-default-on-known-virtual-GPUs.patch
Patch2:     0001-Refuse-to-run-on-UEFI-machines.patch
ExclusiveArch: %{ix86} x86_64

BuildRequires: make
BuildRequires: xorg-x11-server-devel >= 1.10.99.902
BuildRequires: autoconf automake libtool

Requires: Xorg %([ -e /usr/bin/xserver-sdk-abi-requires ] && xserver-sdk-abi-requires ansic)
Requires: Xorg %([ -e /usr/bin/xserver-sdk-abi-requires ] && xserver-sdk-abi-requires videodrv)
Requires: xorg-x11-server-wrapper

%description 
X.Org X11 vesa video driver.

%prep
%autosetup -p1 -n %{tarball}-%{version}

%build
autoreconf -v --install || exit 1
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%files
%{driverdir}/vesa_drv.so
%{_mandir}/man4/vesa.4*

%changelog
* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 10:25:29 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 2.4.0-10
- Add BuildRequires for make

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Dave Airlie <airlied@redhat.com> - 2.4.0-6
- Refuse to run in UEFI systems

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Adam Jackson <ajax@redhat.com> - 2.4.0-3
- Rebase virt/shadow patch
- Drop ancient 24bpp awareness, 1.20 no longer has any

* Mon Apr 02 2018 Adam Jackson <ajax@redhat.com> - 2.4.0-2
- Rebuild for xserver 1.20

* Fri Feb 23 2018 Adam Jackson <ajax@redhat.com> - 2.4.0-1
- vesa 2.4.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 29 2016 Hans de Goede <hdegoede@redhat.com> - 2.3.2-25
- Rebuild against xserver-1.19

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Peter Hutterer <peter.hutterer@redhat.com>
- Remove unnecessary defattr

* Wed Jan 20 2016 Peter Hutterer <peter.hutterer@redhat.com>
- s/define/global/

* Wed Jul 29 2015 Dave Airlie <airlied@redhat.com> - 2.3.2-23
- 1.15 ABI rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Dave Airlie <airlied@redhat.com> 2.3.2-21
- drop hardened builds for vesa

* Wed Feb 11 2015 Hans de Goede <hdegoede@redhat.com> - 2.3.2-20
- xserver 1.17 ABI rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Hans de Goede <hdegoede@redhat.com> - 2.3.2-18
- xserver 1.15.99.903 ABI rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Hans de Goede <hdegoede@redhat.com> - 2.3.2-16
- xserver 1.15.99-20140428 git snapshot ABI rebuild

* Mon Jan 13 2014 Adam Jackson <ajax@redhat.com> - 2.3.2-15
- 1.15 ABI rebuild

* Tue Dec 17 2013 Adam Jackson <ajax@redhat.com> - 2.3.2-14
- 1.15RC4 ABI rebuild

* Wed Nov 20 2013 Adam Jackson <ajax@redhat.com> - 2.3.2-13
- 1.15RC2 ABI rebuild

* Wed Nov 06 2013 Adam Jackson <ajax@redhat.com> - 2.3.2-12
- 1.15RC1 ABI rebuild

* Fri Oct 25 2013 Adam Jackson <ajax@redhat.com> - 2.3.2-11
- ABI rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Dave Airlie <airlied@redhat.com> 2.3.2-9
- autoreconf for aarch64

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 2.3.2-8
- require xorg-x11-server-devel, not -sdk

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 2.3.2-7
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 2.3.2-6
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 2.3.2-5
- ABI rebuild

* Thu Jan 10 2013 Adam Jackson <ajax@redhat.com> - 2.3.2-4
- ABI rebuild

* Wed Aug 15 2012 Adam Jackson <ajax@redhat.com> 2.3.2-3
- Only build on arches where xserver builds VBE support

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 18 2012 Dave Airlie <airlied@redhat.com> 2.3.2-1
- vesa 2.3.2

* Thu Apr 26 2012 Adam Jackson <ajax@redhat.com> 2.3.1-1
- vesa 2.3.1

* Thu Apr 05 2012 Adam Jackson <ajax@redhat.com> - 2.3.0-16
- RHEL arch exclude updates

* Sat Feb 11 2012 Peter Hutterer <peter.hutterer@redhat.com> - 2.3.0-15
- ABI rebuild

* Fri Feb 10 2012 Peter Hutterer <peter.hutterer@redhat.com> - 2.3.0-14
- ABI rebuild

* Tue Jan 24 2012 Peter Hutterer <peter.hutterer@redhat.com> - 2.3.0-13
- ABI rebuild

* Wed Jan 04 2012 Peter Hutterer <peter.hutterer@redhat.com> - 2.3.0-12
- Rebuild for server 1.12

* Mon Nov 14 2011 Adam Jackson <ajax@redhat.com> - 2.3.0-11
- ABI rebuild

* Thu Nov 10 2011 Adam Jackson <ajax@redhat.com> 2.3.0-10
- vesa-2.3.0-git.patch: Sync with git for new ABI.

* Thu Aug 18 2011 Adam Jackson <ajax@redhat.com> - 2.3.0-9
- Rebuild for xserver 1.11 ABI

* Wed May 11 2011 Peter Hutterer <peter.hutterer@redhat.com> - 2.3.0-8
- Rebuild for server 1.11

* Mon Feb 28 2011 Peter Hutterer <peter.hutterer@redhat.com> - 2.3.0-7
- Rebuild for server 1.10

* Mon Feb 21 2011 Adam Jackson <ajax@redhat.com> 2.3.0-6
- vesa-2.3.0-no-virt-shadowfb.patch: Disable shadowfb on virt hardware, just
  makes things slower.
- vesa-2.3.0-kms-anathema.patch: Refuse to bind to devices with a kernel
  driver.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 02 2010 Peter Hutterer <peter.hutterer@redhat.com> - 2.3.0-4
- Rebuild for server 1.10

* Wed Oct 27 2010 Adam Jackson <ajax@redhat.com> 2.3.0-3
- Add ABI requires magic (#542742)

* Mon Oct 11 2010 Adam Jackson <ajax@redhat.com> 2.3.0-2
- vesa-2.3.0-24bpp-sucks.patch: Prefer 16bpp to 24bpp. (#533879)

* Mon Jul 05 2010 Dave Airlie <airlied@redhat.com> 2.3.0-1
- pull in latest vesa

* Mon Jul 05 2010 Peter Hutterer <peter.hutterer@redhat.com> - 2.2.1-3
- rebuild for X Server 1.9

* Thu Jan 21 2010 Peter Hutterer <peter.hutterer@redhat.com> - 2.2.1-2
- Rebuild for server 1.8

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 2.2.1-1
- vesa 2.2.1

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 2.2.0-3.1
- ABI bump

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Adam Jackson <ajax@redhat.com> 2.2.0-2
- Check VBE PanelID if DDC fails.

* Tue Feb 17 2009 Adam Jackson <ajax@redhat.com> 2.2.0-1
- vesa 2.2.0

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 2.1.0-1
- Update to new upstream release

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 2.0.0-2
- bump for new server API

* Tue Jul 01 2008 Adam Jackson <ajax@redhat.com> 2.0.0-1
- vesa 2.0.0

* Tue Apr 29 2008 Adam Jackson <ajax@redhat.com> 1.3.0-15.20080404
- vesa-1.9-32bpp-dammit.patch: Prefer 24+32 instead of 24+24. (#427383)

* Fri Apr 04 2008 Adam Jackson <ajax@redhat.com> 1.3.0-14.20080404
- Today's git snapshot for FTBFS and other.  (#440720)

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.0-13.20071113
- Autorebuild for GCC 4.3

* Tue Jan 08 2008 Adam Jackson <ajax@redhat.com> 1.3.0-12.20071113
- Rebuild for new ABI.

* Tue Nov 13 2007 Adam Jackson <ajax@redhat.com> 1.3.0-11.20071113
- Update to git snapshot for pciaccess goodness.
- Rip out legacy framebuffer support.

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> - 1.3.0-10
- Rebuild for ppc toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 1.3.0-9
- Update Requires and BuildRequires.

* Thu May 31 2007 Adam Jackson <ajax@redhat.com> 1.3.0-8
- vesa-1.3.0-mode-heuristics.patch: Fix a typo that would crash on
  some cards. (#241491)

* Wed May 09 2007 Adam Jackson <ajax@redhat.com> 1.3.0-6
- Re-add the sync range hack. (#235066)

* Tue Mar 20 2007 Adam Jackson <ajax@redhat.com> 1.3.0-5
- vesa-1.3.0-mode-heuristics.patch: If strict intersection of VBE and EDID
  modes leaves no modes remaining after validation, try again with just
  range and VBE checks.  Replaces earlier range-hack and validmode patches.

* Tue Feb 27 2007 Adam Jackson <ajax@redhat.com> 1.3.0-4
- vesa-1.3.0-range-hack.patch: Work around broken ATI video BIOSes.
- Disown the module dir
- Fix the License

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 1.3.0-3
- ExclusiveArch -> ExcludeArch

* Wed Jan 24 2007 Adam Jackson <ajax@redhat.com> 1.3.0-2
- vesa-1.2.1-validmode.patch: Strictly limit runtime modes to the intersection
  of the BIOS and DDC lists, if a DDC list exists; fixes cases where we'd
  choose 1600x1200 on 1680x1050 panel.  Conversely, be more forgiving when
  validating the resulting set against the sync ranges; fixes 640x480 syndrome
  when the monitor has broken DDC.  Don't be deceived though, vesa still sucks.

* Mon Dec 4 2006 Adam Jackson <ajax@redhat.com> 1.3.0-1
- Update to 1.3.0
- vesa-1.2.1-validmode.patch: Implement a ValidMode driver hook, which rejects
  modes not present in the BIOS or outside the capability of the monitor.

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 1.2.1-4
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Adam Jackson <ajackson@redhat.com> 1.2.1-3
- vesa-1.2.1-fix-shadowfb.patch: Fix massive performance regression relative
  to FC5.

* Fri Jul 28 2006 Adam Jackson <ajackson@redhat.com> 1.2.1-2
- vesa-1.2.1-randr-crash.patch: Fix a RANDR crash.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 1.2.1-1.1
- rebuild

* Sat Jun 17 2006 Mike A. Harris <mharris@redhat.com> 1.2.1-1
- Updated to version 1.2.1 for X11R7.1 server.

* Tue Jun 13 2006 Adam Jackson <ajackson@redhat.com> 1.2.0-2
- Build on ppc64

* Tue May 30 2006 Adam Jackson <ajackson@redhat.com> 1.2.0-1
- Update to 1.2.0 from 7.1.

* Sun Apr 09 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-1
- Update to 1.1.0 from 7.1RC1.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 1.0.1.3-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 1.0.1.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.1.3-1
- Updated xorg-x11-drv-vesa to version 1.0.1.3 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 1.0.1.2-1
- Updated xorg-x11-drv-vesa to version 1.0.1.2 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.1-1
- Updated xorg-x11-drv-vesa to version 1.0.1 from X11R7 RC2

* Fri Nov 04 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.1-1
- Updated xorg-x11-drv-vesa to version 1.0.0.1 from X11R7 RC1
- Fix *.la file removal.

* Tue Oct 04 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Limit "ExclusiveArch" to x86, x86_64 ia64 ppc alpha sparc sparc64

* Fri Sep 02 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-0
- Initial spec file for vesa video driver generated automatically
  by my xorg-driverspecgen script.
