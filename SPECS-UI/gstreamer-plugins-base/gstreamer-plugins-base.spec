#
# spec file for package gstreamer-plugins-base
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


%define _name gst-plugins-base
%define gst_branch 1.0
%define gstreamer_req_version %(echo %{version} | sed -e "s/+.*//")
Name:           gstreamer-plugins-base
Version:        1.20.0
Release:        1%{?dist}
Summary:        GStreamer Streaming-Media Framework Plug-Ins
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://gstreamer.freedesktop.org
# Disable tarball source url, use _service
#Source0:        %%{url}/src/gst-plugins-base/%%{_name}-%%{version}.tar.xz
Source0:        %{_name}-%{version}.tar.xz
Source1:        gstreamer-plugins-base.appdata.xml
Source2:        baselibs.conf
# PATCH-FIX-OPENSUSE gstreamer-plugins-base-gl-deps.patch dimstar@opensuse.org -- Local workaround for https://gitlab.freedesktop.org/gstreamer/gst-plugins-base/issues/735
# Patch3:         gstreamer-plugins-base-gl-deps.patch
# Patch4:         add_wayland_dep_to_tests.patch
Patch5:         MR-221-video-anc-add-two-new-CEA-608-caption-formats.patch

BuildRequires:  cdparanoia-devel
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel >= 2.40.0
BuildRequires:  gobject-introspection-devel >= 1.31.1
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libXext-devel
BuildRequires:  libXv-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  meson >= 0.47.0
BuildRequires:  orc >= 0.4.24
BuildRequires:  orc-devel >= 0.4.24
BuildRequires:  orc-compiler >= 0.4.24
BuildRequires:  pkg-config alsa-lib-devel
BuildRequires:  cmake graphene-devel graphene
BuildRequires:  python3 python3-devel python3-libs
BuildRequires:  python3-xml
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(alsa) >= 0.9.1
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freetype2) >= 2.0.9
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.40
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv1_cm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  iso-codes-devel
BuildRequires:  pkgconfig(libdrm) >= 2.4.55
BuildRequires:  pkgconfig(libvisual-0.4) >= 0.4.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(ogg) >= 1.0
BuildRequires:  pkgconfig(opus) >= 0.9.4
BuildRequires:  pkgconfig(pango) >= 1.22.0
BuildRequires:  pkgconfig(pangocairo) >= 1.22.0
BuildRequires:  pkgconfig(theoradec) >= 1.1
BuildRequires:  pkgconfig(theoraenc) >= 1.1
BuildRequires:  pkgconfig(vorbis) >= 1.0
BuildRequires:  pkgconfig(vorbisenc) >= 1.0
BuildRequires:  pkgconfig(wayland-client) >= 1.0
BuildRequires:  pkgconfig(wayland-cursor) >= 1.0
BuildRequires:  pkgconfig(wayland-egl) >= 1.0
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-vulkan-devel

Requires:       gstreamer1 >= %{gstreamer_req_version}
Supplements:    gstreamer
# Conflicts:      gstreamer-plugins-bad < 1.18.1
# Generic name, never used in SuSE:
Provides:       gst-plugins-base = %{version}
Obsoletes:      libgstbadvideo-1_0-0
Obsoletes:      typelib-1_0-GstFft-1_0 < 1.14.0
%if 0%{?suse_version} < 1550
BuildRequires:  pkgconfig(cairo)
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(graphene-1.0)
%endif

%description
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstallocators-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstallocators-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstAllocators-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstAllocators-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgstapp-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstapp-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstApp-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstApp-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgstaudio-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstaudio-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstAudio-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstAudio-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgstfft-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstfft-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstFft-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstFft-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstgl-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstgl-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstGL-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstGL-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n typelib-1_0-GstGLEGL-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstGLEGL-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n typelib-1_0-GstGLWayland-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstGLWayland-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n typelib-1_0-GstGLX11-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstGLX11-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgstpbutils-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstpbutils-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstPbutils-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstPbutils-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgstriff-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstriff-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstrtp-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstrtp-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstRtp-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstRtp-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgstrtsp-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstrtsp-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstRtsp-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstRtsp-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgstsdp-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstsdp-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstSdp-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstSdp-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgsttag-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgsttag-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstTag-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstTag-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgstvideo-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstvideo-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstVideo-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstVideo-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package devel
Summary:        Include files and librs mandatory for development with gstreamer-plugins-base
Group:          Development/Libraries/C and C++
Requires:       libgstallocators-1_0-0 = %{version}
Requires:       libgstapp-1_0-0 = %{version}
Requires:       libgstaudio-1_0-0 = %{version}
Requires:       libgstfft-1_0-0 = %{version}
Requires:       libgstgl-1_0-0 = %{version}
Requires:       libgstpbutils-1_0-0 = %{version}
Requires:       libgstriff-1_0-0 = %{version}
Requires:       libgstrtp-1_0-0 = %{version}
Requires:       libgstrtsp-1_0-0 = %{version}
Requires:       libgstsdp-1_0-0 = %{version}
Requires:       libgsttag-1_0-0 = %{version}
Requires:       libgstvideo-1_0-0 = %{version}
Requires:       typelib-1_0-GstAllocators-1_0 = %{version}
Requires:       typelib-1_0-GstApp-1_0 = %{version}
Requires:       typelib-1_0-GstAudio-1_0 = %{version}
Requires:       typelib-1_0-GstGL-1_0 = %{version}
Requires:       typelib-1_0-GstGLEGL-1_0 = %{version}
Requires:       typelib-1_0-GstGLWayland-1_0 = %{version}
Requires:       typelib-1_0-GstGLX11-1_0 = %{version}
Requires:       typelib-1_0-GstPbutils-1_0 = %{version}
Requires:       typelib-1_0-GstRtp-1_0 = %{version}
Requires:       typelib-1_0-GstRtsp-1_0 = %{version}
Requires:       typelib-1_0-GstSdp-1_0 = %{version}
Requires:       typelib-1_0-GstTag-1_0 = %{version}
Requires:       typelib-1_0-GstVideo-1_0 = %{version}
# Generic name, never used in SuSE:
Provides:       gst-plugins-base-devel = %{version}

%description devel
This package contains all necessary include files and libraries needed
to compile and link applications that use gstreamer-plugins-base.


%prep
%autosetup -n %{_name}-%{version} -p1

%build
export PYTHON=%{_bindir}/python3
# TODO: tremor needs libvorbisidec
%meson \
	-Dpackage-name='Mariner GStreamer-plugins-base package'\
	-Dpackage-origin='https://packages.microsoft.com'\
	-Ddoc=disabled \
	-Dintrospection=enabled \
	-Dorc=enabled \
	-Dexamples=disabled \
	-Dtremor=disabled \
	%{nil}
%meson_build

%install
%meson_install
if [ -f %{buildroot}%{_datadir}/appdata/gstreamer-plugins-base.appdata.xml ]; then
  echo "Please remove the added gstreamer-plugins-base.appdata.xml file from the sources - the tarball installs it"
  false
else
  mkdir -p %{buildroot}%{_datadir}/appdata
  cp %{SOURCE1} %{buildroot}%{_datadir}/appdata/
fi

find %{buildroot} -type f -name "*.la" -delete -print


%post -n libgstallocators-1_0-0 -p /sbin/ldconfig
%postun -n libgstallocators-1_0-0 -p /sbin/ldconfig
%post -n libgstapp-1_0-0 -p /sbin/ldconfig
%postun -n libgstapp-1_0-0 -p /sbin/ldconfig
%post -n libgstaudio-1_0-0 -p /sbin/ldconfig
%postun -n libgstaudio-1_0-0 -p /sbin/ldconfig
%post -n libgstfft-1_0-0 -p /sbin/ldconfig
%postun -n libgstfft-1_0-0 -p /sbin/ldconfig
%post -n libgstgl-1_0-0 -p /sbin/ldconfig
%postun -n libgstgl-1_0-0 -p /sbin/ldconfig
%post -n libgstpbutils-1_0-0 -p /sbin/ldconfig
%postun -n libgstpbutils-1_0-0 -p /sbin/ldconfig
%post -n libgstriff-1_0-0 -p /sbin/ldconfig
%postun -n libgstriff-1_0-0 -p /sbin/ldconfig
%post -n libgstrtp-1_0-0 -p /sbin/ldconfig
%postun -n libgstrtp-1_0-0 -p /sbin/ldconfig
%post -n libgstrtsp-1_0-0 -p /sbin/ldconfig
%postun -n libgstrtsp-1_0-0 -p /sbin/ldconfig
%post -n libgstsdp-1_0-0 -p /sbin/ldconfig
%postun -n libgstsdp-1_0-0 -p /sbin/ldconfig
%post -n libgsttag-1_0-0 -p /sbin/ldconfig
%postun -n libgsttag-1_0-0 -p /sbin/ldconfig
%post -n libgstvideo-1_0-0 -p /sbin/ldconfig
%postun -n libgstvideo-1_0-0 -p /sbin/ldconfig

%files
%license COPYING
%{_mandir}/man1/gst-device-monitor-*
%{_mandir}/man1/gst-discoverer-*
%{_mandir}/man1/gst-play-*
%{_bindir}/gst-device-monitor-%{gst_branch}
%{_bindir}/gst-discoverer-%{gst_branch}
%{_bindir}/gst-play-%{gst_branch}
%{_datadir}/appdata/gstreamer-plugins-base.appdata.xml
%{_libdir}/gstreamer-%{gst_branch}/libgstadder.so
%{_libdir}/gstreamer-%{gst_branch}/libgstalsa.so
%{_libdir}/gstreamer-%{gst_branch}/libgstapp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudioconvert.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudiomixer.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudioresample.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudiotestsrc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudiorate.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcdparanoia.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcompositor.so
%{_libdir}/gstreamer-%{gst_branch}/libgstencoding.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgio.so
%{_libdir}/gstreamer-%{gst_branch}/libgstlibvisual.so
%{_libdir}/gstreamer-%{gst_branch}/libgstogg.so
%{_libdir}/gstreamer-%{gst_branch}/libgstopengl.so
%{_libdir}/gstreamer-%{gst_branch}/libgstopus.so
%{_libdir}/gstreamer-%{gst_branch}/libgstoverlaycomposition.so
%{_libdir}/gstreamer-%{gst_branch}/libgstpango.so
%{_libdir}/gstreamer-%{gst_branch}/libgstpbtypes.so
%{_libdir}/gstreamer-%{gst_branch}/libgstplayback.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrawparse.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsubparse.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttcp.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttheora.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttypefindfunctions.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideoconvert.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideorate.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideoscale.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideotestsrc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvolume.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvorbis.so
%{_libdir}/gstreamer-%{gst_branch}/libgstximagesink.so
%{_libdir}/gstreamer-%{gst_branch}/libgstxvimagesink.so
/usr/share/locale

%files -n libgstallocators-1_0-0
%{_libdir}/libgstallocators*.so.*

%files -n typelib-1_0-GstAllocators-1_0
%{_libdir}/girepository-1.0/GstAllocators-*.typelib

%files -n libgstapp-1_0-0
%{_libdir}/libgstapp*.so.*

%files -n typelib-1_0-GstApp-1_0
%{_libdir}/girepository-1.0/GstApp-*.typelib

%files -n libgstaudio-1_0-0
%{_libdir}/libgstaudio*.so.*

%files -n typelib-1_0-GstAudio-1_0
%{_libdir}/girepository-1.0/GstAudio-*.typelib

%files -n libgstfft-1_0-0
%{_libdir}/libgstfft*.so.*

%files -n libgstgl-1_0-0
%{_libdir}/libgstgl-%{gst_branch}.so.0*

%files -n typelib-1_0-GstGL-1_0
%{_libdir}/girepository-1.0/GstGL-*.typelib

%files -n typelib-1_0-GstGLEGL-1_0
%{_libdir}/girepository-1.0/GstGLEGL-1.0.typelib

%files -n typelib-1_0-GstGLWayland-1_0
%{_libdir}/girepository-1.0/GstGLWayland-1.0.typelib

%files -n typelib-1_0-GstGLX11-1_0
%{_libdir}/girepository-1.0/GstGLX11-1.0.typelib

%files -n libgstpbutils-1_0-0
%{_libdir}/libgstpbutils*.so.*

%files -n typelib-1_0-GstPbutils-1_0
%{_libdir}/girepository-1.0/GstPbutils-*.typelib

%files -n libgstriff-1_0-0
%{_libdir}/libgstriff*.so.*

%files -n libgstrtp-1_0-0
%{_libdir}/libgstrtp*.so.*

%files -n typelib-1_0-GstRtp-1_0
%{_libdir}/girepository-1.0/GstRtp-*.typelib

%files -n libgstrtsp-1_0-0
%{_libdir}/libgstrtsp*.so.*

%files -n typelib-1_0-GstRtsp-1_0
%{_libdir}/girepository-1.0/GstRtsp-*.typelib

%files -n libgstsdp-1_0-0
%{_libdir}/libgstsdp*.so.*

%files -n typelib-1_0-GstSdp-1_0
%{_libdir}/girepository-1.0/GstSdp-*.typelib

%files -n libgsttag-1_0-0
%{_libdir}/libgsttag*.so.*

%files -n typelib-1_0-GstTag-1_0
%{_libdir}/girepository-1.0/GstTag-*.typelib

%files -n libgstvideo-1_0-0
%{_libdir}/libgstvideo*.so.*

%files -n typelib-1_0-GstVideo-1_0
%{_libdir}/girepository-1.0/GstVideo-*.typelib

%files devel
%doc AUTHORS NEWS README RELEASE REQUIREMENTS
%{_includedir}/gstreamer-%{gst_branch}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/gst-plugins-base/
%dir %{_datadir}/gst-plugins-base/%{gst_branch}/
%{_datadir}/gst-plugins-base/%{gst_branch}/license-translations.dict
%dir %{_libdir}/gstreamer-%{gst_branch}/include
%dir %{_libdir}/gstreamer-%{gst_branch}/include/gst
%dir %{_libdir}/gstreamer-%{gst_branch}/include/gst/gl
%{_libdir}/gstreamer-%{gst_branch}/include/gst/gl/gstglconfig.h


%changelog
* Thu Sep 16 2021 Bjørn Lie <bjorn.lie@gmail.com>
- Stop building doc sub-package, we will in the future use
  upstreams own standalone doc package. Following this: Drop
  fdupes, gtk-doc and hotdoc BuildRequires, and fdupes call, no
  longer needed nor usefull.
* Thu Sep 16 2021 Stanislav Brabec <sbrabec@suse.com>
- Remove obsolete translation-update-upstream support
  (jsc#SLE-21105).
* Wed Sep 15 2021 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 1.18.5:
  + appsrc: Don't leak buffer list while wrongly unreffing buffer
    on EOS/flushing
  + audioaggregator:
  - Don't overwrite already written samples
  - Resync on the next buffer when dropping a buffer on discont
    resyncing
  + audiobasesink: Fix of double lock release
  + audiobasesrc: Fix divide by zero assertion
  + clockoverlay: Fix broken string formatting by strftime() on
    Windows
  + compositor: Fix NV12 blend operation
  + giosrc: Don't leak scheme string in gst_gio_src_query()
  + giobasesink: Handle incomplete writes in
    gst_gio_base_sink_render()
  + gl/wayland:
  - Use consistent wl_display when creating work queue for proxy
    wrapper
  - Provide a dummy global_remove function
  + gl: Fix build when Meson >= 0.58.0rc1
  + playbin2: fix base_time selection when flush seeking live (such
    as with RTSP)
  + rtspconnection:
  - Add IPv6 support for tunneled mode
  - Consistently translate GIOError to GstRTSPResult (for
    rtspsrc)
  + rawbaseparse: check destination format correctly
  + uridecodebin: Don't force floating reference for future
    reusable decodebin
  + parsebin: Put stream flags in GstStream
  + splitmuxsink: always use factory property when set
  + video-converter: Set up matrix tables only once.
  + videoscale: Performance degradation from 1.16.2 -> 1.18.4
  + videotestsrc: Fix a leak when computing alpha caps
  + audio/video-converter: Plug some minor leaks
  + audio,video-format: Make generate_raw_formats idempotent for
    assertions
  + Don't use volatile to mean atomic (fixes compiler warnings with
    gcc 11)
  + Fix build issue on MinGW64
