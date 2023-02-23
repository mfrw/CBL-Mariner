Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

%global bundle org.apache.felix.utils

Name:           felix-utils
Version:        1.11.6
Release:        5%{?dist}
Summary:        Utility classes for OSGi
License:        ASL 2.0
URL:            https://felix.apache.org
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/felix/%{bundle}/%{version}/%{bundle}-%{version}-source-release.tar.gz

# The module org.osgi.cmpn requires implementing methods which were not
# implemented in previous versions where org.osgi.compendium was used
Patch0:         0000-Port-to-osgi-cmpn.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
%endif

%description
Utility classes for OSGi

%package javadoc
Summary:          API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}
%patch0 -p1

%pom_remove_parent
%pom_xpath_inject pom:project "<groupId>org.apache.felix</groupId>"
%pom_remove_plugin :apache-rat-plugin

%mvn_file :%{bundle} "felix/%{bundle}"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE
%doc DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.11.6-5
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.11.6-2
- Bootstrap build
- Non-bootstrap build

* Tue Feb 02 2021 Fabio Valentini <decathorpe@gmail.com> - 1.11.6-1
- Update to version 1.11.6.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Marian Koncek <mkoncek@redhat.com> - 1.11.6-1
- Update to upstream version 1.11.6

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.11.4-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Mar 02 2020 Fabio Valentini <decathorpe@gmail.com> - 1.11.4-1
- Update to version 1.11.4.

* Wed Jan 29 2020 Marian Koncek <mkoncek@redhat.com> - 1.11.4-1
- Update to upstream version 1.11.4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.11.2-2
- Mass rebuild for javapackages-tools 201902

* Sun Aug 18 2019 Fabio Valentini <decathorpe@gmail.com> - 1.11.2-1
- Update to version 1.11.2.

* Sun Aug 18 2019 Fabio Valentini <decathorpe@gmail.com> - 1.11.0-1
- Update to version 1.11.0.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Marian Koncek <mkoncek@redhat.com> - 1.11.2-1
- Update to upstream version 1.11.2

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.11.0-2
- Mass rebuild for javapackages-tools 201901

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Marian Koncek <mkoncek@redhat.com> - 1.11.0-1
- Update to upstream version 1.11.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Michael Simacek <msimacek@redhat.com> - 1.10.4-1
- Update to upstream version 1.10.4

* Tue Sep 12 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.10.2-1
- Update to upstream version 1.10.2

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 02 2017 Roman Vais <rvais@redhat.com> - 1.10.0-1
- Update to upstream version 1.10.0

* Wed Mar 29 2017 Michael Simacek <msimacek@redhat.com> - 1.9.0-1
- Update to upstream version 1.9.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Michael Simacek <msimacek@redhat.com> - 1.8.6-1
- Update to upstream version 1.8.6

* Thu Oct 13 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.2-4
- Remove build-dependency on maven-source-plugin

* Thu Jun 16 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.2-3
- Regenerate build-requires
- Update to current packaging guidelines

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Michael Simacek <msimacek@redhat.com> - 1.8.2-1
- Update to upstream version 1.8.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 12 2015 Michael Simacek <msimacek@redhat.com> - 1.8.0-1
- Update to upstream version 1.8.0

* Tue Jan 27 2015 Michael Simacek <msimacek@redhat.com> - 1.6.0-1
- Update to upstream version 1.6.0

* Tue Jan 27 2015 Mat Booth <mat.booth@redhat.com> - 1.4.0-1
- Update to upstream 1.4.0 release
- Re-enable tests

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-8
- Add build-requires on mockito

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Michal Srb <msrb@redhat.com> - 1.2.0-6
- Update BR

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-5
- Remove BuildRequires on maven-surefire-provider-junit4

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.0-4
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 05 2013 Mat Booth <fedora@matbooth.co.uk> - 1.2.0-3
- Update for latest guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 17 2013 Mat Booth <fedora@matbooth.co.uk> - 1.2.0-1
- Update to latest upstream version rhbz #892553.
- Drop patch, use preferred %%pom_* macros instead.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1.0-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 03 2013 Jaromir Capik <jcapik@redhat.com> - 1.1.0-7
- Changing target from jsr14 to 1.5 (#842593)

* Tue Sep  4 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.0-6
- Install NOTICE with javadoc pakcage

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 13 2011 Jaromir Capik <jcapik@redhat.com> - 1.1.0-3
- osgi.org groupId patch removed (fixed in felix-osgi-* packages)

* Thu Sep 08 2011 Jaromir Capik <jcapik@redhat.com> - 1.1.0-2
- Moved to felix subdir
- Minor spec file changes

* Wed Jul 13 2011 Jaromir Capik <jcapik@redhat.com> - 1.1.0-1
- Initial version
