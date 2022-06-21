Summary:	PCManFM file manager.
Name:		pcmanfm
Version:	1.3.2
Release:	2%{?dist}
License:	LGPLv2+
URL:		http://downloads.sourceforge.net/pcmanfm
Group:		User Interface/Desktops
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	http://downloads.sourceforge.net/pcmanfm/%{name}-%{version}.tar.xz
%define sha1 pcmanfm=0a195301de31c82f1c169e620be7cea8b91813b5
BuildRequires:	libfm-devel
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

Requires:	libfm

# support new desktop insertion
# https://sourceforge.net/p/pcmanfm/bugs/1064/
Patch101:	pcmanfm-0101-split-out-per-monitor-initialization-part-from-fm_de.patch
Patch102:	pcmanfm-0102-use-GList-for-FmDesktop-entries-instead-of-static-ar.patch
Patch103:	pcmanfm-0103-Fix-the-bug-that-desktop-configuration-is-not-proper.patch
Patch104:	pcmanfm-0104-Finish-implementation-of-inserting-new-monitor.patch

# connect_model: connect to signal before setting folder for model
Patch202:	pcmanfm-0202-connect_model-connect-to-signal-before-setting-folde.patch

%description
The PCManFM package contains an extremely fast, lightweight, yet feature-rich file manager with tabbed browsing.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
Requires:	libfm-devel
%description 	devel
Install this package if you want do compile applications using the pcre
library.
%prep
%setup -q
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch202 -p1

%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
sed -i 's/System;//' %{buildroot}/usr/share/applications/pcmanfm.desktop
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_libdir}
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 1.3.2-2
-	Mariner initial version
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 1.2.3-2
-	Mariner initial version
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 1.2.3-1
-	initial version
