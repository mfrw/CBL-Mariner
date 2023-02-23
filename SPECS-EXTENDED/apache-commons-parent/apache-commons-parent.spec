Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

Name:           apache-commons-parent
Version:        52
Release:        6%{?dist}
Summary:        Apache Commons Parent Pom
License:        ASL 2.0
URL:            https://commons.apache.org/commons-parent-pom.html
BuildArch:      noarch

Source0:        https://github.com/apache/commons-parent/archive/rel/commons-parent-%{version}.tar.gz

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%endif

# Not generated automatically
%if %{without bootstrap}
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
%endif
Requires:       mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
The Project Object Model files for the apache-commons packages.

%prep
%setup -q -n commons-parent-rel-commons-parent-%{version}

# Plugin is not in fedora
%pom_remove_plugin org.apache.commons:commons-build-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-scm-publish-plugin

# Plugins useless in package builds
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin

# Remove profiles for plugins that are useless in package builds
for profile in animal-sniffer japicmp jacoco cobertura clirr; do
    %pom_xpath_remove "pom:profile[pom:id='$profile']"
done

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 52-6
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 52-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 52-3
- Bootstrap build
- Non-bootstrap build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Fabio Valentini <decathorpe@gmail.com> - 52-1
- Update to version 52.

* Fri Aug 21 2020 Marian Koncek <mkoncek@redhat.com> - 52-1
- Update to upstream version 52

* Tue Jul 28 2020 Marian Koncek <mkoncek@redhat.com> - 51-1
- Update to upstream version 51

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 47-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 47-5
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Marian Koncek <mkoncek@redhat.com> - 50-1
- Update to upstream version 50

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 47-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 49-2
- Mass rebuild for javapackages-tools 201902

* Wed Sep 18 2019 Marian Koncek <mkoncek@redhat.com> - 49-1
- Update to upstream version 49

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 48-2
- Mass rebuild for javapackages-tools 201901

* Fri May 03 2019 Marian Koncek <mkoncek@redhat.com> - 48-1
- Update to upstream version 48

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Marian Koncek <mkoncek@redhat.com> - 47-1
- Update to upstream version 47

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 43-1
- Update to upstream version 43

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 06 2017 Michael Simacek <msimacek@redhat.com> - 42-3
- Remove more useless plugins

* Thu Jan 05 2017 Michael Simacek <msimacek@redhat.com> - 42-2
- Remove profiles for plugins that are useless in package builds

* Mon Jan 02 2017 Michael Simacek <msimacek@redhat.com> - 42-1
- Update to upstream version 42

* Tue Jun 14 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 40-2
- Add missing dependency

* Wed May 11 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 40-1
- Update to upstream version 40

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep  8 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 39-1
- Update to upstream version 39

* Thu Jun 25 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 38-1
- Update to upstream version 38

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb  3 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 37-2
- Remove animal-sniffer profile

* Mon Feb  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 37-1
- Update to upstream version 37

* Mon Oct 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 35-1
- Update to upstream version 35

* Wed Jul 30 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 34-4
- Fix build-requires on apache-parent

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 34-2
- Rebuild to regenerate Maven auto-requires

* Thu Apr 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 34-1
- Update to upstream version 34

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 33-2
- Remove maven 3 profile

* Wed Feb 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 33-1
- Update to upstream version 33

* Tue Aug 06 2013 Mat Booth <fedora@matbooth.co.uk> - 32-2
- Remove use of maven-scm-publish-plugin plugin

* Tue Aug 06 2013 Mat Booth <fedora@matbooth.co.uk> - 32-1
- Updated to latest upstream, rhbz #904731

* Tue Aug 06 2013 Mat Booth <fedora@matbooth.co.uk> - 26-7
- Use pom macros instead of patching
- Update spec for latest guidelines rhbz #991975

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-5
- Add buildnumber-maven-plugin to R/BR

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-4
- Fix Requires and BuildRequires

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 26-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Oct 19 2012 Chris Spike <spike@fedoraproject.org> 22-4
- Updated to 26

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Alexander Kurtakov <akurtako@redhat.com> 22-2
- Add missing BR/R on buildbumber-maven-plugin.

* Wed Dec 7 2011 Alexander Kurtakov <akurtako@redhat.com> 22-1
- Update to latest upstream.

* Fri Apr 15 2011 Chris Spike <spike@fedoraproject.org> 20-1
- Updated to 20
- Fixed Rs for maven 3

* Sat Nov 6 2010 Chris Spike <spike@fedoraproject.org> 15-2
- Added patch to remove commons-build-plugin from pom file

* Wed Oct 20 2010 Chris Spike <spike@fedoraproject.org> 15-1
- Initial version of the package
