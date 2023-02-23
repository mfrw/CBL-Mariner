Vendor:         Microsoft Corporation
Distribution:   Mariner
%global build_javadoc 0

Name:     mariadb-java-client
Version:  3.0.5
Release:  1%{?dist}
Summary:  Connects applications developed in Java to MariaDB and MySQL databases
# added BSD license because of https://bugzilla.redhat.com/show_bug.cgi?id=1291558#c13
License:  BSD and LGPLv2+
URL:      https://mariadb.com/kb/en/mariadb/about-mariadb-connector-j/
Source0:  https://github.com/mariadb-corporation/mariadb-connector-j/archive/refs/tags/%{version}.tar.gz#/mariadb-connector-j-%{version}.tar.gz
# optional dependency not in Fedora
Patch0:   remove_waffle-jna.patch

BuildArch:	noarch
BuildRequires:	maven-local
BuildRequires:	mvn(net.java.dev.jna:jna)
BuildRequires:	mvn(net.java.dev.jna:jna-platform)
BuildRequires:	mvn(com.google.code.maven-replacer-plugin:replacer)
# fedora 25
BuildRequires:	mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:	mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
# Since version 2.4.0
# removing coverage test because of dependencies
#BuildRequires:	mvn(org.jacoco:jacoco-maven-plugin)
# since version 1.5.2 missing optional dependency (windows)
#BuildRequires:	mvn(com.github.dblock.waffle:waffle-jna)

%if %build_javadoc == 0
Obsoletes:     %{name}-javadoc < 3.0.3
%endif

%description
MariaDB Connector/J is a Type 4 JDBC driver, also known as the Direct to
Database Pure Java Driver. It was developed specifically as a lightweight
JDBC connector for use with MySQL and MariaDB database servers.

%if %build_javadoc
%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.
%endif

%prep
%setup -qn mariadb-connector-j-%{version}

# remove missing optional dependency waffle-jna
%pom_remove_dep com.github.waffle:waffle-jna
%pom_remove_dep ch.qos.logback:logback-classic
%pom_remove_dep software.amazon.awssdk:bom
%pom_remove_dep software.amazon.awssdk:rds
%pom_remove_dep org.junit:junit-bom
%pom_remove_dep org.junit.jupiter:junit-jupiter-engine
%pom_remove_dep org.slf4j:slf4j-api
# used in buildtime for generating OSGI metadata
%pom_remove_plugin biz.aQute.bnd:bnd-maven-plugin

%pom_add_dep net.java.dev.jna:jna
%pom_add_dep net.java.dev.jna:jna-platform
# add slf4j dep again, this time not dependent on any specific version
%pom_add_dep org.slf4j:slf4j-api

# use latest OSGi implementation
%pom_change_dep -r :org.osgi.core org.osgi:osgi.core
%pom_change_dep -r :org.osgi.compendium org.osgi:osgi.cmpn

rm -r src/main/java/org/mariadb/jdbc/plugin/credential/aws
# removing dependencies and 'provides', which mariadb-java-client cannot process from module-info.java
sed -i '/aws/d' src/main/java9/module-info.java
sed -i '/waffle/d' src/main/java9/module-info.java
# removing missing dependencies form META-INF, so that the mariadb-java-client module would be valid
sed -i '/aws/d' src/main/resources/META-INF/services/org.mariadb.jdbc.plugin.CredentialPlugin
sed -i '/aws/d' src/test/resources/META-INF/services/org.mariadb.jdbc.plugin.CredentialPlugin


# also remove the file using the removed plugin
rm -f src/main/java/org/mariadb/jdbc/plugin/authentication/addon/gssapi/WindowsNativeSspiAuthentication.java
# patch the sources so that the missing file is not making trouble
%patch0 -p1

%mvn_file org.mariadb.jdbc:%{name} %{name}
%mvn_alias org.mariadb.jdbc:%{name} mariadb:mariadb-connector-java

%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin com.coveo:fmt-maven-plugin
%pom_remove_plugin -r :maven-gpg-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%build
%if %build_javadoc == 0
opts="-j"
%endif
# tests are skipped, while they require running application server
%mvn_build -f $opts

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%if %build_javadoc
%files javadoc -f .mfiles-javadoc
%license LICENSE
%endif

%changelog
* Thu May 26 2022 Zuzana Miklankova <zmiklank@redhat.com> - 3.0.5-1
- Rebase to version 3.0.5

* Mon Mar 28 2022 Zuzana Miklankova <zmiklank@redhat.com> - 3.0.4-1
- Rebase to version 3.0.4

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.0.3-3
- Rebuilt for java-17-openjdk as system jdk

* Mon Jan 31 2022 Zuzana Miklankova <zmiklank@redhat.com> - 3.0.3-2
- Disable javadoc build, because xmvn is not able to build it

* Thu Jan 27 2022 Zuzana Miklankova <zmiklank@redhat.com> - 3.0.3-1
- Rebase to version 3.0.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 18 2021 Ondrej Dubaj <odubaj@redhat.com> - 3.0.1-1
- Rebase to version 3.0.1

