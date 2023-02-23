Vendor:         Microsoft Corporation
Distribution:   Mariner
Name:           maven2
Version:        2.2.1
Release:        70%{?dist}
Summary:        Java project management and project comprehension tool
License:        ASL 2.0
URL:            http://maven.apache.org
BuildArch:      noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        generate-tarball.sh

Patch2:         %{name}-%{version}-update-tests.patch
Patch4:         %{name}-%{version}-unshade.patch
Patch5:         %{name}-%{version}-default-resolver-pool-size.patch
Patch6:         %{name}-%{version}-strip-jackrabbit-dep.patch
Patch8:         %{name}-%{version}-migrate-to-plexus-containers-container-default.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

Provides:       deprecated()

%description
Apache Maven is a software project management and comprehension tool.
Based on the concept of a project object model (POM), Maven can manage
a project's build, reporting and documentation from a central piece of
information.

%package -n maven-artifact
Summary:        Compatibility Maven artifact artifact
Provides:       deprecated()

%description -n maven-artifact
Maven artifact manager artifact

%package -n maven-artifact-manager
Summary:        Compatibility Maven artifact manager artifact
Provides:       deprecated()

%description -n maven-artifact-manager
Maven artifact manager artifact

%package -n maven-model
Summary:        Compatibility Maven model artifact
Provides:       deprecated()

%description -n maven-model
Maven model artifact

%package -n maven-monitor
Summary:        Compatibility Maven monitor artifact
Provides:       deprecated()

%description -n maven-monitor
Maven monitor artifact

%package -n maven-plugin-registry
Summary:        Compatibility Maven plugin registry artifact
Provides:       deprecated()

%description -n maven-plugin-registry
Maven plugin registry artifact

%package -n maven-profile
Summary:        Compatibility Maven profile artifact
Provides:       deprecated()

%description -n maven-profile
Maven profile artifact

%package -n maven-project
Summary:        Compatibility Maven project artifact
Provides:       deprecated()

%description -n maven-project
Maven project artifact

%package -n maven-settings
Summary:        Compatibility Maven settings artifact
Provides:       deprecated()

%description -n maven-settings
Maven settings artifact

%package -n maven-toolchain
Summary:        Compatibility Maven toolchain artifact
Provides:       deprecated()

%description -n maven-toolchain
Maven toolchain artifact

%package -n maven-plugin-descriptor
Summary:        Maven Plugin Description Model
Provides:       deprecated()

%description -n maven-plugin-descriptor
Maven plugin descriptor artifact

%package javadoc
Summary:        Javadoc for %{name}
Provides:       deprecated()

%description javadoc
Javadoc for %{name}.


%prep
%setup -q

%patch2 -b .update-tests

%patch4 -b .unshade

# disable parallel artifact resolution
%patch5 -p1 -b .parallel-artifacts-resolution

# remove unneeded jackrabbit dependency
%patch6 -p1 -b .strip-jackrabbit-dep

%patch8 -p1 -b .plexus-container

for nobuild in apache-maven maven-artifact-test \
               maven-compat maven-core maven-plugin-api \
               maven-plugin-parameter-documenter maven-reporting \
               maven-repository-metadata maven-script \
               maven-error-diagnostics; do
    %pom_disable_module $nobuild
done

# Don't install parent POM
%mvn_package :maven __noinstall

# Install all artifacts in Maven 3 directory.
%mvn_file ":{*}" maven/@1

# these parts are compatibility versions which are available in
# maven-3.x as well. We default to maven-3, but if someone asks for
# 2.x we provide few compat versions
%mvn_compat_version ":maven-{artifact,model,settings}" \
                    2.0.2 2.0.6 2.0.7 2.0.8 2.2.1

# Don't depend on backport-util-concurrent
%pom_remove_dep :backport-util-concurrent
%pom_remove_dep :backport-util-concurrent maven-artifact-manager
sed -i s/edu.emory.mathcs.backport.// `find -name DefaultArtifactResolver.java`

