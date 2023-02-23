Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_without httpclient
%bcond_without oro
%bcond_with vfs
%bcond_without sftp

%global jarname ivy

Name:           apache-%{jarname}
Version:        2.5.0
Release:        10%{?dist}
Summary:        Java-based dependency manager
License:        ASL 2.0
URL:            https://ant.apache.org/ivy
BuildArch:      noarch

Source0:        https://archive.apache.org/dist/ant/%{jarname}/%{version}/%{name}-%{version}-src.tar.gz
Source1:        https://archive.apache.org/dist/ant/%{jarname}/%{version}/%{name}-%{version}-src.tar.gz.asc
Source2:        https://archive.apache.org/dist/ant/KEYS
Source3:        https://repo1.maven.org/maven2/org/apache/ivy/%{jarname}/%{version}/%{jarname}-%{version}.pom

# Non-upstreamable.  Add /etc/ivy/ivysettings.xml at the end list of
# settings files Ivy tries to load.  This file will be used only as
# last resort, when no other setting files exist.
Patch0:         00-global-settings.patch

BuildRequires:  gnupg2
BuildRequires:  maven-local-openjdk11
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15on)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on)

%if %{with httpclient}
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
%endif

%if %{with oro}
BuildRequires:  mvn(oro:oro)
%endif

%if %{with vfs}
BuildRequires:  mvn(org.apache.commons:commons-vfs2)
%endif

%if %{with sftp}
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.jcraft:jsch.agentproxy.connector-factory)
BuildRequires:  mvn(com.jcraft:jsch.agentproxy.jsch)
%endif

Provides:       ivy = %{version}-%{release}

%description
Apache Ivy is a tool for managing (recording, tracking, resolving and
reporting) project dependencies.  It is designed as process agnostic and is
not tied to any methodology or structure. while available as a standalone
tool, Apache Ivy works particularly well with Apache Ant providing a number
of powerful Ant tasks ranging from dependency resolution to dependency
reporting and publication.

%{?javadoc_package}

%prep

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -p1

# Don't hardcode sysconfdir path
sed -i 's:/etc/ivy/:%{_sysconfdir}/ivy/:' src/java/org/apache/ivy/ant/IvyAntSettings.java

find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

cp %{SOURCE3} pom.xml

%pom_remove_parent

# apparently this is not a dependency, reporting upstream
%pom_remove_dep :jsch.agentproxy

%if %{without httpclient}
%pom_remove_dep :httpclient
rm src/java/org/apache/ivy/util/url/HttpClientHandler.java
%endif

%if %{without oro}
%pom_remove_dep :oro
rm src/java/org/apache/ivy/plugins/matcher/GlobPatternMatcher.java
%endif

%if %{without vfs}
%pom_remove_dep :commons-vfs2
rm src/java/org/apache/ivy/plugins/repository/vfs/VfsRepository.java
rm src/java/org/apache/ivy/plugins/repository/vfs/VfsResource.java
rm src/java/org/apache/ivy/plugins/repository/vfs/ivy_vfs.xml
rm src/java/org/apache/ivy/plugins/resolver/VfsResolver.java
%endif

%if %{without sftp}
%pom_remove_dep :jsch
%pom_remove_dep :jsch.agentproxy
%pom_remove_dep :jsch.agentproxy.connector-factory
%pom_remove_dep :jsch.agentproxy.jsch
rm src/java/org/apache/ivy/plugins/repository/sftp/SFTPRepository.java
rm src/java/org/apache/ivy/plugins/repository/sftp/SFTPResource.java
rm src/java/org/apache/ivy/plugins/repository/ssh/AbstractSshBasedRepository.java
rm src/java/org/apache/ivy/plugins/repository/ssh/RemoteScpException.java
rm src/java/org/apache/ivy/plugins/repository/ssh/Scp.java
rm src/java/org/apache/ivy/plugins/repository/ssh/SshCache.java
rm src/java/org/apache/ivy/plugins/repository/ssh/SshRepository.java
rm src/java/org/apache/ivy/plugins/repository/ssh/SshResource.java
rm src/java/org/apache/ivy/plugins/resolver/AbstractSshBasedResolver.java
rm src/java/org/apache/ivy/plugins/resolver/SFTPResolver.java
rm src/java/org/apache/ivy/plugins/resolver/SshResolver.java
%endif

