#
# spec file for package gnome-themes
#
# Copyright (c) 2021 SUSE LLC
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


Name:           gnome-themes
Version:        3.0.0
Release:        1%{?dist}
Summary:        GNOME Themes
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://www.gnome.org/
Source0:        http://download.gnome.org/sources/%{name}/3.0/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM gnome-themes-disable-engine-test.patch bgo#642970 fcrozat@novell.com -- don't check for gtk-engines-3 at build time
Patch0:         gnome-themes-disable-engine-test.patch
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gtk3-devel
BuildRequires:  icon-naming-utils
BuildRequires:  intltool
BuildRequires:  hicolor-icon-theme
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

BuildArch:      noarch

%description
GNOME themes, including Ximian Industrial and selected background
images.

%prep
%setup -q
%patch0 -p1

%build
#needed by patch0
autoreconf -fiv

%configure\
        --enable-all-themes
make %{?_smp_mflags}

%install
%make_install
%if 0%{?suse_version} <= 1120
rm %{buildroot}%{_datadir}/locale/en@shaw/LC_MESSAGES/*
%endif
# remove themes which are now in gnome-themes-standard
rm -rf %{buildroot}%{_datadir}/themes/{HighContrast,HighContrast-SVG,HighContrastInverse}
rm -rf %{buildroot}%{_datadir}/icons/{HighContrast,HighContrast-SVG,HighContrastInverse}

%post
%icon_theme_cache_post Crux
%icon_theme_cache_post HighContrastLargePrint
%icon_theme_cache_post HighContrastLargePrintInverse
%icon_theme_cache_post LargePrint
%icon_theme_cache_post Mist

# No need for %%icon_theme_cache_postun in %%postun since the theme won't exist anymore

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%ghost %{_datadir}/icons/*/icon-theme.cache
%{_datadir}/icons/Crux/
%{_datadir}/icons/HighContrastLargePrint/
%{_datadir}/icons/HighContrastLargePrintInverse/
%{_datadir}/icons/LargePrint/
%{_datadir}/icons/Mist/
%{_datadir}/themes/Clearlooks/
%{_datadir}/themes/ClearlooksClassic/
%{_datadir}/themes/Crux/
%{_datadir}/themes/Glider/
%{_datadir}/themes/Glossy/
%{_datadir}/themes/HighContrastLargePrint/
%{_datadir}/themes/HighContrastLargePrintInverse/
%{_datadir}/themes/Inverted/
%{_datadir}/themes/LargePrint/
%{_datadir}/themes/LowContrast/
%{_datadir}/themes/LowContrastLargePrint/
%{_datadir}/themes/Mist/
%{_datadir}/themes/Simple/
/usr/share/locale

