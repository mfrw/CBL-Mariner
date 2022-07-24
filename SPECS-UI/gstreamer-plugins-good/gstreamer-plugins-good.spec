#
# spec file for package gstreamer-plugins-good
#
# Copyright (c) 2022 SUSE LLC
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


%define gstreamer_req_version %(echo %{version} | sed -e "s/+.*//")

# aasink is just a toy. Once in future, we may want to disable aalib
# support completely: Disabled 25/12/17
%define ENABLE_AALIB 0
#
%define _name gst-plugins-good
%define gst_branch 1.0

# Option doesn't currently exist in meson
%define ENABLE_EXPERIMENTAL 1

Name:           gstreamer-plugins-good
Version:        1.20.0
Release:        1%{?dist}
Summary:        GStreamer Streaming-Media Framework Plug-Ins
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://gstreamer.freedesktop.org
# Disable tarball source url, use _service
#Source0:        %%{url}/src/gst-plugins-good/%%{_name}-%%{version}.tar.xz
Source0:        %{_name}-%{version}.tar.xz
Source1:        gstreamer-plugins-good.appdata.xml
Source99:       baselibs.conf

BuildRequires:  mesa-libGLES-devel
# BuildRequires:  Mesa-libGLESv2-devel
# BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  gcc-c++
BuildRequires:  libICE-devel
BuildRequires:  qt5-qtbase-devel qt5-qtsensors-devel
# BuildRequires:  libQt5PlatformHeaders-devel
BuildRequires:  libSM-devel
# used by libgstvideo4linux2.so
BuildRequires:  libXv-devel
BuildRequires:  libavc1394-devel
# BuildRequires:  libbz2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  lame-devel lame-libs
BuildRequires:  meson >= 0.47.0
BuildRequires:  nasm
BuildRequires:  orc >= 0.4.16
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-xml
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
# BuildRequires:  pkgconfig(Qt5WaylandClient)
# BuildRequires:  pkgconfig(Qt5X11Extras)
# BuildRequires:  pkgconfig(caca)
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(cairo-gobject) >= 1.10.0
BuildRequires:  pkgconfig(flac) >= 1.1.4
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.8.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gstreamer-check-1.0)
BuildRequires:  pkgconfig(gstreamer-controller-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gstreamer-gl-1.0)
BuildRequires:  pkgconfig(gstreamer-net-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.15.0
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(gtk+-wayland-3.0) >= 3.15.0
%endif
BuildRequires:  pkgconfig(gtk+-x11-3.0) >= 3.15.0
BuildRequires:  pkgconfig(gudev-1.0) >= 147
BuildRequires:  pkgconfig(jack) >= 0.99.10
# BuildRequires:  pkgconfig(libdv) >= 0.100
BuildRequires:  pkgconfig(libiec61883) >= 1.0.0
BuildRequires:  mpg123-devel >= 1.13
BuildRequires:  pkgconfig(libpng) >= 1.2
BuildRequires:  pkgconfig(libpulse) >= 2.0
BuildRequires:  pkgconfig(libraw1394) >= 2.0.0
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.48.0
BuildRequires:  pkgconfig(libsoup-gnome-2.4) >= 2.40.0
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.9
# BuildRequires:  pkgconfig(shout) >= 2.0
BuildRequires:  pkgconfig(speex) >= 1.1.6
BuildRequires:  pkgconfig(taglib) >= 1.5
BuildRequires:  pkgconfig(twolame) >= 0.3.10
BuildRequires:  pkgconfig(vpx) >= 1.3.0
BuildRequires:  pkgconfig(wavpack) >= 4.60.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xfixes)
Requires:       mpg123 mpg123-libs
Requires:       gstreamer1 >= %{gstreamer_req_version}
Requires:       gstreamer-plugins-base >= %{gstreamer_req_version}
Recommends:     %{name}-gtk
Enhances:       gstreamer
Conflicts:      gstreamer-plugins-ugly < 1.18.1
# Generic name, never used in SuSE: I wish it had been used I would have used it then I wouldn't have to keep copy pasting and actually type it.
Provides:       gst-plugins-good = %{version}
%if 0%{?ENABLE_AALIB}
BuildRequires:  aalib-devel
%endif

%description
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package extra
Summary:        Complementary plugins for gstreamer-plugins-good
Group:          Productivity/Multimedia/Other
Requires:       %{name} = %{version}
Enhances:       gstreamer-plugins-good

%description extra
This package provides complementary plugins for
gstreamer-plugins-good.

%package jack
Summary:        Jack plugin for gstreamer-plugins-good
Group:          Productivity/Multimedia/Other
Requires:       %{name} = %{version}
Enhances:       gstreamer-plugins-good

%description jack
This package provides the jack plugin for gstreamer-plugins-good.

%package gtk
Summary:        Gtksink plugin for gstreamer-plugins-good
Group:          Productivity/Multimedia/Other
Requires:       %{name} = %{version}
Enhances:       gstreamer-plugins-good

%description gtk
This package provides the gtksink output plugin for gstreamer-plugins-good.

%package qtqml
Summary:        Qmlglsink plugin for gstreamer-plugins-good
Group:          Productivity/Multimedia/Other
Requires:       %{name} = %{version}
Enhances:       gstreamer-plugins-good

%description qtqml
This package provides the qmlglsink output plugin for gstreamer-plugins-good.


%prep
%autosetup -n %{_name}-%{version} -p1

%build
export PYTHON=%{_bindir}/python3
%meson \
	-Dpackage-name='Mariner GStreamer-plugins-good package' \
	-Dpackage-origin='http://packages.microsoft.com' \
%if ! 0%{?ENABLE_AALIB}
	-Daalib=disabled \
%endif
	-Ddoc=disabled \
        -Drpicamsrc=disabled \
	-Dv4l2-probe=true \
        -Dbz2=disabled \
        -Ddv=disabled \
        -Dlibcaca=disabled \
        -Dshout2=disabled \
        -Dqt5=disabled \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{_name}-%{gst_branch}
if [ -f %{buildroot}%{_datadir}/appdata/gstreamer-plugins-good.appdata.xml ]; then
  echo "Please remove the added gstreamer-plugins-good.appdata.xml file from the sources - the tarball installs it"
  false
else
  mkdir -p %{buildroot}%{_datadir}/appdata
  cp %{SOURCE1} %{buildroot}%{_datadir}/appdata/
fi

%files
%license COPYING
%doc AUTHORS README RELEASE REQUIREMENTS NEWS
%dir %{_datadir}/appdata
%{_datadir}/appdata/gstreamer-plugins-good.appdata.xml
%{_datadir}/gstreamer-%{gst_branch}/presets/GstIirEqualizer10Bands.prs
%{_datadir}/gstreamer-%{gst_branch}/presets/GstIirEqualizer3Bands.prs
%{_datadir}/gstreamer-%{gst_branch}/presets/GstQTMux.prs
%{_datadir}/gstreamer-%{gst_branch}/presets/GstVP8Enc.prs
%{_libdir}/gstreamer-%{gst_branch}/libgstalaw.so
%{_libdir}/gstreamer-%{gst_branch}/libgstalpha.so
%{_libdir}/gstreamer-%{gst_branch}/libgstalphacolor.so
%{_libdir}/gstreamer-%{gst_branch}/libgstapetag.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudiofx.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudioparsers.so
%{_libdir}/gstreamer-%{gst_branch}/libgstauparse.so
%{_libdir}/gstreamer-%{gst_branch}/libgstautodetect.so
%{_libdir}/gstreamer-%{gst_branch}/libgstavi.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcutter.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdebug.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdeinterlace.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdtmf.so
%{_libdir}/gstreamer-%{gst_branch}/libgsteffectv.so
%{_libdir}/gstreamer-%{gst_branch}/libgstequalizer.so
%{_libdir}/gstreamer-%{gst_branch}/libgstflac.so
%{_libdir}/gstreamer-%{gst_branch}/libgstflv.so
%{_libdir}/gstreamer-%{gst_branch}/libgstflxdec.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgdkpixbuf.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgoom.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgoom2k1.so
%{_libdir}/gstreamer-%{gst_branch}/libgsticydemux.so
%{_libdir}/gstreamer-%{gst_branch}/libgstid3demux.so
%{_libdir}/gstreamer-%{gst_branch}/libgstimagefreeze.so
%{_libdir}/gstreamer-%{gst_branch}/libgstinterleave.so
%{_libdir}/gstreamer-%{gst_branch}/libgstisomp4.so
%{_libdir}/gstreamer-%{gst_branch}/libgstjpeg.so
%{_libdir}/gstreamer-%{gst_branch}/libgstlame.so
%{_libdir}/gstreamer-%{gst_branch}/libgstlevel.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmatroska.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmpg123.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmulaw.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmultifile.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmultipart.so
%{_libdir}/gstreamer-%{gst_branch}/libgstnavigationtest.so
%{_libdir}/gstreamer-%{gst_branch}/libgstoss4.so
%{_libdir}/gstreamer-%{gst_branch}/libgstossaudio.so
%{_libdir}/gstreamer-%{gst_branch}/libgstpng.so
%{_libdir}/gstreamer-%{gst_branch}/libgstpulseaudio.so
%{_libdir}/gstreamer-%{gst_branch}/libgstreplaygain.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrtp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrtpmanager.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrtsp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstshapewipe.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsmpte.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsoup.so
%{_libdir}/gstreamer-%{gst_branch}/libgstspectrum.so
%{_libdir}/gstreamer-%{gst_branch}/libgstspeex.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttaglib.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttwolame.so
%{_libdir}/gstreamer-%{gst_branch}/libgstudp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideo4linux2.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideobox.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideocrop.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideofilter.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideomixer.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvpx.so
%{_libdir}/gstreamer-%{gst_branch}/libgstwavenc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstwavpack.so
%{_libdir}/gstreamer-%{gst_branch}/libgstwavparse.so
%{_libdir}/gstreamer-%{gst_branch}/libgstximagesrc.so
%{_libdir}/gstreamer-%{gst_branch}/libgsty4menc.so
/usr/share/locale

%files extra
%{_libdir}/gstreamer-%{gst_branch}/libgst1394.so
%if 0%{?ENABLE_AALIB}
%{_libdir}/gstreamer-%{gst_branch}/libgstaasink.so
%endif
# %{_libdir}/gstreamer-%{gst_branch}/libgstcacasink.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcairo.so
# %{_libdir}/gstreamer-%{gst_branch}/libgstdv.so
%if 0%{?ENABLE_EXPERIMENTAL}
%{_libdir}/gstreamer-%{gst_branch}/libgstmonoscope.so
%endif
# %{_libdir}/gstreamer-%{gst_branch}/libgstshout2.so

%files jack
%{_libdir}/gstreamer-%{gst_branch}/libgstjack.so

%files gtk
%{_libdir}/gstreamer-%{gst_branch}/libgstgtk.so

%files qtqml
# %{_libdir}/gstreamer-%{gst_branch}/libgstqmlgl.so