- Drop 90903917.patch: Fixed upstream.
* Sat Jul 17 2021 Dominique Leuenberger <dimstar@opensuse.org>
- Add 90903917.patch: Fix build with meson >= 0.58.0rc1
* Sat May  8 2021 Dirk Müller <dmueller@suse.com>
- don't own appdata dir - comes from filesystem rpm
* Tue Mar 30 2021 Antonio Larrosa <alarrosa@suse.com>
- Update to version 1.18.4:
  + tag: id3v2: fix frame size check and potential invalid reads
  + audio: Fix gst_audio_buffer_truncate() meta handling for non-interleaved audio
  + audioresample: respect buffer layout when draining
  + audioaggregator: fix input_buffer ownership
  + decodebin3: change stream selection message owner, so that the app sends the stream-selection event to the right element
  + rtspconnection: correct data_size when tunneled mode
  + uridecodebin3: make caps property work
  + video-converter: Don't upsample invalid lines
  + videodecoder: Fix racy critical when pool negotiation occurs during flush
  + video: Convert gst_video_info_to_caps() to take self as const ptr
  + examples: added qt core dependency for qt overlay example
* Sat Jan 16 2021 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 1.18.3:
  + audiorate: Make buffer writable before changing its metadata
  + compositor: fix blending of subsampled components
  + decodebin3:
  - When reconfiguring a slot make sure that the ghostpad is
    unlinked
  - Release selection lock when pushing EOS
  + encodebasebin: Ensure that parsers are compatible with selected
    encoders
  + tagdemux: resize and trim buffer in place to fix interaction
    with oggdemux
  + videoaggregator: Pop out old buffers on timeout
  + video-blend: fix blending 8-bit and 16-bit frames together
  + appsrc: fix signal documentation
  + gl: document some GL caps specifics
  + libvisual: workaround clang compiler warning
* Wed Dec  9 2020 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 1.18.2:
  + gl/eagl: internal view resize fixes for glimagesink
  + video-converter: increase the number of cache lines for
    resampling, fixes significant color issues and artefacts with
    "special" resizing parameters in compositor
  + compositor: Don't crash in prepare_frame() if the pad was just
    removed
  + decodebin3: Properly handle caps query with no filter
  + videoaggregator:
  - Guarantee that the output format is supported
  - Fix locking around vagg->info
  - Fix renegotiation when using convert pad
  - document and fix locking in convert pad
  + gluploadelement:
  - Avoid race condition of base class' context
  - Avoid race condition of inside upload creation
  + gl: Fix prototype of glGetSynciv()
  + tcpserversink: Don't assume g_socket_get_remote_address()
    succeeds
  + audiodecoder, videodecoder: Don't reset max-errors property
    value in reset()
  + audioencoder: Fix incorrect GST_LOG_OBJECT usage
  + pbutils: Fix segfault when using invalid encoding profile
  + g-i: videometa: gir annotate the size of plane array in new API
  + examples/gl/gtk: Add missing dependency on gstgl
  + video: fix doc warning.
- Fix the _service file and spec to really use the tarball
  generated by service.
* Tue Oct 27 2020 Antonio Larrosa <alarrosa@suse.com>
- Update to 1.18.1:
  + Highlighted bugfixes in 1.18.1
  - important security fixes
  - bug fixes and memory leak fixes
  - various stability and reliability improvements
  + gst-plugins-base changes:
  - theoradec: Set telemetry options only if they are nonzero
  - glslstage: delete shader on finalize of stage
  - urisourcebin: Fix crash caused by use after free
  - decodebin3: Store stream-start event on output pad before
    exposing it
  - Add some missing nullable annotations
  - typefind/xdgmime: Validate mimetypes to be valid
    GstStructure names before using them
  - uridecodebin3: Forward upstream events to decodebin3 directly
  - video-converter: Add fast paths from v210 to I420/YV12, Y42B,
    UYVY and YUY2
  - videoaggregator: Limit accepted caps by template caps
  - gstrtpbuffer: fix header extension length validation
  - decodebin3: only force streams-selected seqnum after a
    select-streams
  - videodecoder: don't copy interlace-mode from reference state
  - enable abi checks
  - multihandlesink: Don't pass NULL caps to gst_caps_is_equal
  - audio: video: Fix in/outbuf confusion of transform_meta
  - meson: Always wrap "prefix" option with join_paths() to make
    Windows happy
  - videoaggregator: ensure peek_next_sample() uses the correct
    caps
  - meson: Actually build gstgl without implicit include dirs
  - videoaggregator: Don't require any pads to be configured for
    negotiating source pad caps
  - gst-libs: gl: Fix documentation typo and clarify
    gl_memory_texsubimage
  - audioaggregator: Reset offset if the output rate is
    renegotiated
  - video-anc: Implement transform functions for AFD/Bar metas
  - appsrc: Wake up the create() function on caps changes
  - rtpbasepayload: do not forget delayed segment when forwarding
    gaps
* Tue Oct 13 2020 Antonio Larrosa <alarrosa@suse.com>
- Add patch from gl#gstreamer/gst-plugins-base#221 to support two
  new CEA 608 caption formats:
  * MR-221-video-anc-add-two-new-CEA-608-caption-formats.patch
* Wed Sep  2 2020 Antonio Larrosa <alarrosa@suse.com>
- Update to 1.18.0:
  + Highlights:
  - GstTranscoder: new high level API for applications to
    transcode media files from one format to another
  - High Dynamic Range (HDR) video information representation
    and signalling enhancements
  - Instant playback rate change support
  - Active Format Description (AFD) and Bar Data support
  - RTSP server and client implementations gained ONVIF trick
    modes support
  - Hardware-accelerated video decoding on Windows via
    DXVA2/Direct3D11
  - Microsoft Media Foundation plugin for video capture and
    hardware-accelerated video encoding on Windows
  - qmlgloverlay: New overlay element that renders a QtQuick
    scene over the top of an input video stream
  - imagesequencesrc: New element to easily create a video
    stream from a sequence of jpeg or png images
  - dashsink: New sink to produce DASH content
  - dvbsubenc: New DVB Subtitle encoder element
  - MPEG-TS muxing now also supports TV broadcast compliant
    muxing with constant bitrate muxing and SCTE-35 support
  - rtmp2: New RTMP client source and sink element from-scratch
    implementation
  - svthevcenc: New SVT-HEVC-based H.265 video encoder
  - vaapioverlay: New compositor element using VA-API
  - rtpmanager gained support for Google's Transport-Wide
    Congestion Control (twcc) RTP extension
  - splitmuxsink and splitmuxsrc gained support for auxiliary
    video streams
  - webrtcbin now contains some initial support for
    renegotiation involving stream addition and removal
  - RTP support was enhanced with new RTP source and sink
    elements to easily set up RTP streaming via rtp:// URIs
  - avtp: New Audio Video Transport Protocol (AVTP) plugin for
    Time-Sensitive Applications
  - Support for the Video Services Forum's Reliable Internet
    Stream Transport (RIST) TR-06-1 Simple Profile
  - Universal Windows Platform (UWP) support
  - rpicamsrc: New element for capturing from the Raspberry Pi
    camera
  - RTSP Server TCP interleaved backpressure handling
    improvements as well as support for Scale/Speed headers
  - GStreamer Editing Services gained support for nested
    timelines, per-clip speed rate control and the OpenTimelineIO
    format.
  - Autotools build system has been removed in favour of Meson
- Drop patches already included in upstream:
  * gst-base-audioencoder-fix-leak.patch
  * gst-base-fft-update-kiss-version.patch
  * gst-base-playbin-handle-error.patch
- Add patch to add wayland dependencies to tests to fix build:
  * add_wayland_dep_to_tests.patch
* Wed Aug 26 2020 Dominique Leuenberger <dimstar@opensuse.org>
- Do not recommend PackageKit-gstreamer-plugin: that package
  already supplements the combination of gstreamer-plugins-base
  and packagekit.
