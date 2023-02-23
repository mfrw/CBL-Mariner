Vendor:         Microsoft Corporation
Distribution:   Mariner
# review https://bugzilla.redhat.com/show_bug.cgi?id=502404
# renamed from lxsession-lite. Original review at
# https://bugzilla.redhat.com/show_bug.cgi?id=442268

%global	use_release	0
%global	use_git		0
%global	use_gitbare 	1

%if 0%{?use_git} < 1
%if 0%{?use_gitbare} < 1
# force
%global	use_release 	1
%endif
%endif

%if 0%{?use_git}
%global	git_rev	138ff9b22b45192a3b020ebbbed04e9060470a66
%global	git_date	20161125
%global	git_short	%(echo %{git_rev} | cut -c-8)
%global	git_version	D%{git_date}git%{git_short}
%endif

%if 0%{?use_gitbare}
%global	gittardate	20210202
%global	gittartime	1502
%global	gitbaredate	20210130
%global	git_rev	8543c00a2de2533d1fb2d661508410df1c073011
%global	git_short	%(echo %{git_rev} | cut -c-8)
%global	git_version	D%{gitbaredate}git%{git_short}
%endif

%global	mainrel 7

%if 0%{?use_release} >= 1
%global         fedorarel   %{?prever:0.}%{mainrel}%{?prever:.%{prerpmver}}
%endif
%if 0%{?use_git} >= 1
%global         fedorarel   %{mainrel}.%{git_version}
%endif
%if 0%{?use_gitbare} >= 1
%global         fedorarel   %{mainrel}.%{git_version}
%endif

Name:           lxsession
Version:        0.5.5
Release:        %{fedorarel}%{?dist}.2
Summary:        Lightweight X11 session manager
Summary(de):    Leichtgewichtiger X11 Sitzungsverwalter

License:        GPLv2+
URL:            http://lxde.sourceforge.net/
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_git}
Source0:        %{name}-%{version}-%{?git_version}.tar.bz2
%endif
%if 0%{?use_release}
Source0:        http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz
%endif
# https://github.com/lxde/lxsession/pull/27
# Fix lxsession-xdg-autostart segfault
Patch1:		lxsession-0.5.5-0001-xdg-autostart-never-reuse-GKeyFile-object.patch
# https://github.com/lxde/lxsession/pull/28
# Fix lxsession-default-apps segfault
Patch2:		lxsession-0.5.5-0002-load_autostart-never-reuse-GKeyFile-object.patch
#http://sourceforge.net/p/lxde/bugs/760/
Patch1000:      lxsession-0.5.2-git9f8d6133-reload.patch
Patch1002:      lxsession-0.5.2-notify-daemon-default.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1801071
# race condition when calling "lxsession -r" from imsettings-lxde and when daemon is not configured yet
# explicitly do nullptr check
Patch1005:      lxsession-0.5.4-load-settings-nullcheck.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1830588
# add custom directory to XDG_CONFIG_DIRS
Patch2001:      lxsession-0.5.5-add-custom-xdg-config-dir.patch

BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(indicator-0.4)
BuildRequires:  pkgconfig(appindicator-0.1)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  make
BuildRequires:  vala
BuildRequires:  docbook-utils
BuildRequires:  intltool
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  %{_bindir}/xsltproc

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  %{_bindir}/git

# name changed back from lxsession-lite to lxsession
Obsoletes:      lxsession-lite <= 0.3.6-6
Provides:       lxsession-lite = %{version}-%{release}
# lxde-settings-daemon was merged into lxsession
Obsoletes:      lxde-settings-daemon <= 0.4.1-2
Provides:       lxde-settings-daemon = 0.4.1-3
# required for suspend and hibernate
Requires:       upower

%description
LXSession is a standard-compliant X11 session manager with shutdown/
reboot/suspend support via systemd. In connection with gdm it also supports user 
switching.

LXSession is derived from XSM and is developed as default X11 session manager 
of LXDE, the Lightweight X11 Desktop Environment. Though being part of LXDE, 
it's totally desktop-independent and only has few dependencies.

%description -l de
LXSession Lite ist ein Standard konformer X11 Sitzungsverwalter mit 
Unterstützung für Herunterfahren, Neustart und Schlafmodus mittels systemd. 
Zusammen mit GDM unterstützt auch Benutzerwechsel.

LXSession Lite ist von XSM abgeleitet und wird als Sitzungsverwalter von LXDE,
der leichtgewichtigen X11 Desktop Umgebung, entwickelt. Obwohl er Teil von 
LXDE ist, ist er komplett Desktop unabhängig und hat nur wenige 
Abhängigkeiten.


%package edit
Summary:        Simple GUI to configure what’s automatically started in LXDE