%changelog
* Thu Sep 16 2021 Bjørn Lie <bjorn.lie@gmail.com>
- Drop doc sub-package, following this drop gtk-doc BuildRequires.
* Thu Sep 16 2021 Stanislav Brabec <sbrabec@suse.com>
- Remove obsolete translation-update-upstream support
  (jsc#SLE-21105).
* Wed Sep 15 2021 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 1.18.5:
  + avidemux: Also detect 0x000001 as H264 byte-stream start code
    in codec_data
  + deinterlace:
  - Plug a method subobject leak
  - Drop field-order field if outputting progressive
  + jpegdec: Fix crash when interlaced field height is not DCT
    block size aligned
  + qmlglsink: Keep old buffers around a bit longer if they were
    bound by QML
  + qml: qtitem: don't potentially leak a large number of buffers
  + qtdemux: Force stream-start push when re-using EOS'd streams
  + qtmux:
  - For Apple ProRes, allow overriding pixel bit depth, e.g. when
    exporting an opaque image, yet with alpha.
  - Make sure to write 64-bit STCO table when needed.
  + rtpjpegpay: fix image corruption when compiled with MSVC on
    Windows
  + rtpptdemux: Remove pads also in PAUSED->READY
  + rtph265depay: update codec_data in caps regardless of format
  + rtspsrc:
  - Do not overwrite the known duration after a seek
  - De-dup seek event seqnums to avoid multiple seeks
  - Fix race saving seek event seqnum
  - Using multicast UDP has no relation to seekability, also add
    some logging
  - Fix more signals
  - Fix accumulation of before-send signal return values
  + rtpjitterbuffer:
  - Fix parsing of the mediaclk:direct= field
  - Avoid generation of invalid timestamps
  - Check srcresult before waiting on the condition variable too
  - More logging when calculating rfc7273 timestamps
  + souphttpsrc: Always use the content decoder but set
    `Accept-Encoding:...
  + udpsrc: Plug leaks of saddr in error cases
  + multiudpsink: Fix broken SO_SNDBUF get/set on Windows
  + v4l2object:
  - Add interlace-mode back to caps for camera
  - Use default colorimetry if that in caps is unknown
  - Avoid colorimetry mismatch for streams with invalid
    colorimetry
  - Add support for hdr10 stream playback
  + wavparse: adtl/note/labl chunk parsing fixes
  + Don't use volatile to mean atomic (fixes compiler warnings with
    gcc 11)
  + 1.18.4: build fails with glib 2.67.6 and gcc-11: argument 2 of
    ‘_atomicload’ must not be a pointer to a ‘volatile’ type
- Drop 612102fdbc3f813bf9d3406165692b5f742e51a6.patch: Fixed
  upstream.
* Thu Apr 15 2021 Dominique Leuenberger <dimstar@opensuse.org>
- Add 612102fdbc3f813bf9d3406165692b5f742e51a6.patch: Fix build
  with gcc 11, based on upstream git.
* Tue Mar 30 2021 Antonio Larrosa <alarrosa@suse.com>
- Update to version 1.18.4:
  + matroskademux: header parsing fixes (boo#1184735, CVE-2021-3498
    and boo#1184739, CVE-2021-3497)
  + rpicamsrc: depend on posix threads and vchiq_arm to fix build
    on raspios again
  + wavenc: Fixed INFO chunk corruption, caused by odd sized data
    not being padded
  + wavpackdec: Add floating point format support to fix
    distortions in some cases
  + v4l2: recognize V4L2 bt601 colorimetry again
  + v4l2videoenc: support resolution change stream encode
  + v4l2h265codec: fix HEVC profile string issue
  + v4l2object: Need keep same transfer as input caps
  + v4l2videodec: Fix vp8 and vp9 streams can't play on board
    with vendor bsp
  + v4l2videodec: fix src side frame rate negotiation
* Sat Jan 16 2021 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 1.18.3:
  + splitmuxsink:
  - Avoid deadlock when releasing a pad from a running muxer
  - Fix bogus fragment split
  + v4l2object: Map correct video format for RGBA
  + videoflip: fix possible crash when changing
    video-direction/method while running
* Thu Dec 10 2020 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 1.18.2:
  + rpicamsrc: add vchostif library as it is required to build
    successful
  + deinterlace: Enable x86 assembly with nasm on MSVC
  + v4l2: caps negotiate wrong as interlace feature
  + aacparse: Fix caps change handling
  + rtspsrc: Use URI hash for stream id
  + flvmux: Release pads via GstAggregator
  + qtmux: Chain up when releasing pad, and fix some locking
  + matroska-mux: Fix sparse stream crash
  + Splitmux testsuite races
- Fix the _service file and spec to really use the tarball
  generated by service.
* Wed Nov 11 2020 Dirk Mueller <dmueller@suse.com>
- disable rpicams - requires downstream bcm_host.h kernel headers
* Tue Oct 27 2020 Antonio Larrosa <alarrosa@suse.com>
- Update to 1.18.1:
  + Highlighted bugfixes in 1.18.1
  - important security fixes (bsc#1181255, CVE-2021-3185)
  - bug fixes and memory leak fixes
  - various stability and reliability improvements
  + gst-plugins-good changes:
  - v4l2object: Only offer inactive pools and if needed
  - vpx: Fix the check to unfixed/unknown framerate to set
    bitrate
  - qmlglsink: fix crash when created/destroyed in quick
    succession
  - rtputils: Count metas with an empty tag list for
    copying/keeping
  - rtpbin: Remove the rtpjitterbuffer with the stream
  - rtph26*depay: drop FU's without a corresponding start bit
  - imagefreeze: Response caps query from srcpad
  - rtpmp4gdepay: Allow lower-case "aac-hbr" instead of correct
    "AAC-hbr"
  - rtspsrc: Fix push-backchannel-buffer parameter mismatch
  - jpegdec: check buffer size before dereferencing
  - flvmux: Move stream skipping to
    GstAggregatorPadClass.skip_buffer
  - v4l2object: plug memory leak
  - splitmuxsink: fix sink pad release while PLAYING
* Fri Sep 11 2020 Antonio Larrosa <alarrosa@suse.com>
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
- Drop patches:
  * gst-good-qtdemux-Specify-REDIRECT-info.patch
  * gst-good-rtpjpegdepay-outputs-framed-jpeg.patch
* Fri Jan 31 2020 Bjørn Lie <bjorn.lie@gmail.com>
- No longer recommend -lang: supplements are in use.
* Mon Dec 30 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Add upstream bugfix patches:
  + gst-good-qtdemux-Specify-REDIRECT-info.patch: qtdemux: Specify
    REDIRECT information in error message.
  + gst-good-rtpjpegdepay-outputs-framed-jpeg.patch: rtpjpegdepay:
    outputs framed jpeg.
* Wed Dec  4 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 1.16.2:
  + vp9dec: Fix broken 4:4:4 8bits decoding
  + rtpsession: add locking for clear-pt-map
  + rtpL16depay: don't crash if data is not modulo channels*width
  + wavparse:
  - Fix push mode ignoring audio with a size smaller than segment
    buffer
  - Fix push mode ignoring last audio payload chunk
  + aacparse: fix wrong offset of the channel number in adts header
  + jpegdec:
  - Fix incorrect logic in EOI tag detection
  - Don't overwrite the last valid line
  + videocrop: Also update the coordinate when in-place
  + vpx: Error out if enabled and no features found
  + v4l2videodec: ensure pool exists before orphaning it
  + v4l2videoenc: fix type conversion errors
  + v4l2bufferpool: Queue number of allocated buffers to capture
  + v4l2object:
  - Fix mpegversion number typo
  - Work around bad TRY_FMT colorimetry implementations
* Tue Sep 24 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 1.16.1:
  + See main gstreamer package for changelog.
- Drop gstreamer-plugins-good-fix-glibc-incompat.patch: Fixed
  upstream.
* Sun Aug 25 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Add gstreamer-plugins-good-fix-glibc-incompat.patch: v4l2: Fix
  type compatibility issue with glibc 2.30.
- Use make_build macro.
* Wed Jul  3 2019 Fabian Vogt <fvogt@suse.com>
- Add missing pkgconfig(Qt5X11Extras) BuildRequires: Needed to
  build Qt X11 integration.
* Wed Jun 12 2019 mgorse@suse.com
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
- Add meson support, but disable because plugin documentation is
  currently not being built.
* Fri May 31 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 1.14.5:
  + flv: Use 8kHz sample rate for alaw/mulaw audio.
  + flvdemux: Do not error out if the first added and chained pad
    is not linked.
  + flvmux: try harder to make sure timestamps are always
    increasing.
  + gdkpixbufdec: output a TIME segment which is what’s expected
    for raw video.
  + matroskademux: fix handling of MS ACM audio.
  + matroska: fix handling of FlagInterlaced.
  + pulsesink: Deal with not being able to convert a format to
    caps.
  + rtph265depay, rtph264depay; aggregation packet marker handling
    fixes.
  + rtpmp4gdepay: detect broken senders who send AAC with ADTS
    frames.
  + rtprawdepay: keep buffer pool around when flushing/seeking.
  + rtpssrcdemux: Forward serialized events to all pads.
  + qmlglsink: Handle OPENGL header guard changes.
  + qtdemux: fix track language code parsing; ignore corrupted CTTS
    box.
  + qtmux: Correctly set tkhd width/height to the display size.
  + splitmuxsink:
  - Various timecode meta handling fixes.
  - Make work with audio-only encoders as muxers, e.g. wavenc
  + v4l2sink: fix pool-less allocation query handling.
  + v4l2dec/enc: fix use after free when handling events.
  + vpx: Fix build against libvpx 1.8.
  + webmmux: allow resolutions above 4096.
- Drop gstreamer-plugins-good-fix-vpx-build.patch: Fixed upstream.
- Drop automake and libtool BuildRequires and autogen.sh call: No
  longer needed.
* Fri Mar  8 2019 olaf@aepfle.de
- Require automake >= 1.14
* Tue Feb  5 2019 bjorn.lie@gmail.com
- Add gstreamer-plugins-good-fix-vpx-build.patch: Fix build with
  libvpx 1.8.0.
- Add libtool BuildRequires and pass autogen.sh, as the above patch
  touches the buildsystem.
* Wed Oct  3 2018 bjorn.lie@gmail.com
- Update to version 1.14.4:
  + Bugfix release, please see .changes in gstreamer main package.
- Update Source url to new home.
* Wed Sep 26 2018 bjorn.lie@gmail.com
- Update to version 1.14.3:
  + Bugfix release, please see .changes in gstreamer main package.
* Sun Jul 22 2018 bjorn.lie@gmail.com
- Update to version 1.14.2:
  + qmlgl: Fix conflicting declaration of type GLsync for
    non-android.
  + souphttpsrc: Protect input stream with lock.
  + splitmuxsrc: Make sure events are writable before setting their
    seqnum.
  + Various v4l2 fixes.
  + scaletempo: Mark as Audio in classification.
* Fri Jun 22 2018 bjorn.lie@gmail.com
- Conditionalize pkgconfig(gtk+-wayland-3.0) BuildRequires: fix
  build for Leap 42.3.
* Thu May 31 2018 bjorn.lie@gmail.com
- Add pkgconfig(Qt5Core), pkgconfig(Qt5Gui), pkgconfig(Qt5Qml),
  pkgconfig(Qt5Quick) and pkgconfig(Qt5WaylandClient)
  BuildRequires: Build qmlgl sink and package it in new qtqml
  sub-package.
- Add gstreamer-plugins-good-gtk Recommends to the main package,
  install it by default.
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
* Mon May 14 2018 bjorn.lie@gmail.com
- Split out gtk plugin in own sub-package.
- Add conditional ENABLE_EXPERIMENTAL define and set to 0, we do
  not want to build experimental plugins by default.
* Fri Mar 30 2018 luc14n0@linuxmail.org
- Update to version 1.14.0:
  + Highlights:
  - WebRTC support: real-time audio/video streaming to and from
    web browsers;
  - Experimental support for the next-gen royalty-free AV1 video
    codec
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
  + Mesa-libGLESv3-devel and Mesa-libGLESv2-devel, libmp3lame-devel
    and gstreamer-gl-1.0, gtk+-wayland-3.0, libmpg123 and twolame
    pkgconfig modules as build time dependencies.
  + pkgconfig(x11) BuildRequires to avoid implicit dependencies.
  + Gtk, MPG123, lame and TwoLame plugins moved from
    gstreamer-plugins-bad/ugly, following upstream changes.
  + gstreamer-plugins-ugly Conflicts, ensure we do not have
    clashing files.
* Thu Mar 29 2018 bjorn.lie@gmail.com
- Update to version 1.12.5:
  + Bugs fixed: bgo#792775, bgo#793067, bgo#792376, bgo#792644,
    bgo#791473, bgo#757449, bgo#791494.
- Drop upstream fixed patches:
  + gst-good-equalizer-fix-Wincompatible-pointer-types-warning.patch.
  + gst-good-fix-memory-leak-GAP-buffers.patch.
  + gst-good-flacdec-flush-flac-decoder.patch
* Tue Mar 20 2018 dimstar@opensuse.org
- Unconditionally enable translation-update-upstream: on
  Tumbleweed, this results in a NOP and for Leap in SLE paid
  translations being used (boo#1086036).
* Wed Feb 28 2018 dimstar@opensuse.org
- Modernize spec-file by calling spec-cleaner.
- Split out jack plugin into new sub-package jack, also add it to
  baselibs.conf.
* Wed Feb 14 2018 bjorn.lie@gmail.com
- Add gst-good-flacdec-flush-flac-decoder.patch: flacdec: flush
  flac decoder on lost sync (bgo#791473).
- Add gst-good-fix-memory-leak-GAP-buffers.patch: interleave: Fix
  memory leak of GAP buffer (bgo#793067).
* Sat Dec 23 2017 zaitor@opensuse.org
- Add
  gst-good-equalizer-fix-Wincompatible-pointer-types-warning.patch:
  equalizer: Fix -Wincompatible-pointer-types warning (bgo#791494).
- Clean up spec with spec-cleaner.
- Toggle ENABLE_AALIB, no longer build aasink support.
* Mon Dec 11 2017 zaitor@opensuse.org
- Update to version 1.12.4:
  + Bugs fixed: bgo#788777, bgo#779957, bgo#783542, bgo#784749,
    bgo#787795, bgo#788759, bgo#789197, bgo#791034, bgo#791074,
    bgo#787586.
* Thu Nov 30 2017 zaitor@opensuse.org
- Add python3-xml BuildRequires as it is needed for xml support.
* Wed Nov 29 2017 dimstar@opensuse.org
- Switch to python3:
  + Replace python-base BuildRequires with python3-base.
  + Export PYTHON=/usr/bin/python3 before calling configure.
* Mon Sep 18 2017 zaitor@opensuse.org
- Update to version 1.12.3:
  + Bugs fixed: bgo#759292, bgo#781458, bgo#783086, bgo#784250,
    bgo#784971, bgo#785429, bgo#785435, bgo#785990, bgo#785991,
    bgo#786268, bgo#786670, bgo#786718, bgo#787160, bgo#787254,
    bgo#787313.
* Fri Aug 25 2017 zaitor@opensuse.org
- Drop conditional valgrind-devel BuildRequires, this type of
  debugging is probably not done by users of binary packages.
* Fri Jul 14 2017 zaitor@opensuse.org
- Update to version 1.12.2:
  + Bugs fixed: bgo#783778, bgo#784282, bgo#784486, bgo#784616,
    bgo#784812.
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
* Mon May  8 2017 zaitor@opensuse.org
- Update to version 1.12.0:
  + Bugs fixed: bgo#782042.
* Thu Feb 23 2017 zaitor@opensuse.org
- Update to version 1.11.2:
  + Bugs fixed: bgo#778690, bgo#736752, bgo#761761, bgo#766177,
    bgo#768762, bgo#774209, bgo#775440, bgo#775817, bgo#776714,
    bgo#776715, bgo#776899, bgo#777100, bgo#777182, bgo#777330,
    bgo#777331, bgo#777540, bgo#778013, bgo#778330, bgo#778389,
    bgo#776962.
- Drop chmod call on tarball, no longer needed.
* Thu Feb 23 2017 zaitor@opensuse.org
- Update to version 1.11.1:
  + Bugs fixed: bgo#708221, bgo#746574, bgo#748360, bgo#749098,
    bgo#754696, bgo#757631, bgo#766991, bgo#767771, bgo#768723,
    bgo#769041, bgo#769048, bgo#772181, bgo#772740, bgo#773217,
    bgo#773514, bgo#773712, bgo#773785, bgo#773828, bgo#774129,
    bgo#774131, bgo#774403, bgo#774409, bgo#774566, bgo#774674,
    bgo#774747, bgo#774789, bgo#774840, bgo#774876, bgo#775287,
    bgo#775414, bgo#775702, bgo#775752, bgo#776030, bgo#776106,
    bgo#776789, bgo#777095, bgo#777157.
- Pass --with-package-name='openSUSE GStreamer-plugins-good
  package' and --with-package-origin='http://download.opensuse.org'
  to configure we want to show where the gstreamer package is from.
- Move cairo plugin to the extra sub package.
- Drop obsolete clean section from spec.
* Thu Feb 23 2017 zaitor@opensuse.org
- Update to version 1.10.4:
  + Bugs fixed: bgo#778341, bgo#775702, bgo#776106, bgo#777399,
    bgo#777940, bgo#778428, bgo#778437, bgo#778453, bgo#778815,
    bgo#775564.
- Drop gstreamer-plugins-good-qtdemux-sanity-check.patch: Fixed
  upstream.
* Sat Feb  4 2017 zaitor@opensuse.org
- Add gstreamer-plugins-good-qtdemux-sanity-check.patch: qtdemux:
  sanity check number of segments in edit list. Fixes crash with
  fuzzed file (bgo#777940).
* Mon Jan 30 2017 zaitor@opensuse.org
- Update to version 1.10.3 (CVE-2017-5838):
  + Bugs fixed: bgo#775898, bgo#754230, bgo#765498, bgo#772646,
    bgo#773218, bgo#773891, bgo#773905, bgo#775071, bgo#775450,
    bgo#775451, bgo#775455, bgo#775472, bgo#775479, bgo#775543,
    bgo#775794, bgo#775888, bgo#776107, bgo#776720, bgo#777101,
    bgo#777123, bgo#777157, bgo#777174, bgo#777222, bgo#777327,
    bgo#777362, bgo#777469, bgo#777500, bgo#777532, bgo#777832.
* Sat Dec  3 2016 zaitor@opensuse.org
- Update to version 1.10.2:
  + Bugs fixed: bgo#757292, bgo#774428, bgo#774834, bgo#774859,
    bgo#774897, bgo#775219.
* Sun Nov 27 2016 zaitor@opensuse.org
- Update to version 1.10.1:
  + Bugs fixed: bgo#769765, bgo#770568, bgo#772610, bgo#773269,
    bgo#773512, bgo#773515, bgo#773516, bgo#773784, bgo#773861,
    bgo#774507, bgo#774556.
* Wed Nov  2 2016 zaitor@opensuse.org
- Update to version 1.10.0:
  + Bugs fixed: bgo#762207, bgo#772496, bgo#772497, bgo#772644,
    bgo#772656, bgo#773509, bgo#773580, bgo#773582, bgo#773643.
  + Updated translations.
- Conditionally apply translations-update-upstream BuildRequires
  and macro for non-openSUSE only.
- Drop gstreamer-plugins-good-wavparse.patch: Fixed upstream.
- Stop passing --enabel-gtk to configure, no longer needed nor
  recognized.
- Move monoscape plugin to extra subpackage as it is an
  experimental plugin.
* Tue Nov  1 2016 dimstar@opensuse.org
- Add gstreamer-plugins-good-wavparse.patch: Don't try to add
  srcpad if we don't know valid caps yet. Otherwise we'll run into
  an assertion on specially crafted files (bgo#773643,
  boo#1007595).
* Mon Aug 22 2016 zaitor@opensuse.org
- Update to version 1.8.3 (boo#996937):
  + Bugs fixed: bgo#769773, bgo#762208, bgo#769514, bgo#747275,
    bgo#768509, bgo#768232, bgo#768623, bgo#768195, bgo#768268,
    bgo#753760, bgo#767980, bgo#766025, bgo#767680, bgo#767496.
  + Updated translations.
* Tue Jun 14 2016 zaitor@opensuse.org
- Update to version 1.8.2:
  + bgo#766025: rtpsession: race condition accessing ssrcs hash
    table.
  + bgo#733864: v4l2videodec: Implement EOS handling through
    V4L2_DEC_CMD_STOP.
  + bgo#736252: gdkpixbufdec: packetized mode logic.
  + bgo#748700: avimux: stopping file without index fails.
  + bgo#754042: v4l2src: Asserts on renegotiation with USERPTR.
  + bgo#758424: v4l2videodec: Keep the input buffers, they are
    needed to copy metadata.
  + bgo#758703: v4l2src: gst_v4l2_set_attribute warning messages
    cause infinite loop with .dot dump.
  + bgo#761165: Setting overlay parameters on v4l2sink fails.
  + bgo#761787: qtdemux: seek fails with CENC encrypted streams.
  + bgo#762219: rtpsession: don't act on suspicious BYE RTCP.
  + bgo#764679: IPv6 UDP stream to site-local multicast address.
  + bgo#764733: qtdemux: Regression in YouTube TV tests in WebKit
    MSE after fix for bgo#760779.
  + bgo#764897: Using non IPv6-socket in IPv6 scope.
  + bgo#765072: splitmuxsink: Sometimes creates a small one-frame
    file after EOS.
  + bgo#765320: flvmux: segfault when no buffers have arrived
    before EOS.
  + bgo#765391: vpxenc: Handle frames with too low duration
    correctly.
  + bgo#765689: rtspsrc: Various problems related to seeking
    causing scrub seeking to fail.
  + bgo#765725: qtmux: Allow MPEG-1 Layer 1 and 2 in addition to 3
    in MP4.
  + bgo#765805: qtdemux: Only first fragment played for fragmented
    mp4 files recorded with non-seekable sink.
  + bgo#765806: qtdemux: Store the segment sequence number in the
    EOS events and STREAM_DONE events/message.
  + bgo#765933: rtpjitterbuffer: Fix stall when receiving already
    lost packet.
  + bgo#765946: dv: Uses different pixel-aspect-ratio than
    gst-libav.
  + bgo#766172: v4l2videodec: [Regressions] Should not fail if
    S_FMT(CAPTURE) fail after STREAMON(CAPTURE).
  + bgo#766359: auparse: sticky event misordering, got 'segment'
    before 'caps'.
  + bgo#766382: v4l2videodec: use visible size, not coded size, for
    downstream negotiation filter.
  + bgo#766558: deinterlace: fix caps leak.
  + bgo#766610: v4l2object: fix caps leak.
  + bgo#766645: matroskademux: don't hold object lock whilst
    pushing out headers, might lead to query deadlock.
  + bgo#766711: v4l2transform: scaling is broken in case of fixed
    pixel aspect ratio.
  + bgo#766712: v4l2transform should allow to change pixel aspect
    ratio.
  + bgo#766719: v4l2transform: Does not fully fixate the caps.
  + bgo#766868: qtdemux: Segments start at 0 on live MSS time-based
    streams, ignoring the start time configured upstream.
  + bgo#766870: rtpj2kpay: leaks input buffer.
  + bgo#767300: v4l2object uses deprecated RGB15 V4L2 format code.
  + bgo#767424: flvdemux: Fix unref assertion failure.
  + bgo#767086: v4l2src: pushes incomplete raw video buffers.
* Thu May 19 2016 alarrosa@suse.com
- Update to GNOME 3.20.2 (Fate#318572)
* Wed Apr 20 2016 zaitor@opensuse.org
- Update to version 1.8.1:
  + bgo#764733: qtdemux: Regression in YouTube TV tests in WebKit
    MSE after fix for bgo#760779.
  + bgo#763711: splitmuxsink: deadlock when one streams doesn't
    have regular buffers.
  + bgo#730540: rtspsrc: parse crypto sessions to support
    rollover counters.
  + bgo#744612: splitmuxsink: add property for specifing maximum
    number of files to store.
  + bgo#757569: rtspsrc: avoid potentially overflowing expression.
  + bgo#761345: rtpjpegpay: Allow different quantization tables for
    components 2 and 3.
  + bgo#762893: splitmuxsink critical assertion when changing from
    null to ready.
  + bgo#763780: flvdemux: don't emit pad-added until caps are
    ready.
  + bgo#763973: qtdemux: Fix qtdemux memory leak.
  + bgo#764169: vp9dec: Dogslow VP9 4k playback with libvpx, works
    fine with avdec_vp9.
  + bgo#764798: rtspsrc Critical errors when connecting with TLS /
    rtsps.
  + bgo#764870: qtdemux: Fix parsing segment duration of empty edit
    list box.
  + bgo#764889: rtpjitterbuffer: Drops wrong number of packets with
    drop-on-latency=true.
  + bgo#765072: splitmuxsink: Sometimes creates a small one-frame
    file after EOS.
  + bgo#765116: scaletempo: memory corruption.
- Replace glib2-devel, gstreamer-devel and
  gstreamer-plugins-base-devel BuildRequires for their pkgconfig
  counterparts: pkgconfig(glib-2.0), pkgconfig(gstreamer-1.0) and
  pkgconfig(gstreamer-plugins-base-1.0).
- Also add explicit BuildRequires that configure looks for:
  + pkgconfig(gstreamer-base-1.0),
  + pkgconfig(gstreamer-check-1.0),
  + pkgconfig(gstreamer-controller-1.0),
  + pkgconfig(gstreamer-net-1.0).
- Properly escape a macro in comment to silence rpmlint.
* Mon Apr 18 2016 joerg.lorenzen@ki.tng.de
- Changed required version of libvpx to >= 1.3.0, package can be
  successfully built against it and version >= 1.4.0 isn't
  available for openSUSE 13.2 and Leap 42.1 on PMBS.
* Wed Apr 13 2016 idonmez@suse.com
- Update to GNOME 3.20  Fate#318572
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
- Add explicit pkgconfig(libsoup-2.4) BuildRequires and version it.
- Pass --enable-v4l2-probe to configure. This is a runtime check.
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
- Switch to using http://gstreamer.freedesktop.org/ as the source
  URL instead of http://download.gnome.org/; the former seems to
  be updated more frequently.
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
  + splitmuxsink:
  - Post messages when fragments are being opened and closed
  - Allow non-video streams to serve as reference.
  - Do not destroy the multiqueue & muxer when going to NULL.
  - Initialize mux_start_time properly.
  + cutter: Fix buffer leak.
  + aacparse: Wrong LOAS config reading.
  + matroskademux: Assertion failed: (stream- > alignment < =
    G_MEM_ALIGN).
  + gdkpixbufoverlay memleak.
  + qtmux:
  - Fix sample memory leak.
  - Doesn't compile on OS X 10.6: strnlen not available.
  - Fix date memory leak.
  - Allow negotiating to S8 as a raw format but stop making it
    best choice.
  - Add ProRes support.
  + qtdemux:
  - Fix taglist leak.
  - Fix caps leak.
  + auparse: Fix event leak.
  + matroskamux: Drops JPEG input buffers with just PTS and no DTS
    set on them.
  + scaletempo: Does not work properly with negative rates
    playback.
  + splitmux: Unit test fails due to missing files.
* Fri Oct  2 2015 zaitor@opensuse.org
- Update to version 1.6.0:
  + For changelog, see mainpackage changes, everything is condensed
    there.
* Fri May  8 2015 dimstar@opensuse.org
- Use manuel Requires for gstreamer-plugins-base and gstreamer:
  the source_validator service has some issues finding the tarball
  otherwise.
* Thu May  7 2015 dimstar@opensuse.org
- Rename gstreamer-good.appdata.xml to
  gstreamer-plugins-good.appdata.xml to match the package name.
- Add Summary to appdata file.
* Fri Dec 26 2014 zaitor@opensuse.org
- Update to version 1.4.5:
  + Bugs fixed: bgo#711437, bgo#726194, bgo#736397, bgo#737603,
    bgo#739476, bgo#739722, bgo#739789, bgo#739791, bgo#739792,
    bgo#739996, bgo#740040, bgo#740392, bgo#740407, bgo#740633,
    bgo#740636, bgo#740671, bgo#740905, bgo#741271, bgo#741381,
    bgo#741407, bgo#737579, bgo#739754.
  + Updated translations.
* Fri Nov 14 2014 zaitor@opensuse.org
- Update to version 1.4.4:
  + Bugs fixed: bgo#726329, bgo#736071, bgo#737735, bgo#737739,
    bgo#737761, bgo#737771, bgo#737886, bgo#738102, bgo#738152,
    bgo#738297, bgo#738722, bgo#738793, bgo#739430.
  + Updated translations.
* Thu Oct 23 2014 dimstar@opensuse.org
- Add gstreamer-good.appdata.xml so the codec package shows up in
  GNOME Software.
* Wed Sep 24 2014 dimstar@opensuse.org
- Update to version 1.4.3:
  + Minor bug fixes.
  + Updated translations.
* Sun Sep 21 2014 dimstar@opensuse.org
- Update to version 1.4.2:
  + Bugs fixed: bgo#719359, bgo#733607, bgo#734266, bgo#735520,
    bgo#735660, bgo#735804, bgo#735833, bgo#735859, bgo#736192,
    bgo#736266, bgo#736384, bgo#736670, bgo#736739, bgo#736805,
    bgo#736807.
  + Updated translations.
* Thu Aug 28 2014 zaitor@opensuse.org
- Update to version 1.4.1:
  + Bugs fixed: bgo#727180, bgo#733695, bgo#733866, bgo#734435,
    bgo#734473, bgo#734474, bgo#734475, bgo#734476, bgo#734478,
    bgo#734764.
  + Updated translations.
* Mon Jul 21 2014 dimstar@opensuse.org
- Update to version 1.4.0:
  + Bugs fixed: bgo#732912, bgo#733122, bgo#733190, bgo#733380.
  + Updated translations.
- Package baselibs.conf.
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
* Fri Apr 25 2014 dimstar@opensuse.org
- Update to version 1.2.4:
  + Bugs fixed: bgo#725104, bgo#722185, bgo#724619, bgo#725124,
    bgo#725712, bgo#725860, bgo#726777, bgo#728017, bgo#728041,
    bgo#724638, bgo#727329.
- Drop gsp-docs-fix-mismatched-para-tags.patch and
  gsp-docs-use-docbook-markup-for-xi:include.patch: fixed upstream.
* Thu Feb 20 2014 zaitor@opensuse.org
- Add gsp-docs-use-docbook-markup-for-xi:include.patch: fix yet an
  other fallout from gtk-doc 1.20 version. Patch from upstream git.
* Sun Feb 16 2014 zaitor@opensuse.org
- Add gsp-docs-fix-mismatched-para-tags.patch, fixes build with new
  gtk-doc, newer gtkdoc is more sensitive to mismatched docbook
  tags (bgo#724085).
* Sun Feb  9 2014 zaitor@opensuse.org
- Update to version 1.2.3:
  + Bugs fixed: bgo#682276, bgo#712134, bgo#719544, bgo#720659,
    bgo#721241, bgo#721268, bgo#722159, bgo#722163, bgo#722953,
    bgo#723125.
* Tue Dec 31 2013 zaitor@opensuse.org
- Update to version 1.2.2:
  + Bugs fixed: bgo#688153, bgo#709800, bgo#710013, bgo#711131,
    bgo#711829, bgo#712137, bgo#712328, bgo#712335, bgo#712401,
    bgo#712611, bgo#712722, bgo#712744, bgo#715039, bgo#719431,
    bgo#719811, bgo#720813, bgo#720986, bgo#721003.
* Mon Nov 11 2013 dimstar@opensuse.org
- Update to version 1.2.1:
  + Bugs fixed: bgo#683536, bgo#707975, bgo#708505, bgo#708864,
    bgo#709270, bgo#709352, bgo#709384, bgo#709390, bgo#709423,
    bgo#709457, bgo#709507, bgo#709614, bgo#709728, bgo#710110,
    bgo#710215, bgo#710623, bgo#711230, bgo#711497, bgo#711699.
  + Updated translations.
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
* Sat Aug 31 2013 zaitor@opensuse.org
- Update to version 1.0.10:
  + qtdemux: add variant field to H.263 caps, fixing H.263
    playback.
  + flvdemux: memory leak fix.
  + goom: fix issue with caps writability.
  + Bugs fixed: bgo#705142, bgo#705475, bgo#705477, bgo#706422.
* Thu Aug 15 2013 zaitor@opensuse.org
- Update to version 1.0.9:
  + udpsink, multiudpsink: unbreak IPv4 fallback on systems without
    IPv6 support.
  + deinterlace: fix changing 'mode' property on-the-fly to
    enable/disable deinterlacing.
  + rtp: fix autoplugging of depayloaders if there's only one of
    the payload number and the encoding-name.
  + pulse: fixes for alaw/mulaw.
  + matroskademux, avidemux: fix some buffer leaks.
  + flacenc: fix image tag handling.
  + Bugs fixed: bgo#641599, bgo#695981, bgo#704162, bgo#704533,
    bgo#704553, bgo#705018.
* Sat Jul 13 2013 dimstar@opensuse.org
- Update to version 1.0.8:
  + pngenc: fix massive memory leak.
  + pngdec: parse incoming data into frames before decoding.
  + osvideo: many osxvideosink fixes.
  + udpsink, multiudpsink, dynudpsink: bind socket before using it,
    fixes sending udp on windows.
  + Bugs fixed: bgo#682110, bgo#692400, bgo#693727, bgo#699260,
    bgo#699303, bgo#699314, bgo#700047, bgo#700382, bgo#700514,
    bgo#700878, bgo#701586, bgo#702167, bgo#702457, bgo#702705,
    bgo#702732, bgo#703076, bgo#703100, bgo#703171, bgo#703729,
    bgo#691419.
* Sat Apr 27 2013 dimstar@opensuse.org
- Update to version 1.0.7:
  + osxaudio plugin ported to 1.0.
  + Bugs fixed: bgo#695709, bgo#697103, bgo#677560, bgo#685209,
    bgo#693005, bgo#693727, bgo#696052, bgo#696651, bgo#697113,
    bgo#697303, bgo#697984, bgo#698224.
* Sat Mar 23 2013 zaitor@opensuse.org
- Update to version 1.0.6:
  + auparse: fix caps leak.
  + avidemux: push mode: handle some more 0-size buffer cases.
  + deinterlace: fix infinite loop on EOS with non-default methods
    or fields.
  + dvdemux: don't return FALSE when dropping sink events, fixes
    flow errors.
  + level: send a last message on EOS.
  + mp4mux: in faststart mode, don't output up to 4 kB of garbage
    at the end.
  + osxvideosink:
  - Fix crash in osxvideosink with external window output.
  - Make GstGLView propagate input events to its parent view.
  - Make GstNavigation key input events in osxvideosink
    compatible with x(v)imagesink ones.
  + pulsesink: don't error out if pa_stream_proplist_update() with
    new tags fails.
  + qtdemux:
  - fix potential crash on short MOOV atom.
  - fix sample leak when processing private qt tags.
  - push mode: only parse moov 1 once.
  - skip disabled tracks.
  + qtmux: set stream language code from tag.
  + rtph264pay: Don't use upstream caps with peer_query_caps().
  + rtpmp4gdepay: streamtype is not put by all RTSP server, not
    make it optional.
  + rtpptdemux: forward sticky events and then set caps.
  + rtpsession: Fix wrong code organisation in case of collision.
  + rtspsrc:
  - flush connection when stopping.
  - only EOS when our source sends BYE.
  + rtspsrc: save the stream SSRC.
  + v4l2:
  - don't check stride for encoded formats.
  - fix compilation against newer kernel headers as on FC19.
  + videomixer2: avoid caps leak.
  + videomixer: fix eos timestamp check.
  + ximagesrc: Set the pixel aspect ratio correctly in the caps.
  + build:
  - allow calling autogen.sh from out-of-tree.
  - fix build with automake 1.13.
  + Bugs fixed: bgo#628790, bgo#656068, bgo#675453, bgo#678429,
    bgo#684924, bgo#684944, bgo#688935, bgo#689809, bgo#691484,
    bgo#691570, bgo#691580, bgo#691832, bgo#692309, bgo#692786,
    bgo#692935, bgo#692950, bgo#693055, bgo#693173, bgo#693307,
    bgo#693373, bgo#694010, bgo#694184, bgo#694275, bgo#695629,
    bgo#695643, bgo#695644, bgo#696355, bgo#696358.
* Wed Jan  9 2013 dimstar@opensuse.org
- Update to version 1.0.5:
  + rtspsrc: fix regression that make rtspsrc hang when stopping
  + audio/video parsers: fix negotiation with encoders in some
    transcoding cases
  + cairo: port cairooverlay to 1.0
  + jpegenc: pass flow returns upstream
  + qtdemux: fix pixel-aspect-ratio of some files with ProRes video
  + Bugs fixed: bgo#690184, bgo#690476, bgo#691098.
* Wed Dec 19 2012 dimstar@opensuse.org
- Update to version 1.0.4:
  + deinterleave: properly set srcpad channel position
  + osxvideosink: Fix resizing the Cocoa window on receiving new
    caps
  + rtspsrc fixes
  + shout2send: also accept audio/webm in addition to video/webm
  + videobox: fix border filling for planar YUV formats
  + webmmux: fix linking to shout2send
  + v4l2: fix build on FreeBSD
  + Bugs fixed: bgo#684312, bgo#684991, bgo#687469, bgo#689732,
    bgo#689336.
* Thu Nov 22 2012 dimstar@opensuse.org
- Update to version 1.0.3:
  + rtspsrc: numerous improvements
  + build fix for gst-plugins-base installed in non-default prefix
  + multifilesink: post messages in max-size mode as well
  + vp8dec: improve robustness on decoding errors, e.g. for
    videocalls over RTP
  + Bugs fixed: bgo#639420, bgo#686837, bgo#686985, bgo#687013,
    bgo#687154, bgo#687330, bgo#687464, bgo#688382.
* Thu Oct 25 2012 dimstar@opensuse.org
- Update to version 1.0.2:
  + Parallel installability with 0.10.x series
  + avidemux: fix handling of paletted and other raw RGB data
  + flacparse: ignore bad headers if we have a valid STREAMINFO
    header; improve coverart extraction
  + jpegdepay: store quant tables in zigzag order
  + matroskamux: do not use unoffical V_MJPEG codec id; fix
    subtitle request sink pad name and functionality
  + videofilter: add videomedian element
  + multiudpsink: add "force-ipv4" option and "multicast-iface"
    property
  + pulsesink: fix caps leak and potential crasher in acceptcaps
    function
  + pulsesink: start the ringbuffer on GAP events without duration
  + qtdemux: add support for 'generic' samples; allow more streams
  + qtdemux: support more ProRes variants; fix memory leak for
    MS/RIFF audio
  + qtdemux: with raw audio, set a default channel-mask for
    multichannel audio
  + rtpbin: set PTS and DTS in jitterbufffer
  + rtpbin: use running-time for NTP time when use-pipeline-clock
    is set
  + rtpsession: inform source when caps change
  + udpsrc: use negotiated allocator or pool
  + videobox: use out_info for out properties
  + videocrop: port to videofilter
  + videomixer2: Fix race condition where a src setcaps is ignored
  + vp8enc: fix default target-bitrate value; set DECODE_ONLY flag
    on invisible frames
  + Bugs fixed: bgo#654216, bgo#682481, bgo#683782, bgo#683842,
    bgo#684701, bgo#685864, bgo#686008, bgo#686046, bgo#686550,
    bgo#686642.
* Tue Oct  9 2012 dimstar@opensuse.org
- Update to version 1.0.1:
  + interleave, deinterlave: channel handling fixes for mono audio
  + videobalance now supports NV12 and NV21 as well
  + Bugs fixed: bgo#683622, bgo#684972, bgo#684977, bgo#685059,
    bgo#685213, bgo#685512.
* Mon Sep 24 2012 dimstar@opensuse.org
- Update to version 1.0.0:
  + Minor bug fixes
  + Bugs fixed: bgo#684237, bgo#678021, bgo#684430, bgo#684469.
* Tue Sep 18 2012 dimstar@opensuse.org
- Update to version 0.11.99:
  + Move vp8 decoder and encoder from -bad to -good.
  + Rename vp8 to vpx.
- Add pkgconfig(vpx) BuildRequires: Needed for the vpx
  encoder/decoder.
* Fri Sep 14 2012 dimstar@opensuse.org
- Update to version 0.11.94:
  + deinterlace:
  - Don't treat every custom-downstream event as EOS
  - improve framerate transform
  + videomixer2: Adding nv12 and nv21 support
  + qtdemux: add support for prores
  + pulsesrc: consider stream alive when not connected yet
  + Bugs fixed: bgo#54089, bgo#540891, bgo#609049, bgo#656317,
    bgo#657941, bgo#670257, bgo#673509, bgo#673898, bgo#675448,
    bgo#676302, bgo#677306, bgo#677535, bgo#677722, bgo#677838,
    bgo#677905, bgo#679301, bgo#679343, bgo#679807, bgo#679994,
    bgo#680206, bgo#680275, bgo#680277, bgo#680278, bgo#680283,
    bgo#680388, bgo#680427, bgo#680540, bgo#680551, bgo#680558,
    bgo#680706, bgo#681077, bgo#681247, bgo#681335, bgo#681369,
    bgo#681491, bgo#681677, bgo#682446, bgo#682481, bgo#682770,
    bgo#682959, bgo#683065, bgo#683839, bgo#683841, bgo#683861,
    bgo#683902
* Wed Aug  8 2012 dimstar@opensuse.org
- Update to version 0.11.93:
  + Bug fixes
  + Sync with GStreamer changes.
* Sat Jul 28 2012 dimstar@opensuse.org
- Update to version 0.11.92:
  + Parallel installability with 0.10.x series.
  + API cleanup and minor API improvements.
  + Lots of bugfixes, cleanup and other improvements.
* Mon May 14 2012 vuntz@opensuse.org
- Update to version 0.11.91:
  + Ported flx, dv1394, oss and oss4 plugins
  + Lots of bugfixes and other improvements
* Fri Apr 20 2012 vuntz@opensuse.org
- Update to version 0.11.90:
  + Lots of bugfixes, cleanup and other improvements
  + The interleave/deinterleave plugin was ported to 0.11
* Fri Mar 23 2012 vuntz@opensuse.org
- Update to version 0.11.2:
  + Many cleanups
  + Ported to new 0.11 core API changes
  + flacenc: various fixes
  + gdkpixbuf: port to 0.11
  + imagefreeze: port to 0.11
  + qtdemux:
  - negotiate allocators
  - use PTS and DTS
  + rtpbin: many fixes
  + wavpack: port to 0.11
  + Bugs fixed: bgo#628773, bgo#658357, bgo#662615, bgo#667085,
    bgo#669607, bgo#669612, bgo#669643, bgo#670303, bgo#670320,
    bgo#670623, bgo#671534.
- Drop gst-plugins-good-buildfix.patch: fixed upstream.
- Drop libtool BuildRequires and call to autogen.sh, that were only
  needed for above patch.
- Completely drop optional packaging for hal plugin, since it's
  gone:
  + Remove build_hal macro.
  + Remove optional hal-devel BuildRequires.
  + Remove gstreamer-plugin-hal subpackage.
- Add explicit glib2-devel and gstreamer-devel BuildRequires so
  they can be versioned.
- Move to pkgconfig()-style BuildRequires:
  + Old ones: cairo-devel, flac-devel, libcaca-devel, libdv-devel,
    libiec61883-devel, libjack-devel, libpulse-devel,
    libshout-devel, libsoup-devel, libtag-devel, libv4l-devel,
    speex-devel, wavpack-devel.
  + New ones: caca, cairo, cairo-gobject, flac, jack, libdv,
    libiec61883, libpulse, libsoup-gnome-2.4, libv4l2, shout,
    speex, taglib, wavpack.
- Add explicit BuildRequires needed by plugins: libICE-devel,
  libSM-devel, libXv-devel, libbz2-devel, zlib-devel.
- Add explicit pkgconfig() BuildRequires needed by plugins:
  gdk-pixbuf-2.0, gudev-1.0, libpng, libraw1394, libxml-2.0,
  xdamage, xfixes.
- Change python-devel BuildRequires to python-base as only python
  is needed, not the development files.
- Remove now unneeded BuildRequires: esound-devel, ftgl-devel,
  gconf2-devel, ladspa-devel, libtheora-devel, libvorbis-devel.
  Those were used by plugins that were moved to plugins-base, or
  removed.
- Remove BuildRequires that, as far as I can tell, are not needed
  (else, they are implicitly brought in by something else):
  check-devel, python-xml, sgml-skel.
- Move to use GTK+ 3 for the build:
  + Replace gtk2-devel BuildRequires with pkgconfig(gtk+-3.0) and
    pkgconfig(gtk+-x11-3.0).
  + Pass --with-gtk=3.0 to configure.
- Remove Provides/Obsoletes/Conflicts for gstreamer010-* packages
  in doc and extra subpackages.
* Fri Feb 17 2012 dimstar@opensuse.org
- Update to version 0.11.1:
  + Many cleanups
  + Ported to new 0.11 core API changes
  + v4l2 major improvements
  + Ported network elements to GIO
- Rename package to gstreamer-plugins-good; drop -esd subpackage.
- Drop gst-pulsesink-bufsize.diff: new codebase.
- Add gst-plugins-good-buildfix.patch: Fix build.
- Add libtool BuildRequires and call to autogen.sh, as above patch
  touches the build system.
* Sun Sep 11 2011 vuntz@opensuse.org
- Split esound plugin in a gstreamer-0_10-plugin-esd subpackage: we
  do not want to have libesd0 installed by default just because of
  this plugin.
* Sat Aug  6 2011 chris@computersalat.de
- fix deps
  o gstreamer-0_10-plugins-base-devel >= 0.10.33
* Sat Jun 18 2011 reddwarf@opensuse.org
- Update taglib BuildRequire to reflect the package new name. Fixes
  build in Packman OBS.
* Fri Jun 17 2011 vuntz@opensuse.org
- Update to version 0.10.30:
  + Work around GLib atomic ops API change
  + Better handling of malformed buffers in RTP depayloders
    (bgo#650470)
  + Build fixes (including bgo#652144).
* Sat Jun 11 2011 vuntz@opensuse.org
- On 12.1 and later, stop building the gstreamer-0_10-plugin-hal
  subpackage:
  + we don't want hal anymore on 12.1 and later (see bnc#697018).
    We use a build_hal define to control that behavior.
  + remove hal-devel BuildRequires
  + do not build a gstreamer-0_10-plugin-hal subpackage anymore
  + add gstreamer-0_10-plugin-hal Obsoletes for smooth upgrades
* Wed May 11 2011 dimstar@opensuse.org
- Update to version 0.10.29:
  + audioparser: new amrparse, aacparse, ac3parse, flacparse,
    mpegaudioparse, dcaparse elements
  + audiowsincband:
  - Add new windowing functions: gaussian, cos and hann
  - Fix range of kernel elements (lim -> lim-1)
  + audiowsinclimit:
  - Add new windows to high/low-pass filters: gaussian, cosine,
    hann
  - Fix range of kernel elements (lim -> lim-1) in high/low-pass
    filters
  + avidemux:
  - also add the frame-type for the stream index.
  - flvdemux: mark delta-units in the index
  - stream->current_total is accumulated byte size and not time
  + avimux:
  - add stream-format field to h264 pad template caps
  - rework _request_new_pad to handle explict req-pad-names
  - use running time for synchronization
  + cairooverlay: Add generic Cairo overlay video element.
  + debugutils: remove bitrotten negotiation element
  + deinterlace: add support for NV12 and NV21 formats; fix greedyl
    method
  + dvdemux: first try if upstream handles TIME seeks before
    handling them here and other event handling fixes
  + flacdec: fix issues with large metadata blocks when streaming
    unframed flac
  + flacenc:
  - Add support for writing METADATA_BLOCK_PICTURE blocks for
    GST_TAG_IMAGE and GST_TAG_PREVIEW_IMAGE
  - Don't store image tags inside the vorbiscomments and the flac
    metadata
  + flvdemux:
  - add width, height and framerate to caps when present on
    onMetaData
  - Do not build an index if upstream is not seekable
  - fix deadlock on setting index on flvdemux
  + flvmux:
  - don't overwrite metadata tag with duration in streaming mode
  - don't set duration for live stream
  - use running time for synchronization
  + flv: specify stream-format for h264 in the pad template caps
  + icydemux: fix tag list handling issues that might have caused
    crashes
  + j2kpay: skip EPH packets
  + jitterbuffer:
  - also estimate eos if very near eos
  - avoid trying to buffer more than is available
  - handle position query
  + matroskademux:
  - better calculation of output framerate
  - properly resume cluster scanning
  - pull mode should always report seekable
  - set stream-format=byte-stream on h264 caps if there's no
    codec data
  - store cluster positions provided by SeekHead
  + matroskamux:
  - add support for A-Law and µ-Law
  - avoid building index when streamable
  - use running time for stream synchronization
  - add stream-format field to h264 pad template caps
  + matroska: Use ARTIST Matroska tag instead of AUTHOR for
    GST_TAG_ARTIST
  + matroskaparse: new element
  + monoscope: stability (off-by-one) and memory leak fixes
  + pngdec: handle 16-bit-per-channel images
  + pulsesink:
  - also uncork during EOS waiting (and after EOS is rendered)
  - fix deadlock if connecting to PA fails
  - release pa_shared_resource_mutex before
    pa_threaded_mainloop_wait
  + qtdemux:
  - Adds more h264 fields to its caps
  - Add support for 2Vuy and r210
  - don't error out when there's a problem parsing non-vital
    headers
  - avoid skipping exposing a stream following a removed stream
  - Check for invalid (empty) classification info entity strings
  - extract MusicBrainz tags
  - mind rounding issues when converting from global time to mov time
  - propagate error during expose_streams
  - support some more mpeg-4 fourcc variants
  - take configured start time into account
  + isomp4: move mp4mux/3gppmux/qtmux from -bad to -good, rename
    qtdemux plugin to isomp4
  + rtpbin: Don't try to request the same request pad twice
  + rtpbin: fix setting the SDES property
  + rtpbin: Get and use the NTP time when receiving RTCP
  + rtpmanager: ignore a BYE if it is sent with our internal SSRC
  + rtpptdemux: Tag upstream custom events with payload type
  + rtpsession:
  - add action signal to request early RTCP
  - add "rtcp-min-interval" property for minimum interval between
    Regular RTCP messages
  - Don't relay more than one PLI request per RTT
  - Emit "on-ssrc-validated" when validating by RTCP
  - Emit signal on incoming RTCP feedback packet
  - Emit signal when sending a compound RTCP packet
  - Implement sending PLI packets in response to GstForceKeyUnit
  - Number of active sources should be updated whenever the
    status of the source changes to active
  - Send GstForceKeyUnit event in response to received RTCP PLI
  + rtpsource: Retain RTCP Feedback packets for a specified amount
    of time
  + rtpssrcdemux:
  - Tag upstream custom events with SSRC
  - Unknown SSRC is not fatal
  + rtpspeexpay: Do not transmit samples with GAP flag
  + rtptheoradepay: Request new keyframe on lost packets
  + rtpvrawpay: add support for interlaced video
  + rtspsrc:
  - distribute new base_time to manager children following flush
    seek
  - handle * control correctly
  - improve recovery from failed seek
  + spectrum: misc, optimisations, add multi-channel support
  + speexdec:
  - Always process the number of frames per packet as specified
    in the header
  - get and use streamheader from the caps if possible
  - Use speex intern silence detection
  + theorapay: handle 0-sized packets (which are repeat frames)
  + udpsink: warn when packet is too large
  + v4l2:
  - Add PJPG mapping
  - fix interlaced set_format configuration
  - new v4l2radio element to control analog radio devices
  + videobalance: fix handling of YUV images with 'odd' widths
  + videoflip:
  - add support for YUY2, UVYV and YVYU
  - fix invalid memory access for odd resolutions and Y422
  + videomixer2: Add transparent background option for alpha
    channel formats
  + videomixer:
  - Add transparent background option for alpha channel formats
  - Fix argb/rgba overlay orc code
  + wavparse: tune output max buffer size to material
  + Bugs fixed: bgo#564122, bgo#432612, bgo#593482, bgo#595520,
    bgo#622553, bgo#636699, bgo#639994, bgo#640118, bgo#640163,
    bgo#640249, bgo#640483, bgo#640542, bgo#641330, bgo#641332,
    bgo#641400, bgo#641827, bgo#642205, bgo#642337, bgo#642412,
    bgo#642691, bgo#642879, bgo#642961, bgo#642963, bgo#643087,
    bgo#643981, bgo#644288, bgo#644477, bgo#644510, bgo#644669,
    bgo#644773, bgo#644849, bgo#644875, bgo#645858, bgo#645961,
    bgo#646397, bgo#646474, bgo#646567, bgo#646800, bgo#646954,
    bgo#646964, bgo#646965, bgo#646966, bgo#646967, bgo#646999,
    bgo#647263, bgo#647510, bgo#647511, bgo#647659, bgo#647833,
    bgo#647848, bgo#647919, bgo#648004, bgo#648160, bgo#648589,
    bgo#649060, bgo#649449, bgo#566769
- Drop gstreamer-0_10-plugins-good-fix-tag-list-handling-issue.patch:
  fixed upstream.
* Mon May  9 2011 vuntz@opensuse.org
- Move plugins from extra subpackage to main subpackage:
  libgstgdkpixbuf, libgstmonoscope, libgstsmpte, libgstspeex,
  libgstvideobox. This only adds dependencies on gdk-pixbuf and
  speex to the main subpackage, which is reasonable.
- Move plugins from main subpackage to extra subpackage:
  libgstcacasink. We don't want to depend on the caca library by
  default.
- Remove wrongs Provides from extra subpackage:
  gst-plugins-good:%%{_libdir}/gstreamer-%%{gst_branch}/libgstvideo4linux2.so
  This is wrong because the plugin is in the main subpackage.
* Sun Apr 24 2011 toddrme2178@gmail.com
- Add 32bit compatibility libraries
* Fri Apr  8 2011 gburt@suse.de
- Build against libv4l, so libv4lconvert.so gets loaded, which
  gives Cheese et al using camerabin support for old,
  JPEG-producing webcams (bnc#674287)
* Wed Apr  6 2011 tiwai@suse.de
- Updated to version 0.10.28:
  * Fix build issue with new kernels
* Wed Apr  6 2011 tiwai@suse.de
- Increase the pulsesink chunk size to the buffer size for more
  smooth playback (bnc#684781)
* Sat Mar  5 2011 timshel@rocketmail.com
- added possible fix for gstreamer crashes (bnc#673914, bgo#641330)
* Tue Feb  1 2011 davejplater@gmail.com
- Update to version 0.10.27:
- Upsream changes (see documentation directory NEWS for all changes)
  * avidemux add workaround for buggy list size extract datetime tags
  * cacasink: fix masks and strides
  * deinterlace: change the default to linear
  * deinterlace: avoid infinite loop draining
  * deinterlace: rewrite/fix how neighboring scan lines are calculated
  * flvdemux: use aac codec-data to adjust samplerate if needed
  * flvmux: Fix for nellymoser codecid setting
  * icydemux: Add 'StreamUrl' metadata as GST_TAG_HOMEPAGE tag
  * id3demux: fix parsing of ID3v2.4 genre frames with multiple genres
  * imagefreeze: pass along eos if received before buffer arrives
  * jpegdec: add "max-errors" property to ignore decoding errors
  * jpegdec: avoid infinite loop when resyncing; discard incomplete image
  * matroskademux: add stream-format and alignment properties for h264
  * matroskademux: assume matroska if no doctype is specified
  * matroskademux: increase allowed max. block size for push mode
  from 10M to 15M
  * matroskademux: normalize empty Cues to no Cues
  * matroskamux: add support for DTS and E-AC3 audio
  * matroskamux: try to write timestamps in all the outgoing buffers
  * multifilesink: send stream headers in key-frame mode
  * multiudpsink: add buffer-size property
  * navseek: add basic support to change playback rate
  * pulsemixer: Implement MIXER_FLAG_AUTO_NOTIFICATIONS
  * pulsesink: flush remaining buffered samples on EOS
  * pulsesink: make corking during pause synchronous; don't uncork
  in _start
  * pulsesink: Uncork stream while flushing the ringbuffer
  * pulsesrc: add "client" property
  * qtdemux: add support for fragmented mp4
  * qtdemux: add support for (E)AC-3, WMA and VC-1 audio
* Tue Dec  7 2010 vuntz@opensuse.org
- Update to version 0.10.26:
  + alphacolor: make passthrough work
  + avidemux: reverse playback fixes; prevent overlap of subsequent
    fragments
  + deinterlace: remove assembly code in favor of orc
  + dvdemux: parse SMPTE time codes
  + flvdemux: parse and use cts (fixes jittery H.264 playback in
    some cases)
  + flvmux: resend onMetada tag when tags changes in streamable
    mode
  + g729pay: extend from right parent
  + gconf: Don't install schemas when GConf is disabled
  + goom, goom2k1: add latency compensation code, report latency
    correctly
  + gstrtpjpegpay: Added Define Restart Interval (DRI) Marker
  + h264depay: always mark the codec_data as keyframe
  + icydemux: forward tag events
  + id3v2mux: Add mapping for album artist
  + imagefreeze: generate a perfectly timestamped stream
  + level: avoid division by zero on silence
  + matroskademux:
  - more robustness for parse errors and corner-cases
  - extract H.264 profile and level and set on caps
  + matroskamux: reduce newsegment event spam and set discont flag
    where needed
  + pulse:
  - allow setting of pulse stream properties
  - fix device_description in READY
  + pulsesink:
  - Add "client" property to set the PA client name
  - share the PA context between all clients with the same name
  + qtdemux: export AAC/MPEG-4/H.264 profile and level in caps
  + rtp: add G722 payloader and depayloader elements
  + rtpamr(de)pay: support AMR-WB SID frame
  + rtpamrpay: proper duration for multiple frame payload; properly
    support perfect-rtptime
  + rtpbin: add "ntp-sync" property and "use-pipeline-clock"
    properties
  + rtpg729pay: properly support perfect-rtptime
  + rtph264depay: only set delta unit on all-non-key units
  + rtpmanager: provide additional statistics
  + rtpmp4adepay: grab the sampling rate and put into caps
  + rtpmparobustdepay: properly insert dummy buffers; use valid
    bitrate for dummy frame
  + rtpmpvpay: fix timestamping of rtp buffers
  + rtpsession:
  - Add the option to auto-discover the RTP bandwidth
  - Calculate RTCP bandwidth as a fraction of the RTP bandwidth
  - Count sent RTCP packets after they have been finished
  - relax third-party collision detection
  + rtpstats: Rectify description of current_time in
    RTPArrivalStats
  + rtspext: stop configuration on first failure
  + rtspsrc:
  - Add property to configure udpsrc buffer size
  - add rtsp-sdp protocol support
  - don't add /UDP in the transport, it's the default
  - fix duration reporting
  - handle stale digest authentication session data
  - use sdp uri parse method
  + shapewipe:
  - add optional border parameter and slowdown animation
  - Force format to AYUV in the example pipeline for the same
    reason
  - Force the input to AYUV to prevent negotiation failures in
    videomixer
  + spectrum: only aggregate magnitude/phase if user asks for it,
    performance fixes
  + v4l2src:
  - add controllable colorbalance parameters, add decimate
    property
  - fix using mpegts via the mmap interface; use
    GstBaseSrc::block-size as fallback size
  + videomixer2: new videomixer2 element that behaves better than
    videomixer
  + vrawdepay: handle invalid payload better
  + Bugs fixed: bgo#625825, bgo#629047, bgo#537544, bgo#628996,
    bgo#529672, bgo#581294, bgo#598915, bgo#612313, bgo#616521,
    bgo#617318, bgo#620790, bgo#622390, bgo#624338, bgo#625547,
    bgo#626048, bgo#626518, bgo#627162, bgo#627174, bgo#627289,
    bgo#627341, bgo#627796, bgo#628020, bgo#628058, bgo#628127,
    bgo#628214, bgo#628349, bgo#628454, bgo#628608, bgo#629018,
    bgo#629522, bgo#629839, bgo#629896, bgo#630088, bgo#630205,
    bgo#630256, bgo#630317, bgo#630378, bgo#630446, bgo#630447,
    bgo#630449, bgo#630451, bgo#630452, bgo#630457, bgo#630458,
    bgo#630500, bgo#630888, bgo#631082, bgo#631303, bgo#631330,
    bgo#631996, bgo#632548, bgo#632553, bgo#632682, bgo#632945,
    bgo#633205, bgo#633212, bgo#633970, bgo#635532, bgo#635843,
    bgo#636179, bgo#626463, bgo#628894, bgo#633294.
* Fri Sep  3 2010 dimstar@opensuse.org
- Update to version 0.10.25:
  + v4l2src: massive performance improvement in many cases
  + streaming mode fixes for avi and matroska/webm
  + seeking in matroska and webm files that don't have an index
  + new cpureport element for debugging
  + avidemux:
  - improve VBR audio stream handling
  - streaming mode fixes: use proper offset for movi-based index,
    handle 0-size data chunks
  + debugutils: new element cpureport, posts "cpu-report" element
    messages on bus
  + flacdec, rtspsrc, rtph264pay, rtpmp4vdepay: memory leak fixes
  + gconfvideosrc: use correct GConf key (ie. not the audiosrc key)
  + gdkpixbuf: remove gdkpixbuf3 plugin again, gdk-pixbuf was split
    out of gtk+ and will stay at 2.x
  + id3v2mux: write beats-per-minute tag using TBPM frame
  + jpegdec: fix markers parsing regression
  + matroskademux:
  - do not error out on a block with unknown tracknumber
  - fix streaming in case where the size in bytes is unknown
  - handle bogus files storing ADTS AAC data
  - support seeking in local files even if they don't have an
    index
  + matroskamux: don't try to seek back and fix up headers if
    streamable=TRUE
  + pulsesink: fix race when creating multiple pulsesinks at the
    same time
  + qtdemux:
  - also calculate PAR using track width and height for QT files
  - fix the max/avg in btrt atom reading
  - improve reverse playback
  - parse 64-bit version of mvhd atom as well instead of erroring
    out
  - prevent reading past avc1 atom when parsing
  + rtpg729pay: avoid basertppayload perfect-rtptime mode
  + rtph263pdepay: allow more clock-rates as input
  + rtpL16depay:
  - also parse encoding-params for the number of channels
  - default to 1 channel if number of channels not specified
  + rtpmp4gpay: implement perfect timestamps
  + rtspsrc:
  - add "port-range" property, useful for setups with
    firewall/ipsec
  - don't reuse udp sockets (avoids odd errors when data from
    previous streams is received)
  + udpsrc: add "reuse" property to enable or disable port reuse
    (enabled by default, but disabled in rtspsrc)
  + v4l2: sort formats in the right order so that non-emulated
    formats are prefered
  + videobalance: fix wrong locking order that could lead to a
    deadlock
  + videomixer: only reset QoS information and send a NEWSEGMENT
    event downstream for NEWSEGMENT events on the master pad
  + Bugs fixed: bgo#626463, bgo#593117, bgo#618535, bgo#621520,
    bgo#622017, bgo#622577, bgo#623209, bgo#623357, bgo#623629,
    bgo#624173, bgo#624331, bgo#624455, bgo#624770, bgo#625002,
    bgo#625153, bgo#625302, bgo#625371, bgo#625442, bgo#625452,
    bgo#626467, bgo#626609, bgo#626619, bgo#627689, bgo#617368
* Tue Aug 31 2010 aj@suse.de
- Recommend instead of require lang package since it's not mandatory.
* Thu Aug 12 2010 dimstar@opensuse.org
- Update to version 0.10.24:
  + Use Orc (Optimized Inner Loops Runtime Compiler) for SIMD and
    other optimisations, and remove liboil dependency
  + alpha: add "prefer-passthrough" property to allow passthrough
    mode
  + avidemux: improve audio vbr detection
  + cmmlenc: Remove hack to let oggmux start a new page for every
    CMML buffer
  + deinterlace: add mmx implementations of greedyh for UYVY;
    orcify some deinterlacing methods
  + dv1394: fix the internal clock even more
  + flvmux:
  - add "streamable" property
  - write duration at the correct position
  + gdkpixbuf: Add a gdkpixbuf3 plugin that uses gdkpixbuf3
  + jpegdec: improved parsing, and better buffer handling that
    minimises memcpys
  + jpegdec, jpegenc: add grayscale support
  + matroskademux:
  - QoS fixes and improvements; reverse playback improvements
  - handle zero-sized numbers correctly
  + matroskamux:
  - add "streamable" property; set streamheaders on output caps
  - try harder to make sure clusters start with a key frame
  - mark output buffers properly as keyframe or delta unit
  - do some write caching to avoid newsegment events before each
    output buffer
  - fix some timestamp drift caused by rounding errors
  + pngenc: Support 8 bit grayscale
  + pulsesink:
  - optimize communication with PulseAudio using
    pa_stream_begin_write
  - Post provide-clock message on the bus if the clock
    appears/disappears
  + rtph264depay: consider SPS, PPS and IDR as keyframe, all
    others as DELTA_UNIT
  + rtph264pay: handle short startcodes in the h264 bytestream
  + rtpjitterbuffer: stop buffering and emit EOS at the end of a
    stream
  + rtpmparobustdepay: add mpa-robust depayloader
  + rtpmp4gdepay: calculate the frame duration correctly
  + rtptheorapay: keep announcing the delivery-method in the
    capabilities, restores compatibility with older farsight
    versions again
  + rtspsrc: respect aggregate control attributes; try all ranges
    from the sdp
  + spectrum: support 24-bit width and arbitrary bit depth
  + udp: make url parsing compatible with VLC syntax
  + udpsrc: fix multicast support on windows
  + v4l2sink: destroy buffer pool when changing state to NULL
  + videobox: fix negotiation for I420/YV12
  + videomixer: don't mix input with different pixel aspect ratios;
    negotiation fixes
  + wavparse:
  - proper closing segment construction when doing non-flushing
    seeks
  - use typefind functions to check if PCM data contains dts
    stream
  + Bugs fixed: bgo#555967, bgo#570761, bgo#583047, bgo#589997,
    bgo#595978, bgo#597695, bgo#611117, bgo#613066, bgo#615461,
    bgo#617339, bgo#618530, bgo#618871, bgo#618982, bgo#619198,
    bgo#619273, bgo#619293, bgo#619531, bgo#619717, bgo#619824,
    bgo#619848, bgo#620148, bgo#620154, bgo#620162, bgo#620277,
    bgo#620358, bgo#620390, bgo#620494, bgo#620540, bgo#620591,
    bgo#620743, bgo#620929, bgo#621510, bgo#621566, bgo#621723,
    bgo#622498, bgo#622500, bgo#622501, bgo#622816, bgo#623103,
    bgo#623172, bgo#623196, bgo#623366, bgo#623379, bgo#623585,
    bgo#623654, bgo#619817, bgo#617512, bgo#619485, bgo#413942
- Add orc BuildRequires
- remove liboild-devel BuildRequires
* Mon Aug  9 2010 dimstar@opensuse.org
- Update to version 0.10.23
  + alpha: add support for YUY2, YVYU, UYVY and YV12; YUV->RGB
    conversion fixes
  + avimux, flvmux, matroskamux: don't crash if tags arrive on
    multiple input pads at the same time
  + avimux, matroskamux: add support for On2 VP8
  + capssetter: element moved from gst-plugins-bad
  + deinterlace:
  - add support for most YUV and RGB formats for some methods
  - make automatic detection of interlacing the default
  + gamma: add support for more YUV/RGB formats, make gamma
    property controllable
  + jpegdec, jpegenc: support more colour spaces and pixel formats
  + matroskademux:
  - implement push mode seeking
  - add support for WebM
  + imagefreeze: plugin moved from gst-plugins-bad
  + oss4: plugin moved from gst-plugins-bad
  + osxvideosink: implement the xoverlay interface, allow switching
    views at runtime
  + qcelpdepay: add a QCELP depayloader
  + qtdemux: add support for VP8; push-mode seeking and ctts table
    parsing fixes
  + rtph263depay: use Picture Start Code to detect packet loss and
    frame start
  + rtph263pay: use found GOBs to apply Mode A payloading
  + rtph264depay: DELTA_UNIT marking of output buffers
  + rtph264pay:
  - extract SPS and PPS from property provided parameter set
  - add config-interval property to re-send SPS/PPS in stream
  + rtpmp4vpay: add config-interval property to re-insert config in
    stream
  + rtptheoradepay: fix in-band configuration parsing
  + rtptheorapay: add config-interval parameter to re-insert config
    in stream
  + rtpvorbisdepay, rtptheoradepay: also accept in-line
    configuration
  + rtsp: configure bandwidth properties in the session
  + rtspsrc:
  - fall back to SDP ports instead of server_port
  - use the SDP connection info in multicast
  - handle SEEKING queries
  + smptealpha: add support for all 4 ARGB formats and YV12
    (converted to AYUV)
  + videobalance: add support for all RGB formats, Y41B, Y42B and
    Y444, YUY2, UYVY, AYUV and YVYU
  + videobox:
  - add support for Y444, Y42B, Y41B, YUY2, UYUV, and YVYU
  - fix floating point to integer conversion for the alpha values
  - handle ranges/lists of width or height when transforming caps
  - translate navigation events to make sense again upstream
  + videofilter: merge gamma, videobalance, and videoflip plugin
    into single plu
  + videoflip:
  - add support for all RGB formats and AYUV, Y41B, Y42B and Y444
  - also flip the pixel-aspect-ratio if width/height are
    exchanged
  + videomixer: add support for Y444, Y42B, Y41B, YV12, YUY2, YVYU,
    UYVY
  + webmmux: Add new webmmux element that only supports muxing of
    WebM
  + y4menc: add 4:2:2, 4:1:1, and 4:4:4 output support
  + Bugs fixed: bgo#576286, bgo#618349, bgo#574416, bgo#590662,
    bgo#592270, bgo#599585, bgo#600553, bgo#606689, bgo#607452,
    bgo#609405, bgo#609658, bgo#610172, bgo#610902, bgo#613786,
    bgo#614305, bgo#614765, bgo#615798, bgo#616516, bgo#616700,
    bgo#617164, bgo#617537, bgo#617733, bgo#617739, bgo#618305,
    bgo#618351, bgo#618386, bgo#618419, bgo#618733, bgo#618874,
    bgo#618940, bgo#619018, bgo#619103, bgo#619105, bgo#619219,
    bgo#619835, bgo#619943, bgo#620002, bgo#605231, bgo#619533
* Tue May  4 2010 dimstar@opensuse.org
- Update to 0.10.22:
  + alpha: add support for different color matrixes
  + alpha: add support for generating ARGB output
  + alpha: add support for ARGB, RGB and xRGB input
  + alphacolor: support inplace and on-the-fly conversions from
    AYUV to ARGB
  + alphacolor: Implement color-matrix support and use integer
    arithmetic only
  + videobox: add support for most common RGB(A), (A)YUV, and
    grayscale formats
  + videobox: add support for on-the-fly conversions for some
    formats
  + videobox: add support for filling the background with red,
    yellow and white
  + videobox: add support for YV12, including conversion support
    for I420/AYUV
  + videomixer: add support for ABGR and RGBA
  + shapewipe: add support for the remaining ARGB formats
  + qtdemux, matroska: export h.264 profile and level in caps
  + multifilesink: Add key-frame option to next-file
  + directsoundsink: Implement SPDIF support for AC3
  + h264depay: handle STAPs properly
  + speexdec: adapt to new oggdemux
  + flvdemux: mark delta frames properly
  + flvdemux: improve index building and scaning in pull mode
  + flvdemux: add support for backwards playback (when operating in
    pull mode)
  + avidemux: fix offset handling in push mode seeking
  + matroskademux: prefer index of video track to perform seeking
  + matroskademux: add support for backwards playback (when
    operating in pull mode)
  + matroskademux: push correctly sized flac header buffers
  + matroskademux: restrict resyncing to subtitle tracks
  + rtpsession: Make it possible to favor new sources in case of
    SSRC conflict
  + rtspsrc: send keep alive when paused
  + rtspsrc: handle ipv6 listening ports when needed
  + rtspsrc: require a destination for multicast
  + rtspsrc: parse connection information
  + qtdemux: Set stream-format=raw on AAC caps
  + qtdemux: add XMP parsing support
  + qtdemux: Read replaygain peak/gain tags
  + qtdemux: extract stream language in more cases
  + id3demux: fix parsing of unsynced frames with data length
    indicator
  + jpegdec: don't crash if jpeg image contains more than three
    components
  + ximagesrc: send new segment event in TIME format
  + mp4gdepay: improve constantDuration guessing
  + h264pay: fix config-interval property
  + rtspsrc: add property to control the buffering method
  + png: make work with libpng 1.4
- Drop gstreamer-0_10-plugins-good-libpng14.patch, upstream fixed.
* Thu Apr  8 2010 pgajdos@suse.cz
- build against libpng14
* Thu Mar 25 2010 vuntz@opensuse.org
- Split the hal plugin in a gstreamer-0_10-plugin-hal subpackage to
  not require hal (which is deprecated) with this package. Fix
  bnc#590715.
* Sat Mar 13 2010 dimstar@opensuse.org
- Update to version 0.10.21:
  + Fixes for RTP h263 depayloader timestamping regressions that
    broke video calls
  + Fixes for FLAC decoder when FLAC is embedded in a container
    such as Ogg or Matroska
  + rtpsource: bitrate estimation improvements
  + rtspsrc, udp: multicast fixes
* Mon Mar  8 2010 dimstar@opensuse.org
- Update to version 0.10.19:
  + Features of this release:
  - shapewipe: moved from -bad to -good
  - avidemux: push mode seeking support
  - avidemux: drop video frames up to the desired keyframe after
    a seek
  - configure: cross-compilation fixes (use $PKG_CONFIG instead
    of pkg-config)
  - dvdepay: don't output frames until we have a header, fixes
    crash
  - flacdec: fix tag extraction in push mode
  - flvdemux: obtain the index from the end of an flv file in
    push mode
  - flvdemux: audio tags without any content are valid; indexing
    improvements
  - jpegdec: fix invalid memory access in parser
  - jitterbuffer: new buffering modes: low/high watermark
    buffering, rtp timestamps
  - matroskademux: seeking/segment fixes (esp. regression with
    gnonlin)
  - matroskademux: subtitle stream improvements (advance sparse
    streams in smaller steps)
  - multipartdemux: improve header mime-type parsing
  - qtdemux: fix ALAC codec-data handling; handle signed values
    in 3GPP location tag
  - qtdemux: fix frame rate cap regression; fix sample durations
    corner-case
  - qtdemux: Use the correct duration when comparing segments
  - pulsesink: avoid segfault when shutting down
  - pulsesink: return previous mute state if sink is not active
    at the moment
  - rtpbin: change how NTP time is calculated in RTCP, generating
    more accurate NTP timestamps if the system clock is
    synchronised with NTP or similar
  - rtpmp4gdepay: avoid division by 0 in corner case
  - v4l2sink: change rank to NONE so we don't try to autoplug it
  - videomixer: fix timestamping problems for input streams with
    different lengths
  - videomixer: fix problem when used with gnonlin (always send
    FLUSH_STOP)
    + Bugs fixed: bgo#584536, bgo#587304, bgo#599292, bgo#604711,
    bgo#608026, bgo#608843, bgo#610004, bgo#610053, bgo#610238,
    bgo#610265, bgo#610280, bgo#610296, bgo#610337, bgo#610483,
    bgo#610556, bgo#610839, bgo#610894, bgo#611501, bgo#609724
* Wed Feb 17 2010 dimstar@opensuse.org
- Update to version 0.10.18:
  + Changes:
  - v4l2src: implement GstURIHandler interface
  - matroskamux: make index size configurable
  - matroskademux: support push based mode
  - matroskademux: improve stream synchronization
  - flacdec: fix possible hanging in pull mode seeking
  - flacdec: use a single decoder field for both push and pull
    mode
  - flacenc: optionally add a seek table
  - rtp: add BroadcomVoice payloader and depayloader
  - rtp: add G.723 payloader and depayloader
  - rtph264pay: add option to insert PPS/SPS in streams
  - rtph264depay: optionally merge NALUs into Access Units
  - rtspsrc: add user-id and user-pw properties; fix major memory
    leak
  - avimux: many fixes, also better compatibility with Windows
    Media Player
  - avidemux: per-stream index parsing (= much faster startup)
  - qtdemux: progressive download support / seeking in push mode
  - qtdemux: per sample parsing (= much faster start up)
  - wavenc: Post warning if file hasn't been finalised properly
  - videomixer: MMX optimisations and other improvements;
    implement basic QoS
  - matroska, qtdemux, id3demux: fix language code writing and
    extraction
  + Bugs fixed: bgo#503582, bgo#351595, bgo#505823, bgo#515073,
    bgo#539858, bgo#554839, bgo#582575, bgo#583367, bgo#583985,
    bgo#587323, bgo#593354, bgo#595265, bgo#597497, bgo#597823,
    bgo#599300, bgo#601143, bgo#601242, bgo#601728, bgo#602231,
    bgo#602508, bgo#602887, bgo#602940, bgo#603376, bgo#603471,
    bgo#603547, bgo#603779, bgo#604352, bgo#604611, bgo#604679,
    bgo#604814, bgo#604872, bgo#604913, bgo#605222, bgo#605269,
    bgo#605447, bgo#605882, bgo#606198, bgo#606438, bgo#606692,
    bgo#606807, bgo#607353, bgo#607440, bgo#607718, bgo#607949,
    bgo#608209, bgo#608255, bgo#608268, bgo#608629, bgo#608671,
    bgo#608990, bgo#609107, bgo#598610
* Wed Dec 23 2009 dimstar@opensuse.org
- Update to version 0.10.17:
  + RTP improvements
  + Support automatic cropping in videobox
  + Add TTL multicast UDP property
  + AVI demux push mode fixes and performance improvements
  + Support large and unusual chunks sizes in wav
  + Quicktime demuxer improvements
  + JPEG decode fixes and speedups
  + Support interlaced Y4M file output
  + DV demuxer improvements
  + Pulseaudio fixes and improvements
  + Support Pulseaudio PLAY/PAUSE requests
  + speexdec improvements
  + FLV demuxer improvements
  + Fix audio noise in the Equalizer plugin, and other improvements
  + Fix compilation on OS/X Snow Leopard
  + AVI muxer fixes
  + Support MPEG V4L2 devices and improve timestamping
  + Better jpeg2k support
  + Many other bug fixes and improvements
  + Bugs fixed: bgo#597848, bgo#588245, bgo#368681, bgo#458629,
    bgo#561825, bgo#581334, bgo#582238, bgo#590362, bgo#591713,
    bgo#593354, bgo#593391, bgo#593688, bgo#593757, bgo#593764,
    bgo#593955, bgo#594039, bgo#594133, bgo#594247, bgo#594248,
    bgo#594251, bgo#594253, bgo#594254, bgo#594283, bgo#594298,
    bgo#594490, bgo#594520, bgo#594599, bgo#594663, bgo#594691,
    bgo#595029, bgo#595220, bgo#595231, bgo#595888, bgo#595897,
    bgo#595942, bgo#596319, bgo#597091, bgo#597214, bgo#597348,
    bgo#597351, bgo#597397, bgo#597463, bgo#597601, bgo#597730,
    bgo#597847, bgo#597867, bgo#598377, bgo#598517, bgo#598810,
    bgo#598933, bgo#601381
- Changes from version 0.10.16:
  + Moved rtpmanager from -bad to -good
  + Implement SEEKING query in more demuxers and decoders (notably
    mkv, flv, flac)
  + avimux: adds support to WMA/WMV
  + cairo: Add cairo-based PDF/PS/SVG encoder element (cairorender)
  + dv1394src: fix element for live usage
  + effectv: new elements: rippletv, streaktv, radioactv, optv
  + flacdec: fix intermittent FLAC__STREAM_DECODER_ABORTED errors
    when seeking
  + flacenc: fix issue with broken duration / sample count into
    flac header in some cases
  + flvmux: lots of fixes and improvements
  + id3demux: fix parsing of unsync'ed ID3 v2.4 tags and frames
  + matroska: add kate subtitle support, add/improve WMA/WMV
    handling and read bluray PGS subpicture streams
  + multipartdemux: support more mime types, do proper flow
    aggregation
  + pulsesrc: cleanups, report real latency, set the default slave
    method to skew
  + qtdemux: support for agsm, misc. tag reading fixes
  + rtp: new QDM2 and CELT depayloaders; fix SVQ3 depayloader and
    make it autopluggable
  + souphttpsrc: Only assume seekability if the server provides
    Content-Length
  + v4l2: add v4l2sink element, open device in NULL->READY,
    optional gudev support
  + v4l2src: fix 'hang' with some cameras caused by bad
    timestamping if no framerate is available
  + videomixer: add RGB format support; fix I420 blending
  + Bugs fixed: bgo#331420, bgo#499242, bgo#521625, bgo#560033,
    bgo#564100, bgo#564501, bgo#567983, bgo#577017, bgo#577318,
    bgo#578052, bgo#578166, bgo#578612, bgo#580214, bgo#580732,
    bgo#582153, bgo#582169, bgo#582462, bgo#583593, bgo#583640,
    bgo#584455, bgo#584613, bgo#585205, bgo#585361, bgo#585559,
    bgo#585576, bgo#585630, bgo#585699, bgo#585757, bgo#585828,
    bgo#585831, bgo#586397, bgo#587426, bgo#587680, bgo#587826,
    bgo#585831, bgo#586397, bgo#587426, bgo#587680, bgo#587826,
    bgo#587982, bgo#587983, bgo#588148, bgo#588349, bgo#588359,
    bgo#588368, bgo#588483, bgo#588695, bgo#588777, bgo#589056,
    bgo#589365, bgo#589423, bgo#589424, bgo#589459, bgo#590038,
    bgo#590280, bgo#590401, bgo#590447, bgo#590970, bgo#591451,
    bgo#591476, bgo#591712, bgo#591747, bgo#591951, bgo#592232,
    bgo#592530, bgo#593015, bgo#585911, bgo#576378, bgo#564437,
    bgo#582515, bgo#583048, bgo#583371, bgo#583803, bgo#584981,
    bgo#585056, bgo#585549, bgo#585842
* Mon Oct 26 2009 sbrabec@suse.cz
- Added support for translation-update-upstream (FATE#301344).
* Wed Aug 12 2009 sbrabec@suse.cz
- Fixed directory ownership.
* Fri May 22 2009 vuntz@novell.com
- Update to version 0.10.15:
  + Some fixes for seeking in wav and FLAC files
  + Faster seeking in Matroska and AVI files
  + RTSP and RTP improvements
  + directdrawsink moved to Bad
  + y4menc and flvmux/flvdemux moved from Bad
  + deinterlace2 moved from Bad, replacing deinterlace
  + Many bug fixes and improvements
  + Pulseaudio sink completely overhauled
  + Bugs fixed: bgo#572551, bgo#577318, bgo#576286, bgo#581333,
    bgo#478092, bgo#486915, bgo#509311, bgo#516031, bgo#537537,
    bgo#537609, bgo#552650, bgo#562168, bgo#563574, bgo#567140,
    bgo#567857, bgo#570781, bgo#571153, bgo#571321, bgo#572256,
    bgo#572358, bgo#572413, bgo#573173, bgo#573342, bgo#573343,
    bgo#573721, bgo#573737, bgo#574270, bgo#574275, bgo#577468,
    bgo#577609, bgo#577671, bgo#578052, bgo#578135, bgo#578310,
    bgo#579070, bgo#579422, bgo#579808, bgo#580746, bgo#580783,
    bgo#580851, bgo#580880, bgo#581329, bgo#581568, bgo#581806,
    bgo#581884, bgo#582252, bgo#582281, bgo#582387, bgo#582420,
    bgo#582661, bgo#582715, bgo#582753, bgo#582794, bgo#568278,
    bgo#569611, bgo#571294, bgo#574169, bgo#575234, bgo#576729,
    bgo#578257, bgo#579069, bgo#580554, bgo#581432, bgo#581444,
    bgo#582218, bgo#575937
- Drop gst-plugins-good-pulsemixerctrl-strict-aliasing.patch: fixed
  upstream.
- Remove hack in setup to fix an old error, and do not call autogen
  anymore.
- Remove checks for old versions of openSUSE.
- Remove --enable-ladspa from configure: it doesn't exist anymore.
* Thu Apr 30 2009 sbrabec@suse.cz
- Don't call autogen in older products.
- Require python-xml explicitly to get minidom on all products.
* Wed Feb 25 2009 sbrabec@suse.cz
- Strict aliasing fix.
* Sat Feb 21 2009 vuntz@novell.com
- Update to version 0.10.14:
  + Add autodetect source elements
  + Improvements in RTP payload/depayload and RTSP
  + Support float input in wav, and require depth == width
  + Support inverted RGB video in avi
  + Compilation fixes and smarter format selection in V4L2 support
  + Use libv4l when available
  + Don't install static plugin libraries any more
  + Matroska muxing: Add Dirac, fix AAC
  + Improve qtdemux segment handling
  + Add presets to equalizer
  + OS/X video and audio output improvements
  + Rework Pulseaudio audio output
  + Support basic and digest auth in souphttpsrc
  + Use libsoup-gnome instead of libsoup when available
  + DV demuxer fixes
  + New IIR and FIR base classes and echo filter in audiofx plugin
  + Improved spectrum analysis plugin
  + 8 bit greyscale support in v4l2src and videocrop
  + New aspectratiocrop element
  + Many other bug fixes and improvements
  + Bugs fixed: bgo#561502, bgo#522183, bgo#523813, bgo#557709,
    bgo#560155, bgo#527951, bgo#529379, bgo#532409, bgo#537539,
    bgo#537540, bgo#537543, bgo#545033, bgo#552140, bgo#556019,
    bgo#556484, bgo#556641, bgo#556802, bgo#556955, bgo#556986,
    bgo#557260, bgo#557293, bgo#557294, bgo#557710, bgo#558427,
    bgo#558638, bgo#558711, bgo#559288, bgo#559545, bgo#559547,
    bgo#560641, bgo#560756, bgo#561625, bgo#561775, bgo#561802,
    bgo#561990, bgo#562434, bgo#562572, bgo#563414, bgo#563504,
    bgo#563509, bgo#563510, bgo#564437, bgo#564948, bgo#565850,
    bgo#566616, bgo#566843, bgo#567577, bgo#567642, bgo#567746,
    bgo#567794, bgo#567800, bgo#567853, bgo#567874, bgo#567955,
    bgo#567992, bgo#568395, bgo#568780, bgo#568809, bgo#569820,
    bgo#570343, bgo#570435, bgo#571038, bgo#571150, bgo#571153,
    bgo#571204, bgo#570581, bgo#341752, bgo#420658, bgo#558554,
    bgo#561580, bgo#563056, bgo#565441, bgo#567952
  + We now have a /usr/share/gstreamer-0.10 directory. We don't
  package blindly all files, though, since we can't know for sure
  to which package the files belong.
* Thu Feb  5 2009 vuntz@novell.com
- Update to version 0.10.13:
  + Fix bad autopoint substitution in the po subdir
- Change from version 0.10.12:
  + Fix for security advisory TKADV2009-0xx
* Fri Jan  2 2009 mboman@suse.de
- Update to version 0.10.11:
  + Bugs fixed: bgo#545433, bgo#311586, bgo#350830, bgo#413841, bgo#536067,
    bgo#537361, bgo#543101, bgo#544956, bgo#545463, bgo#545710, bgo#546465,
    bgo#547075, bgo#547217, bgo#547227, bgo#547518, bgo#547519, bgo#548530,
    bgo#548831, bgo#549073, bgo#549090, bgo#549551, bgo#549784, bgo#550015,
    bgo#550791, bgo#551048, bgo#551570, bgo#551584, bgo#552213, bgo#553191,
    bgo#554771, bgo#556010, bgo#556381, bgo#556424, bgo#557085, bgo#557610,
    bgo#547842, bgo#550288
  + HDV capture support
  + Port flactag element to 0.10
  + Support FLAC in alternate bit-depths and more samplerates
  + Matroska muxing improvements
  + Support Google RTSP variant
  + Many other bug-fixes and improvements
* Thu Nov  6 2008 sbrabec@suse.cz
- Enabled souphttpsrc module, aasink moved to extra (bnc#441855).
- Fixed valgrid BuildRequires.
* Thu Oct 23 2008 sbrabec@suse.cz
- Obsolete any released version of gstreamer-0_10-pulse.
* Wed Sep 17 2008 jpr@novell.com
- Update to version 0.10.10:
  + Move the libcdio cddasrc element to -ugly
  + Replaygain elements moved from Bad
  + Interleave/Deinterleave elements moved from Bad
  + Pulseaudio plugin http://pulseaudio.org is now integrated
  + New simple Karaoke audio effect plugin
  + Improvements in v4l2src
  + Multi-channel FLAC file fixes
  + AVI and Quicktime reverse playback support
  + AVI and Matroska muxing improvements
  + New element for rendering SMPTE transitions into alpha channels
  + Many improvements in the Win32 directdraw elements
  + Error out cleanly for encrypted streams
  + RTP/UDP handling improvements
  + RTSP digest authentatication implemented.
  + New RTP Pay/Depay-loaders for Speex, G.729, DV & raw video/audio
  + Error concealment for Speex
  + bgo#413705, bgo#541787, bgo#345393, bgo#400679, bgo#422917,
    bgo#429322, bgo#465146, bgo#469917, bgo#499318, bgo#503288,
    bgo#511489, bgo#512345, bgo#515962, bgo#516509, bgo#519301,
    bgo#519460, bgo#520092, bgo#520885, bgo#527865, bgo#529454,
    bgo#529692, bgo#529707, bgo#530886, bgo#531532, bgo#531672,
    bgo#532295, bgo#532393, bgo#532409, bgo#532423, bgo#533264,
    bgo#533619, bgo#535121, bgo#535300, bgo#535935, bgo#536228,
    bgo#536317, bgo#536646, bgo#536831, bgo#536903, bgo#537021,
    bgo#537031, bgo#537361, bgo#537377, bgo#537622, bgo#537675,
    bgo#537832, bgo#539372, bgo#539548, bgo#540067, bgo#540300,
    bgo#540940, bgo#541081, bgo#541384, bgo#541412, bgo#541650,
    bgo#541956, bgo#542410, bgo#543054, bgo#543255, bgo#543259,
    bgo#543300, bgo#544509, bgo#539482, bgo#544433, bgo#536994,
    bgo#329198, bgo#532065, bgo#533287, bgo#538891, bgo#516509,
    bgo#515978, bgo#516649, bgo#517237, bgo#517933, bgo#518188,
    bgo#518213, bgo#518564, bgo#519088, bgo#519417, bgo#520073,
    bgo#520764, bgo#520880, bgo#520888, bgo#521102, bgo#521875,
    bgo#522278, bgo#522767, bgo#523124, bgo#523134, bgo#524593,
    bgo#525359, bgo#525833, bgo#525860, bgo#525946, bgo#526557,
    bgo#527848, bgo#527984, bgo#527999, bgo#528143, bgo#528615,
    bgo#529268
- Enable pulseaudio plugin, replaces gstreamer-0_10-pulse
- Remove gst-plugins-good-speex-header-boundscheck.patch, it was
  upstreamed
- Remove gst-plugins-good-esdsink.patch, it was upstreamed
- Remove libcdio-devel, the dependent plugin was moved to ugly
* Tue Sep  2 2008 kukuk@suse.de
- Get rid of aalib dependency.
* Fri May 23 2008 sbrabec@suse.de
- Moved v4l2 to the main package (bnc#390317).
- Added Enhances for the extra package.
* Tue May 20 2008 maw@suse.de
- Add gst-plugins-good-esdsink.patch (bnc#392706).
* Mon Apr 14 2008 maw@suse.de
- Add gst-plugins-good-speex-header-boundscheck.patch (bnc#379099,
  bnc#377602, and CVE-2008-1686).
* Tue Apr  8 2008 sbrabec@suse.cz
- Fixed Obsoletes (bnc#357153).
* Mon Mar 10 2008 maw@suse.de
- Update to version 0.10.7:
  + Massive RTSP/RTP improvements
  + Fixes in pngdec, gdkpixbufdec, wavpackparse, wavpackdec,
    smokeenc, mulawdec, alwdec, id3demux
  + More Fixes in matroskademux, udpsrc, apedemux, flacenc, avimux,
    dv1394src
  + V4L2 support improved
  + Fixes for OS/X and Windows video/audio sources and sinks
  + Support more formats in QT files
  + Elements moved from gst-plugins-bad: equalizer, lpwsinc (now
    audiowsinclimit), bpwsinc (now audiowsincband), spectrum,
    multifilesrc/sink
  + New audio effects: High/Low/Band-pass filters
  + Bugs fixed: bgo#415627, bgo#463624, bgo#347848, bgo#348085,
    bgo#351726, bgo#358841, bgo#417420, bgo#427573, bgo#435435,
    bgo#442034, bgo#447000, bgo#448278, bgo#449747, bgo#450190,
    bgo#450878, bgo#451249, bgo#451388, bgo#453037, bgo#453417,
    bgo#453630, bgo#455086, bgo#455808, bgo#457097, bgo#461600,
    bgo#464475, bgo#464800, bgo#465040, bgo#465774, bgo#467214,
    bgo#467666, bgo#470502, bgo#471364, bgo#471823, bgo#473670,
    bgo#474616, bgo#475424, bgo#477199, bgo#477456, bgo#479960,
    bgo#480557, bgo#482495, bgo#484998, bgo#485828, bgo#487488,
    bgo#487563, bgo#488112, bgo#488844, bgo#488879, bgo#489940,
    bgo#490034, bgo#490283, bgo#491323, bgo#492388, bgo#496752,
    bgo#496773, bgo#496983, bgo#497007, bgo#497017, bgo#497292,
    bgo#497293, bgo#498181, bgo#498297, bgo#498395, bgo#498715,
    bgo#499178, bgo#499239, bgo#499383, bgo#500403, bgo#501775,
    bgo#502655, bgo#502814, bgo#502966, bgo#503023, bgo#504018,
    bgo#504081, bgo#504895, bgo#505745, bgo#506025, bgo#506715,
    bgo#507642, bgo#508644, bgo#509298, bgo#509301, bgo#509531,
    bgo#510505, bgo#510592, bgo#513628, bgo#514397, bgo#514573,
    bgo#514889, bgo#514965, bgo#515457, bgo#515562, bgo#515697,
    bgo#515701, bgo#515703, bgo#515704, bgo#515706, bgo#515905,
    bgo#515979, bgo#515980, bgo#515984, bgo#515985, bgo#516371,
    bgo#516524, bgo#517386, bgo#508291, bgo#447961, bgo#475784,
    bgo#478244, bgo#480707, bgo#502187, bgo#509329, and bgo#512544
- Remove gst-plugins-good-ac.diff.
* Wed Jan 23 2008 sbrabec@suse.cz
- Rename package according to shared library packaging policy
  (#223286).
- Created lang package.
- Added gst-plugins-good-0.10.6 incompatibility work-around.
* Tue Oct 16 2007 sbrabec@suse.cz
- Fixed typo and backslash expansion in previous change.
* Mon Oct 15 2007 sbrabec@suse.cz
- Worked around OBS spec file corruption bug (#332132).
* Fri Oct  5 2007 sbrabec@suse.cz
- Use less restrictive Requires based on the sources.
* Thu Aug  2 2007 sbrabec@suse.cz
- Use Enhances: gstreamer010 instead of Supplements (#294358).
* Wed Jun 20 2007 sbrabec@suse.cz
- Updated to version 0.10.6:
  * Much improved RTSP/RTP and V4l2 support
  * New plugins - audiopanorama, audioinvert, audiodynamic,
    audioamplify
  * qtdemux, videocrop and wavpack elements moved from Bad Plugins
  * Fixes in avi and matroska muxing
  * Fixes in wavparse, sunaudio, AVI demuxing, ID3 tag handling
  * gamma element ported to 0.10
  * Parallel installability with 0.8.x series
  * Threadsafe design and API
  * Many bugs fixed
* Wed May 30 2007 dmueller@suse.de
- remove redundant buildrequires
* Wed May 16 2007 sbrabec@suse.cz
- Use Supplements instead of not yet supported Enhances.
- Fixed invalid comparison.
* Sat May 12 2007 olh@suse.de
- remove unneded Buildrequires for libraw1394-devel
* Thu Apr 19 2007 schwab@suse.de
- Fix quoting in autoconf macros.
* Wed Apr 18 2007 sbrabec@suse.cz
- Build correctly in older products (flac, kernel headers).
* Fri Apr 13 2007 tiwai@suse.de
- fix build and support FLAC 1.1.4.
* Wed Apr 11 2007 sbrabec@suse.cz
- V4L2 source moved from Bad Plugins. Use Conflicts (#260445).
* Tue Mar 27 2007 sbrabec@suse.cz
- Updated to version 0.10.5:
  * Parallel installability with 0.8.x series
  * Threadsafe design and API
  * RTP/RTSP improvements
  * Fixes in OSS support
  * Addition of the audiopanorama element
  * Improvements in AVI playback
  * Annodex playback fixes
  * Support FLAC in OGG and Matroska
  * Fixes in the Speex decoder
  * V4L2 source moved from Bad Plugins
  * SMPTE element ported to 0.10
  * GStreamer Data Protocol (GDP) Payloader and Depayloader
    elements added
  * Many other bug-fixes
* Fri Dec 29 2006 sbrabec@suse.cz
- Fixed schemas installation.
* Mon Dec 18 2006 sbrabec@suse.cz
- Prefix changed to /usr.
- Spec file cleanup.
* Tue Nov  7 2006 abockover@suse.de
- Updated to version 0.10.4:
  * Scores of bug fixes
  * Firewires/1394 support needs libiec61883 now
  * Lots of id3demux fixes including image support
  * Added apev2mux element
  * Added HAL elements
  * Support push-based FLAC decoding
* Tue Jun 20 2006 sbrabec@suse.cz
- Updated to version 0.10.3:
  * Annodex/CMML support
  * RTSP and RTP enhancements
  * HAL configured audio device support
  * FLAC, Matroska, AVI, WAV, ID3, APE, DV and JPEG plugin
    improvements
  * Recognise SSA/ASS and USF subtitles in Matroska files
  * Fixes for ESD and SunAudio output plugins
  * More uniform plugin descriptions
  * IceCast metadata reading plugin added
  * New plugins ported from 0.8: OSX audio, AVI muxer, X-Windows
    input, WAV encoder, Gdk-Pixbuf image decoder, Smoke decoder,
    Video colour balance
  * Lots of bug fixes
* Wed May 31 2006 hpj@suse.de
- Added backported ID3v2 muxer element, required for Banshee
  tagging. Fixes part of Novell bug #132801.
* Mon Apr 10 2006 jpr@suse.de
- Move some more plugins to and extras package
* Fri Apr  7 2006 jpr@suse.de
- Split out oil dependant plugins
* Thu Feb 23 2006 jpr@suse.de
- update to 0.10.2
- Changes since 0.10.1:
  * New libcdio based CDDA reading element
  * APE tag reader ported
  * ID3 tag reading fixes
  * Sun Audio Sink fixes
  * GOOM and gconf element fixes
  * lots of bug and leak fixes
  Bugs fixed since 0.10.1:
  * 328336 : silence warings which make dvdec / dvdemux unusable
  * 315557 : Internal event problem with MP3s from vgmix.com
  * 323327 : [cdio] port cddasrc to 0.10
  * 325148 : Bugs in G711 RTP packetization logic
  * 325649 : apetag plugin needs porting to 0.10
  * 326446 : check that all elements in -good pass queries they can't ...
  * 326602 : id3demux is not compiling without ZLIB
  * 326683 : build problem caused by AS_LIBTOOL_TAGS([CXX])
  * 326736 : gconf(audio|video)sink response to key changes
  * 326864 : [wavparse] time to bytes format conversion broken
  * 327009 : [esdsink] won't compile with includes in non-standard prefix
  * 327765 : [sunaudio] fixes for mixer and stuttering mp3 playback
  * 327825 : [matroskamux]  Matroska muxer deadlock
  * 327871 : [videobox] crash when cropping
  * 328241 : id3demux emits NULL date for year tags
  * 328264 : Fix build with gcc 2.95
  * 328531 : [matroskamux] doesn't send newsegment event, critical war...
  * 329181 : totem crash when using goom effect
  * 329810 : Fails to read ID3 tag
  * 330005 : Please use the autodetect sinks by default
  * 317658 : [cdio] support for cd-text and cd-g
* Tue Feb 14 2006 sbrabec@suse.cz
- Fixed Requires.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Jan 24 2006 ro@suse.de
- avoid gstreamer installation (-gstreamer in nfb)
* Wed Jan 18 2006 sbrabec@suse.cz
- Updated to version 0.10.1.
* Fri Jan  6 2006 sbrabec@suse.cz
- Removed obsolete configure option.
* Wed Jan  4 2006 sbrabec@suse.cz
- New SuSE package, version 0.10.0.
- Worked around -export-symbols-regex libtool problems.
