%global fontname cascadia
%global fontconf 60-%{fontname}-code-fonts.conf
%global fontconfmono 57-%{fontname}-mono-fonts.conf
%global fontconfmonopl 60-%{fontname}-mono-pl-fonts.conf
%global fontconfpl 60-%{fontname}-code-pl-fonts.conf

# We cannot build this from source until fontmake arrives in Fedora.
%global fromsource 0

Name:		%{fontname}-code-fonts
Summary:	A mono-spaced font designed for programming and terminal emulation
Version:	2111.01
Release:	2%{?dist}
License:	OFL
URL:		https://github.com/microsoft/cascadia-code/
Source0:	https://github.com/microsoft/cascadia-code/archive/v%{version}.tar.gz
Source1:	%{fontconf}
Source2:	%{fontname}-code.metainfo.xml
Source3:	%{fontconfmono}
Source4:	%{fontname}-mono.metainfo.xml
Source5:	%{fontconfmonopl}
Source6:	%{fontname}-mono-pl.metainfo.xml
Source7:	%{fontconfpl}
Source8:	%{fontname}-code-pl.metainfo.xml
%if 0%{?fromsource}
BuildRequires:	python3-fontmake
%else
Source20:	https://github.com/microsoft/cascadia-code/releases/download/v%{version}/CascadiaCode-%{version}.zip
%endif
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
Cascadia Code is a mono-spaced font designed to provide a fresh experience for
command line experiences and code editors. Notably, it supports programming
ligatures.

%package -n %{fontname}-mono-fonts
Summary:	A mono-spaced font family designed for terminal emulation

%description -n %{fontname}-mono-fonts
The Cascadia Mono font family is a variant of Cascadia Code, without
programming ligatures.

%package -n %{fontname}-mono-pl-fonts
Summary:	A mono-spaced font family with power line symbols

%description -n %{fontname}-mono-pl-fonts
The Cascadia Mono PL font family is a variant of Cascadia Code, without
programming ligatures, and with power line symbols.

%package -n %{fontname}-code-pl-fonts
Summary:	A mono-spaced font family with ligatures and power line symbols

%description -n %{fontname}-code-pl-fonts
The Cascadia Code PL font family is a variant of Cascadia Code, with power line
symbols.

%package -n %{fontname}-fonts-all
Summary:	A meta-package to enable easy installation of all Cascadia font families
Requires:	%{fontname}-code-fonts
Requires:	%{fontname}-code-pl-fonts
Requires:	%{fontname}-mono-fonts
Requires:	%{fontname}-mono-pl-fonts

%description -n %{fontname}-fonts-all
This is a meta-package which enables easy installation of all Cascadia font
families.

%prep
%setup -q -n %{fontname}-code-%{version}

# correct end-of-line encoding
for i in OFL-FAQ.txt FONTLOG.txt README.md; do
	sed -i 's/\r//' $i
done

%build

%if 0%{?fromsource}
python3 build.py
%else
unzip %{SOURCE20}
%endif

%install
install -m 0755 -d %{buildroot}%{_fontbasedir}/%{fontname}-code-fonts/
install -m 0755 -d %{buildroot}%{_fontbasedir}/%{fontname}-code-pl-fonts/
install -m 0755 -d %{buildroot}%{_fontbasedir}/%{fontname}-mono-fonts/
install -m 0755 -d %{buildroot}%{_fontbasedir}/%{fontname}-mono-pl-fonts/

install -m 0644 -p otf/static/CascadiaCode-*.otf %{buildroot}%{_fontbasedir}/%{fontname}-code-fonts/
install -m 0644 -p otf/static/CascadiaCodePL-*.otf %{buildroot}%{_fontbasedir}/%{fontname}-code-pl-fonts/
install -m 0644 -p otf/static/CascadiaMono-*.otf %{buildroot}%{_fontbasedir}/%{fontname}-mono-fonts/
install -m 0644 -p otf/static/CascadiaMonoPL-*.otf %{buildroot}%{_fontbasedir}/%{fontname}-mono-pl-fonts/

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/
install -m 0644 -p %{SOURCE3} %{buildroot}%{_fontconfig_templatedir}/
install -m 0644 -p %{SOURCE5} %{buildroot}%{_fontconfig_templatedir}/
install -m 0644 -p %{SOURCE7} %{buildroot}%{_fontconfig_templatedir}/

