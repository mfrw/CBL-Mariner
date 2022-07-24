Name:          alsa-plugins
Version:       1.1.4
Release:       1%{?dist}
Summary:       Plugins for the Advanced Linux Sound Architecture (ALSA)
Group:         System/Libraries
Vendor:		Microsoft Corporation
Distribution:	Mariner
URL:           http://www.alsa-project.org/
Source0:        ftp://ftp.alsa-project.org/pub/plugins/alsa-plugins-%{version}.tar.bz2
%define sha1 alsa-plugins=3fae66ffa7b25d52e57793240f775634c18b1e80
Patch0:        libalsa-plugins-1.0.23-jack_torben.patch
License:       LGPL
BuildRequires: glibc-devel
BuildRequires: alsa-lib-devel
BuildRequires: speex-devel
BuildRequires: libpulse-devel
BuildRequires:  systemd-devel
BuildRequires:  dbus-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXtst-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXau-devel
BuildRequires:  libXtst-devel

%description
Plugins for the Advanced Linux Sound Architecture (ALSA).

%prep
%setup -q
#%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%{_libdir}/alsa-lib/libasound_module_*
%if "%{stage1}" != "1"
%{_datadir}/alsa/alsa.conf.d/50-pulseaudio.conf
%{_datadir}/alsa/alsa.conf.d/99-pulseaudio-default.conf.example
%endif
%doc COPYING

%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 1.1.4-1
-	Initial Version Mariner UI