# Tests are skipped, so remove dependencies with scope 'test'.
for pom in $(grep -l ">test<" $(find -name pom.xml | grep -v /test/)); do
    %pom_xpath_remove "pom:dependency[pom:scope[text()='test']]" $pom
done

# Remove outdated maven-compiler-plugin configuration
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

%build
%mvn_build -f -s -- -P all-models -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -n maven-artifact -f .mfiles-maven-artifact
%license apache-maven/LICENSE.txt apache-maven/NOTICE.txt

%files -n maven-artifact-manager -f .mfiles-maven-artifact-manager
%license apache-maven/LICENSE.txt apache-maven/NOTICE.txt

%files -n maven-model -f .mfiles-maven-model
%license apache-maven/LICENSE.txt apache-maven/NOTICE.txt

%files -n maven-monitor -f .mfiles-maven-monitor
%license apache-maven/LICENSE.txt apache-maven/NOTICE.txt

%files -n maven-plugin-registry -f .mfiles-maven-plugin-registry
%license apache-maven/LICENSE.txt apache-maven/NOTICE.txt

%files -n maven-profile -f .mfiles-maven-profile
%license apache-maven/LICENSE.txt apache-maven/NOTICE.txt

%files -n maven-project -f .mfiles-maven-project
%license apache-maven/LICENSE.txt apache-maven/NOTICE.txt

%files -n maven-settings -f .mfiles-maven-settings
%license apache-maven/LICENSE.txt apache-maven/NOTICE.txt

%files -n maven-toolchain -f .mfiles-maven-toolchain
%license apache-maven/LICENSE.txt apache-maven/NOTICE.txt

%files -n maven-plugin-descriptor -f .mfiles-maven-plugin-descriptor
%license apache-maven/LICENSE.txt apache-maven/NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license apache-maven/LICENSE.txt apache-maven/NOTICE.txt


%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.2.1-70
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Fabio Valentini <decathorpe@gmail.com> - 2.2.1-65
- Override maven compiler source and target versions to fix build with Java 11.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.2.1-64
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-60
- Mark package as deprecated

* Mon Jul 23 2018 Michael Simacek <msimacek@redhat.com> - 2.2.1-59
- Repack tarball without bundled jars
- Fix license tag

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-54
- Add missing build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-51
- Remove maven-error-diagnostics subpackage
- Cleanup spec file

* Fri Oct 31 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-50
- Remove direct dependency on classworlds

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-48
- Add missing BR: modello

