Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_without activation
%bcond_without cglib
%bcond_without dom4j
%bcond_without jdom
%bcond_without jdom2
%bcond_with jettison
%bcond_with joda-time
%bcond_with kxml2
%bcond_with stax
%bcond_with woodstox
%bcond_with xom
%bcond_with xpp3

Name:           xstream
Version:        1.4.19
Release:        2%{?dist}
Summary:        Java XML serialization library
License:        BSD
URL:            https://x-stream.github.io
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/com/thoughtworks/%{name}/%{name}-distribution/%{version}/%{name}-distribution-%{version}-src.zip

BuildRequires:  maven-local
BuildRequires:  mvn(io.github.x-stream:mxparser)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%if %{with activation}
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
%endif

%if %{with cglib}
BuildRequires:  mvn(cglib:cglib-nodep)
%endif

%if %{with dom4j}
BuildRequires:  mvn(dom4j:dom4j)
%endif

%if %{with jdom}
BuildRequires:  mvn(org.jdom:jdom)
%endif

%if %{with jdom2}
BuildRequires:  mvn(org.jdom:jdom2)
%endif

%if %{with jettison}
BuildRequires:  mvn(org.codehaus.jettison:jettison)
%endif

%if %{with joda-time}
BuildRequires:  mvn(joda-time:joda-time)
%endif

%if %{with kxml2}
BuildRequires:  mvn(net.sf.kxml:kxml2-min)
%endif

%if %{with stax}
BuildRequires:  mvn(stax:stax)
BuildRequires:  mvn(stax:stax-api)
%endif

%if %{with woodstox}
BuildRequires:  mvn(org.codehaus.woodstox:wstx-asl)
%endif

%if %{with xom}
BuildRequires:  mvn(xom:xom)
%endif

%if %{with xpp3}
BuildRequires:  mvn(xpp3:xpp3_min)
%endif

%description
XStream is a simple library to serialize objects to XML
and back again. A high level facade is supplied that
simplifies common use cases. Custom objects can be serialized
without need for specifying mappings. Speed and low memory
footprint are a crucial part of the design, making it suitable
for large object graphs or systems with high message throughput.
No information is duplicated that can be obtained via reflection.
This results in XML that is easier to read for humans and more
compact than native Java serialization. XStream serializes internal
fields, including private and final. Supports non-public and inner
classes. Classes are not required to have default constructor.
Duplicate references encountered in the object-model will be
maintained. Supports circular references. By implementing an
interface, XStream can serialize directly to/from any tree
structure (not just XML). Strategies can be registered allowing
customization of how particular types are represented as XML.
When an exception occurs due to malformed XML, detailed diagnostics
are provided to help isolate and fix the problem.

%package -n %{name}-benchmark
Summary:        Benchmark module for %{name}
%description -n %{name}-benchmark
Benchmark module for %{name}.

%{?javadoc_package}

%prep
%autosetup -n %{name}-%{version}

find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

# https://jakarta.ee/about/faq#What_happened_with_javax.*_namespace?
%pom_change_dep javax.activation:activation jakarta.activation:jakarta.activation-api %{name}

%pom_remove_plugin -r :maven-dependency-plugin

%if %{without activation}
%pom_remove_dep -r jakarta.activation:jakarta.activation-api
rm xstream/src/java/com/thoughtworks/xstream/converters/extended/ActivationDataFlavorConverter.java
%endif

%if %{without cglib}
%pom_remove_dep -r cglib:cglib-nodep
rm xstream/src/java/com/thoughtworks/xstream/converters/reflection/CGLIBEnhancedConverter.java
rm xstream/src/java/com/thoughtworks/xstream/mapper/CGLIBMapper.java
rm xstream/src/java/com/thoughtworks/xstream/security/CGLIBProxyTypePermission.java
%endif

%if %{without dom4j}
%pom_remove_dep -r dom4j:dom4j
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Dom4JDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Dom4JReader.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Dom4JWriter.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Dom4JXmlWriter.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamDom4J.java
%endif

%if %{without jdom}
%pom_remove_dep -r org.jdom:jdom
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDomDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDomReader.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDomWriter.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamJDom.java
%endif

%if %{without jdom2}
%pom_remove_dep -r org.jdom:jdom2
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDom2Driver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDom2Reader.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDom2Writer.java
%endif

