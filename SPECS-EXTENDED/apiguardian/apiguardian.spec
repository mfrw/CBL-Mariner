Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

Name:           apiguardian
Version:        1.1.2
Release:        3%{?dist}
Summary:        API Guardian Java annotation
License:        ASL 2.0
URL:            https://github.com/apiguardian-team/apiguardian
BuildArch:      noarch

Source0:        https://github.com/apiguardian-team/apiguardian/archive/r%{version}.tar.gz

Source100:      https://repo1.maven.org/maven2/org/apiguardian/apiguardian-api/%{version}/apiguardian-api-%{version}.pom

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%endif

%description
API Guardian indicates the status of an API element and therefore its
level of stability as well.  It is used to annotate public types,
methods, constructors, and fields within a framework or application in
order to publish their API status and level of stability and to
indicate how they are intended to be used by consumers of the API.

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
API documentation for %{name}.

%prep
%setup -q -n apiguardian-r%{version}
find -name \*.jar -delete
cp -p %{SOURCE100} pom.xml

# Inject OSGi manifest required by Eclipse
%pom_xpath_inject pom:project "
  <build>
    <pluginManagement>
      <plugins>
        <plugin>
          <artifactId>maven-jar-plugin</artifactId>
          <configuration>
            <archive>
              <manifestEntries>
                <Automatic-Module-Name>org.apiguardian.api</Automatic-Module-Name>
                <Implementation-Title>apiguardian-api</Implementation-Title>
                <Implementation-Vendor>apiguardian.org</Implementation-Vendor>
                <Implementation-Version>%{version}</Implementation-Version>
                <Specification-Title>apiguardian-api</Specification-Title>
                <Specification-Vendor>apiguardian.org</Specification-Vendor>
                <Specification-Version>%{version}</Specification-Version>
                <!-- OSGi metadata required by Eclipse -->
                <Bundle-ManifestVersion>2</Bundle-ManifestVersion>
                <Bundle-SymbolicName>org.apiguardian</Bundle-SymbolicName>
                <Bundle-Version>%{version}</Bundle-Version>
                <Export-Package>org.apiguardian.api;version=\"%{version}\"</Export-Package>
              </manifestEntries>
            </archive>
          </configuration>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>"

%build
%mvn_build -- -Dmaven.compiler.source=1.7 -Dmaven.compiler.target=1.7

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.1.2-3
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 02 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.2-1
- Update to upstream version 1.1.2
- Set explicit Java compiler source/target levels to 1.7

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-2
- Bootstrap build
- Non-bootstrap build

* Mon Feb 01 2021 Fabio Valentini <decathorpe@gmail.com> - 1.1.1-1
- Update to version 1.1.1.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Marian Koncek <mkoncek@redhat.com> - 1.1.1-1
- Update to upstream version 1.1.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.1.0-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.0-2
- Mass rebuild for javapackages-tools 201902

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Marian Koncek <mkoncek@redhat.com> - 1.1.0-1
- Update to upstream version 1.1.0

* Thu Jun 27 2019 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- Update to version 1.1.0.

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-5
- Mass rebuild for javapackages-tools 201901

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0-1
- Initial packaging