* Tue Sep 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-47
- Remove code related to bootstrapping
- Remove empty-dep JAR and POM
- Remove local depmap
- Use mfiles to simplify %%files sections
- Remove handling of custom settings.xml
- Build with XMvn

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 Michal Srb <msrb@redhat.com> - 2.2.1-45
- Add missing BR: maven-install-plugin (Resolves: #979504)
- Migrate to plexus-containers-container-default

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-44
- Don't depend on plexus-container-default
- Unset M2_HOME before calling mvn-rpmbuild
- Remove test dependencies

* Mon Mar 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-43
- Rebuild to generate mvn(*) versioned provides

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2.1-41
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Nov 23 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-40
- Add license to javadoc subpackage

* Thu Nov 22 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-39
- Add license and notice files to packages
- Add javadoc subpackage

* Fri Nov  9 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-38
- Don't depend on backport-util-concurrent

* Mon Aug 20 2012 Michel Salim <salimma@fedoraproject.org> - 2.2.1-37
- Provide compatibility versions for maven-artifact and -settings

* Thu Jul 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-36
- Remove mistaken epoch use in requires

* Wed Jul 25 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-35
- Move artifacts together with maven-3 files
- Provide compatibility versions for maven-model

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  9 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-33
- Completely remove main package since it was just confusing

* Wed Jan 25 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-32
- Stip down maven 2 to bare minimum
- Remove scripts and most of home

* Mon Jan 23 2012 Tomas Radej <tradej@redhat.com> - 2.2.1-31
- Fixed Requires for plugin-descriptor

* Mon Jan 23 2012 Tomas Radej <tradej@redhat.com> - 2.2.1-30
- Moved plugin-descriptor into subpackage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-28
- Provide mvn2 script instead of mvn (maven provides that now)

* Tue Jul 19 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-27
- Add maven-error-diagnostics subpackage
- Order subpackages according to alphabet

* Tue Jul 19 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-26
- Unown jars contained in subpackages (#723124)

* Mon Jun 27 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-25
- Add maven-toolchain subpackage

* Fri Jun 24 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-24
- Add few new subpackages
- Add several missing requires to new subpackages

* Fri Jun 24 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-23
- Split artifact-manager and project into subpackages
- Fix resolver to process poms and fragments from datadir
- No more need to update_maven_depmap after this update

* Mon Apr 18 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-22
- Fix jpp script to limit maven2.jpp.mode scope

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-20
- Add maven-artifact-test to installation

* Tue Jan 18 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-19
- Print plugin collector debug output only when maven2.jpp.debug mode is on

* Wed Dec 22 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-18
- Add xml-commons-apis to lib directory
- fixes NoClassDefFoundError org/w3c/dom/ElementTraversal

* Fri Dec 10 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-17
- Add conditional BRs to enable ff merge between f14 and f15
- Remove jackrabbit dependency from pom files

* Fri Dec 10 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-16
- Fix installation of pom files for artifact jars

* Mon Nov 22 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-15
- Add apache-commons-parent to BR/R
- Rename BRs from jakarta-commons to apache-commons

* Thu Nov 11 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-14
- Remove old depmaps from -depmap.xml file
- Fix argument quoting for mvn scripts (Resolves rhbz#647945)

* Mon Sep 20 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-13
- Create dangling symlinks during install (Resolves rhbz#613866)

* Fri Sep 17 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-12
- Update JPackageRepositoryLayout to handle "signature" packaging

* Mon Sep 13 2010 Yong Yang <yyang@redhat.com> 2.2.1-11
- Add -P all-models to generate maven model v3

* Wed Sep 1 2010 Alexander Kurtakov <akurtako@redhat.com> 2.2.1-10
- Remove buildnumber-maven-plugins deps now that is fixed.
- Use new package names in BR/R.
- Use global instead of define.

* Fri Aug 27 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-9
- Remove failing tests after maven-surefire 2.6 update

* Thu Aug 26 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-8
- Remove incorrect testcase failing with ant 1.8
- Cleanup whitespace

* Tue Jun 29 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-7
- Updated previous patch to only modify behaviour in JPP mode

* Mon Jun 28 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-6
- Disable parallel artifact resolution

* Wed Jun 23 2010 Yong Yang <yyang@redhat.com> 2.2.1-5
- Add Requires: maven-enforcer-plugin

* Fri Jun 18 2010 Deepak Bhole <dbhole@redhat.com> 2.2.1-4
- Final non-bootstrap build against non-bootstrap maven

* Fri Jun 18 2010 Deepak Bhole <dbhole@redhat.com> 2.2.1-3
- Added buildnumber plugin requirements
- Rebuild in non-bootstrap

* Thu Jun 17 2010 Deepak Bhole <dbhole@redhat.com> - 0:2.2.1-2
- Added support for dumping mapping info (in debug mode)
- Add a custom depmap
- Added empty-dep
- Added proper requirements
- Fixed classworlds jar name used at runtime
- Install individual components
- Install poms and mappings
- Remove non maven items from shaded uber jar
- Create dependency links in $M2_HOME/lib at install time

* Thu Nov 26 2009 Deepak Bhole <dbhole@redhat.com> - 0:2.2.1-1
- Initial bootstrap build
