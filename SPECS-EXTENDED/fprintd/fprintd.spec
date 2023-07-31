Vendor:         Microsoft Corporation
Distribution:   Mariner
## START: Set by rpmautospec
## (rpmautospec version 0.2.5)
%define autorelease(e:s:pb:) %{?-p:0.}%{lua:
    release_number = 2;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{?dist}
## END: Set by rpmautospec

Name:		fprintd
Version:	1.94.2
Release:	%autorelease
Summary:	D-Bus service for Fingerprint reader access

License:	GPLv2+
Source0:	https://gitlab.freedesktop.org/libfprint/fprintd/-/archive/v%{version}/fprintd-v%{version}.tar.gz
Url:		http://www.freedesktop.org/wiki/Software/fprint/fprintd
ExcludeArch:    s390 s390x

BuildRequires:	meson
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	git
BuildRequires:	pam-devel
BuildRequires:	libfprint-devel >= 1.94.0
BuildRequires:	polkit-devel
BuildRequires:	gtk-doc
BuildRequires:	gettext
BuildRequires:	perl-podlators
BuildRequires:	systemd-devel
BuildRequires:	python3-dbusmock
BuildRequires:	python3-libpamtest


%description
D-Bus service to access fingerprint readers.

%package pam
Summary:	PAM module for fingerprint authentication
Requires:	%{name} = %{version}-%{release}
# Note that we obsolete pam_fprint, but as the configuration
# is different, it will be mentioned in the release notes
Provides:	pam_fprint = %{version}-%{release}
Obsoletes:	pam_fprint < 0.2-3
Requires(postun): authselect >= 0.3

License:	GPLv2+

%description pam
PAM module that uses the fprintd D-Bus service for fingerprint
authentication.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
License:	GFDL
BuildArch:	noarch

%description devel
Development documentation for fprintd, the D-Bus service for
fingerprint readers access.

%prep
%autosetup -S git -n %{name}-v%{version}

%build
%meson -Dgtk_doc=true -Dpam=true -Dpam_modules_dir=%{_libdir}/security
%meson_build

%install
%meson_install
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/lib/fprint

%find_lang %{name}

%postun pam
if [ $1 -eq 0 ]; then
  /bin/authselect disable-feature with-fingerprint || :
fi

%files -f %{name}.lang
%doc README COPYING AUTHORS TODO
%{_bindir}/fprintd-*
%{_libexecdir}/fprintd
# FIXME This file should be marked as config when it does something useful
%{_sysconfdir}/fprintd.conf
%{_datadir}/dbus-1/system.d/net.reactivated.Fprint.conf
%{_datadir}/dbus-1/system-services/net.reactivated.Fprint.service
%{_unitdir}/fprintd.service
%{_datadir}/polkit-1/actions/net.reactivated.fprint.device.policy
%{_localstatedir}/lib/fprint
%{_mandir}/man1/fprintd.1.gz

%files pam
%doc pam/README
%{_libdir}/security/pam_fprintd.so
%{_mandir}/man8/pam_fprintd.8.gz

%files devel
%{_datadir}/gtk-doc/
%{_datadir}/dbus-1/interfaces/net.reactivated.Fprint.Device.xml
%{_datadir}/dbus-1/interfaces/net.reactivated.Fprint.Manager.xml

%changelog
* Thu Feb 24 2022 Benjamin Berg <bberg@redhat.com> 1.94.2-1
- Update to 1.94.2

* Thu Feb 24 2022 Benjamin Berg <bberg@redhat.com> 1.94.1-3
- Switch to rpmautospec

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> 1.94.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 03 2021 Benjamin Berg <bberg@redhat.com> 1.94.1-1
- Update to 1.94.1 (#1978269)

* Mon Oct 25 2021 Benjamin Berg <bberg@redhat.com> 1.94.0-2
- Drop unneeded rm and fix changelog

* Fri Aug 20 2021 Benjamin Berg <bberg@redhat.com> 1.94.0-1
- Update to 1.94.0 (#1978269)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> 1.92.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 01 2021 Benjamin Berg <bberg@redhat.com> 1.92.0-1
- Update to 1.92.0 (#1978269)

* Thu May 27 2021 Benjamin Berg <bberg@redhat.com> 1.90.9-3
- Spec file fixes

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> 1.90.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Benjamin Berg <bberg@redhat.com> 1.90.9-1
- Update to 1.90.9 (#1915788)

* Fri Dec 18 2020 Adam Williamson <awilliam@redhat.com> 1.90.8-2
- Rebuild for libnss dependency issue

* Fri Dec 11 2020 Benjamin Berg <bberg@redhat.com> 1.90.8-1
- Update to 1.90.8 (#1902255)

* Fri Dec 11 2020 Benjamin Berg <bberg@redhat.com> 1.90.7-2
- Fix bogus date in changelog

* Wed Dec 09 2020 Benjamin Berg <bberg@redhat.com> 1.90.7-1
- Update to 1.90.7 (#1902255)

* Mon Dec 07 2020 Benjamin Berg <bberg@redhat.com> 1.90.6-1
- Update to 1.90.6 (#1902255)

* Tue Dec 01 2020 Benjamin Berg <bberg@redhat.com> 1.90.5-1
- Update to 1.90.5 (#1902255)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> 1.90.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 13 2020 Bastien Nocera <hadess@hadess.net> 1.90.1-1
- + fprintd-1.90.1-1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Benjamin Berg <bberg@redhat.com> 0.9.0-1
- + fprintd-0.9.0-1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> 0.8.1-5
- Remove obsolete Group tag

* Fri Jul 20 2018 Bastien Nocera <hadess@hadess.net> 0.8.1-4
- + fprintd-0.8.1-3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Jason Tibbitts <tibbs@math.uh.edu> 0.8.1-2
- Remove needless use of %defattr

* Fri Jun 15 2018 Bastien Nocera <hadess@hadess.net> 0.8.1-1
- + fprintd-0.8.1-1

* Wed May 30 2018 Bastien Nocera <hadess@hadess.net> 0.8.0-6
- + fprintd-0.8.0-4

* Tue Feb 20 2018 Pavel Březina <pbrezina@redhat.com> 0.8.0-5
- Switch from authconfig to authselect

* Wed Feb 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> 0.8.0-4
- Remove %clean section

* Tue Feb 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> 0.8.0-3
- Remove BuildRoot definition

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 13 2017 Bastien Nocera <hadess@hadess.net> 0.8.0-1
- + fprintd-0.8.0-1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> 0.7.0-4
- Rebuilt for
  https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 09 2017 Bastien Nocera <hadess@hadess.net> 0.7.0-2
- + fprintd-0.7.0-2

* Thu Oct 13 2016 Bastien Nocera <hadess@hadess.net> 0.7.0-1
- + fprintd-0.7.0-1

* Thu Sep 22 2016 Bastien Nocera <hadess@hadess.net> 0.6.0-5
- Fix warning when uninstalling fprintd-pam (#1203671)

* Wed Feb 03 2016 Dennis Gilmore <dennis@ausil.us> 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Dennis Gilmore <dennis@ausil.us> 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> 0.6.0-2
- Rebuilt for Fedora 23 Change

* Tue Feb 03 2015 Bastien Nocera <hadess@hadess.net> 0.6.0-1
- Update to 0.6.0

* Sat Aug 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Dennis Gilmore <dennis@ausil.us> 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 11 2013 Bastien Nocera <hadess@hadess.net> 0.5.1-2
- Fix man page syntax error

* Sun Aug 11 2013 Bastien Nocera <hadess@hadess.net> 0.5.1-1
- Update to 0.5.1

* Sat Aug 03 2013 Dennis Gilmore <dennis@ausil.us> 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 05 2013 Bastien Nocera <hadess@hadess.net> 0.5.0-2
- Update filelist

* Tue Mar 05 2013 Bastien Nocera <hadess@hadess.net> 0.5.0-1
- Update to 0.5.0

* Tue Feb 26 2013 Bastien Nocera <hadess@hadess.net> 0.4.1-9
- You awful perl packaging

* Tue Feb 19 2013 Bastien Nocera <hadess@hadess.net> 0.4.1-8
- Another try for the pod2man BR...

* Tue Feb 19 2013 Bastien Nocera <hadess@hadess.net> 0.4.1-7
- pod2man isn't in the main perl package anymore...

* Tue Feb 19 2013 Bastien Nocera <hadess@hadess.net> 0.4.1-6
- Add perl for pod2man BR

* Tue Feb 19 2013 Bastien Nocera <hadess@hadess.net> 0.4.1-5
- Co-own the gtk-doc directory (#604351)

* Wed Feb 13 2013 Dennis Gilmore <dennis@ausil.us> 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Dennis Gilmore <dennis@ausil.us> 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Dennis Gilmore <dennis@ausil.us> 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Bastien Nocera <hadess@hadess.net> 0.4.1-1
- Update to 0.4.1

* Tue Feb 08 2011 Dennis Gilmore <dennis@ausil.us> 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 09 2010 Ray Strode <rstrode@redhat.com> 0.2.0-4
- Don't every allow pam module to get unloaded

* Mon Nov 08 2010 Ray Strode <rstrode@redhat.com> 0.2.0-3
- Revert "Fix crash in gnome-screensaver"

* Mon Nov 08 2010 Ray Strode <rstrode@redhat.com> 0.2.0-2
- Fix crash in gnome-screensaver

* Thu Aug 19 2010 Bastien Nocera <hadess@hadess.net> 0.2.0-1
- * Thu Aug 19 2010 Bastien Nocera <bnocera@redhat.com> 0.2.0-1

* Wed Jul 28 2010 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.1-20
- dist-git conversion

* Wed Dec 09 2009 Bastien Nocera <hadess@fedoraproject.org> 0.1-19
- Remove use of g_error(), or people think that it crashes when we actually

* Wed Nov 25 2009 Bill Nottingham <notting@fedoraproject.org> 0.1-18
- Fix typo that causes a failure to update the common directory. (releng

* Fri Jul 24 2009 Jesse Keating <jkeating@fedoraproject.org> 0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Bastien Nocera <hadess@fedoraproject.org> 0.1-16
- Merge polkit patch and fix for polkit patch

* Tue Jul 21 2009 Bastien Nocera <hadess@fedoraproject.org> 0.1-15
- Make the -devel package noarch (#507698)

* Thu Jul 09 2009 Matthias Clasen <mclasen@fedoraproject.org> 0.1-14
- fix the pam module

* Sat Jun 20 2009 Bastien Nocera <hadess@fedoraproject.org> 0.1-13
- Remove obsolete patch

* Wed Jun 10 2009 Matthias Clasen <mclasen@fedoraproject.org> 0.1-12
- oops

* Wed Jun 10 2009 Matthias Clasen <mclasen@fedoraproject.org> 0.1-11
- fix file lists

* Wed Jun 10 2009 Matthias Clasen <mclasen@fedoraproject.org> 0.1-10
- Port to PolicyKit 1

* Thu May 07 2009 Bastien Nocera <hadess@fedoraproject.org> 0.1-9
- Add /var/lib/fprint to the RPM to avoid SELinux errors (#499513)

* Tue Apr 21 2009 Karsten Hopp <karsten@fedoraproject.org> 0.1-8
- Excludearch s390 s390x, as we don't have libusb1 on mainframe, we can't

* Tue Feb 24 2009 Jesse Keating <jkeating@fedoraproject.org> 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 Bastien Nocera <hadess@fedoraproject.org> 0.1-6
- Add a patch to handle device disconnects

* Mon Jan 26 2009 Bastien Nocera <hadess@fedoraproject.org> 0.1-5
- Some new files

* Mon Jan 26 2009 Bastien Nocera <hadess@fedoraproject.org> 0.1-4
- Update to latest git, fixes some run-time warnings

* Wed Dec 17 2008 Bastien Nocera <hadess@fedoraproject.org> 0.1-3
- Add patch to stop leaking a D-Bus connection on failure

* Tue Dec 09 2008 Bastien Nocera <hadess@fedoraproject.org> 0.1-2
- Update D-Bus config file for recent D-Bus changes

* Fri Dec 05 2008 Bastien Nocera <hadess@fedoraproject.org> 0.1-1
- Update following comments in the review