%description edit
LXSession-edit is a tool to manage freedesktop.org compliant desktop session 
autostarts. Currently adding and removing applications from the startup list 
is not yet available, but it will be support in the next release.

%package -n lxpolkit
Summary:        Simple PolicyKit authentication agent
Requires:       polkit >= 0.95
# required to replace polkit-gnome and polkit-kde
Provides:       PolicyKit-authentication-agent


%description -n lxpolkit
LXPolKit is a simple PolicyKit authentication agent developed for LXDE, the 
Lightweight X11 Desktop Environment.

%prep
%if 0%{?use_release} || 0%{?use_git}
%setup -q %{?git_version:-n %{name}-%{version}-%{?git_version}}

git init
%endif

%if 0%{?use_gitbare}
%setup -q -c -T -a 0
git clone ./%{name}.git/
cd %{name}

#git checkout -b %{version}-fedora %{version}
git checkout -b %{version}-fedora %{git_rev}
cp -a [A-Z]* ..
cp -a data/ ..

cat > GITHASH <<EOF
EOF

cat GITHASH | while read line
do
  commit=$(echo "$line" | sed -e 's|[ \t].*||')
  git cherry-pick $commit
done

%endif

git config user.name "lxpanel Fedora maintainer"
git config user.email "lxpanel-owner@fedoraproject.org"

%if 0%{?use_release} || 0%{?use_git}
git add .
git commit -m "base" -q
%endif

#%patch0 -p1 -b .dsofix
%__cat %PATCH1 | git am
%__cat %PATCH2 | git am
%patch1000 -p1 -b .reload
%patch1002 -p1 -b .notify
%patch1005 -p1 -b .nullcheck
%patch2001 -p1 -b .custom
%if 0%{?use_gitbare}
git commit -m "Apply Fedora specific configulation" -a
%endif

# Umm?? Why are warnings killed by default?
sed -i.warn Makefile.am \
	-e '\@include.*config\.h@s| -w | |'

%if 0%{?use_gitbare}
git commit -m "Enable warnings" -a
%endif

# Don't start in Xfce to avoid bugs like
# https://bugzilla.redhat.com/show_bug.cgi?id=616730
sed -i 's/^NotShowIn=GNOME;KDE;/NotShowIn=GNOME;KDE;XFCE;/g' data/lxpolkit.desktop.in.in

# fix icon in desktop file
# http://lxde.git.sourceforge.net/git/gitweb.cgi?p=lxde/lxsession-edit;a=commit;h=3789a96691eadac9b8f3bf3034a97645860bd138
sed -i 's/^Icon=xfwm4/Icon=session-properties/g' data/lxsession-edit.desktop.in
%if 0%{?use_gitbare}
git commit -m "Apply Fedora specific configulation 2" -a
%endif


mkdir m4 || :
sh autogen.sh

%build
%if 0%{?use_gitbare}
cd %{name}
%endif

%configure \
	--enable-man \
	--disable-silent-rules \
	--enable-advanced-notifications \
	--enable-debug \
	%{nil}
make clean

# Tweak optflags here
find . -name Makefile | \
	xargs sed -i -e 's|\(-Werror=format-security\)|\1 -Werror=implicit-function-declaration -Werror=return-type |'
%make_build -k


%install
%if 0%{?use_gitbare}
cd %{name}
%endif

rm -rf $RPM_BUILD_ROOT
%make_install
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/xdg/%{name}

desktop-file-install \
    --remove-key="NotShowIn" \
    --add-only-show-in="LXDE;" \
    --delete-original \
    --dir=%{buildroot}%{_sysconfdir}/xdg/autostart \
    %{buildroot}%{_sysconfdir}/xdg/autostart/lxpolkit.desktop

desktop-file-install \
    --remove-key="NotShowIn" \
    --add-only-show-in="LXDE;" \
    --delete-original \
     %{buildroot}%{_datadir}/applications/*.desktop


%if 0%{?use_gitbare}
cd ..
%endif
%find_lang %{name}

%files -f %{name}.lang

%doc AUTHORS ChangeLog COPYING README data/desktop.conf.example
%{_bindir}/%{name}
%{_bindir}/%{name}-logout
%{_bindir}/%{name}-db
%{_bindir}/%{name}-default
%{_bindir}/%{name}-default-apps
%{_bindir}/%{name}-default-terminal
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}-xsettings
%{_bindir}/lxsettings-daemon
%{_bindir}/%{name}-xdg-autostart
%{_bindir}/lxlock
%{_bindir}/lxclipboard
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/ui/lxpolkit.ui
%exclude %{_datadir}/%{name}/ui/lxsession-edit.ui
%{_mandir}/man*/%{name}*.*
# we need to own
%dir %{_sysconfdir}/xdg/%{name}

