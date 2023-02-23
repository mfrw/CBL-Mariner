Vendor:         Microsoft Corporation
Distribution:   Mariner
%undefine _package_note_flags
# If we should verify tarball signature with GPGv2.
%global verify_tarball_signature 1

# If there are patches which touch autotools files, set this to 1.
%if !0%{?rhel}
%global patches_touch_autotools %{nil}
%else
# On RHEL the downstream patches always touch autotools files.
%global patches_touch_autotools 1
%endif

# The source directory.
%global source_directory 2.0-stable

Name:          virt-v2v
Epoch:         1
Version:       2.0.7
Release:       1%{?dist}
Summary:       Convert a virtual machine to run on KVM

License:       GPLv2+
URL:           https://github.com/libguestfs/virt-v2v

Source0:       http://download.libguestfs.org/virt-v2v/%{source_directory}/%{name}-%{version}.tar.gz
%if 0%{verify_tarball_signature}
Source1:       http://download.libguestfs.org/virt-v2v/%{source_directory}/%{name}-%{version}.tar.gz.sig
# Keyring used to verify tarball signature.
Source2:       libguestfs.keyring
%endif

# Maintainer script which helps with handling patches.
Source3:       copy-patches.sh

%if !0%{?rhel}
# libguestfs hasn't been built on i686 for a while since there is no
# kernel built for this architecture any longer and libguestfs rather
# fundamentally depends on the kernel.  Therefore we must exclude this
# arch.  Note there is no bug filed for this because we do not ever
# expect that libguestfs or virt-v2v will be available on i686 so
# there is nothing that needs fixing.
ExcludeArch:   %{ix86}
%else
# Architectures where virt-v2v is shipped on RHEL:
#
# not on aarch64 because it is not useful there
# not on %%{power64} because of RHBZ#1287826
# not on s390x because it is not useful there
ExclusiveArch: x86_64
%endif

%if 0%{patches_touch_autotools}
BuildRequires: autoconf, automake, libtool
%endif

BuildRequires: make
BuildRequires: /usr/bin/pod2man
BuildRequires: gcc
BuildRequires: ocaml >= 4.04

BuildRequires: libguestfs-devel >= 1:1.44
BuildRequires: augeas-devel
BuildRequires: bash-completion
BuildRequires: file-devel
BuildRequires: gettext-devel
BuildRequires: jansson-devel
BuildRequires: libnbd-devel
BuildRequires: libosinfo-devel
BuildRequires: libvirt-daemon-kvm
BuildRequires: libvirt-devel
BuildRequires: libxml2-devel
BuildRequires: pcre2-devel
BuildRequires: perl(Sys::Guestfs)
BuildRequires: po4a
BuildRequires: /usr/bin/virsh
BuildRequires: xorriso

BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-libguestfs-devel
BuildRequires: ocaml-libnbd-devel
BuildRequires: ocaml-fileutils-devel
BuildRequires: ocaml-gettext-devel
%if !0%{?rhel}
BuildRequires: ocaml-ounit-devel
%endif

BuildRequires: nbdkit-python-plugin

%if 0%{verify_tarball_signature}
BuildRequires: gnupg2
%endif

Requires:      libguestfs%{?_isa} >= 1:1.42
Requires:      guestfs-tools >= 1.42

# XFS is the default filesystem in Fedora and RHEL.
Requires:      libguestfs-xfs

%if 0%{?rhel}
# For Windows conversions on RHEL.
Requires:      libguestfs-winsupport >= 7.2
%endif

Requires:      gawk
Requires:      gzip
Requires:      unzip
Requires:      curl
Requires:      openssh-clients >= 8.8p1
Requires:      %{_bindir}/virsh

# Ensure the UEFI firmware is available, to properly convert
# EFI guests (RHBZ#1429643).
%ifarch x86_64
Requires:      edk2-ovmf
%endif
%ifarch aarch64
Requires:      edk2-aarch64
%endif

Requires:      libnbd >= 1.10
Requires:      %{_bindir}/qemu-nbd
Requires:      %{_bindir}/nbdcopy
Requires:      %{_bindir}/nbdinfo
Requires:      nbdkit-server >= 1.28.3-1.el9
Requires:      nbdkit-curl-plugin
Requires:      nbdkit-file-plugin
Requires:      nbdkit-nbd-plugin
Requires:      nbdkit-null-plugin
Requires:      nbdkit-python-plugin
Requires:      nbdkit-ssh-plugin
%ifarch x86_64
Requires:      nbdkit-vddk-plugin
%endif
Requires:      nbdkit-blocksize-filter
Requires:      nbdkit-cacheextents-filter
Requires:      nbdkit-cow-filter >= 1.28.3-1.el9
Requires:      nbdkit-multi-conn-filter
Requires:      nbdkit-rate-filter
Requires:      nbdkit-readahead-filter
Requires:      nbdkit-retry-filter

# For rhsrvany.exe, used to install firstboot scripts in Windows guests.
Requires:      mingw32-srvany >= 1.0-13

