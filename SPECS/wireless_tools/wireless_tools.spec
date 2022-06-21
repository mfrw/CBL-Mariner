%define majver %(echo %version | cut -d. -f1)
Name:          wireless_tools
Version:       30.pre9
Release:       2%{?dist}
Summary:       A set of tools allowing to manipulate the Wireless Extensions
Group:         System/Kernel and Hardware
Vendor:		Microsoft Corporation
Distribution:	Mariner
URL:           http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Tools.html
Source0:       http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/wireless_tools.%{version}.tar.gz
%define sha1 wireless_tools.%{version}=41db5ced9ed3d8d3cc104ce43c19af1d72f07eec
Source1:       wireless_tools-ifrename_iftab
Patch0:        %{name}-29-iwlib_h_fix.patch
License:       GPL
BuildRequires: pkg-config
Requires:      libiw = %{?epoch:%epoch:}%{version}-%{release}

%description
A set of tools and a library allowing to manipulate the Wireless Extensions.

%package -n libiw
Summary:       A library implementing wireless tools functions
Group:         System/Libraries

%description -n libiw
A library implementing wireless tools functions

%package -n libiw-devel
Summary:       Devel files for wireless_tools library
Group:         Development/Libraries
Requires:      libiw = %{?epoch:%epoch:}%{version}-%{release}

%description -n libiw-devel
A set of tools and a library allowing to manipulate the Wireless Extensions.
This package contains static libraries and header files need for development.

%package -n ifrename
Summary:       A tool allowing you to assign a consistent name to each of your network interface
Group:         System/Tools

%description -n ifrename
Ifrename  is a tool allowing you to assign a consistent name to each of your network interface.

%prep
%setup -q -n wireless_tools.%{majver}
sed -i "s|\(BUILD_STATIC = y\)|#\1|" Makefile
%patch0 -p1

%build
make \
   BUILD_STATIC= \
   PREFIX=%{_prefix}

%install
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"
%makeinstall install-static \
     PREFIX=%{buildroot}%{_prefix} \
     INSTALL_LIB=%{buildroot}%{_libdir} \
     INSTALL_MAN=%{buildroot}%{_mandir}

install -d %{buildroot}%{_bindir}
ln -s ../sbin/iwlist %{buildroot}%{_bindir}/iwlist
install -D -m 0644 %{S:1} %{buildroot}%{_sysconfdir}/iftab

%post -n libiw -p /sbin/ldconfig
%postun -n libiw -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_sbindir}/iwconfig
%{_sbindir}/iwevent
%{_sbindir}/iwgetid
%{_sbindir}/iwlist
%{_sbindir}/iwpriv
%{_sbindir}/iwspy
%{_bindir}/iwlist
%{_mandir}/man7/wireless.*
%{_mandir}/man8/iwconfig.*
%{_mandir}/man8/iwevent.*
%{_mandir}/man8/iwgetid.*
%{_mandir}/man8/iwlist.*
%{_mandir}/man8/iwpriv.*
%{_mandir}/man8/iwspy.*
%lang(cs) %{_mandir}/cs/man*/*
%lang(fr) %{_mandir}/fr.*/man*/*

%files -n libiw
%defattr(-,root,root)
%{_libdir}/libiw.so.*

%files -n libiw-devel
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h

%files -n ifrename
%defattr(-,root,root)
%{_sbindir}/ifrename
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/iftab
%{_mandir}/man5/iftab.*
%{_mandir}/man8/ifrename.*

%changelog
*	Mon Jun 29 2020 Andrew Phelps <anphel@microsoft.com> 30.pre9-2
-	Use default value of "CC" in make command.
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 30.pre9-1
-	Mariner