%{_datadir}/applications/lxsession-default-apps.desktop

%{_mandir}/man1/lxlock.1*
%{_mandir}/man1/lxpolkit.1*
%{_mandir}/man1/lxclipboard.1*
%{_mandir}/man1/lxsettings-daemon.1*

%files edit
%{_bindir}/%{name}-edit
%{_datadir}/applications/lxsession-edit.desktop
%{_datadir}/%{name}/ui/lxsession-edit.ui

%files -n lxpolkit
%{_bindir}/lxpolkit
%config %{_sysconfdir}/xdg/autostart/lxpolkit.desktop
%{_datadir}/%{name}/ui/lxpolkit.ui

%changelog
* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-7.D20210130git8543c00a.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-7.D20210130git8543c00a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Mar 20 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.5-7.D20210130git8543c00a
- Avoid lxsession-default-apps segfault (with recent glib2)

* Fri Mar 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.5-6.D20210130git8543c00a
- Avoid lxsession-xdg-autostart segfault (with recent glib2)

* Tue Feb  2 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.5-5.D20210130git8543c00a
- Update to the latest git

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 12 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.5-4
- Turn on warning flags disabled by default on tarball
- Turn some warnings into error
- Enable LTO again
  - Breakage by LTO was because of -Wreturn-type issue

* Thu Aug 27 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.5-3
- Disable LTO for now for workaround (bug 1872429)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May  7 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.5-2
- Add custom directory to XDG_CONFIG_DIRS (ref: bug 1830588)

* Sun Mar 22 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.5-1
- 0.5.5

* Fri Feb 14 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.4-2
- load_settings: explicitly do null check when reloading daemon
  from imsettings-lxde (bug 1801071)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.4-1
- 0.5.4

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3-2
- 0.5.3 retagged and released.

* Sun Dec 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.3-1.D20161210gite284f41ad4
- 0.5.3 (and some minor fix from git)

* Tue Nov  8 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.2-12.D20161106git7b9a9580da
- Update to the latest git

* Sun Aug 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.2-11.D20160817git699c1695c2
- Update to the latest git
- Never free buffer returned by gtk_entry_get_text()
  (bug 1334064, github:lxsession#10)

* Tue Jun 21 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.2-10.D20160417git9f8d613332
- Update to the latest git

* Sat Apr 30 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.2-9
- Only set dpy variable when reloading to aviod polling on
  subsequent process (bug 1294579)

* Mon Feb 15 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.2-8
- Fix invalid memcpy() usage on lxsession-edit (possibly fix
  bug 1308300)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.2-6
- set notification default command and launch it by default
  (bug 1250742)

* Mon Jul 13 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.2-5
- Handle config key when key2 is null correctly (bug 1242273)

* Fri Jun 26 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.2-4
- Patch to work with imsettings-lxde

* Mon Jun 22 2015 Kevin Fenzi <kevin@scrye.com> 0.5.2-3
- Fix typo in last Change with desktop name.

* Mon Jun 22 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.5.2-2
- Add only-show-in LXDE

* Sun Jun 21 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.5.2-1
- Update to 0.5.2

* Wed Jun 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.2-1
- 0.5.2
- lxpolkit is now a subpackage of lxsession
- lxsession-edit is now a subpackage of lxsession

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 21 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.6.1-3
- Require ConsoleKit (#800658)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 09 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.6.1-1
- Update to 0.4.6.1
- Require upower (#755376)

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4.5-4
- Rebuild for new libpng

* Fri Mar 25 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.5-3
- No longer require hal (#688959)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.5-1
- Update to 0.4.5

* Tue Apr 06 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4

* Sat Mar 20 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3
- Fix labels of the German logout dialog

* Mon Mar 08 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Wed Feb 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-2
- Add patch to fix DSO linking (#564645)

* Fri Dec 11 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Tue Dec 08 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0
- Obsolete lxde-settings-deamon

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.8-1
- Update to 0.3.8 and remove all patches
- Rename back to lxsession again (upstream)

* Mon Apr 27 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.6-5
- Fix Session name (Andrew Lee)

* Mon Apr 27 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.6-4
- Support user switching also with newer gdm
- Add patch to fix icon search path (Marty Jack)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 09 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.6-2
- Preserve timestamps during install

* Thu Jun 12 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.6-1
- Update to 0.3.6
- Remove docbook hack

* Sun Apr 20 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.5-1
- Switch to LXSession lite and drop xorg-x11-xsm requirement again.

* Sat Apr 12 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.2-2
- Require xorg-x11-xsm

* Sat Apr 12 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Mon Mar 10 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0-1
- Initial Fedora RPM
