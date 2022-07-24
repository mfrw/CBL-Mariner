Name:           gdk-pixbuf2-xlib
Version:        2.40.2
Release:        3%{?dist}
Summary:        Deprecated Xlib integration for gdk-pixbuf2

License:        LGPLv2+
URL:            https://gitlab.gnome.org/Archive/gdk-pixbuf-xlib
Source0:        https://download.gnome.org/sources/gdk-pixbuf-xlib/2.40/gdk-pixbuf-xlib-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(x11)

%description
gdk-pixbuf2-xlib contains the deprecated API for integrating gdk-pixbuf2 with
Xlib data types.

This library was originally shipped by gdk-pixbuf2, and has
since been moved out of the original repository.

No newly written code should ever use this library.

If your existing code depends on gdk-pixbuf2-xlib, then you're strongly
encouraged to port away from it.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n gdk-pixbuf-xlib-%{version}


%build
%meson -Dgtk_doc=false
%meson_build


%install
%meson_install


%files
%license COPYING
%doc README.md
%{_libdir}/libgdk_pixbuf_xlib-2.0.so.0*

%files devel
%{_includedir}/gdk-pixbuf-2.0/
%{_libdir}/libgdk_pixbuf_xlib-2.0.so
%{_libdir}/pkgconfig/gdk-pixbuf-xlib-2.0.pc
# %{_datadir}/gtk-doc/


%changelog
* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 17 2021 Kalev Lember <klember@redhat.com> - 2.40.2-2
- Use actual gdk-pixbuf2 package names in package description and summary

* Wed Feb 17 2021 Kalev Lember <klember@redhat.com> - 2.40.2-1
- Initial Fedora packaging, package split off from gdk-pixbuf2