%pom_xpath_inject pom:project '
<build>
  <sourceDirectory>src/java</sourceDirectory>
  <resources>
    <resource>
      <directory>src/java</directory>
      <includes>
        <include>**/*.css</include>
        <include>**/*.ent</include>
        <include>**/*.png</include>
        <include>**/*.properties</include>
        <include>**/*.template</include>
        <include>**/*.xml</include>
        <include>**/*.xsd</include>
        <include>**/*.xsl</include>
      </includes>
      <excludes>
        <exclude>**/*.java</exclude>
      </excludes>
    </resource>
  </resources>
</build>'

%pom_add_plugin :maven-antrun-plugin '
<executions>
  <execution>
    <id>compile</id>
    <phase>compile</phase>
    <goals>
      <goal>run</goal>
    </goals>
    <configuration>
      <target>
        <!-- copy licenses -->
        <copy file="${project.basedir}/NOTICE" 
          tofile="${project.build.outputDirectory}/META-INF/NOTICE"/> 
        <copy file="${project.basedir}/LICENSE" 
          tofile="${project.build.outputDirectory}/META-INF/LICENSE"/> 

        <!-- copy settings files for backward compatibility with ivyconf naming -->
        <copy file="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivysettings-local.xml" 
          tofile="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivyconf-local.xml"/> 
        <copy file="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivysettings-default-chain.xml" 
          tofile="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivyconf-default-chain.xml"/> 
        <copy file="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivysettings-main-chain.xml" 
          tofile="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivyconf-main-chain.xml"/> 
        <copy file="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivysettings-public.xml" 
          tofile="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivyconf-public.xml"/> 
        <copy file="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivysettings-shared.xml" 
          tofile="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivyconf-shared.xml"/> 
        <copy file="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivysettings.xml" 
          tofile="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivyconf.xml"/> 

        <!-- copy antlib for backward compatibility with fr.jayasoft.ivy package -->
        <copy file="${project.build.outputDirectory}/org/apache/ivy/ant/antlib.xml"
          todir="${project.build.outputDirectory}/fr/jayasoft/ivy/ant"/>

        <!--
          there is a default Bundle-Version attribute in the source MANIFEST, used to ease
          development in eclipse.
          We remove this line to make sure we get the Bundle-Version as set in the jar task
        -->
        <copy file="${project.basedir}/META-INF/MANIFEST.MF" tofile="${project.build.outputDirectory}/META-INF/MANIFEST.MF">
          <filterchain>
            <replaceregex pattern="Bundle-Version:.*" replace="Bundle-Version: ${project.version}" byline="true"/>
            <replaceregex pattern="Bundle-RequiredExecutionEnvironment:.*" replace="Bundle-RequiredExecutionEnvironment: ${java.version} (${java.vendor})" byline="true"/>
          </filterchain>
        </copy>
      </target>
    </configuration>
  </execution>
</executions>'

%pom_add_plugin :maven-jar-plugin '
<configuration>
  <archive>
    <manifestEntries>
      <Specification-Title>Apache Ivy with Ant tasks</Specification-Title>
      <Specification-Version>${project.version}</Specification-Version>
      <Specification-Vendor>Apache Software Foundation</Specification-Vendor>
      <Implementation-Title>${project.groupId}</Implementation-Title>
      <Implementation-Version>${project.version}</Implementation-Version>
      <Implementation-Vendor>Apache Software Foundation</Implementation-Vendor>
      <Implementation-Vendor-Id>org.apache</Implementation-Vendor-Id>
      <Extension-name>${project.groupId}</Extension-name>
      <Build-Version>${project.version}</Build-Version>
    </manifestEntries>
    <manifestFile>${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>'

%mvn_alias : jayasoft:ivy
%mvn_file : %{name}/ivy ivy

# Remove prebuilt documentation
rm -rf asciidoc

%build
export JAVA_HOME=%{_jvmdir}/java-11
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "apache-ivy/ivy" > %{buildroot}%{_sysconfdir}/ant.d/%{name}

%files -f .mfiles
%license LICENSE NOTICE
%doc README.adoc
%{_sysconfdir}/ant.d/%{name}

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.5.0-10
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 2.5.0-8
- Enable ssh support

* Wed Dec 01 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 2.5.0-7
- Change BR: maven-local-openjdk11

* Wed Nov 17 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 2.5.0-6
- Re-add global settings

* Sat Oct 02 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 2.5.0-5
- Enable httpclient and oro

* Fri Oct 01 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 2.5.0-4
- Fix FTBFS (Resolves: #1987365)
- Rebuild with maven

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 13 2020 Fabio Valentini <decathorpe@gmail.com> - 2.5.0-1
- Update to version 2.5.0.
- Disable running the very very broken test suite.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.4.0-22
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-21
- bumped minimal sources/target to 1.6
- changed javadoc to palceholder. The javadoc build fails, but it looks like it is not affecting thebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.0-19
- Drop unnecessary dependencies on parent POMs.

* Wed Aug 14 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.0-18
- Disable ssh, bouncycastle, and vfs support.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Marian Koncek <mkoncek@redhat.com> - 2.4.0-15
- Enabled tests during build and disabled few failing tests
- Resolves: rhbz#1055418

* Tue Jul 17 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.0-14
- Allow building without vfs support

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 28 2018 Michael Simacek <msimacek@redhat.com> - 2.4.0-12
- Remove now unneeded patch

* Fri Mar 16 2018 Michael Simacek <msimacek@redhat.com> - 2.4.0-11
- Fix build against ant 1.10.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar  1 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.0-8
- Don't hardcode sysconfdir path

* Tue Feb 14 2017 Michael Simacek <msimacek@redhat.com> - 2.4.0-7
- Add conditional for bouncycastle

* Mon Feb 06 2017 Michael Simacek <msimacek@redhat.com> - 2.4.0-6
- Add conditional for ssh

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Michal Srb <msrb@redhat.com> - 2.4.0-3
- Update comment

* Mon May 04 2015 Michal Srb <msrb@redhat.com> - 2.4.0-2
- Port to bouncycastle 1.52

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.0-1
- Update to upstream version 2.4.0

* Fri Sep 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-17
- Add compat symlink for ivy.jar

* Mon Aug 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-16
- Add alias for jayasoft:ivy

* Thu Jun 26 2014 Michal Srb <msrb@redhat.com> - 2.3.0-15
- Drop workaround for broken apache-ivy

* Thu Jun 26 2014 Michal Srb <msrb@redhat.com> - 2.3.0-14
- Fix /etc/ant.d/apache-ivy (Resolves: rhbz#1113275)

* Mon Jun 23 2014 Michal Srb <msrb@redhat.com> - 2.3.0-13
- Add BR on missing parent POMs

* Mon Jun 09 2014 Michal Srb <msrb@redhat.com> - 2.3.0-12
- Add missing BR: apache-commons-lang

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-10
- Use features of XMvn 2.0.0

* Thu Jan 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-9
- BuildRequire ivy-local >= 3.5.0-2

* Thu Jan 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-8
- Build with ivy-local
- Add patch for global settings

* Thu Jan 02 2014 Michal Srb <msrb@redhat.com> - 2.3.0-7
- Remove prebuilt documentation in %%prep
- Install NOTICE file with javadoc subpackage

* Thu Jan 02 2014 Michal Srb <msrb@redhat.com> - 2.3.0-6
- Restore PGP signing ability
- Remove unneeded R

* Thu Dec 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-5
- Enable VFS resolver

* Wed Dec  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-4
- Install POM files, resolves: rhbz#1032258
- Remove explicit requires; auto-requires are in effect now

* Fri Nov  1 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-3
- Add Maven depmap

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 1 2013 Alexander Kurtakov <akurtako@redhat.com> 2.3.0-1
- Update to latest upstream.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 31 2012 Alexander Kurtakov <akurtako@redhat.com> 2.2.0-5
- Fix osgi metadata.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 6 2011 Alexander Kurtakov <akurtako@redhat.com> 2.2.0-2
- Fix ant integration.

* Fri Feb 25 2011 Alexander Kurtakov <akurtako@redhat.com> 2.2.0-1
- Update to 2.2.0.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 09 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.1.0-1
- Initial Fedora packaging