%if %{without jettison}
%pom_remove_dep -r org.codehaus.jettison:jettison
rm xstream/src/java/com/thoughtworks/xstream/io/json/JettisonMappedXmlDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/json/JettisonStaxWriter.java
%endif

%if %{without joda-time}
%pom_remove_dep -r joda-time:joda-time
rm xstream/src/java/com/thoughtworks/xstream/core/util/ISO8601JodaTimeConverter.java
%endif

%if %{without kxml2}
%pom_remove_dep -r net.sf.kxml:kxml2-min
rm xstream/src/java/com/thoughtworks/xstream/io/xml/KXml2DomDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/KXml2Driver.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamKXml2.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamKXml2DOM.java
%endif

%if %{without stax}
%pom_remove_dep -r stax:stax
%pom_remove_dep -r stax:stax-api
rm xstream/src/java/com/thoughtworks/xstream/io/xml/BEAStaxDriver.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamBEAStax.java
%endif

%if %{without woodstox}
%pom_remove_dep -r org.codehaus.woodstox:wstx-asl
rm xstream/src/java/com/thoughtworks/xstream/io/xml/WstxDriver.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamWoodstox.java
%endif

%if %{without xom}
%pom_remove_dep -r xom:xom
rm xstream/src/java/com/thoughtworks/xstream/io/xml/XomDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/XomReader.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/XomWriter.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamXom.java
%endif

%if %{without xpp3}
%pom_remove_dep -r xpp3:xpp3_min
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Xpp3DomDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Xpp3Driver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/xppdom/Xpp3DomBuilder.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamXpp3.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamXpp3DOM.java
%endif

%pom_disable_module %{name}-distribution

%pom_disable_module %{name}-hibernate

%pom_disable_module %{name}-jmh

%mvn_package :%{name}-parent __noinstall

%build
%mvn_build -s -f -- -Dversion.java.source=1.8 -Dversion.java.target=1.8

%install
%mvn_install

%files -n %{name} -f .mfiles-%{name}
%license LICENSE.txt
%doc README.txt

%files -n %{name}-benchmark -f .mfiles-%{name}-benchmark
%license LICENSE.txt
%doc README.txt

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.4.19-2
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 29 2022 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.4.19-1
- New upstream release 1.4.19

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.4.18-2
- Enable activation, cglib, dom4j, jdom, and jdom2

* Fri Oct 01 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.4.18-1
- Update to version 1.4.18

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild
 
* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
 
* Tue Nov 17 2020 Ding-Yi Chen <dchen@redhat.com> - 1.4.14-1
- Upstream update to 1.4.14
 
* Fri Aug 07 2020 Mat Booth <mat.booth@redhat.com> - 1.4.12-6
- Allow building on JDK11
 
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
 
* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.4.12-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11
 
* Wed Jun 17 2020 Fabio Valentini <decathorpe@gmail.com> - 1.4.12-3
- Disable unused optional dom4j, jdom, jdom2, kxml, and woodstox support.
 
* Mon Jun 08 2020 Fabio Valentini <decathorpe@gmail.com> - 1.4.12-2
- Disable optional support for joda-time by default.
 
* Mon Apr 27 2020 Fabio Valentini <decathorpe@gmail.com> - 1.4.12-1
- Update to version 1.4.12.
- Disable optional support for BEA Stax by default.
 
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
 
* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 1.4.11.1-4
- Use Java version override compatible with both xmvn 3.0.0 and 3.1.0.
 
* Fri Jul 26 2019 Fabio Valentini <decathorpe@gmail.com> - 1.4.11.1-3
- Disable hibernate support by default.
 
* Tue Mar 05 2019 Mat Booth <mat.booth@redhat.com> - 1.4.11.1-2
- Allow building with reduced dependency set
 
* Thu Feb 14 2019 Mat Booth <mat.booth@redhat.com> - 1.4.11.1-1
- Update to latest upstream release
 
* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
 
* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
 
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
 
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
 
* Wed Apr 12 2017 Michael Simacek <msimacek@redhat.com> - 1.4.9-5
- Backport fix for void deserialization
- Resolves rhbz#1441542
- Update upstream URL
 
* Mon Feb 06 2017 Michael Simacek <msimacek@redhat.com> - 1.4.9-4
- Add conditional for hibernate
 