* Fri May  1 2020 Michael Gorse <mgorse@suse.com>
- Remove is_opensuse conditionals / really enable orc on SLE 15
  (jsc#SLE-12265).
* Fri Mar  6 2020 Dominique Leuenberger <dimstar@opensuse.org>
- Add gstreamer-plugins-base-gl-deps.patch: Workaround incomplete
  gstreamer-gl.pc file, which is missing the (dynamic) dependency
  on wayland.
* Wed Feb 26 2020 Bjørn Lie <bjorn.lie@gmail.com>
- Enable meson build conditionally for Tumbleweed.
* Fri Jan 31 2020 Bjørn Lie <bjorn.lie@gmail.com>
- No longer recommend -lang: supplements are in use.
* Mon Jan  6 2020 Bjørn Lie <bjorn.lie@gmail.com>
- Add upstream bugfix patches:
  + gst-base-playbin-handle-error.patch: playbin: Handle error
    message with redirection indication.
  + gst-base-audioencoder-fix-leak.patch: audioencoder: fix segment
    event leak.
  + gst-base-fft-update-kiss-version.patch: fft: Update our kiss
    fft version.
* Fri Dec 13 2019 Frederic Crozat <fcrozat@suse.com>
- Enable orc / wayland-egl on SLE15.
* Wed Dec  4 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 1.16.2:
  + xvimagepool: Update size, stride, and offset with allocated
    XvImage
  + video-converter: Fix RGB-XYZ-RGB conversion
  + audiorate: Update next_offset on rate change
  + audioringbuffer: Reset reorder flag before check
  + audio-buffer: Don't fail to map buffers with zero samples
  + videorate: Fix max-duplication-time handling
  + gl/gbm: ensure we call the resize callback before attempting to
    draw
  + video-converter: Various fixes for interlaced scaling
  + gstrtspconnection: messages_bytes not decreased
  + check: Don't use real audio devices for tests
  + riff: add CineForm mapping
  + glfilters: Don't use static variables for storing per-element
    state
  + glupload: Add VideoMetas and GLSyncMeta to the raw uploaded
    buffers
  + streamsynchronizer: avoid pad release race during logging.
* Tue Sep 24 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 1.16.1:
  + See main gstreamer package for changelog.
- Drop upstream fixed patches:
  + gst-plugins-base-doc-build-fix.patch.
  + gstreamer-plugins-base-arm-neon-configuration.patch.
* Mon Aug 19 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Drop pkgconfig(gdk-pixbuf-2.0), pkgconfig(gtk+-3.0) and
  pkgconfig(gtk+-x11-3.0) BuildRequires and pass --disable-examples
  to configure (we already do in meson conditional): Only needed to
  build the examples.
- Add explicit pkgconfig(wayland-protocols) BuildRequires:
  Previously pulled in by gtk3 dependency.
- Add explicit conditional pkgconfig(cairo) BuildRequires for
  openSUSE versions older than current Tumbleweed, workaround bug
  in pangocairo dependencies in those releases. Also previously
  pulled in by gtk3 dependency.
* Wed Jul 24 2019 Martin Liška <mliska@suse.cz>
- Add gstreamer-plugins-base-arm-neon-configuration.patch
  as an upstream backport of:
  https://gitlab.freedesktop.org/gstreamer/gst-plugins-base/commit/d8d4904e
- Use %%make_build.
* Tue Jun 18 2019 mgorse@suse.com
- Update to version 1.16.0:
  + Highlights
  - GStreamer WebRTC stack gained support for data channels for
    peer-to-peer communication based on SCTP, BUNDLE support, as
    well as support for multiple TURN servers.
  - AV1 video codec support for Matroska and QuickTime/MP4
    containers and more configuration options and supported
    input formats for the AOMedia AV1 encoder
  - Support for Closed Captions and other Ancillary Data in video
  - Support for planar (non-interleaved) raw audio
  - GstVideoAggregator, compositor and OpenGL mixer elements are
    now in -base
  - New alternate fields interlace mode where each buffer carries
    a single field
  - WebM and Matroska ContentEncryption support in the Matroska
    demuxer
  - new WebKit WPE-based web browser source element
  - Video4Linux: HEVC encoding and decoding, JPEG encoding, and
    improved dmabuf import/export
  - Hardware-accelerated Nvidia video decoder gained support for
    VP8/VP9 decoding, whilst the encoder gained support for
    H.265/HEVC encoding.
  - Many improvements to the Intel Media SDK based
    hardware-accelerated video decoder and encoder plugin (msdk):
    dmabuf import/export for zero-copy integration with other
    components; VP9 decoding; 10-bit HEVC encoding; video
    post-processing (vpp) support including deinterlacing; and
    the video decoder now handles dynamic resolution changes.
  - The ASS/SSA subtitle overlay renderer can now handle multiple
    subtitles that overlap in time and will show them on screen
    simultaneously
  - The Meson build is now feature-complete (*) and it is now the
    recommended build system on all platforms. The Autotools
    build is scheduled to be removed in the next cycle.
  - The GStreamer Rust bindings and Rust plugins module are now
    officially part of upstream GStreamer.
  - The GStreamer Editing Services gained a gesdemux element that
    allows directly playing back serialized edit list with
    playbin or (uri)decodebin
  - Many performance improvements
- Switch to meson for Tumbleweed.
- Adjust line to get the minimum required gstreamer version.
- Disable tremor (needs libvorbisidec)
- Disable examples.
- Package libgstcompositor.so and libgstoverlaycomposition.so.
- Adjust documentation directory.
- Add gst-plugins-base-doc-build-fix.patch: fix build with
  automake.
- Up gstreamer-plugins-bad Conflicts.
- Now requires glib2 >= 2.40.
- Obsolete libgstbadvideo-1_0-0: now part of -base.
* Fri May 31 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 1.14.5:
  + audioconvert: fix endianness conversion for unpacked formats
    (e.g. S24_32BE).
  + audioringbuffer: Fix wrong memcpy address when reordering
    channels.
  + decodebin2: Make sure to remove pad probes when freeing
    GstDecodeGroup.
  + glviewconvert: fix output when a transformation matrix is used.
  + glupload:
  - Prevent segfault when updating caps.
  - dmabuf: be explicit about gl formats used.
  + gl/egl: Determine correct format on dmabuf import.
  + id3tag: validate the year from v1 tags before passing to
    GstDateTime.
  + rtpbasepayload: Fix sequence numbers when using buffer lists.
  + rtspconnection:
  - Fix security issue, potential heap overflow (CVE-2019-9928).
  - Fix GError set over the top of a previous GError.
  - Do not duplicate authentication headers.
  + subparse: don’t assert when failing to parse subrip timestamp.
  + video: various convert sample frame fixes.
  + video-converter: fix conversion from I420_10LE/BE, I420_12LE/BE,
    A420_10LE/BE to BGRA/RGBA which created corrupted output.
  + video-format: Fix GBRA_10/12 alpha channel pixel strides.
- Drop upstream fixed patches:
  + CVE-2019-9928.patch
  + 0001-id3tag-Correctly-validate-the-year-from-v1-tags-befo.patch
* Thu May 16 2019 mgorse@suse.com
- Add CVE-2019-9928.patch: fix a heap overflow in the rtsp
  connection parser (boo#1133375 CVE-2019-9928).
* Fri Apr 26 2019 plater <davejplater@gmail.com>
- Added:
  0001-id3tag-Correctly-validate-the-year-from-v1-tags-befo.patch
  which fixes:
  https://gitlab.freedesktop.org/gstreamer/gstreamer/issues/384
  "Segfault since 1.16" which also occurs in 1.14.4.
* Wed Oct  3 2018 bjorn.lie@gmail.com
- Update to version 1.14.4:
  + Bugfix release, please see .changes in gstreamer main package.
* Wed Sep 26 2018 bjorn.lie@gmail.com
- Update to version 1.14.3:
  + Bugfix release, please see .changes in gstreamer main package.
* Fri Jul 20 2018 bjorn.lie@gmail.com
- Update to version 1.14.2:
  + Update docs.
  + xvimage: Fix symbol redefine build error.
  + glcolorbalance: Support OES textures for input/passthrough.
  + meson: gl: fix backported patch.
  + gl/build: fixed failed compilation due to missing EGLuint64KHR
    typedef.
  + parsebin: Don't try to continue autoplugging a parser if we got
    raw caps.
  + audiobasesrc: Round down segsize to an integer number of
    samples.
  + discoverer: Don't crash when running with -v if channel-mask==0
    and >7 channels.
  + gldownloadelement: fix build with msvc.
  + subparse: Don't read beyond array.
  + ogg: Avoid undefined granule shift.
  + libs: g-ir-scanner: do not hardcode libtool path.
  + rawvideoparse: fix typo in 'plane-offsets' description.
  + video: fix some GIR array annotations.
  + audio: fix some GIR array annotations.
  + meson: gl: remove non-headers from gl_prototype_headers.
  + meson: install the man pages for the command line tools.
  + meson: Fix detection of glib-mkenums under MSYS2.
* Sat Jun 23 2018 bjorn.lie@gmail.com
- Conditionalize orc and pkgconfig(wayland-egl) BuildRequires and
  enable-orc call, fix build for SLE 12 SP3.
* Wed Jun 13 2018 bjorn.lie@gmail.com
- Conditionalize pkgconfig(graphene-1.0) BuildRequires: fix build
  for Leap 42.3.
* Sun May 20 2018 bjorn.lie@gmail.com
- Update to version 1.14.1:
  + GstPad: Fix race condition causing the same probe to be called
    multiple times
  + Fix occasional deadlocks on windows when outputting debug
    logging
  + Fix debug levels being applied in the wrong order
  + GIR annotation fixes for bindings
  + audiomixer, audioaggregator: fix some negotiation issues
  + gst-play-1.0: fix leaving stdin in non-blocking mode after exit
  + flvmux: wait for caps on all input pads before writing header
    even if source is live
  + flvmux: don't wake up the muxer unless there is data, fixes
    busy looping if there's no input data
  + flvmux: fix major leak of input buffers
  + rtspsrc, rtsp-server: revert to RTSP RFC handling of
    sendonly/recvonly attributes
  + rtpvrawpay: fix payloading with very large mtu sizes where
    everything fits into a single RTP packet
  + v4l2: Fix hard-coded enabled v4l2 probe on Linux/ARM
  + v4l2: Disable DMABuf for emulated formats when using libv4l2
  + v4l2: Always set colorimetry in S_FMT
  + asfdemux: Set stream-format field for H264 streams and handle
    H.264 in bytestream format
  + x265enc: Fix tagging of keyframes on output buffers
  + ladspa: Fix critical during plugin load on Windows
  + decklink: Fix COM initialisation on Windows
  + h264parse: fix re-use across pipeline stop/restart
  + mpegtsmux: fix force-keyframe event handling and PCR/PMT
    changes that would confuse some players with generated HLS
    streams
  + adaptivedemux: Support period change in live playlist
  + rfbsrc: Fix support for applevncserver and support NULL pool in
    decide_allocation
  + jpegparse: Fix APP1 marker segment parsing
  + h265parse: Make caps writable before modifying them, fixes
    criticals
  + fakevideosink: request an extra buffer if enable-last-sample is
    enabled
  + wasapisrc: Don't provide a clock based on WASAPI's clock
  + wasapi: Only use audioclient3 when low-latency, as it might
    otherwise glitch with slow CPUs or VMs
  + wasapi: Don't derive device period from latency time, should
    make it more robust against glitches
  + audiolatency: Fix wave detection in buffers and avoid bogus pts
    values while starting
  + msdk: fix plugin load on implementations with only HW support
  + msdk: dec: set framerate to the driver only if provided, not in
    0/1 case
  + msdk: Don't set extended coding options for JPEG encode
  + rtponviftimestamp: fix state change function init/reset causing
    races/crashes on shutdown
  + decklink: fix initialization failure in windows binary
  + ladspa: Fix critical warnings during plugin load on Windows and
    fix dependencies in meson build
  + gl: fix cross-compilation error with viv-fb
  + qmlglsink: make work with eglfs_kms
  + rtspclientsink: Don't deadlock in preroll on early close
  + rtspclientsink: Fix client ports for the RTCP backchannel
  + rtsp-server: Fix session timeout when streaming data to client
    over TCP
  + vaapiencode: h264: find best profile in those available, fixing
    negotiation errors
  + vaapi: remove custom GstGL context handling, use GstGL instead.
    Fixes GL Context sharing with WebkitGtk on wayland
  + gst-editing-services: various fixes
  + gst-python: bump pygobject req to 3.8;
    fix GstPad.set_query_function(); dist autogen.sh and
    configure.ac in tarball
  + g-i: pick up GstVideo-1.0.gir from local build directory in
    GstGL build
  + g-i: update constant values for bindings
  + avoid duplicate symbols in plugins across modules in static
    builds
  + ... and many, many more!
- Drop gst-pb-base-fix-unresolvable.patch: Fixed upstream.
- Following the above, drop libtool BuildRequires and stop running
  autogen.sh, no longer needed.
* Fri Mar 30 2018 luc14n0@linuxmail.org
- Update to version 1.14.0:
  + Highlights:
  - WebRTC support: real-time audio/video streaming to and from
    web browsers;
  - Experimental support for the next-gen royalty-free AV1 video
    codec;
  - Video4Linux: encoding support, stable element names and
    faster device probing;
  - Support for the Secure Reliable Transport (SRT) video
    streaming protocol;
  - RTP Forward Error Correction (FEC) support (ULPFEC);
  - RTSP 2.0 support in rtspsrc and gst-rtsp-server;
  - ONVIF audio backchannel support in gst-rtsp-server and
    rtspsrc;
  - playbin3 gapless playback and pre-buffering support;
  - Tee, our stream splitter/duplication element, now does
    allocation query aggregation which is important for efficient
    data handling and zero-copy;
  - QuickTime muxer has a new prefill recording mode that allows
    file import in Adobe Premiere and FinalCut Pro while the file
    is still being written;
  - rtpjitterbuffer fast-start mode and timestamp offset
    adjustment smoothing;
  - souphttpsrc connection sharing, which allows for connection
    reuse, cookie sharing, etc;
  - nvdec: new plugin for hardware-accelerated video decoding
    using the NVIDIA NVDEC API;
  - Adaptive DASH trick play support;
  - ipcpipeline: new plugin that allows splitting a pipeline
    across multiple processes;
  - Major gobject-introspection annotation improvements for large
    parts of the library API;
  - GStreamer C# bindings have been revived and seen many updates
    and fixes;
  - The externally maintained GStreamer Rust bindings had many
    usability improvements and cover most of the API now.
    Coinciding with the 1.14 release, a new release with the 1.14
    API additions is happening.
  + Updated translations.
- Add:
  + gcc-c++, libjpeg-devel, libpng-devel and Mesa-libGLESv3-devel,
    and egl, gbm, gl, glesv1_cm, glesv2, graphene-1.0, gudev-1.0,
    gdk-pixbuf-2.0, gmodule-no-export-2.0, libdrm, wayland-client,
    wayland-cursor, wayland-egl and x11-xcb pkgconfig modules as
    build time dependencies.
  + gio-unix-2.0, glib-2.0, xext, xv and x11 BuildRequires to avoid
    implicit dependencies.
  + OpenGL shared library and its GI bindings and plugin plus
    audiomixer plugin from gstreamer-plugins-bad/good, following
    upstream changes.
- Add new sub-package libgstgl-1_0-0 to baselibs.conf.
- Add versioned gstreamer-plugins-bad Conflicts: Several
  sub-packages moved here, conflict on older versions.
- Add gst-pb-base-fix-unresolvable.patch: Fix unresolvable problem
  due to moved plugins, take 2 commits from upstream stable branch.
- Following the above patch: Add libtool BuildRequires and pass
  autogen.sh
* Thu Mar 29 2018 bjorn.lie@gmail.com
- Update to version 1.12.5:
  + Bugs fixed: bgo#668995, bgo#792983, bgo#784530, bgo#771853,
    bgo#789358, bgo#791638
- Drop gst-pb-playbin3-fix-accessing-invalid-index.patch: Fixed
  upstream.
* Tue Mar 20 2018 dimstar@opensuse.org
- Unconditionally enable translation-update-upstream: on
  Tumbleweed, this results in a NOP and for Leap in SLE paid
  translations being used (boo#1086036).
* Wed Feb 28 2018 dimstar@opensuse.org
- Modernize spec-file by calling spec-cleaner.
- Drop filesystem PreRequires: this is simply nonsense.
* Sat Dec 23 2017 zaitor@opensuse.org
- Add gst-pb-playbin3-fix-accessing-invalid-index.patch: playbin3:
  Fix accessing invalid index in GstStream when received
  select-stream event (bgo#791638).
- Clean up spec with spec-cleaner.
* Mon Dec 11 2017 zaitor@opensuse.org
- Update to version 1.12.4:
  + Bugs fixed: bgo#789458, bgo#789547, bgo790329.
* Fri Dec  1 2017 zaitor@opensuse.org
- Add explicit python3-xml BuildRequires: fix build on older
  versions of openSUSE.
* Wed Nov 29 2017 dimstar@opensuse.org
- Switch to python3:
  + Replace python-base BuildRequires with python3-base.
  + Export PYTHON=/usr/bin/python3 before calling configure.
* Mon Sep 18 2017 zaitor@opensuse.org
- Update to version 1.12.3:
  + Bugs fixed: bgo#785011, bgo#771088, bgo#777735, bgo#785065,
    bgo#785331, bgo#785341, bgo#785799, bgo#785948, bgo#785951,
    bgo#786200.
* Fri Aug 25 2017 zaitor@opensuse.org
- Drop conditional valgrind-devel BuildRequires, this type of
  debugging is probably not done by users of binary packages.
* Fri Jul 14 2017 zaitor@opensuse.org
- Update to version 1.12.2:
  + Bugs fixed: bgo#784639.
* Tue Jun 20 2017 dimstar@opensuse.org
- Update to version 1.12.1:
  + Various fixes for crashes, assertions, deadlocks and memory
    leaks.
  + Fix for regression when seeking to the end of ASF files.
  + Fix for regression in (raw)videoparse that caused it to omit
    video metadata.
  + Fix for regression in discoverer that made it show more streams
    than actually available.
  + Numerous bugfixes to the adaptive demuxer base class and the
    DASH demuxer.
  + Various playbin3/urisourcebin related bugfixes.
  + Vivante DirectVIV (imx6) texture uploader works with
    single-plane (e.g. RGB) video formats now.
  + Intel Media SDK encoder now outputs valid PTS and keyframe
    flags.
  + OpenJPEG2000 plugin can be loaded again on MacOS and correctly
    displays 8 bit RGB images now.
  + Fixes to DirectSound source/sink for high CPU usage and wrong
    latency/buffer size calculations.
  + gst-libav was updated to ffmpeg n3.3.2.
* Fri May 19 2017 jengelh@inai.de
- Run parallel build with smp_mflags. Recast a slightly
  convoluted find call. Replace old $RPM shell vars by macros.
* Mon May  8 2017 zaitor@opensuse.org
- Update to version 1.12.0:
  + Bugs fixed: bgo#782095, bgo#782018.
* Wed May  3 2017 dimstar@opensuse.org
- Update to version 1.11.91:
  + Bugs fixed: bgo#779866, bgo#781149, bgo#781152, bgo#781168,
    bgo#781490.
- Changes from version 1.11.90:
  + Bugs fixed: bgo#774544, bgo#776140, bgo#776172, bgo#776446,
    bgo#779344, bgo#779515, bgo#779866, bgo#780053, bgo#780100,
    bgo#780257, bgo#780297, bgo#780429, bgo#780559, bgo#780566,
    bgo#780764, bgo#780769.
  + Updated translations.
* Fri Feb 24 2017 zaitor@opensuse.org
- Update to versions 1.11.2:
  + Bugs fixed: bgo#740557, bgo#775553, bgo#775893, bgo#776797,
    bgo#777458, bgo#777530, bgo#778298, bgo#778702, bgo#778974,
    bgo#779010.
* Thu Feb 23 2017 zaitor@opensuse.org
- Update to version 1.11.1:
  + Bugs fixed: bgo#678301, bgo#699077, bgo#744191, bgo#749567,
    bgo#752052, bgo#756628, bgo#758259, bgo#759358, bgo#765796,
    bgo#767450, bgo#769698, bgo#770355, bgo#771376, bgo#772445,
    bgo#772550, bgo#772832, bgo#772864, bgo#773073, bgo#773102,
    bgo#773165, bgo#773341, bgo#773944, bgo#774445, bgo#774454,
    bgo#774484, bgo#774588, bgo#774728, bgo#774878, bgo#774959,
    bgo#775310, bgo#775369, bgo#775917, bgo#776038, bgo#776188,
    bgo#776447, bgo#776458, bgo#777009, bgo#772764.
- Pass --with-package-name='openSUSE GStreamer package' and
  - -with-package-origin='http://download.opensuse.org' to configure
  we want to show where the gstreamer package is from.
- Pass --enable-orc to configure to ensure we build orc support.
- Drop obsolete clean section from spec.
- Move AUTHORS, NEWS, README, RELEASE and REQUIREMENTS to doc sub
  package.
- Add fdupes BuildRequires and macro, remove duplicates.
- Drop libgstinterfaces-1_0-0 and typelib-1_0-GstInterfaces-1_0
  Obsoletes: They were added to ensure smooth upgrades, and are not
  present in any current openSUSE release.
- Move license-translations.dict to devel package, it's only needed
  for development.
- Replace gstreamer-devel and gstreamer-utils for
  pkgconfig(gstreamer-1.0) BuildRequires: Following what configure
  looks for.
* Thu Feb 23 2017 zaitor@opensuse.org
- Update to version 1.10.4:
  + Bugs fixed: bgo#778432.
- Drop aarch64-no-neon.patch: No longer needed.
* Mon Jan 30 2017 zaitor@opensuse.org
- Update to version 1.10.3:
  + Bugs fixed: bgo#758389, bgo#771723, bgo#774908, bgo#775351,
    bgo#775459, bgo#775480, bgo#775687, bgo#775887, bgo#776403,
    bgo#776623, bgo#777262, bgo#777265, bgo#777502, bgo#777525,
    bgo#777921.
* Sat Dec  3 2016 zaitor@opensuse.org
- Update to version 1.10.2:
  + Bugs fixed: bgo#774911, bgo#774585, bgo#774902, bgo#775224.
* Sun Nov 27 2016 zaitor@opensuse.org
- Update to version 1.10.1:
  + Bugs fixed: bgo#773131, bgo#774322, bgo#774343, bgo#727802.
* Wed Nov  2 2016 zaitor@opensuse.org
- Update to version 1.10.0:
  + Bugs fixed: bgo#768763, bgo#772500, bgo#772501, bgo#772676,
    bgo#772855, bgo#773103, bgo#773105, bgo#773107, bgo#773181,
    bgo#773441.
- Conditionally apply translations-update-upstream BuildRequires
  and macro for non-openSUSE only.
- Disable aarch64-no-neon.patch: It needs a rebase, or may possibly
  be dropped as fixed upstream.
* Mon Aug 22 2016 zaitor@opensuse.org
- Update to version 1.8.3 (boo#996937):
  + Bugs fixed: bgo#767689, bgo#768991, bgo#767712, bgo#768566,
    bgo#768249, bgo#766970, bgo#768361, bgo#768178, bgo#757472,
    bgo#767859.
  + Updated translations.
* Tue Jun 14 2016 zaitor@opensuse.org
- Update to version 1.8.2:
  + bgo#765534: encoding-profile: Remove codec_data and
    streamheader fields from constraint caps.
  + bgo#765538: codec-utils: Don't put level=0 into the caps.
  + bgo#765541: smartencoder: Only accept TIME segments for real.
  + bgo#765684: opusdec: Won't negotiate sampling rate anymore.
  + bgo#765706: opusdec: caps leak in gst_opus_dec_negotiate().
  + bgo#765708: encoding-profile: Make creation of encoding profile
    from discoverer info more robust.
  + bgo#766204: sdp: rtpjpegdepay regression: Does not extract
    frame dimensions from SDP anymore.
  + bgo#766265: opusdec with FEC breaks when packet sizes change.
  + bgo#766510: videosink: test_video_center_rect raise a warning
    when turning on debug.
  + bgo#766515: playbin: fix suburidecodebin leak.
  + bgo#767163: video-color: Fix colorimetry IS_UNKNOWN.
- Stop passing --enable-experimental to configure, we should not
  have experimental codecs (and currently none are built).
* Wed Jun  1 2016 idonmez@suse.com
- Add proper dependencies to the 32bit devel package
* Tue May 31 2016 meissner@suse.com
- baselibs.conf: add -devel for building 32bit Wine.
* Thu May 19 2016 alarrosa@suse.com
- Update to GNOME 3.20.2 (Fate#318572)
* Wed Apr 20 2016 zaitor@opensuse.org
- Update to version 1.8.1:
  + bgo#764020: adaptivedemux: Deadlock on HLS and DASH streams
    when scrub seeking.
  + bgo#764865: audiosrc, audiosink: race in gstaudiosrc
    audioringbuffer thread.
  + bgo#765027: critical warning in rtspsrc when doing srtp.
  + bgo#765082: mikey: add new function gst_mikey_message_to_caps.
- Properly escape some macros in comments to silence rpmlint.
* Wed Apr 13 2016 idonmez@suse.com
- Update to GNOME 3.20  Fate#318572
- Remove gstreamer-plugins-base-discid.patch
* Sat Mar 26 2016 zaitor@opensuse.org
- Update to version 1.8.0:
  + Hardware-accelerated zero-copy video decoding on Android
  + New video capture source for Android using the
    android.hardware.Camera API.
  + Windows Media reverse playback support (ASF/WMV/WMA).
  + New tracing system provides support for more sophisticated
    debugging tools.
  + New high-level GstPlayer playback convenience API.
  + Initial support for the new Vulkan API, see Matthew Waters'
    blog post for more details.
  + Improved Opus audio codec support: Support for more than two
    channels; MPEG-TS demuxer/muxer can now handle Opus;
    sample-accurate encoding/decoding/transmuxing with Ogg,
    Matroska, ISOBMFF (Quicktime/MP4), and MPEG-TS as container;
    new codec utility functions for Opus header and caps handling
    in pbutils library. The Opus encoder/decoder elements were
    also moved to gst-plugins-base (from -bad), and the opus RTP
    depayloader/payloader to -good.
  + GStreamer VAAPI module now released and maintained as part of
    the GStreamer project.
  + Asset proxy support in the GStreamer Editing Services.
  + Bugs fixed: bgo#763316.
- Add pkgconfig(opus) BuildRequires: New optional dependency.
- Add explicit pkgconfig(gio-unix-2.0) BuildRequires: Already
  pulled in, but add it so we can version it.
* Wed Feb 17 2016 dimstar@opensuse.org
- Add gstreamer-plugins-base.appdata.xml so that the codecs can
  show up in a Software Center.
* Thu Jan 21 2016 badshah400@gmail.com
- Update to version 1.6.3:
  - Fix regression in GL library that made glimagesink unsable on
    Android.
  - Integer arithmetic overflow in queue2 element that could break
    buffering or cause crashes due to NULL pointer dereference.
  - Fix crash in AAC/ADTS typefinder caused by reading more memory
    than is available.
  - Stop ignoring encoder errors in the VP8/VP9 encoders.
  - Deprecate GstVideoEncoder GST_VIDEO_ENCODER_FLOW_DROPPED. It's
    redudant and was never actually implemented.
  - Ensure to store the correct video info in GstVideoBufferPool.
  - Fix caps in rtspsrc when doing SRTP over interleaved TCP.
  - Fix crash in pcap parser on 0-sized packets.
  - Clear EOS flag in appsrc to allow reuse after EOS and
    flushing.
  - Ignore flushing streams in streamsynchronizer during stream
    switches to fix problems caused by this in
    gst-editing-services.
  - Ignore tags and other metadata in WAV files after the "data"
    chunk in PUSH mode to prevent them from being interpreted as
    audio.
  - Correctly use colorimetry in v4l2 only for YUV color formats.
  - Set reserved bits in MPEG TS muxer to 1s.
  - Fix calculation of SBC frame lengths.
  - Fix output of the RTP JPEG2000 depayloader to have one frame
    per buffer and crash in the OpenJPEG decoder on incomplete
    frames.
  - Update ffmpeg snapshot in gst-libav to 2.8.5.
  - Memory leak fixes in scaletempo, the raw video RTP
    depayloader, and in playsink related to audio/video filters.
  - Fixes for error handling in the OSX audio plugin.
  - Various gobject-introspection annotation fixes and additions.
  - Compiler warning fixes for latest clang compiler.
- Change source URL to http://gstreamer.freedesktop.org/ instead
  of http://download.gnome.org/; the former seems to be more
  frequently updated.
* Wed Dec 23 2015 dimstar@opensuse.org
- Update to version 1.6.2:
  + Crashes in gst-libav with sinks that did not provide a buffer
    pool but supported video metadata were fixed. This affected
    d3dvideosink and some 3rd party sinks. Also related fixes for
    crashes when a downstream buffer pool failed allocation.
  + Big GL performance improvement on iOS by a factor of 2 by using
    Apple's sync extension.
  + Deadlocks in the DirectSound elements on Windows, and the
    behaviour of its mute property were fixed.
  + The Direct3D video sink does not crash anymore when minimizing
    the window.
  + The library soname generation on Android >= 6.0 was fixed,
    which previously caused GStreamer to fail to load there.
  + File related elements have large-file (>2GB) support on Android
    now.
  + gst-libav was updated to ffmpeg 2.8.3.
  + Deserialization of custom events in the GDP depayloader was
    fixed.
  + Missing OpenGL context initialization in the Qt/QML video sink
    was fixed in certain situations.
  + Interoperability with some broken RTSP servers using HTTP
    tunnel was improved.
  + Various compilation fixes for Windows.
  + Various smaller memory leak and other fixes in different
    places.
  + Bugs fixed: bgo#734098, bgo#738292, bgo#741608, bgo#753823,
    bgo#755106, bgo#755222, bgo#755614, bgo#756028, bgo#756951,
    bgo#757155, bgo#757264, bgo#757453, bgo#757454, bgo#757732,
    bgo#757854, bgo#757873, bgo#757895, bgo#757924, bgo#757929,
    bgo#757935, bgo#758029, bgo#758151, bgo#758204, bgo#758205,
    bgo#758276, bgo#758285, bgo#758286, bgo#758337, bgo#758344,
    bgo#758512, bgo#758620, bgo#758861, bgo#758912, bgo#758913,
    bgo#758921, bgo#759019, bgo#759380.
* Sat Oct 31 2015 zaitor@opensuse.org
- Update to version 1.6.1:
  + rtpbuffer: Add map flag to skip padding.
  + decodebin:
  - Fix event leak with validate.hls.playback.play_15s.hls_bibbop
    scenario.
  - Free unlinked chains at time of switching chains.
  + video:
  - gst_video_calculate_display_ratio() should have out
    parameter.
  - Missing closing parenthesis in video overlay composition
    cast macros.
  + audiobasesink: audio skipping when playing it repeatedly.
  + gst-plugins-base fails to build with --with-pkg-config-path.
  + playsink: fix leak of audio sink.
  + subparse: < / i > should be handled like < /i >.
  + playbin: Leak of playbin on errors from the source element.
* Fri Oct  2 2015 zaitor@opensuse.org
- Update to version 1.6.0:
  + For changelog, see mainpackage changes, everything is condensed
    there.
- Remove subpackage typelib-1_0-GstRiff-1_0: no longer built.
* Fri Dec 26 2014 zaitor@opensuse.org
- Update to version 1.4.5:
  + Bugs fixed: bgo#741420, bgo#715050, bgo#739544, bgo#739840,
    bgo#740556, bgo#740675, bgo#740730, bgo#740853, bgo#740952,
    bgo#741045, bgo#741198.
  + Updated translations.
* Fri Nov 14 2014 zaitor@opensuse.org
- Update to version 1.4.4:
  + Bugs fixed: bgo#736969, bgo#737055, bgo#737706, bgo#737742,
    bgo#737752, bgo#738064.
  + Updated translations.
* Wed Sep 24 2014 dimstar@opensuse.org
- Update to version 1.4.3:
  + Bugs fixed: bgo#734617, bgo#736944.
  + Updated translations.
* Sun Sep 21 2014 dimstar@opensuse.org
- Update to version 1.4.2:
  + Bugs fixed: bgo#727255, bgo#732908, bgo#735569, bgo#735748,
    bgo#735800, bgo#735844, bgo#735952, bgo#736071, bgo#736118,
    bgo#736679, bgo#736739, bgo#736779, bgo#736788, bgo#736796,
    bgo#736861.
  + Updated translations.
* Thu Aug 28 2014 zaitor@opensuse.org
- Update to version 1.4.1:
  + Bugs fixed: bgo#733916 bgo#733976, bgo#734683, bgo#734822.
  + Updated translations.
* Mon Jul 21 2014 dimstar@opensuse.org
- Update to version 1.4.0:
  + Bugs fixed: bgo#733012, bgo#733349, bgo#733386.
  + Updated translations.
* Thu Jul 17 2014 dimstar@opensuse.org
- Update to version 1.3.91:
  + Various API additions.
  + New plugins and elements:
  - v4l2videodec element for accessing hardware codecs on
    platforms that make them accessible via V4L2.
  - New downloadbuffer element that replaces the download
    buffering feature of queue2.
  - rtpstreampay and rtpstreamdepay elements for transmitting RTP
    packets over a stream API (e.g. TCP) according to RFC 4571.
  - rtprtx elements for standard compliant implementation of
    retransmissions, integrated into the rtpmanager plugin.
  - audiomixer element that mixes multiple audio streams together
    into a single one while keeping synchronization.
  - OpenNI2 plugin for 3D cameras like the Kinect camera.
  - OpenEXR plugin for decoding high-dynamic-range EXR images.
  - curlsshsink and curlsftpsink to write files via SSH/SFTP.
  - videosignal, ivfparse and sndfile plugins ported from 0.10.
  - avfvideosrc, vtdec and other elements were ported from 0.10
    and are available on OS X and iOS now.
  + Other changes:
  - gst-libav now uses libav 10.1, and gained support for
    H265/HEVC.
  - Support for hardware codecs and special memory types has been
    improved with bugfixes and feature additions in various
    plugins and base classes.
  - Various bugfixes and improvements to buffering in queue2 and
    multiqueue elements.
  - dvbsrc supports more delivery mechanisms and other features
    now, including DVB S2 and T2 support.
  - The MPEGTS library has support for many more descriptors.
  - Major improvements to tsdemux and tsparse, especially time
    and seeking related.
  - souphttpsrc now has support for keep-alive connections,
    compression, configurable number of retries and configuration
    for SSL certificate validation.
  - hlsdemux has undergone major refactoring and works more
    reliable now and supports more HLS features like trick modes.
  - dashdemux and mssdemux are now also pushing fragments
    downstream while they're downloaded instead of waiting for
    each fragment to finish.
  - videoflip can automatically flip based on the orientation
    tag.
  - openjpeg supports the OpenJPEG2 API.
  - waylandsink was refactored and should be more useful now.
  - gst-rtsp-server supports SRTP and MIKEY now.
  - gst-libav encoders are now negotiating any profile/level
    settings with downstream via caps.
  - Lots of fixes for coverity warnings all over the place.
  - Negotiation related performance improvements.
  - 800+ fixed bug reports.
  + Things to look out for:
  - The eglglessink element was removed and replaced by the
    glimagesink element.
  - The mfcdec element was removed and replaced by v4l2videodec.
  - osxvideosink is only available in OS X 10.6 or newer.
  - On Android the namespace of the automatically generated Java
    class for initialization of GStreamer has changed from
    com.gstreamer to org.freedesktop.gstreamer to prevent
    namespace pollution.
  - On iOS you have to update your gst_ios_init.h and
    gst_ios_init.m in your projects from the one included in the
    binaries if you used the GnuTLS GIO module before.
- Drop gstreamer-plugins-base-discid.patch: fixed upstream.
* Fri Apr 25 2014 dimstar@opensuse.org
- Update to version 1.2.4:
  + Bugs fixed: bgo#693263, bgo#683504, bgo#700770, bgo#723597,
    bgo#724633, bgo#724720, bgo#725313, bgo#725644, bgo#726642,
    bgo#727025.
* Wed Apr  9 2014 dimstar@opensuse.org
- Add gstreamer-plugins-base-discid.patch: fix MB discids for
  trailing data tracks (bnc#872575, bgo#708991).
* Sun Feb  9 2014 zaitor@opensuse.org
- Update to version 1.2.3:
  + Bugs fixed: bgo#603921, bgo#697665, bgo#711816, bgo#712367,
    bgo#715138, bgo#719615, bgo#719684, bgo#720015, bgo#720661,
    bgo#721078, bgo#721666, bgo#721835, bgo#722144, bgo#722656.
  + Updated translations.
* Tue Dec 31 2013 zaitor@opensuse.org
- Update to version 1.2.2:
  + Bugs fixed: bgo#715138, bgo#708200, bgo#707621, bgo#709965,
    bgo#711819, bgo#712280, bgo#712796, bgo#712805, bgo#678011.
* Mon Nov 11 2013 dimstar@opensuse.org
- Update to version 1.2.1:
  + Bugs fixed: bgo#708689, bgo#708773, bgo#708789, bgo#708880,
    bgo#708952, bgo#708953, bgo#708954, bgo#709210, bgo#709408,
    bgo#709637, bgo#709754, bgo#709938, bgo#710325, bgo#711003,
    bgo#711231, bgo#711550.
  + Updated translations.
* Mon Nov  4 2013 schwab@suse.de
- aarch64-no-neon.patch: Disable use of NEON on aarch64
* Tue Oct 22 2013 dimstar@opensuse.org
- Update to version 1.2.0:
  + A bunch of API changes (new stable branch 1.2).
  + New tool: gst-play-1.0 in gst-plugins-base for basic playback
    testing on the command line.
  + New plugins:
  - mssdemux for Microsoft Smooth Streaming.
  - dashdemux for DASH adaptive streaming protocol.
  - bluez for interaction with Bluetooth devices.
  - openjpeg for JPEG2000 decoding and encoding.
  - daala for experimental Daala decoding and encoding.
  - vpx plugin has experimental VP9 decoding and encoding
    support.
  - webp plugin for WebP decoding (encoding to be added later).
  - Various others: yadif, srtp, sbc, fluidsynth, midiparse,
    mfc, ivtv, accuraterip and audiofxbad.
  + Moved plugins: dtmf, vp8rtp, scaletempo and rtpmux plugins are
    now in gstreamer-plugins-good.
  + Audio and Video related fixes.
  + Other changes:
  - gst-libav now uses libav 9.
  - Static linking of plugins is supported now.
  - rtspsrc: add support for NetClientClock.
  - RTP retransmission / NACK support and big RTP jitterbuffer
    improvements.
  - SRTP and DTLS support.
  - Changes to many elements and core to use the correct sticky
    event order and also not lose any important sticky events
    during flushing.
  - >1000 fixed bug reports, and many other bug fixes and other
    improvements everywhere that had no bug report.
  + Notes:
  - Single header includes for all libraries,
    e.g. #include <gst/video/video.h>
  - Stricter (correct) caps subset checking in some cases.
  - x264enc now outputs data in byte-stream by default if
    downstream has ANY caps.
  - The MPEG TS demuxer posts messages contain the PMT, PAT,
    etc, in a different format now.
  - The GstContext API has changed between 1.1.4 and 1.1.90.
- Create new subpackage libgstallocators-1_0-0 and
  typelib-1_0-GstAllocators-1_0, following the shared library
  packaging policy (also provide -32bit packages).
* Sat Aug 31 2013 zaitor@opensuse.org
- Update to version 1.0.10:
  + rtpbasedepayload: mark discontinuities after packet loss
    properly.
  + audioconvert: if we have to lose precision, try to lose as
    little precision as possible.
  + gio: fix very inefficient data cache handling.
  + Bugs fixed: bgo#655727, bgo#705415, bgo#706624.
* Thu Aug 15 2013 zaitor@opensuse.org
- Update to version 1.0.9:
  + subparse: re-enable sami parser.
  + tagdemux: fix ACCURATE seeks in push mode.
  + multisocketsink, multifdsink: fix handling of partial writes
    and WOULD_BLOCK errors, and other fixes.
  + audiodecoder: fix input caps leak.
  + Bugs fixed: bgo#693056, bgo#704291, bgo#704301, bgo#704926.
* Sat Jul 13 2013 dimstar@opensuse.org
- Update to version 1.0.8:
  + tag: ignore malformed ID3v2 TDAT frames
  + Bugs fixed: bgo#636245, bgo#688803, bgo#690420, bgo#698896,
    bgo#699923, bgo#701976, bgo#703128, bgo#703283, bgo#699794.
* Sat Apr 27 2013 dimstar@opensuse.org
- Update to version 1.0.7:
  + streamsynchronizer is now a public element, useful in HLS
    pipelines for example.
  + Bugs fixed: bgo#682171, bgo#688240, bgo#696540, bgo#696899,
    bgo#697092, bgo#697162, bgo#697277, bgo#697820, bgo#697824.
* Sat Mar 23 2013 zaitor@opensuse.org
- Update to version 1.0.6:
  + adder: fix setting caps via the "caps" property.
  + alsasink: don't use 100%% CPU.
  + appsrc: fix locking order.
  + encodebin: sync muxer state with parent bin so encodebin can be
    added dynamically to pipeline.
  + libvisual: fix improper video frame clear operation.
  + pango: fix attribute list handling.
  + playbin:
  - fix playsink caps handling so that converters get plugged
    when needed.
  - fix subtitleoverlay caps handling to avoid not-negotiated
    errors when plugins are missing.
  + videoscale: Correct DAR and border calculations.
  + ximagesink: fon't access structures of EMPTY caps.
  + typefinding: fix y4m caps.
  + build: fix build with automake 1.13.
  + Bugs fixed: bgo#688476, bgo#688803, bgo#690937, bgo#691687,
    bgo#693224, bgo#693372, bgo#693981, bgo#696019.
* Wed Jan  9 2013 dimstar@opensuse.org
- Update to version 1.0.5:
  + alsasrc: don't output buffers without timestamps or with bogus
    timestamps
  + discoverer, decodebin: fix state change re-sync race that might
    lead to deadlocks
  + video: fix crashes with and frame sizes of A420 video format
  + Bugs fixed: bgo#691244.
* Wed Dec 19 2012 dimstar@opensuse.org
- Update to version 1.0.4:
  + playbin: fix occasional not-negotiated errors when switching
    visualisations
  + ssaparse: ignore invalid UTF-8 in SSA/ASS subtitles init
    sections in matroska files
  + streamsynchronizer: better timestamp and gap handling at EOS,
    fixing potential OOM in baseaudiosink
  + bindings:
  - fix annotation for gst_app_src_push_buffer(), fixing crash
  - add several missing annotations for GstRtspMessage API
  + Bugs fixed: bgo#679976, bgo#689814, bgo#689873.
* Thu Nov 22 2012 dimstar@opensuse.org
- Update to version 1.0.3:
  + typefind: detect isml ftyp as iso-fragmented video/quicktime
  + typefinding improvements fixing playback of some wavpack files
  + textoverlay rendering fixes
  + gobject-introspection annotation fixes
  + API additions.
  + Bugs fixed: bgo#686276, bgo#687030, bgo#687055, bgo#687057,
    bgo#687421, bgo#687459, bgo#687473, bgo#687620, bgo#687666,
    bgo#687674, bgo#687991, bgo#687994, bgo#688151, bgo#686841.
* Thu Oct 25 2012 dimstar@opensuse.org
- Update to version 1.0.2:
  + Parallel installability with 0.10.x series
  + alsa: fix probing of supported formats, and advertise
    non-native-endianness formats as fallback
  + audiobasesink: properly handle GAP events (fixing some
    isses with e.g. certain DVD menus)
  + audioconvert: try harder to not convert or to preserve input
    format precision
  + audiodecoder: leak fixes and refcounting fixes
  + audioresample: re-enable the SSE/SSE2 code paths for better
    performance
  + riff: fix paletted RGB formats and msvideo mapping
  + rtsp: make formatting and parsing of range floating-point
    values locale-independent
  + playbin: streamsynchronizer fixes, esp. for handling
    corner-cases near EOS
  + tcpserver{sink,src}: add 'current-port' property and signal
    actually used port
  + videoconvert: fix handling of paletted RGB formats
  + videodecoder: don't leak message strings when error is not
    fatal
  + videodecoder: finetune missing timestamp estimating
  + videotestsrc: add palette for paletted RGB formats
  + vorbistag: fix writing of image tags into vorbis comments
  + Bugs fixed: bgo#580093, bgo#680904, bgo#683098, bgo#684411,
    bgo#685273, bgo#685711, bgo#685938, bgo#686081, bgo#686298.
* Tue Oct  9 2012 dimstar@opensuse.org
- Update to version 1.0.1:
  + videodecoder and -encoder timestamp handling improvements
  + thread-safey fixes for GstMeta registrations and
    GstVideoDecoder
  + Bugs fixed: bgo#684424, bgo#684832, bgo#685110, bgo#685242,
    bgo#685332, bgo#685490.
* Mon Sep 24 2012 cfarrell@opensuse.org
- License update: LGPL-2.1+ and GPL-2.0+
  semicolon ambiguous
* Mon Sep 24 2012 dimstar@opensuse.org
- Update to version 1.0.0:
  + Minor bug fixes
  + Bugs fixed: bgo#678021, bgo#684084, bgo#682973, bgo#684658.
* Tue Sep 18 2012 dimstar@opensuse.org
- Update to version 0.11.99:
  + Minor bug fixes
  + Bugs fixed: bgo#683865, bgo#684063, bgo#684063.
* Fri Sep 14 2012 dimstar@opensuse.org
- Update to version 0.11.94:
  + videodecoder: Handle GAP events
  + gdp: move gdp plugin to -bad
  + port to new GLib thread API
  + Updated documentation
  + Bugs fixed: bgo#635256, bgo#667562, bgo#668996, bgo#673185,
    bgo#673888, bgo#674069, bgo#675812, bgo#676022, bgo#676639,
    bgo#677306, bgo#677712, bgo#678301, bgo#678384, bgo#679145,
    bgo#679337, bgo#679443, bgo#679545, bgo#679550, bgo#679612,
    bgo#679823, bgo#679878, bgo#679958, bgo#680025, bgo#680091,
    bgo#680093, bgo#680162, bgo#680262, bgo#680441, bgo#680488,
    bgo#680520, bgo#680553, bgo#680614, bgo#680796, bgo#681196,
    bgo#681260, bgo#681436, bgo#681499, bgo#681535, bgo#681719,
    bgo#681904, bgo#681905, bgo#683180, bgo#683428, bgo#683527,
    bgo#683672, bgo#683838.
- Drop gstreamer-plugins-base-fix.patch: fixed upstream.
* Mon Aug 13 2012 dimstar@opensuse.org
- Update to version 0.11.93:
  + Bug fixes
  + Sync with GStreamer changes.
- Add gstreamer-plugins-base-fix.patch: Fix build; taken from
  upstream.
* Tue Jul 17 2012 dimstar@opensuse.org
- Update to version 0.11.92:
  + Parallel installability with 0.10.x series.
  + API cleanup and minor API improvements.
  + Major cleanup of video/audio libraries.
  + Lots of bugfixes, cleanup and other improvements.
* Mon May 14 2012 vuntz@opensuse.org
- Update to version 0.11.91:
  + Compressed audio passthrough support in alsasink
  + Removal of interfaces library, mixer and tuner interface
  + Addition of video encoder and decoder base classes
  + Improvements/cleanup for the video library API
- Deal with removal of interfaces library:
  + Split separate libraries out of libgstinterfaces-1_0-0 in:
    libgstaudio-1_0-0, libgstfft-1_0-0, libgstpbutils-1_0-0,
    libgstriff-1_0-0, libgstrtp-1_0-0, libgstrtsp-1_0-0,
    libgstsdp-1_0-0, libgsttag-1_0-0, libgstvideo-1_0-0.
  + Similarly split separate typelibs out of
    typelib-1_0-GstInterfaces-1_0 in: typelib-1_0-GstAudio-1_0,
    typelib-1_0-GstFft-1_0, typelib-1_0-GstPbutils-1_0,
    typelib-1_0-GstRiff-1_0, typelib-1_0-GstRtp-1_0,
    typelib-1_0-GstRtsp-1_0, typelib-1_0-GstSdp-1_0,
    typelib-1_0-GstTag-1_0, typelib-1_0-GstVideo-1_0.
  + Drop libgstinterfaces-1_0-0 and typelib-1_0-GstInterfaces-1_0
    subpackages.
  + Add Obsoletes for libgstinterfaces-1_0-0 and
    typelib-1_0-GstInterfaces-1_0 to main subpackage for smooth
    upgrades.
  + Remove Requires for libgstinterfaces-1_0-0 from main
    subpackage.
* Fri Apr 20 2012 vuntz@opensuse.org
- Update to version 0.11.90:
  + Lots of bugfixes, cleanup and other improvements
  + API cleanup in the audio base classes
  + Improvements to the RTP buffer
- Rename packages following upstream soname and typelib name
  changes:
  + libgstapp-0_11-28 to libgstapp-1_0-0
  + libgstinterfaces-0_11-0 to libgstinterfaces-1_0-0
  + typelib-1_0-GstApp-0_11 to typelib-1_0-GstApp-1_0
  + typelib-1_0-GstInterfaces-0_11 to
    typelib-1_0-GstInterfaces-1_0
* Fri Mar 23 2012 vuntz@opensuse.org
- Update to version 0.11.3:
  + Many fixes and improvements
  + Various performance improvements
  + theora: Improve video negotiation
  + video: Improve video frame map/unmap
  + Bugs fixed: bgo#668343, bgo#668542.
- Bump libgstapp-0_11-27 package name to libgstapp-0_11-28,
  following soversion upstream change.
- Completely drop optional packaging for gnomevfs plugin, since
  it's gone:
  + Remove with_vfs macro.
  + Remove optional gnome-vfs2-devel BuildRequires.
  + Remove gstreamer-plugin-gnomevfs subpackage.
- Completely drop optional packaging for video4linux plugin, since
  it's gone:
  + Remove with_v4l macro.
  + Remove optional libv4l-devel BuildRequires.
- Move to pkgconfig()-style BuildRequires:
  + Old ones: alsa-devel, gtk3-devel, iso-codes-devel,
    libtheora-devel, libvisual-devel, libvorbis-devel,
    libxml2-devel, zlib-devel.
  + New ones: alsa, freetype2, gtk+-3.0, gtk+-x11-3.0, iso-codes,
    libvisual-0.4, libxml-2.0, ogg, pango, pangocairo, theoradec,
    theoraenc, vorbis, vorbisenc, zlib.
- Change python-devel BuildRequires to python-base as only python
  is needed, not the development files.
- Remove unneeded BuildRequires: krb5, libgudev-1_0-devel.
- Remove BuildRequires that, as far as I can tell, are not needed
  (else, they are implicitly brought in by something else):
  check-devel, sgml-skel.
- Change pkgconfig(xv) BuildRequires to proper BuildRequires for
  the X libraries that are needed (pkg-config is not used for
  those): libICE-devel, libSM-devel, libXext-devel, libXv-devel.
- Remove checks for obsolete versions of openSUSE (11.2 and
  earlier), as we require recent versions of many libraries.
* Mon Feb 20 2012 vuntz@opensuse.org
- Change gtk2-devel BuildRequires to gtk3-devel since the code
  using GTK+ has been ported.
- Add explicit glib2-devel BuildRequires, so we can version it.
- Add pkgconfig(xv) BuildRequires on openSUSE > 12.1: this used to
  be pulled in by something else, but the relayout of xorg-x11
  packages changed that. Pull in conditionally only to not risk
  breakage in linked OBS instances (pkgconfig() was not supported
  in older openSUSE releases).
* Fri Feb 17 2012 dimstar@opensuse.org
- Update to version 0.11.2:
  + Parallel installability with 0.10.x series
  + Many API cleanups
  + Ported to new 0.11 core API changes
  + Use new GstSample for snapshots
  + Improved video filter base class
  + New multichannel caps with mask
  + Port network elements to GIO
  + Many fixes and improvements
- Rename libgstapp-0_11-26 to libgstapp-0_11-27, following upstream
  soname bump.
* Tue Jan 24 2012 vuntz@opensuse.org
- Update to version 0.11.1:
  + Rename GstXOverlay -> GstVideoOverlay
  + Reworked audio caps
  + Support for multiple frames in buffers
  + Add video colorimetry support
- Add zlib-devel BuildRequires: new dependency upstream.
- Add libxml2-devel BuildRequires: needed for subparse plugin.
- Drop gstreamer-plugins-base-nonvoid.patch: fixed upstream.
- Remove Provides/Obsoletes/Conflicts for gstreamer010-*: this is
  not needed with this new gstreamer branch.
- Change libgstinterfaces-0_10-0 Requires to
  libgstinterfaces-0_11-0: it was missing the version bump for the
  new gstreamer branch.
- Rename libgstapp-0_11-25 to libgstapp-0_11-26, following upstream
  soversion bump.
- Split typelib files into typelib-1_0-GstApp-0_11 and
  typelib-1_0-GstInterfaces-0_11 subpackages.
- Add typelib-1_0-GstApp-0_11 and typelib-1_0-GstInterfaces-0_11
  Requires to devel subpackage.
- Remove explicit Requires for glib2-devel, gstreamer-devel,
  libxml2-devel and zlib-devel in devel subpackage: they will
  automatically be added the pkgconfig way.
- Update baselibs.conf: it was never updated for this new gstreamer
  branch.
- Change group of libgstapp-0_11-26 from
  Productivity/Multimedia/Other to System/Libraries.
- Do not uselessly call autogen.sh.
* Wed Aug 10 2011 dimstar@opensuse.org
- Update to version 0.11.0:
  + Parallel installability with 0.10.x series
  + Ported to the new 0.11 core API
  + Reworked video caps system
  + Improved video helper classes
- Rename package to gstreamer-plugins-base.
- Add gstreamer-plugins-base-nonvoid.patch: Return a value in
  non-void functions. Fixes a BRP error.
* Sat Aug  6 2011 chris@computersalat.de
- fix deps
  o gobject-introspection >= 0.9.12
* Wed Jul  6 2011 dimstar@opensuse.org
- Introduce build_v4l macro. Video4Linux does no longer build
  with linux-glibc-devel >= 3.0, due to the fact that
  VID_TYPE_MPEG_ENCODER is no longer defined (which in turn is used
  to identify if v4l is usable). Video4Linux2 plugin can be found,
  as before, in gstreamer-0_10-plugins-good package.
* Fri Jun 17 2011 dimstar@opensuse.org
- Update to version 0.10.35:
  + Work around GLib atomic ops API change.
  + don't use G_CONST_RETURN in public headers.
  + bgo#600043: subparse: fails to recognise Cyrillic subtitles in
    windows-1251 encoding.
* Wed May 18 2011 dimstar@opensuse.org
- Update to version 0.10.34:
  + None changes: this release is identical to 0.10.33 and just
    done to keep core/base versions in sync.
* Wed May 11 2011 dimstar@opensuse.org
- Update to version 0.10.33:
  + audioringbuffer: make sure to not start if the may_start flag
    is FALSE
  + baseaudiosink:
  - arrange for running clock when rendering eos
  - don't allow aligning behind the read-segment
  - start ringbuffer upon going to PLAYING and already EOS
  + riff: Add support for video/x-camstudio
  + rtcpbuffer:
  - fix invalid read in validation of padding in rtcp packet
  - Round to next 32bit word, not current 32bit word at end of
    SDES chunk
  + rtpbuffer: Off-by-one error when creating RTP header extensions
    with a two-byte header
  + rtsptransport: ensure valid int result when parsing ranges
  + tag:
  - map the ID3v2 TENC frame to GST_TAG_ENCODED_BY
  - add GST_TAG_CAPTURING_EXPOSURE_COMPENSATION incl. EXIF/XMP
    mappings
  - add a new GstTagXmpWriter interface to select XMP schemas to
    be used
  + tagdemux: also push cached events downstream when operating in
    pull mode
  + video:
  - add GST_VIDEO_BUFFER_PROGRESSIVE flag
  - add ARGB64 and AYUV64 (16 bits per channel) formats
  - add r210 (10 bits per channel) format
  - add gst_video_format_get_component_depth() and
    _new_template_caps()
  - fix creation of grayscale caps and height calculation for
    YUV9/YVU9
  + appsink: emit "new-buffer-list" signal for buffer lists if
    handled by app
  + audiorate: add "skip-to-first" property
  + decodebin2:
  - don't use the same parser element multiple times in the same
    chain
  - improve detection of raw caps in expose-all-streams=false
    mode
  + discoverer:
  - don't wait for subtitle streams to preroll; leak fixes
  - use nominal bitrate if bitrate tag is unavailable
  + encodebin:
  - add an audioconvert after the audio resampler
  - fix refcounting issues and leaks related to request pads
  - return a new reference of the pad for the "request-pad"
    signal
  - set all elements to NULL and remove them from the bin when
    removing a source group
  - tear down old profiles when setting new ones
  + multifdsink: disconnect inactive clients in the select loop too
  + oggmux:
  - prefer headers from caps to determine stream type (for VP8)
  - fix issue with ogg page numbering and discont flag handling
  - ensure stream serial numbers are unique
  - use running time for muxing instead of timestamps
  + oggparse: better detection of delta unit flag
  + playbin2:
  - uridecodebin: add "source-setup" signal
  - always prefer the custom set sink and also set it back to
    NULL in all cases
  - check if an already existing sink supports the non-raw format
  - fix handling of non-raw custom sinks
  - if a sink claims to support ANY caps assume that it only
    supports the usual raw formats
  - only consider the audio/video sinks in autoplug_continue for
    the normal uridecodebin
  - use gst_pad_accept_caps() instead of intersecting with the
    getcaps caps
  - set sinks to READY before checking if it accept caps
  + textoverlay:
  - add support for ARGB and other RGB alpha variants, and xBGR
    and RGBx
  - add support for vertical center alignment
  - converted AYUV to use 'A OVER B' alpha compositing
  - use a class wide mutex to work around pango reentrance issues
  + theoraenc:
  - don't reset the video quality when setting the bitrate
  - allow adjustment of the speed level while running
  - set speed-level property defaults from libtheora's defaults
  + typefinding:
  - MPEG-TS detection fixes
  - detect HTTP live streaming m3u8 playlists
  - detect windows icon files and DEGAS images
  - detect raw h.263
  - add depth and endianness fields to DTS caps
  + uridecodebin:
  - Add default handler for autoplug-select
  - add https:// to protocols for which to enable buffering
  - expose "autoplug-sort" signal
  - post proper error message if decodebin2/typefind elements are
    missing
  - Return NULL from the default autoplug-sort handler
  + videorate: fix "skip-to-first" timestamp setup
  + videoscale: add 16-bit-channel support (ARGB64, AYUV64), fix
    ARGB bilinear scaling
  + videotestsrc: add 16-bit-per-channel support (ARGB64, AYUV64)
  + vorbis: add support for using tremolo on android
  + vorbistag:
  - Add support for METADATA_BLOCK_PICTURE tags
  - Write GST_TAG_IMAGE and GST_TAG_PREVIEW_IMAGE as
    METADATA_BLOCK_PICTURE
  + win32: fix DEFAULT_AUDIOSINK, should be direct*sound*sink
  + xvimagesink: don't paint the window black when going to NULL
  + Bugs fixed: bgo#618516, bgo#619778, bgo#633837, bgo#412678,
    bgo#620364, bgo#625129, bgo#626152, bgo#627268, bgo#629196,
    bgo#632291, bgo#632889, bgo#635669, bgo#635784, bgo#635800,
    bgo#636886, bgo#639136, bgo#639159, bgo#639237, bgo#639744,
    bgo#640189, bgo#640211, bgo#640607, bgo#640709, bgo#640804,
    bgo#641706, bgo#641860, bgo#641917, bgo#641927, bgo#641952,
    bgo#642174, bgo#642232, bgo#642274, bgo#642381, bgo#642466,
    bgo#642720, bgo#642942, bgo#642949, bgo#643775, bgo#644416,
    bgo#644745, bgo#644845, bgo#644996, bgo#645167, bgo#645437,
    bgo#646570, bgo#646572, bgo#646573, bgo#646575, bgo#646576,
    bgo#646923, bgo#646924, bgo#646925, bgo#646952, bgo#647399,
    bgo#647721, bgo#647781, bgo#647856, bgo#647857, bgo#647942,
    bgo#647943, bgo#648459, bgo#648466, bgo#648548, bgo#642667,
    bgo#642732, bgo#646744, bgo#647294
* Tue Jan 25 2011 wstephenson@novell.com
- Update to version 0.10.32
  + GLib requirement is now >= 2.22
  + New core elements:
  - valve (moved from -bad)
  - input-selector (N.B. without "select-all" property, use fsfunnel
    instead) (moved from -bad)
  - output-selector (with different negotiation behaviour by
    default, set pad-negotiation-mode=active for previous behaviour)
    (moved from -bad)
  + Performance improvements for many heavily-used code paths:
    GstPad, GstPoll, GstClock, GstTask, basesink, basesrc, queue2,
    multiqueue
  + gobject-introspection: add annotations for most core API
  + clock: make sync clock wait lockfree
  + fdsrc/fdsink: reenable on MSVC
  + registry: fix GStatBuf definition for win32 when building against
    older glib (fixes unnecessary rescanning of plugins at start-up)
  + element: add a more flexible way to get request pads from elements
  + multiqueue: return upon input when already eos
  + object: fix creation of default name
    (when creating more than 100000 elements)
  + pluginloader: fix hangs on OSX
  + poll:
  - fixes for (p)select backend (used e.g. on OSX)
  - refactor and make more lockfree; fixes for win32 and OSX
    (pselect backend)
  + registry: don't replace valid existing plugins by blacklisted ones
  + tags: don't produce duplicated entries when merging same value twice
  + basesink:
  - preroll fixes for async=false case
  - rework position reporting code
  + basetransform: handle downstream giving a buffer with new caps
    but invalid size
  + See NEWS for API additions and deprecations.
  + Bugs fixed: bgo#635785, bgo#638599, bgo#503592, bgo#564056,
    bgo#607513, bgo#632168, bgo#632447, bgo#632557, bgo#632778,
    bgo#632779, bgo#632780, bgo#633918, bgo#634965, bgo#635001,
    bgo#636268, bgo#636455, bgo#637057, bgo#637300, bgo#637549,
    bgo#637776, bgo#638381, bgo#638399, bgo#638900, bgo#638941.
* Sun Jan 16 2011 aj@suse.de
- Remove buildrequire on pyxml, changelog of package with date
  2008-03-21 contains:
  "Don't depend on PyXML and use only XML modules that are shipped
  with python."
* Tue Dec  7 2010 vuntz@opensuse.org
- Update to version 0.10.31:
  + adder: Make sure FLUSH_STOP is always sent after a flushing
    seek
  + alsasrc, alsasink: add "card-name" property to get the card
    name in addition to the device name
  + appsrc: don't override buffer caps if appsrc caps are NULL; fix
    element classification
  + audioclock: add a function to invalidate the clock
  + audioconvert: optimise remaining conversion code paths with Orc
    as well
  + baseaudiosink,baseaudiosrc: post clock-provide and clock-lost
    messages when going from/to READY to/from PAUSED
  + baseaudiosink: subtract the render_delay from our latency
  + decodebin2: don't add non prerolled stream to topology
  + ffmpegcolorspace: add support for A420 and fix support for 8
    bit paletted RGB and IYU1
  + gnomevfsrc: set GST_PARAM_MUTABLE_READY flag on the "handle"
    property
  + libvisual: add latency query; only drop frames that are really
    too old
  + multifdsink: gdp protocol is deprecated. People should use
    gdppay instead
  + oggdemux: fix seeking with negative rate with skeleton; fix
    wrong flowreturn handling
  + pbutils:
  - AAC profile and level detection utility functions
  - H.264 and MPEG-4 profile and level extraction utility
    functions
  - new GstDiscoverer utility API for extracting metadata and
    tags
  + playbin2, decodebin2: declare stable, deprecate the old
    playbin/decodebin
  + playbin2, uridecodebin: add property to configure ring buffer
    size
  + rtcpbuffer: add function to manipulation the data in RTCP
    feedback packets
  + rtpbuffer:
  - add functions to add RFC 5285 header extensions to
    GstBufferLists
  - add function to add RTP header extensions with a two bytes
    header
  - add function to append RFC 5285 one byte header extensions
  - add function to parse RFC 5285 header extensions
  - add function to read RFC 5285 header extensions from
    GstBufferLists
  - add function to transform a GstBuffer into a GstBufferList
  + rtsp: improve rtsp timeout calculation and handling
  + sdp: add methods to convert between uri and message
  + tags:
  - try ISO-8859-1 as second fallback in case WINDOWS-1252 is not
    supported
  - add many more photography/capture tags
  - EXIF and XMP tag handling improvements
  + textoverlay: add support for NV12, NV21 and AYUV; configurable
    text color and position
  + theoradec:
  - expose telemetry properties only if libtheora was compiled
    with --enable-telemetry
  - add support for two-pass encoding; allow change of bitrate
    and quality on-the-fly
  + tools: standalone gst-discoverer-0.10 tool for discovering
    media file properties
  + typefinding:
  - detect avc1 ftyp as video/quicktime
  - export 3gp profile in caps
  - detect enhanced AC-3
  - extend AAC typefinder to detect LOAS streams
  - fix ADTS caps stream-format detail
  - more reliable mpeg-ts typefinding
  + uridecodebin: Only enable progressive downloading if the
    upstream duration in bytes is known
  + video: add  gst_video_convert_frame*() utility functions
  + videorate:
  - fixate the pixel-aspect-ratio if necessary
  - mark duplicated frames with the GAP flag
  + videoscale:
  - add support for adding black borders to keep the DAR if
    necessary ("add-borders" property)
  - Fix caps fixating if the height is fixed but the width isn't
  - only set the PAR if the caps already had a PAR
  - refactor using more Orc code
  + videotestsrc:
  - new patterns: solid-color, ball, bar and smpte100
  - add "foreground-color" and "background-color" properties,
    deprecate "colorspec" property
  - add support for UYVP format, fix NV21 rendering
  + volume: use Orc to optimise many code paths
  + vorbisdec: decode pending buffers upon EOS when doing reverse
    playback
  + xoverlay:
  - add set_window_handle() with guintptr argument, deprecate
    set_xwindow_id() which doesn't work on some platforms
  - allow render rectangle coordinates to be negative
  + See NEWS for API additions and deprecations.
  + Bugs fixed: bgo#628028, bgo#623846, bgo#602437, bgo#612264,
    bgo#615471, bgo#616392, bgo#617314, bgo#617506, bgo#620291,
    bgo#623663, bgo#623807, bgo#623837, bgo#623918, bgo#624598,
    bgo#624656, bgo#624919, bgo#624920, bgo#624949, bgo#625001,
    bgo#625118, bgo#625944, bgo#626125, bgo#626570, bgo#626581,
    bgo#626621, bgo#626629, bgo#626718, bgo#627203, bgo#627297,
    bgo#627565, bgo#627768, bgo#627780, bgo#627924, bgo#628009,
    bgo#628400, bgo#628500, bgo#628747, bgo#629157, bgo#629672,
    bgo#629848, bgo#630303, bgo#630353, bgo#630440, bgo#630443,
    bgo#630471, bgo#630496, bgo#630802, bgo#631128, bgo#631312,
    bgo#631633, bgo#631703, bgo#631756, bgo#631773, bgo#631774,
    bgo#632167, bgo#632653, bgo#632656, bgo#632789, bgo#632809,
    bgo#632988, bgo#633023, bgo#633203, bgo#633311, bgo#633336,
    bgo#633455, bgo#634014, bgo#634584, bgo#635067, bgo#635392,
    bgo#621349, bgo#628488, bgo#629746, bgo#626869.
- Drop gstreamer-0_10-plugins-base-make382.patch: fixed upstream.
* Sat Sep 18 2010 vuntz@opensuse.org
- Move gir files to devel subpackage.
* Sat Sep 11 2010 dimstar@opensuse.org
- Add gstreamer-0_10-plugins-base-make382.patch: fix build with
  make 3.82. Patch taken from common modules upstream repo, commit
  id=4a070a. fdo#29426.
* Tue Aug 31 2010 aj@suse.de
- Recommend instead of require lang package since it's not mandatory.
* Thu Aug 12 2010 dimstar@opensuse.org
- Update to version 0.10.30:
  + Use Orc (Optimized Inner Loops Runtime Compiler) for SIMD and
    other optimisations, and remove liboil dependency.
  + basertpaudiopayload: Set duration on buffers; add extra frame
    for non-complete frame lengths
  + riff: add mappings for On2 VP8 and VP6F: On2 VP6 Flash variant
  + video: Add support for RGB/BGR with 15 and 16 bits, and Y800
    and Y16
  + xmp/exif tags: add mappings for new tags (device, geo
    location, image orientation)
  + adder: rework timestamping; only accept seek-types SEEK_NONE
    and SEEK_SET
  + decodebin2:
  - add "expose-all-streams" property to not expose/decode all
    streams
  - use accumulator for autoplug-sort
  + ffmpegcolorspace:
  - add YUY2/YVYU to all RGB formats conversions
  - fix conversion of packed 4:2:2 YUV to RGB and 8 bit grayscale
  - fix Y16 from/to GRAY8 conversion
  - fix Y42B from/to YUY2/YVYU/UYVY conversion for odd widths
  - Map "Y8  " and "GREY" to "Y800" and add it to the template
    caps
  - negotiation speed-ups
  + oggdemux:
  - implement seeking and duration estimates when operating in
    push mode (http etc.)
  - parse Skeleton index packets for better seeking in push mode
  - fix granulepos->key granule calculation for Dirac video
  - fix EOS flow aggregation: only EOS when all streams are EOS
  + oggmux: Start a new page for every CMML buffer
  + ogg: Implement Ogg VP8 mapping
  + playbin2:
  - add "av-offset" property to adjust audio/video sync
  - add flag for enabling/disabling automatic deinterlacing
  - fix race when querying duration right after preroll, by
    forwarding duration query duration during group switch if no
    cached duration exists
  - if a text sink is provided, let subtitle parsing be done by
    decodebin2 if required
  - set the subtitle encoding on the decodebins again
  + playsink:
  - also expose "convert-frame" action signal and "frame"
    property in playsink
  - reconfigure the video chain correctly when switching from a
    subtitle to a non-subtitle file
  - Don't fail if subtitles are used but only audio is available
    and no visualizations
  + typefinding:
  - add WebM typefinder (was in -good before)
  - add IVF and dts typefinders, improve AC-3 and jpeg
    typefinding
  - detect ISO 14496-14 files as video/quicktime not audio/x-m4a
  + uridecodebin:
  - add all qtdemux types to downloadable types
  - add the 'expose-all-streams' property from decodebin2
  - Allow video/webm for progressive downloading
  + videorate, videotestsrc: fixate color-matrix, chroma-site and
    interlaced fields if necessary
  + videoscale:
  - Try to keep DAR when scaling
  - Add support for Y444, Y42B and Y41B and more gray formats
  - Fix resampling of ARGB scanlines
  - Try harder to keep the DAR if possible
  - Use passthrough mode if width and height are not changed
  + Bugs fixed: bgo#621428, bgo#371108, bgo#512740, bgo#605100,
    bgo#610866, bgo#614872, bgo#614942, bgo#615783, bgo#616396,
    bgo#616422, bgo#616557, bgo#617636, bgo#617855, bgo#617868,
    bgo#618324, bgo#618392, bgo#618625, bgo#619090, bgo#619102,
    bgo#619310, bgo#619396, bgo#620136, bgo#620140, bgo#620211,
    bgo#620279, bgo#620342, bgo#620412, bgo#620441, bgo#620500,
    bgo#620720, bgo#620939, bgo#621071, bgo#621161, bgo#621190,
    bgo#621509, bgo#621572, bgo#622696, bgo#622807, bgo#622944,
    bgo#623003, bgo#623176, bgo#623218, bgo#623233, bgo#623318,
    bgo#623375, bgo#623384, bgo#623418, bgo#623530, bgo#623583,
    bgo#624266, bgo#547603
- Add orc BuildRequires
- Remove liboil-devel BuildRequires
- Drop gstreamer-0_10-plugins-base-fix-introspection-build.patch,
  it was not applied before.
* Tue May  4 2010 dimstar@opensuse.org
- Update to version 0.10.29:
  + video: add support for color-matrix and chroma-site fields in
    video caps and selected elements
  + video: Add support for 8-bit and 16-bit grayscale formats
  + typefinding: add AAC profile, level, channels and rate to ADTS
    caps
  + tags: add basic xmp metadata support
  + gio, gnomevfs: invert ranks of gio and gnomevfs elements: gio
    is prefered now, gnomevfs has been deprecated
  + riff: add mapping for On2 VP62 and VP7 and add some more MPEG4
    fourccs
  + playsink: Don't fail if there are subtitles and audio but no
    video
  + oggdemux: map old FLAC mapping correctly
  + alsa: handle disappearing of sound device whilst in use more
    gracefully
  + playbin: Only unref the volume element on dispose and when a
    new audio sink is set
  + build: build plugin, example and libs directories in parallel
    if make -jN is used
  + uridecodebin/playbin2: we can handle avi in download mode too
  + rtsp: handle closed POST socket in tunneling, ignore unparsable
    ranges, allow for more ipv6 addresses
  + audiopayload: add property to control packet duration
* Sat Apr 10 2010 vuntz@opensuse.org
- Use the PackageKit codec helper instead of our own tool: less
  code to maintain for us, and it will make it possible to directly
  install a package.
- Change opensuse-codecs-installer Recommends to
  PackageKit-gstreamer-plugin.
- Remove --with-install-plugins-helper configure option: the
  PackageKit plugin will install the right file with
  update-alternatives.
* Thu Mar 25 2010 vuntz@opensuse.org
- Split the gnomevfs plugin in a gstreamer-0_10-plugin-gnomevfs
  subpackage to not require gnome-vfs (which is deprecated) with
  this package.
- Add iso-codes-devel BuildRequires.
* Sat Mar 13 2010 dimstar@opensuse.org
- Update to version 0.10.28:
  + Features of this release:
  - Ogg/Dirac fixes
  - build: really dist qtgv-xoverlay.h header file needed by
    overlay examples this time
  - rtspconnection: fix handling of x-server-ip-address
  - alsasrc fixes
  + Bugs fixed:
  - bgo#610832: qtgv-xoverlay.h header file missing in the
    tarball
  - bgo#611900: [oggdemux] Incorrect parsing of Dirac headers
* Mon Mar  8 2010 dimstar@opensuse.org
- Update to version 0.10.27:
  + Features of this release:
  - playbin2,decodebin2: lots of fixes for missing plugin
    installation
  - playbin2, playsink, subtitleoverlay: Set subtitle encoding
    properly
  - videorate: Improve upstream negotiation
  - oggdemux: use the chain begin_time instead of our counter
  - oggdemux: mark skeleton streams correctly
  - oggdemux: theora PAR of 0:N, N:0 or 0:0 is allowed and maps
    to 1:1
  - typefinding: detect stm module format
  - ffmpegcolorspace: add conversions from all ARGB formats to
    AYUV and back
  - theoradec: Fix chroma copying for 4:2:2
  - tcpclientsrc,tcpserversrc: Fix handling of closed sockets
  - examples,build: dist header file for the Qt graphics view
    example
  - playsink: Reset the sink's state to NULL before unreffing it
    unless it's the same instance again
  - rtspconnection: make sure not to dereference NULL username or
    password
  - appsrc: Update segment duration and post a duration message
    if the duration changes
  - vorbisdec: also support ivorbis tremor decoder
  - rtsp: fail gracefully on bad Content-Length headers
  - rtsp: ignore \n and \r as the first line
  + Bugs fixed: bgo#610449, bgo#608025, bgo#608309, bgo#608417,
    bgo#609063, bgo#609314, bgo#609423, bgo#610005, bgo#610268,
    bgo#610310, bgo#610329, bgo#610379, bgo#610386, bgo#610672,
    bgo#610832, bgo#611225, bgo#611227, bgo#604131
* Wed Feb 17 2010 dimstar@opensuse.org
- Update to version 0.10.26:
  + Changes:
  - playbin2:
    . make about-to-finish signal work for raw sources (e.g.
    audio CDs)
    . fix handling of the native audio/video flags
    . add flag to enable decodebin buffering
    . make subtitle error handling more robust and ignore late
    errors
    . improve subtitle passthrough in uridecodebin
    . new subtitleoverlay element for generic subtitle overlaying
    . proxy notify::volume and notify::mute from the volume/mute
    elements (or audio sink)
    . don't stop completely on initialization errors from
    subtitle elements; instead disable the subtitles and play
    the other parts of the stream
  - decodebin2: rewrite autoplugging and how groups of pads are
    exposed
  - uridecodebin: add use-buffering property that will perform
    buffering on parsed or demuxed media.
  - GstXOverlay: flesh out docs and add example for use with
    Gtk+ >= 2.18
  - libgsttag: add utility functions for ISO-639 language codes
    and tags
  - oggdemux:
    . use internal granulepos<->timestamp mapper and make
    oggdemux more like a 'normal' demuxer that outputs
    timestamps
    . seeking improvements
  - subparse: add qttext support
  - ffmpegcolorspace: prefer transforming alpha formats to alpha
    formats and the other way around
  - libgstvideo: add functions to create/parse still frame events
  - theoraenc: make the default quality property 48.
  - videotestsrc: add pattern with out-of-gamut colors
  - theora: port to 'new' theora 1.0 API; make misc. existing
    properties have no effect (quick, keyframe-mindistance,
    noise-sensitivity, sharpness, keyframe_threshold); those
    either never worked or aren't needed/provided/useful any
    longer with the newer API
  - typefinding: misc. performance improvements and fixes
  - baseaudiosink: make drift tolerance configurable
  + Bugs fixed: bgo#597539, bgo#597786, bgo#598288, bgo#598533,
    bgo#598936, bgo#599105, bgo#599154, bgo#599266, bgo#599471,
    bgo#599649, bgo#600027, bgo#600370, bgo#600469, bgo#600479,
    bgo#600726, bgo#600787, bgo#600945, bgo#600948, bgo#601104,
    bgo#601627, bgo#601772, bgo#601809, bgo#601942, bgo#602000,
    bgo#602225, bgo#602790, bgo#602834, bgo#602924, bgo#602954,
    bgo#603345, bgo#603357, bgo#605100, bgo#605219, bgo#605960,
    bgo#606050, bgo#606163, bgo#606687, bgo#606744, bgo#606926,
    bgo#607116, bgo#607226, bgo#607381, bgo#607403, bgo#607569,
    bgo#607652, bgo#607848, bgo#607870, bgo#607926, bgo#607929,
    bgo#608167, bgo#608179, bgo#608446, bgo#608484, bgo#608699,
    bgo#609252, bgo#596078, bgo#596183, bgo#601480, bgo#596313,
    bgo#606949
* Sun Jan 31 2010 jengelh@medozas.de
- Package baselibs.conf
* Thu Dec  3 2009 vuntz@opensuse.org
- Compile introspection support:
  + Add gobject-introspection-devel BuildRequires.
  + Pass --enable-introspection to configure.
  + Add gstreamer-0_10-plugins-base-fix-introspection-build.patch
    to fix the build.
- Fix self-obsoletion of gstreamer010-plugins-bad-devel.
- Small cleanups.
* Mon Nov 16 2009 lmedinas@opensuse.org
- Update to version 0.10.25:
  + Changes:
  - Add per-stream volume controls
  - Theora 1.0 and Y444 and Y42B format support
  - Improve audio capture timing
  - GObject introspection support
  - Improve audio output startup
  - RTSP improvements
  - Use pango-cairo instead of pangoft2
  - Allow cdda://(device#)?track URI scheme in cddabasesrc
  - Support interlaced content in videoscale and ffmpegcolorspace
  - Many other bug fixes and improvements
  + Bugs fixed: bgo#595401, bgo#563828, bgo#591677, bgo#588523,
    bgo#590146, bgo#321532, bgo#340887, bgo#397419, bgo#556537,
    bgo#559049, bgo#567660, bgo#567928, bgo#571610, bgo#583255,
    bgo#586180, bgo#588717, bgo#588761, bgo#588915, bgo#589095,
    bgo#589574, bgo#590243, bgo#590425, bgo#590856, bgo#591207,
    bgo#591357, bgo#591577, bgo#591664, bgo#591934, bgo#592544,
    bgo#592657, bgo#592864, bgo#592884, bgo#593035, bgo#593284,
    bgo#594020, bgo#594094, bgo#594136, bgo#594165, bgo#594256,
    bgo#594258, bgo#594275, bgo#594623, bgo#594732, bgo#594757,
    bgo#594993, bgo#594994, bgo#595454, bgo#545807
* Mon Oct 26 2009 sbrabec@suse.cz
- Added support for translation-update-upstream (FATE#301344).
* Mon Aug 10 2009 vuntz@novell.com
- Only use libgudev-1_0-devel BuildRequires on openSUSE > 11.1.
* Wed Aug  5 2009 vuntz@novell.com
- Update to version 0.10.24:
  + Changes:
  - Recognise Kate subpicture subtitles
  - Support progressive download in playbin2
  - GIO improvements
  - Add buffer-list support in appsink
  - Add gaussian-noise mode to audiotestsrc
  - bump cdparanoia req to 0.10.2 and improve caching
  - Improve audio source base class
  - Add frame-by-frame stepping and examples
  - Extend stream-probing in decodebin2
  - Many RTSP improvements
  - support for PGS subpictures
  - adder improvements
  - Add Y444, v210, v216 formats
  - implement preset interface in vorbisenc, theoraenc, oggmux
  - Improve libvisual visualisation timestamp tracking
  - playbin2 enhancements: custom audiosink, subpictures, cdda
  - Improvements in textrender
  - Support raw YUV 4:2:2 and SIREN in RIFF
  - Add 4:2:2 and 4:4:4 support to theoradec
  - Many other bug-fixes and improvements
  + Bugs fixed: bgo#510417, bgo#513373, bgo#529300, bgo#531035,
    bgo#567997, bgo#576552, bgo#577637, bgo#579692, bgo#580318,
    bgo#581460, bgo#581571, bgo#582021, bgo#582749, bgo#582819,
    bgo#583867, bgo#584020, bgo#584686, bgo#585197, bgo#585758,
    bgo#585970, bgo#585994, bgo#586331, bgo#586356, bgo#586519,
    bgo#587080, bgo#587278, bgo#587676, bgo#587695, bgo#587896,
    bgo#587980, bgo#588078, bgo#588205, bgo#588550, bgo#588551,
    bgo#588724, bgo#588746, bgo#588747, bgo#588748, bgo#589075,
    bgo#589581, bgo#589622, bgo#589663, bgo#589797, bgo#590470,
    bgo#536313, bgo#579642, bgo#582528, bgo#583318, bgo#585079,
    bgo#585708, bgo#588218, bgo#586920
  + API additions:
  - GstNetAddress::gst_netaddress_to_string()
  - Add gst_rtsp_watch_queue_data()
  - playbin2: Add {audio,video,text}-tags-changed signals
  - Add gst_color_balance_get_balance_type()
  - Add gst_mixer_get_mixer_type()
- Change cdparanoia BuildRequires in cdparanoia-devel.
- Add libgudev-1_0-devel BuildRequires.
* Sun May 17 2009 vuntz@novell.com
- Update to version 0.10.23:
  + New navigation API to support DVD playback
  + playbin2 improvements
  + RTSP extensions to allow extra headers and options
  + Replace audioresampler with speexresample based code
  + Support interlacing flags in the gstvideo library
  + Support new RIFF formats
  + Improve typefinding
  + Support more frame formats in videoscale
  + Many other bug-fixes and improvements
  + Bugs fixed: bgo#577637, bgo#580120, bgo#478512, bgo#574962,
    bgo#564139, bgo#577436, bgo#350311, bgo#378094, bgo#543591,
    bgo#553295, bgo#565105, bgo#565777, bgo#566661, bgo#567255,
    bgo#567636, bgo#567740, bgo#568482, bgo#569655, bgo#570142,
    bgo#570356, bgo#570768, bgo#570832, bgo#571009, bgo#571147,
    bgo#572577, bgo#572872, bgo#572993, bgo#573165, bgo#573528,
    bgo#573529, bgo#574293, bgo#574319, bgo#574447, bgo#574939,
    bgo#575550, bgo#575638, bgo#575649, bgo#576019, bgo#576142,
    bgo#576180, bgo#576586, bgo#577054, bgo#577709, bgo#577827,
    bgo#578583, bgo#578656, bgo#579129, bgo#579130, bgo#579192,
    bgo#579203, bgo#579267, bgo#579463, bgo#579668, bgo#579734,
    bgo#579912, bgo#580470, bgo#580952, bgo#581727, bgo#569682,
    bgo#580020, bgo#562794, bgo#567396, bgo#567982, bgo#571299,
    bgo#574443, bgo#574516, bgo#574964, bgo#575256, bgo#575588,
    bgo#576187, bgo#576188, bgo#576190, bgo#577288, bgo#577610,
    bgo#577794, bgo#578118, bgo#578506, bgo#578942, bgo#580271,
    bgo#580649
  + API added:
  - GstRTSP::gst_rtsp_options_as_text()
  - GstRTSPMessage::gst_rtsp_message_take_header()
  - GstRTSPRange::gst_rtsp_range_to_string()
  - New Navigation interface commands, queries and messages
  - gst_rtsp_channel_new()
  - gst_rtsp_channel_unref()
  - gst_rtsp_channel_attach()
  - gst_rtsp_channel_queue_message()
  - gst_rtsp_connection_accept()
  - GstAppSink::gst_app_sink_set_callbacks()
  - GST_VIDEO_FORMAT_YVYU, GST_VIDEO_BUFFER_TFF,
    GST_VIDEO_BUFFER_RFF, GST_VIDEO_BUFFER_ONEFIELD
  - GST_MIXER_FLAG_HAS_WHITELIST, GST_MIXER_FLAG_GROUPING,
    GST_MIXER_TRACK_NO_RECORD, GST_MIXER_TRACK_NO_MUTE,
    GST_MIXER_TRACK_WHITELIST
  - GstAppSrc::emit-signals
  - GstAppSrc::gst_app_src_set_emit_signals()
  - GstAppSrc::gst_app_src_get_emit_signals()
  - GstAppSrc::gst_app_src_set_callbacks()
  - RTSP::gst_rtsp_connection_get_url()
  - GstRTSPLowerTrans::GST_RTSP_LOWER_TRANS_HTTP
  - RTSP:gst_rtsp_connection_set_tunneled()
  - RTSP:gst_rtsp_connection_is_tunneled()
  - RTSP::gst_rtsp_connection_set_ip()
  - RTSP::gst_rtsp_connection_get_tunnelid()
  - RTSP::gst_rtsp_connection_do_tunnel()
  - RTSP::gst_rtsp_watch_reset()
* Thu Apr 30 2009 sbrabec@suse.cz
- Don't call autogen and don't package gio in older products.
* Mon Feb 23 2009 sbrabec@suse.cz
- Split libgstapp into a separate library - its versioning is not
  in sync with other libraries.
- Set conflict for gstapp module.
* Thu Feb  5 2009 vuntz@novell.com
- Update to version 0.10.22:
  + Require gettext 0.17
  + Replace audioresample with speexresample from -bad
  + Support new formats in RIFF: uncompressed RGB, WMA lossless,
    VP6
  + Move libgstapp and elements from -bad
  + Support color-key setting and probing for Xv properties
  + Improve typefinding for various formats
  + Extend audio sinks for pull-mode operation
  + Support for more subtitle formats
  + More development on decode2bin and playbin2
  + RTP and SDP fixes
  + Many bug fixes and improvements
  + Bugs fixed: bgo#562163, bgo#562258, bgo#561789, bgo#554533,
    bgo#567511, bgo#116051, bgo#346218, bgo#385061, bgo#456788,
    bgo#525807, bgo#546955, bgo#549417, bgo#549510, bgo#552237,
    bgo#552559, bgo#552569, bgo#552801, bgo#554879, bgo#555257,
    bgo#555319, bgo#555607, bgo#555699, bgo#556025, bgo#556066,
    bgo#557365, bgo#558124, bgo#559111, bgo#559478, bgo#559567,
    bgo#561436, bgo#561734, bgo#561780, bgo#561924, bgo#562270,
    bgo#563143, bgo#563174, bgo#563508, bgo#563718, bgo#563904
  + API added:
  - clockoverlay::time-format
  - GstRingBuffer:gst_ring_buffer_activate()
  - GstRingBuffer:gst_ring_buffer_is_active()
  - GstRingBuffer:gst_ring_buffer_convert()
  - Add GST_TYPE_BASE_AUDIO_(SRC|SINK)_SLAVE_METHOD to the public API
  - gst_netaddress_get_address_bytes()
  - gst_netaddress_set_address_bytes(
- Move all the libgstapp packaging from gstreamer-0_10-plugins-bad
  to here, in libgstinterfaces (with other libraries).
- Remove .la files.
* Thu Nov  6 2008 sbrabec@suse.cz
- Re-enabled gio (bnc#441855).
- Fixed valgrid BuildRequires.
* Thu Oct 23 2008 maw@suse.de
- Update to version 0.10.21:
  + Continued playbin2 development
  + Ogg improvements - CELT support, skeleton fixes
  + DVD subpicture support
  + Improved audio dithering random number generator
  + xvimagesink/ximagesink fixes
  + Vorbis encoding and decoding fixes
  + Recognise Kate subtitle streams
  + Bugs fixed: bgo#537380, bgo#538656, bgo#540334, bgo#528299,
    bgo#530068, bgo#537009, bgo#537045, bgo#537599, bgo#537889,
    bgo#538232, bgo#538663, bgo#540215, bgo#540351, bgo#540497,
    bgo#541358, bgo#544306, bgo#548898, bgo#548913, bgo#549062,
    bgo#549814, bgo#550582, bgo#550638, bgo#550656, bgo#550729,
    bgo#552960, and bgo#553244
  + New API:
  * Add "index" property to GstMixerTrack to differantiate
    between multiple mixer tracks with the same label.
* Thu Sep  4 2008 mboman@novell.com
- Updated to version 0.10.20:
  + RTP improvements
  + Support digest auth for RTSP
  + Additional documentation
  + Support DSCP QoS in multifdsink
  + Add NV12/NV21 video buffer layouts
  + Video scaling now bilinear by default
  + Support more than 8 channels in audio conversions
  + Channel mapping fixes for audioconvert
  + Improve tmplayer and sami subtitle support
  + Support 1x1 pixel buffers for videoscale
  + Typefinding improvements for MPEG2, musepack
  + Ogg/Dirac mapping updated in oggmux
  + Fixes in ogg demuxing
  + audiosink synchronisation and slaving fixes
  + Support muting of the audio in playbin by selecting -1 as the audio
    stream
  + Work done on playbin2 and uridecodebin
  + Improvements in the experimental GIO plugin
  + decodebin fixes
  + Handle GAP buffers in some places
  + Various other leak and bug-fixes
* Wed May 14 2008 cthiel@suse.de
- fix baselibs.conf
* Tue Apr 29 2008 cthiel@suse.de
- obsolete gstreamer010-plugins-base-<arch> via baselibs.conf
* Mon Apr 14 2008 jpr@suse.de
- Disable the gio plugin temporarily until dbus generated uid on
  install
* Thu Apr 10 2008 ro@suse.de
- added baselibs.conf file to build xxbit packages
  for multilib support
* Tue Apr  8 2008 sbrabec@suse.cz
- Updated to version 0.10.19:
  * Handle EAGAIN when polling sockets in rtspconnection
- Enabled GIO support.
- Fixed Obsoletes (bnc#357153).
* Wed Apr  2 2008 maw@suse.de
- Update to version 0.10.18:
  + Experimental GIO plugin
  + Continued playbing2 development
  + RTP fixes
  + New API:
  * GstRTPBuffer:gst_rtp_buffer_set_extension_data()
  * add GST_VIDEO_FORMAT_Y41B and GST_VIDEO_FORMAT_Y42B
  * add GstMixerOptions::get_values vfunc (bgo#519906)
  * add gst_mixer_options_list_changed(),
    gst_mixer_mixer_changed() and
    gst_mixer_message_parse_options_list_changed() (bgo#519916)
  * gst_base_rtp_audio_payload_set_samplebits_options()
  * GstNetBuffer::gst_netaddress_equal
  + Bugs fixed: bgo#509637, bgo#510229, bgo#511478, bgo#511810,
    bgo#512899, bgo#513167, bgo#514307, bgo#514623, bgo#514937,
    bgo#515654, bgo#516246, bgo#517420, bgo#517991, bgo#518039,
    bgo#518162, bgo#518940, bgo#519906, bgo#519916, bgo#520523,
    bgo#521743, bgo#522625, bgo#523054, bgo#511825, and bgo#520300.
* Tue Feb  5 2008 maw@suse.de
- Update to version 0.10.17:
  + Work around ABI breakge due to unfortunate use of the
    GST_DISABLE_DEPRECATED macro
  + Export two missino functions needed for the win32 build
  + Initialize the GstRingBuffer GType in a thread-safe context
  + Bugs fixed: bgo#511825, bgo#513018, and bgo#512334.
* Tue Feb  5 2008 maw@suse.de
- Update to version 0.10.16:
  + Include decodebin2 and playbin2 APIs -- these are still subject
    to change
  + Handle newer Theora granule-pos semantics
  + Fixes in playbin handling of stream-switching
  + New API for uniform handling of raw-video format buffers.
  + Improvements for RTSP/RTP handling
  + RIFF lib additions for VC-1 and AVC1 fourccs
  + Bugs fixed: bgo#506132, bgo#320984, bgo#373011, bgo#436756,
    bgo#462740, bgo#486840, bgo#497964, bgo#498228, bgo#499697,
    bgo#502497, bgo#503440, bgo#503930, bgo#506928, bgo#508138,
    bgo#509762, bgo#511274, bgo#496731, bgo#496761, and
    bgo#500763
  + API additions
  * New GstVideoFormat API and helper functions in libgstvideo
  * gst_base_audio_sink_set_provide_clock()
  * gst_base_audio_sink_get_provide_clock()
  * gst_base_audio_sink_set_slave_method()
  * gst_base_audio_sink_get_slave_method()
  * gst_base_audio_src_set_provide_clock()
  * gst_base_audio_src_get_provide_clock()
- Build with -fno-strict-aliasing.
* Fri Jan 25 2008 sbrabec@suse.cz
- Renamed shared library bundle to libgstinterfaces-0_10-0.
* Tue Jan 22 2008 sbrabec@suse.cz
- Updated to version 0.10.15:
  * RTP/RTSP/RTCP/SDP support improved
  * New FFT support library libgstfft, based on Kiss FFT
  * New formats supported in volume and audiotestsrc
  * Fixes in audiorate and videorate
  * Audio capture fixes
  * Playbin and decodebin fixes
  * New tagdemux base class for ID3/APE style tag readers
  * Fix a nasty crash in the X sinks on shutdown
  * New tags supported
  * Add support for multichannel WAV files.
  * Preserve channel layout information when up/down-mixing.
  * Many bug-fixes and improvements
  * API additions
- Split package according to shared library packaging policy
  (#223286).
- Created lang package.
* Tue Oct 16 2007 sbrabec@suse.cz
- Removed unneeded backslash expansion in previous change.
* Mon Oct 15 2007 sbrabec@suse.cz
- Worked around OBS spec file corruption bug (#332132).
* Fri Oct  5 2007 sbrabec@suse.cz
- Use less restrictive Requires based on the sources.
* Mon Sep 17 2007 sbrabec@suse.cz
- Updated to version 0.10.14:
  * Audio dither and noise-shaping when reducing bit-depth
  * RTSP and SDP helper libraries added
  * Experimental buffering element "queue2" now supports pull-mode
    and file-based buffering.
  * Support for more 32-bit video pixel layouts
  * Various fixes and improvements
  * RTSP and SDP libraries added
  * gst_rtsp_base64_decode_ip
  * Add buffer clipping function gst_audio_buffer_clip for raw audio
    buffers.
  * gst_mixer_get_mixer_flags
  * gst_mixer_message_parse_mute_toggled
  * gst_mixer_message_parse_record_toggled
  * gst_mixer_message_parse_volume_changed
  * gst_mixer_message_parse_option_changed
  * GstMixerMessageType
  * GstMixerFlags
  * many bug fixes
* Mon Aug 20 2007 abockover@suse.de
- Use %%{_prefix}/lib for opensuse-codecs-installer (BNC #301883)
* Fri Aug 17 2007 abockover@suse.de
- Added Recommends opensuse-codecs-installer
* Thu Aug 16 2007 abockover@suse.de
- Removed gst-install-plugins-helper foo - it is now split out
  into a separate package
- Configure GStreamer to use opensuse-codecs-installer
* Tue Aug  7 2007 abockover@suse.de
- gst-install-plugins-helper: use xdg-open instead of gnome-open;
  added function to check connectivity status; open an offline
  page if not connected; go to online webapp otherwise
- Added an offline web page with some basic information and a link
  to the online webapp at software.opensuse.org
- Fixed typo in spec file
* Fri Aug  3 2007 abockover@suse.de
- Added a basic gst-install-plugins-helper script for GStreamer
  to launch when codecs are missing and application suspport the
  new installation framework hooks. Fate #302459
* Wed Jun 20 2007 sbrabec@suse.cz
- Updated to version 0.10.13:
  * Many fixes and improvements
  * RTP and RTCP support improved
  * Many API additions
* Wed May 16 2007 sbrabec@suse.cz
- Use Supplements instead of not yet supported Enhances.
* Thu Apr 19 2007 schwab@suse.de
- Fix quoting in autoconf macros.
* Tue Mar 27 2007 sbrabec@suse.cz
- Updated to version 0.10.12:
  * New API for on-demand plugin installation
  * API additions
  * Xv thread-safety and configuration enhancements
  * decodebin2 improvements
  * Support more raw audio format conversions
  * Improvements in Ogg support
  * AudioFilter base class ported to 0.10
  * Fixes for subtitles
  * Latency/live-playback support for Alsa
  * Lots of bug fixes and improvements
* Tue Feb 13 2007 sbrabec@suse.cz
- Do not build unusable static libraries (#238552#c17).
* Tue Dec 19 2006 sbrabec@suse.cz
- Merged back oil and visual subpackages (#223286).
* Mon Dec 18 2006 sbrabec@suse.cz
- Prefix changed to /usr.
- Spec file cleanup.
* Tue Nov  7 2006 abockover@suse.de
- Updated to version 0.10.10
  * Scores of bug fixes
  * Subtitle fixes
  * Support for images in tags
  * Playback improvements
  * Gnomevfssrc supports burn:// URIs
  * Video scale supports more RGBA formats
  * New elements: gdppay, gdpdepay
* Fri Jun 16 2006 sbrabec@suse.cz
- Updated to version
  * many bug-fixes
  * QoS in sinks and transform elements
  * Needs GStreamer 0.10.5 for new GstBaseSink::async_playback()
  * added theoraparse element
  * typefind improvements
  * Ice-cast metadata support has moved from gnomevfssrc to the
    icydemux element in gst-plugins-good
  * audioresample now supports floating point samples
  * Fixes for network playback and audio resampling in playbin
* Sat Apr  8 2006 jpr@suse.de
- Split out libvisual dependent plugin/app into a separate package
* Fri Apr  7 2006 jpr@suse.de
- Split out oil dependent plugins into a separate package
* Fri Mar 24 2006 jpr@suse.de
- Update to version 0.10.5
- Changes since 0.10.4:
  * 334216 : [gnomevfssrc] won't open some media on NFS mounts any longer
  * 334226 : typefindfunctions plugin crashes on PPC on registration
* Mon Mar 20 2006 schwab@suse.de
- Fix uninitialized pointer.
* Fri Mar 10 2006 jpr@suse.de
- update to version 0.10.4
- Changes since 0.10.3:
  * (Experimental) QoS support
  * oggmuxer now creates 100%% valid streams for Theora, Vorbis and Speex
  * documentation updates
  * better support for subtitles (seeking)
  Bugs fixed since 0.10.3:
  * 310202 : [subtitles] < i >  < /i > tags and others should be supported i...
  * 312439 : XVideo output doesn't work on remote displays (probably r...
  * 321271 : audio output is truncated at EOS
  * 321650 : Can't decode this ogm file
  * 325732 : [oggdemux] problem when seeking to time less than 4s with...
  * 325972 : [typefinding] doesn't recognise this mp3
  * 326720 : [alsasink] doesn't support more than 2 channels anymore
  * 330711 : [ffmpegcolorspace] problems with palettized RGB (fencount...
  * 330789 : gstbaseaudiosink causes noise on seeking
  * 330888 : Fix build with gcc 2.95 (again)
  * 331295 : gnomevfssink doesn't respect umask when creating files
  * 331526 : 3GP type detection is too simple
  * 331678 : Decodebin is not reusable within a single pipeline (as in...
  * 331690 : playbin won't play my last.fm stream
  * 331763 : [alsamixer] unmute sets the volume to 100%%
  * 331765 : [alsamixer] mixer applet slider doesn't want to move from...
  * 331903 : [videorate] doesnt handle input caps of framerate=0/1 sanely
  * 332778 : [ogmparse] " Already an existing pad " WARNING
  * 332964 : random crashes in mp3_type_find
  * 333254 : theora encoder does not set IN_CAPS flag properly
  * 333352 : [gnomevfssink] reports disk full as generic error
  * 333488 : Allow for palette < 256 colours in AVI files
  * 333510 : [PATCH] Fix gst_pad_new_from_template (gst_static_pad_tem...
  * 333545 : [riff] set depth on wma caps to make asfdemux and pitfdll...
  * 333663 : [patch] unref the result of gst_pad_get_parent
  * 333900 : [typefind] cannot play a particular mp3 file
  * 334112 : variable not initialized
  * 334129 : Disable frame dropping for now
  * 317038 : use default channel layout if none is specified in multic...
  * 319340 : [cdparanoia] uncorrected-error signal never fired
* Thu Feb 23 2006 jpr@suse.de
- update to version 0.10.3
- Changes since 0.10.2:
  * typefind improvements
  * Ogg decoding and encoding fixes
  * Improved audio and video sink classes
  * Bug and leak fixes
  * Improved video scaling
  * On-the-fly visualisation switching
  * Subtitle support
  Bugs fixed since 0.10.2:
  * 330244 : gsttextoverlay.c:895: 'struct _GstCollectData' has no mem...
  * 324000 : [playbin] post error or message on unknown input
  * 153004 : [typefind] can't identify mp3 file with one single mpeg f...
  * 323874 : [playbin] leaks sinks and threads when using gconfaudiosink
  * 324626 : ffmpegcolorspace support for fourcc " UYVY "
  * 326447 : check that all elements in -base pass queries they can't ...
  * 328263 : Fix build with gcc 2.95
  * 328279 : [decodebin] timeout issue when pre-rolling
  * 329326 : Fix oggmux removing pads from collect pads
* Thu Feb 23 2006 danw@suse.de
- remove dependency on gamin, which is no longer needed (related
  to #128037)
* Tue Feb 14 2006 sbrabec@suse.cz
- Fixed Requires.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Wed Jan 18 2006 sbrabec@suse.cz
- Updated to version 0.10.2.
* Wed Jan  4 2006 sbrabec@suse.cz
- Force-enabled unstable cdparanoia plugin.
* Wed Jan  4 2006 sbrabec@suse.cz
- New SuSE package, version 0.10.1.
