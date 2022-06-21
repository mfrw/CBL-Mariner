#
# spec file for package xf86-input-synaptics
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           xf86-input-synaptics
Version:        1.9.1
Release:        3.10
Summary:        Synaptics touchpad input driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
Patch0:         n_xf86-input-synaptics-wait.patch
Patch2:         n_xf86-input-synaptics-xorg.conf.d_snippet.patch
Patch5:         n_xf86-input-synaptics-default-tap.patch
BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(libevdev) >= 1.0.99.1
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(recordproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi) >= 1.2
# BuildRequires:  pkgconfig(xorg-macros) >= 1.13
BuildRequires:  pkgconfig(xorg-server) >= 1.7
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtst)
Requires:       udev
# This was part of the xorg-x11-driver-input package up to version 7.6
Conflicts:      xorg-x11-driver-input <= 7.6
Provides:       x11-input-synaptics = %{version}
Obsoletes:      x11-input-synaptics < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x
# %x11_abi_xinput_req

%description
synaptics is an Xorg input driver for touchpads.

Even though touchpads can be handled by the normal evdev or mouse
drivers, this driver allows more advanced features of the touchpad to
become available.

%package devel
Summary:        Synaptics touchpad input driver for the Xorg X server -- Development Files
Group:          Development/Libraries/X11

%description devel
synaptics is an Xorg input driver for touchpads.

Even though touchpads can be handled by the normal evdev or mouse
drivers, this driver allows more advanced features of the touchpad to
become available.

%prep
%setup -q
%patch0 -p1
%patch2 -p1
%patch5 -p1

%build
autoreconf -fiv
%configure \
  --with-xorg-conf-dir=%{_datadir}/X11/xorg.conf.d/
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%post
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change || :

%postun
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change || :

%files
%defattr(-,root,root)
%doc COPYING README
%dir %{_datadir}/X11/xorg.conf.d/
%{_datadir}/X11/xorg.conf.d/70-synaptics.conf
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/input/synaptics_drv.so
%{_bindir}/synclient
%{_bindir}/syndaemon
# %{_datadir}/man/man1/synclient.1%{?ext_man}
# %{_datadir}/man/man1/syndaemon.1%{?ext_man}
# %{_datadir}/man/man4/synaptics.4%{?ext_man}
%{_datadir}/man

%files devel
%defattr(-,root,root)
%{_includedir}/xorg/synaptics-properties.h
%{_libdir}/pkgconfig/xorg-synaptics.pc