* Mon Jul 18 2016 Michael Simacek <msimacek@redhat.com> - 1.4.9-3
- Regenerate buildrequires
 
* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.9-2
- Regenerate build-requires
 
* Wed Mar 30 2016 Michal Srb <msrb@redhat.com> - 1.4.9-1
- Update to 1.4.9
- Resolves: CVE-2016-3674
 
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
 
* Tue Jan 19 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.8-3
- Fix dependency on xpp3
 
* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
 
* Thu Feb 19 2015 Michal Srb <msrb@redhat.com> - 1.4.8-1
- Update to upstream version 1.4.8
 
* Mon Nov 10 2014 Michael Simacek <msimacek@redhat.com> - 1.4.7-9
- Change org.json:json dependency scope to test
 
* Wed Nov  5 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.7-8
- Remove workaround for RPM bug #646523
 
* Fri Oct 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.7-7
- Fix dependencies in parent POM
 
* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.7-6
- Fix build-requires on codehaus-parent
 
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
 
* Fri Mar 07 2014 Michael Simacek <msimacek@redhat.com> - 1.4.7-4
- Split into subpackages
 
* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.7-3
- Use Requires: java-headless rebuild (#1067528)
 
* Wed Feb 19 2014 Michal Srb <msrb@redhat.com> - 1.4.7-2
- Spec file cleanup
- Fix BR
- Build with kxml2 and json
 
* Mon Feb 10 2014 Michal Srb <msrb@redhat.com> - 1.4.7-1
- Update to latest upstream release 1.4.7
 
* Thu Jan 02 2014 Michal Srb <msrb@redhat.com> - 1.4.6-1
- Update to upstream release 1.4.6
 
* Thu Oct 24 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.5-3
- Rebuild to move arch-independant JARs out of %%_jnidir
* Wed Oct 23 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.5-2
- Rebuild to regenerate broken POM files
- Related: rhbz#1021484
 
* Sun Oct 20 2013 Matt Spaulding <mspaulding06@gmail.com> 1.4.5-1
- update to 1.4.5
 
* Tue Aug 20 2013 gil cattaneo <puntogil@libero.it> 1.4.4-1
- update to 1.4.4
- switch to XMvn
 
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
 
* Fri Jul 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-7
- Update to current packaging guidelines
 
* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571
 
* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
 
* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
 
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
 
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
 
* Mon Jun 14 2010 Alexander Kurtakov <akurtako@redhat.com> 1.3.1-1
- Update to 1.3.1.
- Install maven pom and depmap.
 
* Wed Dec 02 2009 Lubomir Rintel <lkundrak@v3.sk> - 1.2.2-4
- Cosmetic fixes
 
* Fri Nov 27 2009 Lubomir Rintel <lkundrak@v3.sk> - 0:1.2.2-3
- Drop gcj (suggested by Jochen Schmitt), we seem to need OpenJDK anyway
- Fix -javadoc Require
- Drop epoch
 
* Sun Nov 01 2009 Lubomir Rintel <lkundrak@v3.sk> - 0:1.2.2-2
- Greatly simplify for Fedora
- Disable tests, we don't have all that's required to run them
- Remove maven build
 
* Fri Jul 20 2007 Ralph Apel <r.apel at r-apel.de> - 0:1.2.2-1jpp
- Upgrade to 1.2.2
- Build with maven2 by default
- Add poms and depmap frags
 
* Tue May 23 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.1.3-1jpp
- Upgrade to 1.1.3
- Patched to work with bea
 
* Mon Sep 13 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0.2-2jpp
- Drop saxpath requirement
- Require jaxen >= 0:1.1
 
* Mon Aug 30 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0.2-1jpp
- Upgrade to 1.0.2
- Delete included binary jars
- Change -Dbuild.sysclasspath "from only" to "first" (DynamicProxyTest)
- Relax some versioned dependencies
- Build with ant-1.6.2
 
* Fri Aug 06 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0.1-2jpp
- Upgrade to ant-1.6.X
 
* Tue Jun 01 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0.1-1jpp
- Upgrade to 1.0.1
 
* Fri Feb 13 2004 Ralph Apel <r.apel at r-apel.de> - 0:0.3-1jpp
- Upgrade to 0.3
- Add manual subpackage
 
* Mon Jan 19 2004 Ralph Apel <r.apel at r-apel.de> - 0:0.2-1jpp
- First JPackage release
