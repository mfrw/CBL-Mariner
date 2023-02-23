Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_without check

%global udevdir %(pkg-config --variable=udevdir udev)
%global dracutdir %(pkg-config --variable=dracutdir dracut)

Name:           stratisd
Version:        3.4.4
Release:        1%{?dist}
Summary:        Daemon that manages block devices to create filesystems

# ASL 2.0
# ASL 2.0 or Boost
# ASL 2.0 or MIT
# BSD
# ISC
# MIT
# MIT or ASL 2.0
# MPLv2.0
# Unlicense or MIT
License:        MPLv2.0 and ASL 2.0 and BSD and MIT
URL:            https://github.com/stratis-storage/stratisd
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}-vendor.tar.gz
Source2:        %{crates_source}


ExclusiveArch:  %{rust_arches}
%if 0%{?rhel} && !0%{?eln}
ExcludeArch:    i686
%endif

%if 0%{?rhel} && !0%{?eln}
BuildRequires:  rust-toolset
%else
BuildRequires:  rust-packaging
%endif
BuildRequires:  rust-srpm-macros
BuildRequires:  systemd-devel
BuildRequires:  dbus-devel
BuildRequires:  libblkid-devel
BuildRequires:  cryptsetup-devel
BuildRequires:  clang
BuildRequires:  %{_bindir}/a2x

# Required to calculate install directories
BuildRequires:  systemd
BuildRequires:  dracut

Requires:       xfsprogs
Requires:       device-mapper-persistent-data
Requires:       systemd-libs
Requires:       dbus-libs
Requires:       cryptsetup-libs
Requires:       libblkid

# stratisd does not require clevis; it can be used in restricted environments
# where clevis is not available.
Recommends:     clevis-luks >= 18

%description
%{summary}.

%package dracut
Summary: Dracut modules for use with stratisd

ExclusiveArch:  %{rust_arches}

Requires:     stratisd
Requires:     dracut >= 051
Requires:     plymouth

%description dracut
%{summary}.

%prep
%setup -q
tar --strip-components=1 --extract --verbose --file %{SOURCE2}
# Patches must be applied after the upstream package is extracted.
%if 0%{?rhel} && !0%{?eln}
# Source1 is vendored dependencies
%cargo_prep -V 1
%else
%cargo_prep
%generate_buildrequires
%cargo_generate_buildrequires -f dbus_enabled,min,systemd_compat
%endif

%build
%if 0%{?rhel} && !0%{?eln}
%{cargo_build} --bin=stratisd
%{cargo_build} --bin=stratis-min --bin=stratisd-min --bin=stratis-utils --no-default-features --features min,systemd_compat
%else
%{__cargo} build %{?__cargo_common_opts} --release --bin=stratisd
%{__cargo} build %{?__cargo_common_opts} --release --bin=stratis-min --bin=stratisd-min --bin=stratis-utils --no-default-features --features min,systemd_compat
%endif
a2x -f manpage docs/stratisd.txt

%install
%make_install DRACUTDIR=%{dracutdir} PROFILEDIR=release

%if %{with check}
%check
%if 0%{?rhel} && !0%{?eln}
%cargo_test --no-run
%else
%cargo_test -- --no-run
%endif
%endif

%post
%systemd_post stratisd.service

%preun
%systemd_preun stratisd.service

%postun
%systemd_postun_with_restart stratisd.service

%files
%license LICENSE
%doc README.md
%{_libexecdir}/stratisd
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/system.d/stratisd.conf
%{_mandir}/man8/stratisd.8*
%{_unitdir}/stratisd.service
%{_udevrulesdir}/61-stratisd.rules
%{udevdir}/stratis-str-cmp
%{udevdir}/stratis-base32-decode
%{_bindir}/stratis-predict-usage
%{_unitdir}/stratisd-min-postinitrd.service
%{_unitdir}/stratis-fstab-setup@.service
%{_bindir}/stratis-min
%{_libexecdir}/stratisd-min
%{_systemd_util_dir}/stratis-fstab-setup