# On RHEL, virtio-win should be used to install virtio drivers
# and qemu-ga in converted guests.  (RHBZ#1972644)
%if 0%{?rhel}
Recommends:    virtio-win
%endif


%description
Virt-v2v converts a single guest from a foreign hypervisor to run on
KVM.  It can read Linux and Windows guests running on VMware, Xen,
Hyper-V and some other hypervisors, and convert them to KVM managed by
libvirt, OpenStack, oVirt, Red Hat Virtualisation (RHV) or several
other targets.  It can modify the guest to make it bootable on KVM and
install virtio drivers so it will run quickly.


%package bash-completion
Summary:       Bash tab-completion for %{name}
BuildArch:     noarch
Requires:      bash-completion >= 2.0
Requires:      %{name} = %{epoch}:%{version}-%{release}


%description bash-completion
Install this package if you want intelligent bash tab-completion
for %{name}.


%package man-pages-ja
Summary:       Japanese (ja) man pages for %{name}
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description man-pages-ja
%{name}-man-pages-ja contains Japanese (ja) man pages
for %{name}.


%package man-pages-uk
Summary:       Ukrainian (uk) man pages for %{name}
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description man-pages-uk
%{name}-man-pages-uk contains Ukrainian (uk) man pages
for %{name}.


%prep
%if 0%{verify_tarball_signature}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -p1

%if 0%{patches_touch_autotools}
autoreconf -i
%endif


%build
%configure \
%if !0%{?rhel}
  --with-extra="fedora=%{fedora},release=%{release}" \
%else
  --with-extra="rhel=%{rhel},release=%{release}" \
%endif

make V=1 %{?_smp_mflags}


%install
%make_install

# Delete libtool crap.
find $RPM_BUILD_ROOT -name '*.la' -delete

# Virt-tools data directory.  This contains symlinks to rhsrvany.exe
# and pnp_wait.exe which are satisfied by the dependency on
# mingw32-srvany.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/virt-tools
pushd $RPM_BUILD_ROOT%{_datadir}/virt-tools
ln -sf ../../i686-w64-mingw32/sys-root/mingw/bin/rhsrvany.exe
ln -sf ../../i686-w64-mingw32/sys-root/mingw/bin/pnp_wait.exe
popd

%if 0%{?rhel}
# On RHEL remove virt-v2v-in-place.
rm $RPM_BUILD_ROOT%{_bindir}/virt-v2v-in-place
rm $RPM_BUILD_ROOT%{_mandir}/man1/virt-v2v-in-place.1*
%endif

# Find locale files.
%find_lang %{name}


%check
# All tests fail at the moment because of bugs in libvirt blockdev.
# # Tests fail on both armv7 and ppc64le in Fedora 31 because the kernel
# # cannot boot on qemu.
# %ifnarch %{arm} ppc64le

# # On x86_64 this single test fails with: "virt-v2v: warning: the
# # target hypervisor does not support a x86_64 KVM guest".  Missing
# # BuildRequires?
# %ifarch x86_64
# truncate -s 0 tests/test-v2v-o-libvirt.sh
# %endif

# # This test fails in mock.
# truncate -s 0 tests/test-v2v-oa-option.sh

# # Make sure we can see the debug messages (RHBZ#1230160).
# export LIBGUESTFS_DEBUG=1
# export LIBGUESTFS_TRACE=1

# make %{?_smp_mflags} check || {
#     cat tests/test-suite.log
#     exit 1
#   }

# %endif


%files -f %{name}.lang
%license COPYING
%doc README
%{_bindir}/virt-v2v
%if !0%{?rhel}
%{_bindir}/virt-v2v-in-place
%endif
%{_mandir}/man1/virt-v2v.1*
%{_mandir}/man1/virt-v2v-hacking.1*
%{_mandir}/man1/virt-v2v-input-vmware.1*
%{_mandir}/man1/virt-v2v-input-xen.1*
%if !0%{?rhel}
%{_mandir}/man1/virt-v2v-in-place.1*
%endif
%{_mandir}/man1/virt-v2v-output-local.1*
%{_mandir}/man1/virt-v2v-output-openstack.1*
%{_mandir}/man1/virt-v2v-output-rhv.1*
%{_mandir}/man1/virt-v2v-release-notes-1.42.1*
%{_mandir}/man1/virt-v2v-release-notes-2.0.1*
%{_mandir}/man1/virt-v2v-support.1*
%{_datadir}/virt-tools


%files bash-completion
%license COPYING
%{_datadir}/bash-completion/completions/virt-v2v