* Fri Jul 23 2021 Ondrej Dubaj <odubaj@redhat.com> - 3.0.0-1
- Rebase to version 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 09 2021 Ondrej Dubaj <odubaj@redhat.com> - 2.7.3-1
- Rebase to version 2.7.3

* Wed May 12 2021 Ondrej Dubaj <odubaj@redhat.com> - 2.7.2-2
- Remove maven-javadoc-plugin dependency

* Wed May 05 2021 Ondrej Dubaj <odubaj@redhat.com> - 2.7.2-1
- Rebase to version 2.7.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Ondrej Dubaj <odubaj@redhat.com> - 2.7.1-1
- Rebase to version 2.7.1 (#1906291)

* Fri Sep 25 2020 Ondrej Dubaj <odubaj@redhat.com> - 2.7.0-1
- Rebase to version 2.7.0 (#1882558)

* Sun Aug 30 2020 Fabio Valentini <decathorpe@gmail.com> - 2.6.2-2
- Remove unnecessary dependency on sonatype-oss-parent.

* Wed Aug 19 2020 Ondrej Dubaj <odubaj@redhat.com> - 2.6.2-1
- Rebase to version 2.6.2 (#1860212)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 2.6.1-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jun 24 2020 Ondrej Dubaj <odubaj@redhat.com> - 2.6.1-1
- Rebase to version 2.6.1 (#1850111)

* Mon Mar 30 2020 Michal Schorm <mschorm@redhat.com> - 2.6.0-2
- Remove the dependency on mariadb (#1818814)

* Mon Mar 23 2020 Ondrej Dubaj <odubaj@redhat.com> - 2.6.0-1
- Rebase to version 2.6.0 (#1815696)

* Thu Feb 20 2020 Ondrej Dubaj <odubaj@redhat.com> - 2.5.4-1
- Rebase to version 2.5.4 (#1752069)

* Wed Feb 19 2020 Ondrej Dubaj <odubaj@redhat.com> - 2.4.3-3
- Resolved FTBFS (#1799633)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Michal Schorm <mschorm@redhat.com> - 2.4.3-1
- Rebase to version 2.4.3

* Tue Sep 10 2019 Michal Schorm <mschorm@redhat.com> - 2.4.1-3
- Remove dependency to orphaned HikariCP

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Jakub Janco <jjanco@redhat.com> - 2.4.1-1
- new version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Jakub Janco <jjanco@redhat.com> - 2.4.0-1
- new version

* Mon Nov 26 2018 Jakub Janco <jjanco@redhat.com> - 2.3.0-1
- new version

* Tue Aug 07 2018 Jakub Janco <jjanco@redhat.com> - 2.2.6-1
- new version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 04 2018 Jakub Janco <jjanco@redhat.com> - 2.2.5-1
- new version

* Tue May 15 2018 Jakub Janco <jjanco@redhat.com> - 2.2.4-3
- remove unused aws-java-sdk dependency

* Sat May 05 2018 Jakub Janco <jjanco@redhat.com> - 2.2.4-2
- Refactor pom, add tests package

* Sat May 05 2018 Jakub Janco <jjanco@redhat.com> - 2.2.4-1
- new version

* Tue Mar 13 2018 Jakub Janco <jjanco@redhat.com> - 2.2.3-1
- update version

* Mon Feb 26 2018 Jakub Janco <jjanco@redhat.com> - 2.2.2-1
- update version

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Jakub Janco <jjanco@redhat.com> - 2.2.1-1
- Update to 2.2.1

* Tue Nov 21 2017 Jakub Janco <jjanco@redhat.com> - 2.2.0-1
- Update to 2.2.0

* Tue Aug 29 2017 Tomas Repik <trepik@redhat.com> - 2.1.0-1
- Update to 2.1.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Tomas Repik <trepik@redhat.com> - 2.0.2-1
- version update

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Tomas Repik <trepik@redhat.com> - 1.5.5-1
- version update

* Mon Oct 03 2016 Tomas Repik <trepik@redhat.com> - 1.5.3-1
- version update

* Wed Sep 14 2016 Tomas Repik <trepik@redhat.com> - 1.5.2-1
- version update

* Tue Jun 21 2016 Tomas Repik <trepik@redhat.com> - 1.4.6-1
- version update

* Mon Apr 18 2016 Tomas Repik <trepik@redhat.com> - 1.4.2-1
- version update

* Wed Mar 23 2016 Tomas Repik <trepik@redhat.com> - 1.3.7-1
- version update
- BSD license added
- cosmetic updates in prep phase

* Thu Mar 10 2016 Tomas Repik <trepik@redhat.com> - 1.3.6-1
- version update

* Mon Feb 15 2016 Tomas Repik <trepik@redhat.com> - 1.3.5-1
- version update

* Wed Jan 20 2016 Tomáš Repík <trepik@redhat.com> - 1.3.3-3
- generating OSGi manifest file with maven-bundle-plugin

* Wed Dec 16 2015 Tomáš Repík <trepik@redhat.com> - 1.3.3-2
- installing LICENSE added
- conversion from dos to unix line encoding revised
- unnecessary tasks removed

* Wed Dec  9 2015 Tomáš Repík <trepik@redhat.com> - 1.3.3-1
- Initial package