%changelog
* Thu May 28 2020 Stefan Dirsch <sndirsch@suse.com>
- devel package: removed requires to main package, since it's not
  required at all for development (boo#1172153)
* Tue Jul 30 2019 Stefan Dirsch <sndirsch@suse.com>
-  move xorg.conf.d snippet from /etc/X11/xorg.conf.d to
  /usr/share/X11/xorg.conf.d (boo#1139692)
* Wed May 30 2018 sndirsch@suse.com
-  Update to version 1.9.1:
  * A few build system janitorial things, a compatibility patch
    by Luca and one patch to avoid log spam when the device goes
    away (and before udev tells us that it's gone).
* Tue May 30 2017 sndirsch@suse.com
- includes everything needed for missing sle issue entries:
  fate #315643-315645, 319159-319161, 319618 (bsc#1041556)
* Sat Nov 19 2016 tobias.johannes.klausmann@mni.thm.de
- Update to version 1.9.0:
  This release supports the X server 1.19.
* Fri Oct 28 2016 tobias.johannes.klausmann@mni.thm.de
- Update to version 1.8.99.2:
  + Remove upstream patch U_conf-rename-to-70-synaptics.conf.patch
  + Adapt n_xf86-input-synaptics-wait.diff
* Mon May 23 2016 sndirsch@suse.com
- replaced n_conf-rename-to-70-synaptics.conf.patch with upstreamed
  patch U_conf-rename-to-70-synaptics.conf.patch (boo #979554)
* Thu May 19 2016 sndirsch@suse.com
- n_conf-rename-to-70-synaptics.conf.patch
  * bump up synaptics driver to 70, so it get's preferred over
    libinput, which was dropped down to 060 (boo #979554)
- adjusted n_xf86-input-synaptics-default-tap.diff,
  n_xf86-input-synaptics-xorg.conf.d_snippet.diff
- removed Supplements: xorg-x11-server, so the driver no longer
  gets installed by default
* Fri Nov 13 2015 mpluskal@suse.com
- Add gpg signature
- Make building more verbose
* Mon Nov  2 2015 sndirsch@suse.com
- Update to version 1.8.3
  * With Gabriele's fix, the order of fingers on the touchpad doesn't
    matter for two-finger scrolling. Previously, only one of the
    fingers would trigger scroll events. See
    https://bugs.freedesktop.org/show_bug.cgi?id=92622
* Fri Jul 31 2015 jengelh@inai.de
- Ignore absence of udevadm, it won't be present in the build env.
* Tue Mar 31 2015 sndirsch@suse.com
- Update to version 1.8.2:
  * One significant change here: an artificial delay is now used
    between the button events of a doubletap. Some applications
    previously dropped the events because they had the same
    timestamp, with the delay this should now work fine.
* Sun Sep 21 2014 tobias.johannes.klausmann@mni.thm.de
- Update to version 1.8.1:
  A couple of coverity-induced fixes, the
  top software buttons are now 15%% and better detection of two-finger
  taps. A couple of misc other fixes, the only oddity in there is a
  fix for clock drift - if you had clickpad clicks delayed by a
  second or so after a number of suspend/resume cycles then you may
  want to upgrade to this version.
* Tue May 13 2014 sndirsch@suse.com
- Update to version 1.8.0
  * final release; changes since 1.7.99.2:
    + conf: drop the PNPID matching from the fdi file
* Wed May  7 2014 sndirsch@suse.com
- Update to version 1.7.99.2
  * The second snapshot for synaptics 1.8 is now available. Note
    that there are are two significant changes:
  - the event device is not grabbed anymore. In some setups this
    may lead to duplicate events but where it does you're really
    better off using an InputClass instead of an InputDevice
    section in your xorg.conf.
  - the secondary software button area (i.e. the top software
    buttons on the Lenovo *40 series) is now automatically
    enabled based on the INPUT_PROP_TOPBUTTONPAD property,
    slated for kernel 3.15. No more PNPID matching in the
    snippets, which didn't work without a kernel patch anyway.
    If you can't update the kernel, use Option
    "HasSecondarySoftButtons" "on".
* Mon Mar 17 2014 hrvoje.senjan@gmail.com
- Update to version 1.7.99.1:
  - libevdev support:
    The evdev backend on Linux now uses libevdev. We recommend
    to use libevdev 1.1-rc1 or later as the synaptics driver is
    very likely to trigger SYN_DROPPED and we've fixed a bunch
    of issues in libevdev 1.1.
  - Support for T440, T540, X240, Helix, Yoga:
  The bulk of the changes is to support this set of Lenovo
  touchpads. These touchpads don't have separate physical
  buttons for the trackstick and need to be emulated as
  software-button by the driver.
  - TouchpadOff behaviour change:
  Synaptics has a property "Synaptics Off" to disable events.
  Previously, this disabled any event from the touchpad.
  Now, physical button clicks are allowed even when the
  touchpad is disabled.
  - mtdev was dropped:
  There are no touchpad drivers in the kernel tree that
  use protocol A, so using mtdev is just a computationally
  expensiv and memory-wasting noop.
- As per upstream change, swap pkgconfig(mtdev) BuildRequires for
  pkgconfig(evdev) >= 1.0.99.1
- Rebase n_xf86-input-synaptics-wait.diff for this release
* Wed Mar 12 2014 tobias.johannes.klausmann@mni.thm.de
- Update to version 1.7.4:
  One fix: closing the fd again if the device cannot be enabled
  properly, and two reverts: scrollbuttons and circular pad
  support are making a comeback. Apparently there are still a
  few laptops out there that require either feature.
* Thu Feb 20 2014 sndirsch@suse.com
- n_xf86-input-synaptics-xorg.conf.d_snippet.diff: disable
  "HorizEdgeScroll" instead of setting "HorizScrollDelta" to 0
  (bnc#864664, fdo#75074)
- adapted n_xf86-input-synaptics-default-tap.diff
* Mon Jan 13 2014 sndirsch@suse.com
- Update to version 1.7.3
  * Just one fix for the stable branch, fixing the #define for
    server 1.15 (and newer). A bad ABI detection check enabled
    driver scaling on input ABI 20, causing sluggish pointer
    behaviour.
* Mon Dec  9 2013 tobias.johannes.klausmann@mni.thm.de
- Update to version 1.7.2:
  Three patches on top of the previous release, the first of which
  enables proper driver scaling when running against new servers. If
  you're using the server from git, both driver and server would
  scale, resulting in a sluggish touchpad.
* Mon Dec  2 2013 eich@suse.com
- renamed:
  * xf86-input-synaptics-xorg.conf.d_snippet.diff ->
    n_xf86-input-synaptics-xorg.conf.d_snippet.diff
  * xf86-input-synaptics-wait.diff ->
    n_xf86-input-synaptics-wait.diff
  * xf86-input-synaptics-default-tap.diff ->
    n_xf86-input-synaptics-default-tap.diff
  to indicate that these are SUSE specific patches.
* Tue May 14 2013 tobias.johannes.klausmann@mni.thm.de
- Update to version 1.7.1:
  First stable update to synaptics 1.7 is now available.
- User-visible changes:
  + soft button areas may overlap on the edge, so a configuration of
    e.g.middle button 33%%-66%% and right button 66%%-0 is now valid.
  + man page fix to avoid confusion between 0 and 0%% on button configuration
  This release also includes the fix for stack smash caused by Apple
  MagicTrackpads.
* Tue Apr  2 2013 tobias.johannes.klausmann@mni.thm.de
- Update to version 1.7.0:
  This release has seen a bunch of purges in the hope that it will make the
  code more maintainable. Most of the features dropped are expected to have
  few or no users, or hardware that hasn't been around for ages.
  Most other fixes have found their way into the 1.6 branch already.
* Mon Feb  4 2013 sndirsch@suse.com
- xf86-input-synaptics 1.6.3
  * Compared to 1.6.2, we've had a memory leak fixed, better
    behaviour for synaptics soft buttons and, most importantly,
    a fix to reset the touch state after suspend.
- obsoletes xf86-input-synaptics-Reset-num_active_touches-on-DeviceOff-52496.patch
* Sat Jan 19 2013 tchvatal@suse.com
- Use tapTwoFingers and tapThreeFingers for leftMouse and
  middleMouse click respectively. (bnc#799455)
* Fri Jan  4 2013 sndirsch@suse.com
- xf86-input-synaptics-Reset-num_active_touches-on-DeviceOff-52496.patch
  * Reset num_active_touches on DeviceOff (bnc#779452, fdo#52496)
* Thu Jul 26 2012 tiwai@suse.de
- Drop broken LED double-tap patches (bnc#768506,bnc#765524)
* Fri Jun 29 2012 tiwai@suse.de
- Fix double-tap LED behavior (bnc#768506)
- Enable tap-to-click as default (bnc#722457)
* Thu Jun 14 2012 tobias.johannes.klausmann@mni.thm.de
- Update to version 1.6.2
  + #49439: out-of-bounds access if a touch was active at driver init
  + #49965: disallow scroll distances on 0 to avoid division by 0
  + Fix coasting for negative scroll deltas
  + More fixes to avoid jumpy cursors on resume
* Wed Jun  6 2012 tiwai@suse.de
- Remove obsoleted patches and revive LED double-tap (bnc#765524)
  * Remove obsoleted clickpad patches:
    xf86-input-synaptics-add-clickpad-support.diff
    xf86-input-synaptics-fix-clickpad-capabilities.diff
    xf86-input-synaptics-clickpad-doc-update.diff
  * Remove obsoleted stability patches:
    xf86-input-synaptics-filter-bogus-coord.diff
    xf86-input-synaptics-move-threshold.diff
  * Revive LED double-tap patch:
    xf86-input-synaptics-led-double-tap.diff
* Fri May 11 2012 vuntz@opensuse.org
- Update to version 1.6.1:
  + Fix wrong conversion causing coasting to be triggered on almost
    all scroll events.
  + Fix bug where, on clickpads, moving the clicking finger out of
    the soft button area caused erroneous button events.
- Rebase xf86-input-synaptics-wait.diff,
  xf86-input-synaptics-add-clickpad-support.diff,
  xf86-input-synaptics-add-led-support.diff,
  xf86-input-synaptics-fix-clickpad-capabilities.diff,
  xf86-input-synaptics-filter-bogus-coord.diff: this is needed
  because of whitespace changes in the code.
* Wed May  9 2012 vuntz@opensuse.org
- Update to version 1.6.0:
  + Fix coasting for negative scroll directions.
  + Fix issues on resuming after suspend.
  + Documentation fixes.
  + Build fixes.
- Changes from version 1.5.99.904:
  + Ensure hw millis are monotonic.
  + Don't release the button on TS_3 if TapAndDrag is disabled.
  + Various scroll-related fixes.
  + Various coasting-related fixes.
  + Several other bug fixes.
- Rebase xf86-input-synaptics-clickpad-doc-update.diff and
  xf86-input-synaptics-filter-bogus-coord.diff.
* Mon Apr 23 2012 dimstar@opensuse.org
- Disable xf86-input-synaptics-move-threshold.diff: having this
  patch enabled and touching the pad resets X.
* Thu Apr 19 2012 dimstar@opensuse.org
- Update to version 1.5.99.903:
  + Support inverted scroll direction.
  + Use maximum number of touches reported by evdev
  + Don't count fingers twice when guessing distance (fdo#48316)
  + Replace hardcoded max number of touches with a define.
  + Check touch record bounds before access
  + Do not perform a tap action when more than three touches
  + Count number of multitouch touches for multitouch finger count
  + conf: the bcm5974 doesn't have Apple in the product name
- Drop patches:
  + xf86-input-synaptics-settings.diff
  + xf86-input-synaptics-led-double-tap.diff
  + xf86-input-synaptics-clickpad-threshold.diff
- Rebased patches:
  + xf86-input-synaptics-add-clickpad-support.diff
  + xf86-input-synaptics-add-led-support.diff
  + xf86-input-synaptics-fix-clickpad-capabilities.diff
  + xf86-input-synaptics-move-threshold.diff
  + xf86-input-synaptics-filter-bogus-coord.diff
- Add pkgconfig(mtdev) BuildRequires: new dependency.
- Use %%x11_abi_xinput_req instead of static ABI Requires.
* Wed Apr 18 2012 vuntz@opensuse.org
- Split xf86-input-synaptics from xorg-x11-driver-input.
  Initial version: 1.5.0.