%files dracut
%license LICENSE
%{dracutdir}/modules.d/90stratis-clevis/module-setup.sh
%{dracutdir}/modules.d/90stratis-clevis/stratis-clevis-rootfs-setup
%{dracutdir}/modules.d/90stratis/61-stratisd.rules
%{dracutdir}/modules.d/90stratis/module-setup.sh
%{dracutdir}/modules.d/90stratis/stratis-rootfs-setup
%{dracutdir}/modules.d/90stratis/stratisd-min.service
%{_systemd_util_dir}/system-generators/stratis-clevis-setup-generator
%{_systemd_util_dir}/system-generators/stratis-setup-generator

%changelog
* Tue Jan 03 2023 Bryan Gurney <bgurney@redhat.com> - 3.4.4-1
- Update to 3.4.4

* Fri Dec 16 2022 Bryan Gurney <bgurney@redhat.com> - 3.4.3-1
- Update to 3.4.3

* Wed Dec 07 2022 Bryan Gurney <bgurney@redhat.com> - 3.4.2-1
- Update to 3.4.2

* Tue Nov 29 2022 Bryan Gurney <bgurney@redhat.com> - 3.4.1-1
- Update to 3.4.1

* Tue Nov 15 2022 Bryan Gurney <bgurney@redhat.com> - 3.3.0-1
- Update to 3.3.0

* Sun Aug 28 2022 mulhern <amulhern@redhat.com> - 3.2.3-1
- Update to 3.2.3

* Thu Aug 25 2022 Bryan Gurney <bgurney@redhat.com> - 3.2.2-1
- Update to 3.2.2

* Mon Aug 01 2022 Bryan Gurney <bgurney@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Wed Jul 27 2022 mulhern <amulhern@redhat.com> - 3.1.2-1
- Update to 3.1.2

* Thu Jul 21 2022 mulhern <amulhern@redhat.com> - 3.1.1-2
- Rebuild against devicemapper-rs 0.32.1

* Wed Jul 13 2022 Bryan Gurney <bgurney@redhat.com> - 3.1.1-1
- Update to 3.1.1

* Thu Jun 23 2022 Bryan Gurney <bgurney@redhat.com> - 3.1.0-3
- Add gating test

* Mon Jun 06 2022 Bryan Gurney <bgurney@redhat.com> - 3.1.0-2
- Synchronize spec with upstream unified spec file
- Remove .rust2rpm.conf file
- Remove buildhost_subdomain section from rpminspect.yaml

* Wed May 25 2022 mulhern <amulhern@redhat.com> - 3.1.0-1
- Update to 3.1.0

* Tue Mar 15 2022 mulhern <amulhern@redhat.com> - 3.0.4-2
- Use upstream crate for Rust source; install two scripts

* Sat Feb 12 2022 mulhern <amulhern@redhat.com> - 3.0.4-1
- Update to 3.0.4

* Mon Feb 7 2022 mulhern <amulhern@redhat.com> - 3.0.3-1
- Update to 3.0.3

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 mulhern <amulhern@redhat.com> - 3.0.2-1
- Update to 3.0.2

* Sun Nov 28 2021 mulhern <amulhern@redhat.com> - 2.4.4-1
- Update to 2.4.4

* Tue Oct 19 2021 mulhern <amulhern@redhat.com> - 2.4.2-3
- Rebuilt to include dbus-tree 0.9.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 1 2021 mulhern <amulhern@redhat.com> - 2.4.2-1
- Update to 2.4.2

* Tue May 18 2021 John Baublitz <jbaublitz@redhat.com> - 2.4.1-1
- Update to new release and split dracut modules out into subpackage

* Thu May 13 2021 John Baublitz <jbaublitz@redhat.com> - 2.4.0-4
- Ensure that binaries are installed with proper features enabled

