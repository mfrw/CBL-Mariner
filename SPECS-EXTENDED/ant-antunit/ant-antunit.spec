Vendor:         Microsoft Corporation
Distribution:   Mariner
Name:           ant-antunit
Version:        1.4.1
Release:        3%{?dist}
Summary:        Unit Test Framework for Ant Tasks
License:        ASL 2.0
URL:            https://ant.apache.org/antlibs/antunit
BuildArch:      noarch

Source0:        https://archive.apache.org/dist/ant/antlibs/antunit/source/apache-%{name}-%{version}-src.tar.bz2
Source1:        https://archive.apache.org/dist/ant/antlibs/antunit/source/apache-%{name}-%{version}-src.tar.bz2.asc
Source2:        https://archive.apache.org/dist/ant/KEYS

BuildRequires:  gnupg2
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-testutil)

%description
This library contains tasks that enables Ant task developers to test their tasks
with Ant and without JUnit.  It contains a few assertion tasks and an antunit
task that runs build files instead of test classes and is modelled after the
JUnit task.

%{?javadoc_package}

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -n apache-%{name}-%{version}

find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

mv %{name}-%{version}.pom pom.xml

%pom_xpath_inject pom:project/pom:build '
    <resources>
      <resource>
        <directory>${project.basedir}/src/main</directory>
        <includes>
          <include>**/antlib.xml</include>
        </includes>
      </resource>
    </resources>'

# EatYourOwnDogFoodTest
sed -i 's|build/test-classes|target/test-classes|g' src/etc/testcases/antunit/java-io.xml

# AssertTest
sed -i 's|build/classes|target/classes|g' src/etc/testcases/assert.xml src/tests/junit/org/apache/ant/antunit/AssertTest.java

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%check
# enable tests
%pom_xpath_set pom:maven.test.skip false

# compile tests
xmvn test-compile -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

# run tests
java -cp target/classes:target/test-classes:$(build-classpath junit hamcrest ant/ant-testutil ant ant/ant-launcher) \
       org.junit.runner.JUnitCore \
       $(find src/tests/junit/ -name '*.java' -printf '%%P\n' | cut -f 1 -d '.' | tr / .)

%install
%mvn_install

%files -f .mfiles
%license common/LICENSE NOTICE

%changelog
* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.4.1-2
- Swap the order of autosetup and gpgverify
- Enable tests

* Thu Sep 16 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.4.1-1
- Rebuild with new spec

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
 
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
 
* Sun Jul 12 2020 Orion Poplawski <orion@nwra.com> - 1.4-1
- Update to 1.4
 
* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.3-14
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11
 
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
 
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
 
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
 
* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
 
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
 
* Wed Aug 23 2017 Mat Booth <mat.booth@redhat.com> - 1.3-8
- Fix failure to build from source
 
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
 
* Tue Mar 28 2017 Orion Poplawski <orion@cora.nwra.com> 1.3-6
- BR ant
 
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
 
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
 
* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
 
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
 
* Thu May 22 2014 Orion Poplawski <orion@cora.nwra.com> 1.3-1
- Update to 1.3
 
* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2-13
- Use Requires: java-headless rebuild (#1067528)
 
* Thu Aug 15 2013 Orion Poplawski <orion@cora.nwra.com> 1.2-12
- Another attempt at fixing the install
 
* Thu Aug 15 2013 Orion Poplawski <orion@cora.nwra.com> 1.2-11
- Fix install locations (bug 988561)
 
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
 
* Wed Jul 17 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-9
- Update to current packaging guidelines
 
* Wed Jun 12 2013 Orion Poplawski <orion@cora.nwra.com> 1.2-7
- Update spec for new Java guidelines
 
* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
 
* Tue Jan 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-5
- Remove ppc64 ExcludeArch
 
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
 
* Mon Feb 6 2012 Orion Poplawski <orion@cora.nwra.com> 1.2-3
- Drop junit4 references
 
* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
 
* Wed Jan 4 2012 Orion Poplawski <orion@cora.nwra.com> 1.2-1
- Update to 1.2
 
* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
 
* Mon Dec 20 2010 Orion Poplawski <orion@cora.nwra.com> 1.1-4
- ExcludeArch ppc64 - no java >= 1:1.6.0 on ppc64
 
* Mon Dec 6 2010 Orion Poplawski <orion@cora.nwra.com> 1.1-3
- Rename to ant-antunit
- Drop BuildRoot and %%clean
- Drop unneeded Provides
 
* Fri Oct 29 2010 Orion Poplawski <orion@cora.nwra.com> 1.1-2
- Add /etc/ant.d/antunit
- Add Requires: ant
 
* Thu Oct 28 2010 Orion Poplawski <orion@cora.nwra.com> 1.1-1
- Initial package