%files man-pages-ja
%license COPYING
%lang(ja) %{_mandir}/ja/man1/*.1*


%files man-pages-uk
%license COPYING
%lang(uk) %{_mandir}/uk/man1/*.1*


%changelog
* Wed Jul 06 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.0.7-1
- New upstream stable branch version 2.0.7

* Thu May 26 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.0.6-1
- New upstream stable branch version 2.0.6

* Thu May 12 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.0.5-1
- New upstream stable branch version 2.0.5

* Tue Apr 26 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.0.4-1
- New upstream stable branch version 2.0.4

* Tue Apr 12 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.0.3-1
- New upstream stable branch version 2.0.3

* Mon Apr 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.0.2-1
- New upstream stable branch version 2.0.2

* Wed Mar 23 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.0.1-1
- New upstream stable branch version 2.0.1
- Fixes security issue when running virt-v2v as root (RHBZ#2066773).

* Mon Mar 14 2022 Richard W.M. Jones <rjones@redhat.com> - 1:2.0.0-1
- New upstream stable branch version 2.0.0
- New virt-v2v-in-place and release notes man pages.
- Remove the RHEL (downstream) patches which are out of date.
- Don't use absolute symlinks.

* Tue Feb 15 2022 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.99-1
- New upstream development version 1.45.99 (preview of 2.0)
- Requires nbdkit-blocksize-filter.

* Thu Feb 10 2022 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.98-1
- New upstream development version 1.45.98 (preview of 2.0)

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.97-3
- OCaml 4.13.1 rebuild to remove package notes

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.45.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.97-1
- New upstream development version 1.45.97 (preview of 2.0)

* Thu Jan 06 2022 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.96-1
- New upstream development version 1.45.96 (preview of 2.0)

* Sat Dec 18 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.95-1
- New upstream development version 1.45.95 (preview of 2.0)

* Tue Dec 07 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.94-1
- New upstream development version 1.45.94 (preview of 2.0)

* Fri Dec 03 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.93-1
- New upstream development version 1.45.93 (preview of 2.0)

* Thu Dec 02 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.92-1
- New upstream development version 1.45.92 (preview of 2.0)

* Thu Nov 25 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.91-2
- Bump release and rebuild

* Tue Nov 23 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.91-1
- New upstream development version 1.45.91 (preview of 2.0)

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.90-2
- OCaml 4.13.1 build

* Tue Sep 21 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.90-1
- New upstream development version 1.45.90 (preview of 2.0)

* Fri Aug 06 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.3-1
- New upstream development version 1.45.3.
- Rebase RHEL patches.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.45.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.2-1
- New upstream development version 1.45.2.
- Remove --debug-overlays and --print-estimate options.
- Remove -o glance option on RHEL 9 (RHBZ#1977539).
- Remove support for RHEV-APT (RHBZ#1945549).

* Wed Jun 16 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.45.1-1
- New upstream development version 1.45.1.
- Require virtio-win on RHEL (RHBZ#1972644).
- v2v-test-harness, virt-v2v-copy-to-local have been removed upstream.

* Thu Jun 10 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.44.0-2
- nbdkit-vddk-plugin dep only exists on x86-64.

* Fri Apr 30 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.44.0-1
- New upstream stable branch version 1.44.0.

* Wed Apr 14 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.5-1
- New upstream version 1.43.5.

* Thu Apr 01 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.4-5
- Add upstream patch to depend on xorriso.
- Change libguestfs-tools-c -> guestfs-tools.

* Tue Mar 30 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.4-3
- Add downstream (RHEL-only) patches (RHBZ#1931724).

* Mon Mar  8 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.4-2
- Bump and rebuild for ocaml-gettext update.

* Wed Mar  3 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.4-1
- New upstream version 1.43.4.

* Tue Mar  2 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.3-4
- OCaml 4.12.0 build

* Tue Mar  2 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.3-3
- Add fix for OCaml 4.12.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.43.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.3-1
- New upstream version 1.43.3.

* Thu Dec 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.2-3
- Drop obsolete virt-v2v-copy-to-local tool for Fedora 34 and RHEL 9.

* Wed Dec 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.2-2
- Unify Fedora and RHEL spec files.

* Tue Dec 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.2-1
- New upstream version 1.43.2.

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.1-5
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.43.1-4
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.43.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.43.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 06 2020 Richard W.M. Jones <rjones@redhat.com> - 1.43.1-1
- New development branch 1.43.

* Wed May 06 2020 Richard W.M. Jones <rjones@redhat.com> - 1.42.0-4
- Re-add Epoch.  Forgotten when we split this package from libguestfs.

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.42.0-2
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Thu Apr 16 2020 Richard W.M. Jones <rjones@redhat.com> - 1.42.0-1
- New upstream stable version 1.42.0.

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-11
- Update all OCaml dependencies for RPM 4.16.

* Thu Feb 27 2020 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-10
- OCaml 4.10.0 final.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.41.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-8
- Bump release and rebuild.

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-7
- Bump release and rebuild.

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-6
- Bump release and rebuild.

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-5
- OCaml 4.10.0+beta1 rebuild.
- Use nbdkit-python-plugin (now all Python 3 in Rawhide).

* Wed Nov 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-4
- Use license instead of doc for COPYING file.
- Include license in all subpackages.
- Use gpgverify macro.
- Don't own bash-completion directory because we Require the
  bash-completion package which owns it already.

* Tue Nov 26 2019 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-2
- Fix permissions on .sig file.
- Disable -oa preallocated test since it fails in reviewers mock environment.

* Fri Nov 15 2019 Richard W.M. Jones <rjones@redhat.com> - 1.41.8-1
- Initial release of separate virt-v2v program, was part of libguestfs.
