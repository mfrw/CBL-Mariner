Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

Name:           plexus-components-pom
Version:        6.5
Release:        6%{?dist}
Summary:        Plexus Components POM
License:        ASL 2.0
URL:            https://github.com/codehaus-plexus/plexus-components
BuildArch:      noarch

Source0:        https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/%{version}/plexus-components-%{version}.pom
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
%endif

%description
This package provides Plexus Components parent POM used by different
Plexus packages.

%prep
%setup -qcT
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 6.5-6
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 6.5-3
- Bootstrap build
- Non-bootstrap build

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 6.5-1
- Update to upstream version 6.5

* Sat Oct 24 2020 Fabio Valentini <decathorpe@gmail.com> - 6.5-1
- Update to version 6.5.

* Fri Sep 11 2020 Marian Koncek <mkoncek@redhat.com> - 6.4-1
- Update to upstream version 6.4

* Sun Aug 16 2020 Fabio Valentini <decathorpe@gmail.com> - 6.4-1
- Update to version 6.4.

* Wed Jul 29 2020 Marian Koncek <mkoncek@redhat.com> - 6.3-1
- Update to upstream version 6.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Fabio Valentini <decathorpe@gmail.com> - 6.3-1
- Update to version 6.3.

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 6.1-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Feb 13 2020 Fabio Valentini <decathorpe@gmail.com> - 6.1-1
- Update to version 6.1.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.0-2
- Mass rebuild for javapackages-tools 201902

* Tue Aug 20 2019 Fabio Valentini <decathorpe@gmail.com> - 4.0-1
- Update to version 4.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Marian Koncek <mkoncek@redhat.com> - 4.0-1
- Update to upstream version 4.0

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-11
- Mass rebuild for javapackages-tools 201901

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-7
- Regenerate build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-4
- Update upstream URL

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-2
- Rebuild to regenerate Maven auto-requires

* Mon Mar 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-1
- Update to upstream version 1.3.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Dec  7 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-4
- Build with xmvn

* Tue Nov 13 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-3
- Add missing BR/R: plexus-pom

* Mon Nov 12 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-2
- Install LICENSE file

* Wed Oct 31 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-1
- Initial packaging