%changelog
* Thu Sep 16 2021 sbrabec@suse.com
- Remove obsolete translation-update-upstream support
  (jsc#SLE-21105).
* Sat Jan 25 2020 dimstar@opensuse.org
- No longer recommend -lang: supplements are in use
* Wed Feb 28 2018 dimstar@opensuse.org
- Modernize spec-file by calling spec-cleaner
* Fri May 27 2016 idonmez@suse.com
- Update to GNOME 3.20.2 FATE#318572
* Wed Oct  1 2014 dimstar@opensuse.org
- Use autoreconf -fiv instead of plain autoreconf.
* Tue Jul 22 2014 dimstar@opensuse.org
- Drop gnome-icon-theme Requires: no longer functional after the
  merging of the themes into Adwaita theme, which in turn is a
  dependency to GTK+ 3.0.
* Fri Mar 29 2013 dimstar@opensuse.org
- Use full URL for source
* Sat Jul 21 2012 dimstar@opensuse.org
- Split out -lang package (bnc#645077).
* Fri Dec  2 2011 coolo@suse.com
- add automake as buildrequire to avoid implicit dependency
* Wed Apr  6 2011 fcrozat@novell.com
- Update to version 3.0.0:
  + No code changes, just bumping to 3.0.0 for posterity.
- Changes from version 2.91.91:
  + Add notice of impending obsoletion to README file.
  + Updated translations.
- Changes from version 2.91.90:
  + Updated translations.
- Changes from version 2.91.5:
  + Updated translations.
- Changes from version 2.91.2:
  + Switch to GTK+ 3.0
  + Updated translations.
- Add gnome-themes-disable-engine-test.patch: do not rely on
  obsolete gtk-engines-3.pc for build.
- Add gtk3-devel to BuildRequires and remove gtk2-devel and
  gtk2-engines-devel.
* Tue Mar  8 2011 fcrozat@novell.com
- Remove themes which moved to gnome-themes-standard
* Mon Feb 14 2011 sbrabec@suse.cz
- Added support for translation-update-upstream.
* Tue Nov 16 2010 dimstar@opensuse.org
- Update to version 2.32.1:
  + Updated translations.
* Tue Sep 28 2010 vuntz@opensuse.org
- Update to version 2.32.0:
  + No change, just a version bump to stable version.
* Wed Aug 25 2010 vuntz@opensuse.org
- Use the %%icon_theme_cache_* macros to make sure the icon theme
  cache is created/updated.
* Tue Aug 17 2010 dimstar@opensuse.org
- Update to version 2.31.90:
  + Updated translations.
* Fri Aug  6 2010 vuntz@opensuse.org
- Update to version 2.31.6:
  + Updated translations.
* Thu Jul  8 2010 dimstar@opensuse.org
- Update to version 2.31.4:
  + Fix evolution table header workaround for new evo versions.
  + bgo#614343: Fix title vertical geometry in Clearlooks metacity
    theme.
  + bgo#490176: Use large cursors with large print themes
- Changes from previous versions:
  + Add some high contrast icons for Firefox and Thunderbird.
  + Add pidgin icons to HCLP, HCLPI and HCSVG themes.
  + Add gtkam icons to HCLP and HCLPI themes.
  + Add PDA icons to HCLP and HCLPI themes.
  + opy some status icons over from HCLPI that weren't in HCLP.
  + bgo#140773: Add HCLP and HCLPI versions of gnome-netstatus
    icons.
* Thu Apr 29 2010 dimstar@opensuse.org
- Update to version 2.30.1:
  + Copy some status icons over from HCLPI that weren't in HCLP
  + bgo#140773: Add HCLP and HCLPI versions of gnome-netstatus
    icons
  + bgo#580558: Tidy up Type information in high contrast
    index.theme files, which was causing some icons to appear
    larger than intended
  + Updated translations.
* Tue Mar 30 2010 vuntz@opensuse.org
- Update to version 2.30.0:
  + Updated translations.
* Mon Mar  8 2010 dimstar@opensuse.org
- Update to version 2.29.92:
  + Set some GtkHTML colors in the HC inverse themes (used in eg.
    evolution)
  + Set link colors for Pidgin inside HC inverse themes
  + Updated translations.
* Tue Feb 23 2010 vuntz@opensuse.org
- Update to version 2.29.91:
  + Updated translations.
* Mon Jan 25 2010 captain.magnus@opensuse.org
- Update to version 2.29.6:
  + Translation updates
* Wed Dec  2 2009 vuntz@opensuse.org
- Update to version 2.29.2:
  + Fixes from 2.28.1.
  + Updated translations.
* Sat Nov 14 2009 vuntz@opensuse.org
- Update to version 2.28.1:
  + Use gnome icon theme for LowContrastLargePrint desktop theme.
  + Update symlinks to match f.d.o. icon naming spec.
* Wed Sep 23 2009 dimstar@opensuse.org
- Update to version 2.28.0:
  + Updated translations.
* Wed Sep  9 2009 vuntz@opensuse.org
- Update to version 2.27.92:
  + Updated translations.
* Tue Aug 25 2009 vuntz@novell.com
- Update to version 2.27.91:
  + Updated translations.
* Mon Aug 10 2009 dominique-obs@leuenberger.net
- Update to version 2.27.90:
  + Updated translations.
* Sun Jul 19 2009 lmedinas@gmail.com
- Update to version 2.27.4:
  + [HC-svg] Add placeholder for system-reboot
  + Updated translations.
- Update to version 2.27.3.1:
  + Remove a duplicate line that caused build failures with recent
    autotools (bgo#587113)
* Mon Jun 15 2009 vuntz@novell.com
- Update to version 2.27.3:
  + [HC-svg]
  - Fix canvas size for several icons
  - Redraw some icons
  - New icons
* Wed May 27 2009 vuntz@novell.com
- Update to version 2.27.2:
  + [HC-svg] Fixed canvas size for numerous HC-svg icons.
  + Fix wrong background.
  + Updated translations.
* Wed May  6 2009 vuntz@novell.com
- Update to version 2.27.1:
  + Updated translations.
* Tue Apr 14 2009 vuntz@novell.com
- Update to version 2.26.1:
  + Fix shade for the focus color in Clearlooks themes.
  + Updated translations.
* Tue Mar 17 2009 vuntz@novell.com
- Update to version 2.26.0:
  + Fix progress bar color in Simple
  + Improve the progress bar in entries a bit in Glider and Simple
  + Add support for the entry progress in Clearlooks based themes
  + Updated translations.
* Fri Mar  6 2009 vuntz@novell.com
- Update to version 2.25.92:
  + Updated translations.
- Remove unneeded autoreconf call.
* Tue Feb 17 2009 mboman@suse.de
- Update to version 2.25.91:
  + New icons for HC-SVG and HCLPI:
  * printer-printing and printer-error. bgo#564910, bgo#564914
  * battery-low and battery-caution. bgo#564629, bgo#564631
  * network-wireless. bgo#565704
  * mail-send-receive. bgo#565788
  * emblem-unreadable. bgo#565854
  * media-playlist-shuffle. bgo#565243
  * media-playlist-repeat. bgo#564663
  * x-office-presentation. bgo#565705
  * x-office-document. bgo#56580
  + Translation updates
* Tue Feb  3 2009 mboman@suse.de
- Update to version 2.25.90:
  + New icon for 'x-office-calendar' (bgo#565794)
  + HC-SVG: Don't ihnerit HighContrastLargePrint, and use
    "folder" as Example.
  + New icon for 'x-office-address-book' (bgo#565870).
  + New icon 'text-x-generic-template' (bgo#565878)
  + New HC-SVG icons from Vinicius Depizzol (bgo#566037,
    bgo#566038), inverse versions.
  + Translation updates
* Sun Feb  1 2009 mboman@suse.de
- Update to version 2.25.5:
  + New high contrast icons for status/weather
  + Bugs fixed: bgo#564117, bgo#564119, bgo#564193, bgo#564228, bgo#564230,
    bgo#564231, bgo#564234, bgo#564323, bgo#564326, bgo#564420
  + Translation updates
* Sat Dec 20 2008 mboman@suse.de
- Update to version 2.25.3:
  + Many new icons for HighContrast-SVG
  + Apply `inkscape --vacuum-defs` removing wrong/odd stuff (mostly invalid
    URI to sodipodi-0.dtd, due to extraneus space) generating wrong SVG
    files. Thanks WebKit to show this issue
  + Move from apps to apps-extra some icons no longer in Icon Naming Spec:
    internet-group-chat, internet-mail, internet-news-reader,
    internet-web-browser, preferences-system-network-proxy,
    preferences-system-session, preferences-system-windows
  + Fix the bg color of GtkViewport and GtkScrolledWindow in notebooks
  + Add support for HighContrast-SVG placeholder icons. Closes bgo#451878
  + Added "user-bookmarks" copying existing bookmarsk-view from action-extras
  + Set GtkTreeView::grid-line-width to 2px in the large print themes
* Wed Oct 22 2008 mboman@suse.de
- Update to version 2.24.1:
  + Translation updates
* Wed Oct  1 2008 mboman@suse.de
- Update to version 2.24.0:
  + Translation updates
* Tue Sep 16 2008 vuntz@novell.com
- Update to version 2.23.92:
  + Add preferences-desktop-keyboard to the HC themes.
  + Update 'old-style' HC keyboard icons to the new style.
  + Updated translations.
* Tue Sep  2 2008 mboman@novell.com
- Update to version 2.23.91:
  + Add HC icons for new gdm, per
  + Rework the gtkrcs so that all clearlooks based gtkrcs match better.
  + Updated translations.
- Removed gnome-themes-remove-crux.diff. Not used.
- Removed gnome-themes-2.4.1-colors.patch. Not used.
* Sat Aug 30 2008 mboman@novell.com
- Update to version 2.23.90:
  + Add volume control icons to HC and HCI themes, fixes bgo#363342.
  + Add HC and HCI stock_new-tab icon  (bgo#320624)
  + Add desktop-emblem to HC and HCI themes, fixes bgo#140773.
  + Ensure all category icons are represented in the HC and HCI themes
    (fixes bgo#434839).  Also remove extraneous search directories
    from HC and HCI index.theme files.
  + Fix the x/ythickness and increase some other sizes in the
    highcontrast theme. (bug bgo#452062)
  + Bump required gtk-engines version to 2.15.3 (current trunk)
  + Set a style property that is installed by Gecko on GtkEntry.
  + Updated translations.
* Tue Aug  5 2008 captain.magnus@opensuse.org
- Update to version 2.23.6:
  + Updated translations.
* Wed Jun 25 2008 maw@suse.de
- Update to version 2.23.4:
  + Updated translations.
* Mon Jun 16 2008 maw@suse.de
- Update to version 2.23.3:
  + Various bug fixes
  + Updated translations.
* Wed May 14 2008 sbrabec@suse.cz
- Split spheres-and-crystals out and moved to GNOME:Community Build
  Service repository (bnc#380955).
- Split ximian-artwork out to drop or create separate packages
  (bnc#380955).
- Dropped no more used novell-button.
* Wed May 14 2008 sbrabec@suse.cz
- Re-enabled *real* icons - in high contrast themes it is intended
  to have custom icons.
* Thu Apr 10 2008 ro@suse.de
- added baselibs.conf file to build xxbit packages
  for multilib support
* Fri Mar 14 2008 maw@suse.de
- Update to version 2.22.0:
  + Workarounds for dark themes
  + Updated translations.
* Thu Mar  6 2008 maw@suse.de
- Fix the build when against newer versions of intltool.
* Wed Mar  5 2008 maw@suse.de
- Update to version 2.21.92:
  + Bug fixed: bgo#516226
  + Updated translations.
* Mon Feb 18 2008 maw@suse.de
- Update to version 2.21.91:
  + HCLP theme changes
  + Performance boosts
  + Updated translations.
* Wed Jan 30 2008 rodrigo@suse.de
- Update to version 2.21.5:
  * +20-30%% speed boost, obteined by using <line> instead <tint>
    operations
  * Work around bug bgo#382646 in ClearlooksClassic
  * Removed low contrast icon theme
  * All GTK+/GNOME managed fonts on screen will use the same family
    and size when you choose to use suggested font by *LargePrint*
    themes
  * Fix canvas size (60->48), pixel perfect and borders
* Thu Oct  4 2007 sbrabec@suse.cz
- Patched to build ximian-artwork without gtk1 devel.
- Dropped galeon browser support.
- Use %%fdupes.
* Wed Oct  3 2007 sbrabec@suse.cz
- Dropped xmms support.
* Wed Sep 19 2007 sbrabec@suse.cz
- Updated to version 2.20.0:
  * inverted, Clearlooks & Glossy themes: code polish and visual
    tweaks. Fix _A LOT_ of themes (the one with dark fg_selected)
  * Glossy gtkrc: Use gtk-tooltip* instead of gtk-tooltips to match
    the tooltip window
  * add support for tooltip_*_color in Glider and ClearlooksClassic
  * updated translations
* Mon Sep 10 2007 mauro@suse.de
- Update to version 2.19.92:
  + Updated Occitan translation.
* Thu Aug 30 2007 maw@suse.de
- Update to version 2.19.91:
  + Slight improvements to several themes
  + Updated translations.
* Thu Aug  2 2007 mauro@suse.de
- Update to version 2.19.6
- Patch #5 (gnome-themes-remove-crux.diff) is not being applied anymore.
* Fri Jul  6 2007 maw@suse.de
- Update to version 2.19.3
* Wed Apr 11 2007 maw@suse.de
- Update to version 2.18.1 which has new translations.
* Fri Mar 23 2007 maw@suse.de
- Update to version 2.18.0.
* Thu Mar  1 2007 sbrabec@suse.cz
- Removed remaining references to /opt/gnome (#235215).
* Mon Feb 19 2007 maw@suse.de
- Update to version 2.17.91.
* Thu Dec 14 2006 sbrabec@suse.cz
- Prefix changed to /usr.
- Spec file cleanup.
* Mon Oct 23 2006 dobey@suse.de
- Move the Industrial icon and cursor theme to /usr/share
  Fixes https://bugzilla.novell.com/show_bug.cgi?id=214512
* Mon Oct 23 2006 dobey@suse.de
- Update ximian-artwork to version 0.6.3
- Fixes in Industrial icon and gdm themes
* Tue Oct 17 2006 jhargadon@suse.de
- update to version 2.16.1.1
- Bugfixes:
  * icon-themes/HighContrast-SVG/scalable/actions/Makefile.am:
  * icon-themes/HighContrast-SVG/scalable/apps/Makefile.am:
  * icon-themes/HighContrast-SVG/scalable/categories/Makefile.am:
  * icon-themes/HighContrast-SVG/scalable/devices/Makefile.am:
  * icon-themes/HighContrast-SVG/scalable/status/Makefile.am:
* Sun Oct 15 2006 danw@suse.de
- Remove dead patches
- Rename gnome-themes-remove-smokey-and-crux.diff to
  gnome-themes-remove-crux.diff since smokey has been removed upstream
* Tue Oct  3 2006 jhargadon@suse.de
- update to version 2.16.1
- Added 24x24 icons for Mist icon themes
- Minor filename fix to the HighContrast-SVG theme
- translation updates
* Wed Sep 13 2006 jhargadon@suse.de
- update to version 2.16.0
- Clarius theme removed, as no longer need
- Clearlooks metatheme reverted to using Clearlooks gtk+ theme
- Fixes to the Mist icon theme
- New/Improved translations
* Wed Aug 30 2006 jhargadon@suse.de
- update to version 2.15.92
- Require intltool 0.35.0 to make sure translations
  work with the po/LINGUAS scheme
- Fail if icon-naming-utils not found
- desktop-themes/Mist/index.theme.in: Use Mist rather than Flat-Blue
  for the icon theme
- Start to make the Mist icon theme actually work
- translation updates
* Mon Aug 21 2006 jhargadon@suse.de
- update to version 2.15.91
- Updates to the HighContrast SVG theme
- Improved Glider theme
- New Mist icon theme
- New Clarius theme to use as the default theme in GNOME
- updated translations
* Fri Aug 18 2006 aj@suse.de
- Clean up BuildRequires.
* Wed Aug 16 2006 ro@suse.de
- adapt to X.org 7.1 (/usr/X11R6 -> /usr)
* Thu Jun  1 2006 dobey@suse.de
- Update ximian-artwork to 0.6.2 to fix name/screenshot for gdm
  Fixes https://bugzilla.novell.com/show_bug.cgi?id=136812
* Mon Mar 13 2006 sbrabec@suse.cz
- Removed gtk1 Industrial engine, build as NoArch.
* Mon Feb 27 2006 dobey@suse.de
- Remove changes to brand gdm theme for SuSE 9.2
- Update ximian-artwork to use unbranded gdm theme
  Fixes https://bugzilla.novell.com/show_bug.cgi?id=136814
* Thu Feb  2 2006 aj@suse.de
- Reduce BuildRequires.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Dec 12 2005 dobey@suse.de
- Update to ximian-artwork 0.6.0
* Mon Dec 12 2005 sbrabec@suse.cz
- Fixed build of ximian-artwork with latest icon-naming-utils.
* Wed Nov 16 2005 dobey@suse.de
- Update to ximian-artwork 0.3.0 to fix icon theming issues
* Tue Nov 15 2005 dobey@suse.de
- Change Industrial icon theme to inherit from Tango, and add a new
  dependency on tango-icon-theme for the package
* Fri Oct 28 2005 dobey@suse.de
- Update to ximian-artwork 0.2.50 to fix some icon rendering issues
* Thu Oct 13 2005 gekker@suse.de
- Update to version 2.12.1
* Thu Sep 15 2005 clahey@suse.de
- Update to ximian-artwork 0.2.49 to fix trash icon. #78534
* Fri Sep  9 2005 clahey@suse.de
- Remove broken gnome-fs-desktop.png from Industrial icon theme.
  Fixes bug #116263.
* Tue Sep  6 2005 gekker@suse.de
- Update to version 2.12.0 (GNOME 2.12)
* Tue Aug 23 2005 gekker@suse.de
- Update to version 2.11.92
- Rediff partially upstreamed patch
* Thu Aug 11 2005 gekker@suse.de
- Update to version 2.11.91
* Sun Aug  7 2005 aj@suse.de
- Fix lib64 problems.
* Thu Aug  4 2005 clahey@suse.de
- Move Industrial gtk2 theme to gtk2-engines.
* Tue Aug  2 2005 gekker@suse.de
- Update to version 2.11.90
* Wed Jul 27 2005 clahey@suse.de
- Fixed indus_43092.patch to change the gtkrc.in as well.
* Thu Jul  7 2005 gekker@suse.de
- Update to version 2.11.4
- Fix to build with -D_FORTIFY_SOURCE=2
* Mon Jun 20 2005 gekker@suse.de
- Update to version 2.11.3
* Fri Jun 17 2005 federico@novell.com
- Added ximian-artwork-90546-16x16-icons.patch to fix bug #90546.  Now
  we have custom-drawn 16x16 icons for folders and other items which
  the file chooser uses, instead of scalable icons.
- Added Industrial-16x16-icons.tar.gz to the sources; this contains
  the new icons.
* Wed Mar 23 2005 gekker@suse.de
- Fix tree-insensitive-text-color (72880).
* Wed Mar 23 2005 sbrabec@suse.cz
- Do not change icon for mouse over unmaximize button in Industrial
  theme (#74302).
* Fri Mar 18 2005 hhetter@suse.de
- make Grand Canyon use Sandy as Icon Theme (#73765)
* Wed Mar 16 2005 clahey@suse.de
- Add new SuSE themed spinner.
* Mon Mar 14 2005 clahey@suse.de
- Replace novell-button with a SuSE icon.  Art team approved.
* Wed Mar  9 2005 gekker@suse.de
- Update to version 2.10.0 (GNOME 2.10).
* Mon Mar  7 2005 clahey@suse.de
- Change comment of Industrial metatheme to refer to Novell Desktop
  instead of Ximian Desktop.
* Thu Mar  3 2005 clahey@suse.de
- Make Industrial inherit from crystalsvg as well.
* Thu Mar  3 2005 gekker@suse.de
- update to version 2.9.94
* Mon Feb  7 2005 gekker@suse.de
- Update to version 2.9.90
* Thu Jan 20 2005 gekker@suse.de
- Update to version 2.9.4
* Mon Jan  3 2005 gekker@suse.de
- Update to version 2.9.2.1
* Thu Dec 16 2004 gekker@suse.de
- Update version to 2.9.2
- Reworked the colors patch so that it would apply.
- Reworked and combined the remove-smokey and remove-crux patches.
* Sun Nov  7 2004 ro@suse.de
- copy missing mkinstalldirs manually
* Tue Nov  2 2004 ro@suse.de
- locale rename: no -> nb
* Mon Oct  4 2004 hhetter@suse.de
- fixate final suse-linux logo
- change background to final version
* Mon Sep 27 2004 sbrabec@suse.cz
- Removed old RealPlayer branding.
  http://bugzilla.ximian.com/show_bug.cgi?id=66824
* Tue Sep 14 2004 hhetter@suse.de
- add suse-linux gdm titel logo
- on SUSE Linux > 9.0, patch novell.xml to use the
  suse-linux logo
* Mon Sep 13 2004 joeshaw@suse.de
- Update to ximian-artwork 0.2.46 (Ximian #65483)
* Wed Sep  8 2004 dobey@suse.de
- Update to ximian-artwork 0.2.45 (Ximian #58722, #65225)
* Mon Sep  6 2004 hhetter@suse.de
- adapt menu sidebar for SUSE Linux 9.2
* Thu Sep  2 2004 hhetter@suse.de
- "SUSE Linux 9.2" in the title box of Industrial GDM Theme
* Tue Aug 24 2004 joeshaw@suse.de
- Upgraded to ximian-artwork 0.2.43.  (Ximian #63482)
* Mon Aug 23 2004 joeshaw@suse.de
- Upgraded to ximian-artwork 0.2.42.  (Ximian #58715, #62623, #63484)
* Tue Aug 10 2004 clahey@suse.de
- Upgraded to ximian-artwork 0.2.41.
* Tue Aug  3 2004 clahey@suse.de
- Add symlink for X cursors.
* Mon Aug  2 2004 clahey@suse.de
- Apply metacity theme patch inspired by Fitts Law.
* Mon Aug  2 2004 ro@suse.de
- fix file list after Crux removal
* Fri Jul 30 2004 kimmidi@suse.de
- Remove Crux theme (#59019)
* Mon Jul 26 2004 kimmidi@suse.de
- Correct spec file to change to proper directories before applying
  patches.
* Thu Jul 15 2004 kimmidi@suse.de
- Fixes bugs #40127 and #43092 in ximian bugzilla.
* Wed Jul 14 2004 clahey@suse.de
- Upgraded to ximian-artwork 0.2.40.
* Wed Jun  2 2004 clahey@suse.de
- Upgraded to ximian-artwork 0.2.37.
* Tue May 11 2004 clahey@suse.de
- Added a missing directory.
* Mon May 10 2004 clahey@suse.de
- Upgraded to gnome-themes 2.6.1 and ximian-artwork 0.2.36.
* Fri Mar 19 2004 pmladek@suse.cz
- fixed bg[SELECTED] to correspond to the color used by the native
  gtk2 widget, bg[SELECTED] is used only by OpenOffice.org now
* Thu Mar 18 2004 sbrabec@suse.cz
- Added --enable-all-themes (#36317).
* Mon Mar  8 2004 sbrabec@suse.cz
- Fixed xmms skin destination.
* Mon Mar  8 2004 hhetter@suse.de
- include ximian artwork (0.2.32.1, non-branded)
* Mon Mar  1 2004 mmj@suse.de
- Add gtk2-engines to Requires:
* Sat Jan 10 2004 adrian@suse.de
- fix build as user
* Mon Oct 27 2003 sbrabec@suse.cz
- Updated to version 2.4.1.
* Thu Oct  9 2003 sbrabec@suse.cz
- Don't build static engines and don't package *.la files.
* Mon Sep 29 2003 hhetter@suse.de
- updated to version 2.4.0 [GNOME2.4]
* Tue Aug 19 2003 sbrabec@suse.cz
- Updated neededforbuild (rename of librsvg2, eel2).
* Wed Jul 16 2003 sbrabec@suse.cz
- Fixed pixmap_path in spheres-and-crystals.
* Mon Jul 14 2003 sbrabec@suse.cz
- GNOME prefix change to /opt/gnome.
* Wed Jul  9 2003 sbrabec@suse.cz
- Updated to version 2.2.2.
- Require gnome-icon-theme.
- Prefix clash fix (gtk engines),
- Packaged all files.
* Tue Jul  1 2003 ro@suse.de
- removed unpackaged files from buildroot
- added libgsf to neededforbuild
* Thu Mar 27 2003 hhetter@suse.de
- updated gnome-themes to version 2.2.1
- update Spheres and Crystals to version 0.7
* Thu Mar 13 2003 hhetter@suse.de
- fix build (use autoreconf)
* Fri Feb 14 2003 hhetter@suse.de
- again prefix to /opt/gnome2 because, themes path is now fixed
  in control center
* Thu Feb 13 2003 hhetter@suse.de
- prefix to gtk2-prefix to get all themes correctly to work
  with any gdk-pixbufloader engine, and provide pure GTK themes
* Wed Feb 12 2003 hhetter@suse.de
- fix iconrc for spheres and crystals
* Mon Feb 10 2003 hhetter@suse.de
- include the Spheres-and-crystals SVG Theme
* Thu Feb  6 2003 sbrabec@suse.cz
- Update to version 2.2.
- DESTDIR fix.
* Fri Jan 31 2003 hhetter@suse.de
- updated to version 1.0
* Thu Jan 16 2003 sbrabec@suse.cz
- Fixed %%prefix to /opt/gnome2.
* Thu Jan 16 2003 sbrabec@suse.cz
- Added new package.