ln -s %{_fontconfig_templatedir}/%{fontconf} %{buildroot}%{_fontconfig_confdir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconfmono} %{buildroot}%{_fontconfig_confdir}/%{fontconfmono}
ln -s %{_fontconfig_templatedir}/%{fontconfmonopl} %{buildroot}%{_fontconfig_confdir}/%{fontconfmonopl}
ln -s %{_fontconfig_templatedir}/%{fontconfpl} %{buildroot}%{_fontconfig_confdir}/%{fontconfpl}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/appdata/%{fontname}-code.metainfo.xml
install -Dm 0644 -p %{SOURCE4} %{buildroot}%{_datadir}/appdata/%{fontname}-mono.metainfo.xml
install -Dm 0644 -p %{SOURCE6} %{buildroot}%{_datadir}/appdata/%{fontname}-mono-pl.metainfo.xml
install -Dm 0644 -p %{SOURCE8} %{buildroot}%{_datadir}/appdata/%{fontname}-code-pl.metainfo.xml

%files -n %{fontname}-code-fonts
%license LICENSE
%doc FONTLOG.txt OFL-FAQ.txt README.md
%{_datadir}/appdata/%{fontname}-code.metainfo.xml
%dir %{_fontbasedir}/%{fontname}-code-fonts/
%{_fontbasedir}/%{fontname}-code-fonts/*.otf
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}

%files -n %{fontname}-code-pl-fonts
%license LICENSE
%doc FONTLOG.txt OFL-FAQ.txt README.md
%{_datadir}/appdata/%{fontname}-code-pl.metainfo.xml
%dir %{_fontbasedir}/%{fontname}-code-pl-fonts/
%{_fontbasedir}/%{fontname}-code-pl-fonts/*.otf
%{_fontconfig_templatedir}/%{fontconfpl}
%config(noreplace) %{_fontconfig_confdir}/%{fontconfpl}

%files -n %{fontname}-mono-fonts
%license LICENSE
%doc FONTLOG.txt OFL-FAQ.txt README.md
%{_datadir}/appdata/%{fontname}-mono.metainfo.xml
%dir %{_fontbasedir}/%{fontname}-mono-fonts/
%{_fontbasedir}/%{fontname}-mono-fonts/*.otf
%{_fontconfig_templatedir}/%{fontconfmono}
%config(noreplace) %{_fontconfig_confdir}/%{fontconfmono}

%files -n %{fontname}-mono-pl-fonts
%license LICENSE
%doc FONTLOG.txt OFL-FAQ.txt README.md
%{_datadir}/appdata/%{fontname}-mono-pl.metainfo.xml
%dir %{_fontbasedir}/%{fontname}-mono-pl-fonts/
%{_fontbasedir}/%{fontname}-mono-pl-fonts/*.otf
%{_fontconfig_templatedir}/%{fontconfmonopl}
%config(noreplace) %{_fontconfig_confdir}/%{fontconfmonopl}

%files -n %{fontname}-fonts-all

%changelog
* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2111.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Tom Callaway <spot@fedoraproject.org> - 2111.01-1
- update 2111.01

* Thu Sep 16 2021 Tom Callaway <spot@fedoraproject.org> - 2108.26-1
- update 2108.26

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2106.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Tom Callaway <spot@fedoraproject.org> - 2106.17-1
- update to 2106.17

* Thu Jun  3 2021 Tom Callaway <spot@fedoraproject.org> - 2105.24-1
- update to 2105.24
- add Cascadia "Curve", Italic variants

* Mon Mar  1 2021 Tom Callaway <spot@fedoraproject.org> - 2102.25-1
- update to 2102.25

* Fri Feb 12 2021 Tom Callaway <spot@fedoraproject.org> - 2102.03-1
- update to 2102.03

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2009.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 24 2020 Tom Callaway <spot@fedoraproject.org> - 2009.22-1
- update to 2009.22

* Mon Sep 21 2020 Tom Callaway <spot@fedoraproject.org> - 2009.14-1
- update to 2009.14

* Wed Sep  2 2020 Tom Callaway <spot@fedoraproject.org> - 2008.25-1
- update to 2008.25

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2007.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  1 2020 Tom Callaway <spot@fedoraproject.org> - 2007.01-1
- update to 2007.01

* Mon May 18 2020 Tom Callaway <spot@fedoraproject.org> - 2005.15-1
- update to 2005.15
- package OTF files instead of TTF files

* Tue Mar 17 2020 Tom Callaway <spot@fedoraproject.org> - 1911.21-3
- make subpackages for all font families
- make meta-package (cascade-fonts-all)
- eliminate use of deprecated macros

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1911.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec  3 2019 Tom Callaway <spot@fedoraproject.org> - 1911.21-1
- update to 1911.21

* Wed Nov 13 2019 Tom Callaway <spot@fedoraproject.org> - 1910.04-1
- update to 1910.04

* Thu Sep 19 2019 Tom Callaway <spot@fedoraproject.org> - 1909.16-1
- initial package