* Wed May 12 2021 John Baublitz <jbaublitz@redhat.com> - 2.4.0-3
- Fix installed file paths

* Tue Apr 27 2021 mulhern <amulhern@redhat.com> - 2.4.0-2
- Fixes to previous release

* Tue Apr 27 2021 mulhern <amulhern@redhat.com> - 2.4.0-1
- Update to 2.4.0

* Wed Mar 17 2021 mulhern <amulhern@redhat.com> - 2.3.0-10
- Use external URL for vendored sources

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.3.0-9
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.3.0-7
- Fix build on ELN

* Fri Jan 15 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.3.0-6
- Make package compatible without violating guidelines

* Fri Jan 15 2021 mulhern <amulhern@redhat.com> - 2.3.0-5
- Add both sources at the same time

* Fri Jan 15 2021 mulhern <amulhern@redhat.com> - 2.3.0-4
- Restore RHEL/Fedora compatible spec file, adding some additional changes

* Fri Jan 15 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.3.0-3
- Partially revert previous commit

* Thu Jan 14 2021 mulhern <amulhern@redhat.com> - 2.3.0-2
- Make RHEL/Fedora compatible spec file

* Tue Jan 12 2021 mulhern <amulhern@redhat.com> - 2.3.0-1
- Update to 2.3.0

* Mon Dec 28 13:34:26 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.2.1-3
- Rebuild

* Sun Dec 27 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.2.1-2
- Rebuild

* Mon Nov 9 2020 mulhern <amulhern@redhat.com> - 2.2.1-1
- Update to 2.2.1

* Mon Oct 19 2020 mulhern <amulhern@redhat.com> - 2.2.0-1
- Update to 2.2.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 John Baublitz <jbaublitz@redhat.com> - 2.1.0-1
- Update to 2.1.0

* Wed Feb 19 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.1-2
- Fixup license

* Wed Feb 19 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Fri Sep 06 20:52:06 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Josh Stone <jistone@redhat.com> - 1.0.4-2
- Bump nix to 0.14

* Tue May 07 08:16:24 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Wed Mar 06 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Wed Dec 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Fri Nov 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Thu Sep 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Wed Sep 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-4
- Add missing systemd scriptlets

* Wed Sep 19 2018 Tony Asleson <tasleson@redhat.com> - 0.9.0-3
- Add systemd unit file
- Remove systemd activation file

* Tue Sep 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-2
- Rebuild to workaround pungi bug

* Sat Sep 01 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Fri Aug 3 2018 Andy Grover <agrover@redhat.com> - 0.5.5-2
- Disable a failing but noncritical test

* Fri Aug 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.5-1
- Update to 0.5.5

* Thu Jul 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.4-3
- Upgrade dependencies

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.4-1
- Update to 0.5.4

* Fri Jun 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.3-2
- Add -init version of daemon
- Own dbus-1 directory

* Mon Jun 4 2018 Andy Grover <agrover@redhat.com> - 0.5.3-1
- Update to 0.5.3

* Fri May 4 2018 Andy Grover <agrover@redhat.com> - 0.5.2-2
- Add 0002-Prefix-commands-with-entire-path.patch

* Tue May 1 2018 Andy Grover <agrover@redhat.com> - 0.5.2-1
- Update to 0.5.2

* Tue Apr 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Tue Mar 13 2018 Andy Grover <agrover@redhat.com> - 0.5.0-2
- Add stratisd manpage

* Thu Mar 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Thu Feb 15 2018 Andy Grover <agrover@redhat.com> - 0.1.5-2
- Require packages that contain binaries that we exec: xfsprogs and
  device-mapper-persistent-data

* Sun Feb 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-3
- Rebuild for rust-packaging v5

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-2
- Move binary under %%{_libexecdir}
- Add dbus service (so it is activatable)
- Fix rand's version bump

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-1
- Initial package
