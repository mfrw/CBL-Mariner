Vendor:         Microsoft Corporation
Distribution:   Mariner
%global gittag r1rv70
%global classname org.bouncycastle.jce.provider.BouncyCastleProvider

Summary:          Bouncy Castle Cryptography APIs for Java
Name:             bouncycastle
Version:          1.70
Release:          4%{?dist}
License:          MIT
URL:              http://www.bouncycastle.org

Source0:          https://github.com/bcgit/bc-java/archive/%{gittag}.tar.gz

# POMs from Maven Central
Source1:          https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/%{version}/bcprov-jdk15on-%{version}.pom
Source2:          https://repo1.maven.org/maven2/org/bouncycastle/bcpkix-jdk15on/%{version}/bcpkix-jdk15on-%{version}.pom
Source3:          https://repo1.maven.org/maven2/org/bouncycastle/bcpg-jdk15on/%{version}/bcpg-jdk15on-%{version}.pom
Source4:          https://repo1.maven.org/maven2/org/bouncycastle/bcmail-jdk15on/%{version}/bcmail-jdk15on-%{version}.pom
Source5:          https://repo1.maven.org/maven2/org/bouncycastle/bctls-jdk15on/%{version}/bctls-jdk15on-%{version}.pom
Source6:          https://repo1.maven.org/maven2/org/bouncycastle/bcutil-jdk15on/%{version}/bcutil-jdk15on-%{version}.pom

# Script to fetch POMs from Maven Central
Source7:          get-poms.sh

# Backport fix for regression in bouncycastle 1.70
Patch0:           0001-added-back-support-for-subject-key-identifier-check-.patch

BuildArch:        noarch

BuildRequires:    aqute-bnd
BuildRequires:    ant
BuildRequires:    ant-junit
BuildRequires:    jakarta-activation
BuildRequires:    jakarta-mail
BuildRequires:    javapackages-local

Requires(post):   javapackages-tools
Requires(postun): javapackages-tools

Provides:         bcprov = %{version}-%{release}

%description
The Bouncy Castle Crypto package is a Java implementation of cryptographic
algorithms. This jar contains JCE provider and lightweight API for the
Bouncy Castle Cryptography APIs for JDK 1.5 to JDK 1.8.

%package pkix
Summary: Bouncy Castle PKIX, CMS, EAC, TSP, PKCS, OCSP, CMP, and CRMF APIs

%description pkix
The Bouncy Castle Java APIs for CMS, PKCS, EAC, TSP, CMP, CRMF, OCSP, and
certificate generation. This jar contains APIs for JDK 1.5 to JDK 1.8. The
APIs can be used in conjunction with a JCE/JCA provider such as the one
provided with the Bouncy Castle Cryptography APIs.

%package pg
Summary: Bouncy Castle OpenPGP API

%description pg
The Bouncy Castle Java API for handling the OpenPGP protocol. The APIs can be
used in conjunction with a JCE/JCA provider such as the one provided with the
Bouncy Castle Cryptography APIs.

%package mail
Summary: Bouncy Castle S/MIME API

%description mail
The Bouncy Castle Java S/MIME APIs for handling S/MIME protocols. The APIs can
be used in conjunction with a JCE/JCA provider such as the one provided with
the Bouncy Castle Cryptography APIs. The JavaMail API and the Java activation
framework will also be needed.

%package tls
Summary: Bouncy Castle JSSE provider and TLS/DTLS API

%description tls
The Bouncy Castle Java APIs for TLS and DTLS, including a provider for the
JSSE.

%package util
Summary: Bouncy Castle ASN.1 Extension and Utility APIs

%description util
The Bouncy Castle Java APIs for ASN.1 extension and utility APIs used to
support bcpkix and bctls.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
API documentation for the Bouncy Castle Cryptography APIs.

%prep
%setup -q -n bc-java-%{gittag}
%patch0 -p1

# Remove bundled binary libs
find . -type f -name "*.class" -exec rm -f {} \;
find . -type f -name "*.jar" -exec rm -f {} \;

# Relax javadoc linting and set expected source encoding
sed -i -e '/<javadoc/aadditionalparam="-Xdoclint:none" encoding="UTF-8" source="1.8"' \
       -e '/<javac/aencoding="UTF-8"' ant/bc+-build.xml

# Mail and Activation do not yet provide jakarta packages, so don't build jmail module
sed -i -e '/target="build-jmail"/d' ant/jdk15+.xml

# Not shipping lw/lcrypto (lightweight crypto) jar
sed -i -e '/target="build-lw"/d' ant/jdk15+.xml
sed -i -e '/target="javadoc-lw"/d' ant/jdk15+.xml

cp -p %{SOURCE1} bcprov.pom
cp -p %{SOURCE2} bcpkix.pom
cp -p %{SOURCE3} bcpg.pom
cp -p %{SOURCE4} bcmail.pom
cp -p %{SOURCE5} bctls.pom
cp -p %{SOURCE6} bcutil.pom

%build
ant -f ant/jdk15+.xml \
  -Djunit.jar.home=$(build-classpath junit) \
  -Dmail.jar.home=$(build-classpath jakarta-mail/jakarta.mail) \
  -Dactivation.jar.home=$(build-classpath jakarta-activation/jakarta.activation) \
  -Drelease.debug=true -Dbc.javac.source=1.8 -Dbc.javac.target=1.8 \
  clean build-provider build #test

cat > bnd.bnd <<EOF
-classpath=bcprov.jar,bcutil.jar,bcpkix.jar,bcpg.jar,bcmail.jar,bctls.jar
Export-Package: *;version=%{version}
EOF

for bc in bcprov bcutil bcpkix bcpg bcmail bctls ; do
  # Make into OSGi bundle
  bnd wrap -b $bc -v %{version} -p bnd.bnd -o $bc.jar build/artifacts/jdk1.5/jars/$bc-jdk15on-*.jar

  # Request Maven installation
  %mvn_file ":$bc-jdk15on" $bc
  %mvn_package ":$bc-jdk15on" $bc
  %mvn_alias ":$bc-jdk15on" "org.bouncycastle:$bc-jdk16" "org.bouncycastle:$bc-jdk15"
  %mvn_artifact $bc.pom $bc.jar
done

%install
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/java/security/security.d
touch $RPM_BUILD_ROOT%{_sysconfdir}/java/security/security.d/2000-%{classname}

%mvn_install -J build/artifacts/jdk1.5/javadoc

%post
{
  # Rebuild the list of security providers in classpath.security
  suffix=security/classpath.security
  secfiles="/usr/lib/$suffix /usr/lib64/$suffix"

  for secfile in $secfiles
  do
    # check if this classpath.security file exists
    [ -f "$secfile" ] || continue

    sed -i '/^security\.provider\./d' "$secfile"

    count=0
    for provider in $(ls /etc/java/security/security.d)
    do
      count=$((count + 1))
      echo "security.provider.${count}=${provider#*-}" >> "$secfile"
    done
  done
} || :

%postun
if [ "$1" -eq 0 ] ; then

  {
    # Rebuild the list of security providers in classpath.security
    suffix=security/classpath.security
    secfiles="/usr/lib/$suffix /usr/lib64/$suffix"

    for secfile in $secfiles
    do
      # check if this classpath.security file exists
      [ -f "$secfile" ] || continue

      sed -i '/^security\.provider\./d' "$secfile"

      count=0
      for provider in $(ls /etc/java/security/security.d)
      do
        count=$((count + 1))
        echo "security.provider.${count}=${provider#*-}" >> "$secfile"
      done
    done
  } || :

fi

%files -f .mfiles-bcprov
%license build/artifacts/jdk1.5/bcprov-jdk15on-*/LICENSE.html
%doc docs/ *.html
%{_sysconfdir}/java/security/security.d/2000-%{classname}

%files pkix -f .mfiles-bcpkix
%license build/artifacts/jdk1.5/bcpkix-jdk15on-*/LICENSE.html

%files pg -f .mfiles-bcpg
%license build/artifacts/jdk1.5/bcpg-jdk15on-*/LICENSE.html

%files mail -f .mfiles-bcmail
%license build/artifacts/jdk1.5/bcmail-jdk15on-*/LICENSE.html

%files tls -f .mfiles-bctls
%license build/artifacts/jdk1.5/bctls-jdk15on-*/LICENSE.html

%files util -f .mfiles-bcutil
%license build/artifacts/jdk1.5/bcutil-jdk15on-*/LICENSE.html

%files javadoc -f .mfiles-javadoc
%license LICENSE.html

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.70-4
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.70-2
- Backport fix for regression in bouncycastle 1.70, fixes rhbz#2039724

* Fri Dec 17 2021 Mat Booth <mat.booth@gmail.com> - 1.70-1
- Update to latest upstream release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Mat Booth <mbooth@apache.org> - 1.68-1
- Update to latest upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 01 2020 Mat Booth <mat.booth@redhat.com> - 1.67-1
- Update to latest upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.65-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.65-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat Jun 20 2020 Mat Booth <mat.booth@redhat.com> - 1.65-2
- Fix build on Java 11

* Fri Jun 19 2020 Mat Booth <mat.booth@redhat.com> - 1.65-1
- Update to latest upstream release
- Remove old obsoletes
- Avoid using deprecated source/target values

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 12 2019 Mat Booth <mat.booth@redhat.com> - 1.63-1
- Update to latest upstream release

* Mon Sep 09 2019 Mat Booth <mat.booth@redhat.com> - 1.61-2
- Disable tests that take a long time on 32bit arm

* Wed Feb 06 2019 Mat Booth <mat.booth@redhat.com> - 1.61-1
- Update to latest upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Mat Booth <mat.booth@redhat.com> - 1.60-1
- Update to latest upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Mat Booth <mat.booth@redhat.com> - 1.59-1
- Update to latest release
- Fixes CVE-2018-1000180 and CVE-2017-13098

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Mat Booth <mat.booth@redhat.com> - 1.58-2
- Fix error in scriptlet

* Fri Aug 18 2017 Mat Booth <mat.booth@redhat.com> - 1.58-1
- Update to 1.58, fixes rhbz#1482920

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Mat Booth <mat.booth@redhat.com> - 1.57-1
- Update to latest release of bouncycastle
- Build all bouncycastle modules from a single source tree, using upstream's
  own build scripts
- Add sub-packages for each module

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 09 2016 gil cattaneo <puntogil@libero.it> 1.54-2
- readd workaround for test failures

* Thu Apr 07 2016 Mat Booth <mat.booth@redhat.com> - 1.54-1
- Update to 1.54, fixes rhbz#1270249
- Install with mvn_install
- Fix test suite failures, fixes rhbz#1049007
- Move some tests that were erroneously in the main jar,
  avoids a runtime dep on junit in OSGi metadata

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 16 2015 Michael Simacek <msimacek@redhat.com> - 1.52-7
- Re-add geenric Export-Package

* Thu Jul 16 2015 Michael Simacek <msimacek@redhat.com> - 1.52-6
- Use aqute-bnd-2.4.1

* Tue Jun 23 2015 Roland Grunberg <rgrunber@redhat.com> - 1.52-5
- Remove Import/Export-Package statements.
- Related: rhbz#1233354

* Mon Jun 22 2015 Roland Grunberg <rgrunber@redhat.com> - 1.52-4
- Fix typo in OSGi metadata file.

* Thu Jun 18 2015 Mat Booth <mat.booth@redhat.com> - 1.52-3
- Resolves: rhbz#1233354 - Add OSGi metadata

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 22 2015 Alexander Kurtakov <akurtako@redhat.com> 1.52-1
- Update to 1.52.
- Switch source/target to 1.6 as 1.5 is deprecated

* Thu Jan 29 2015 gil cattaneo <puntogil@libero.it> 1.50-6
- introduce license macro

* Wed Oct 22 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.50-5
- Add alias for org.bouncycastle:bcprov-jdk15

* Mon Jun 09 2014 Michal Srb <msrb@redhat.com> - 1.50-4
- Migrate to .mfiles

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Michal Srb <msrb@redhat.com> - 1.50-2
- Fix java BR/R
- Build with -source/target 1.5
- s/organised/organized/

* Fri Feb 21 2014 Michal Srb <msrb@redhat.com> - 1.50-1
- Update to upstream version 1.50
- Switch to java-headless

* Mon Jan  6 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.46-12
- Add Maven alias for bouncycastle:bcprov-jdk15

* Tue Oct 22 2013 gil cattaneo <puntogil@libero.it> 1.46-11
- remove versioned Jars

* Thu Aug 29 2013 gil cattaneo <puntogil@libero.it> 1.46-10
- remove update_maven_depmap

* Mon Aug 05 2013 gil cattaneo <puntogil@libero.it> 1.46-9
- rebuilt rhbz#992026

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 08 2012 Tom Callaway <spot@fedoraproject.org> - 1.46-5
- use original sources from here on out

* Sat Feb 18 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.46-4
- Build with -source 1.6 -target 1.6 

* Thu Jan 12 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.46-3
- Update javac target version to 1.7 to build with new java

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar 01 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.46-1
- Import Bouncy Castle 1.46.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 30 2010 Alexander Kurtakov <akurtako@redhat.com> 1.45-2
- Drop gcj.
- Adapt to current guidelines.

* Thu Feb 11 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.45-1
- Import Bouncy Castle 1.45.

* Sat Nov 14 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.44-1
- Import Bouncy Castle 1.44.

* Sun Sep  6 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.43-6
- Include improvements from #521475:
- Include missing properties files in jar.
- Build with javac -encoding UTF-8.
- Use %%javac and %%jar macros.
- Run test suite during build (ignoring failures for now).
- Follow upstream in excluding various test suite classes from jar; drop
  dependency on junit4.

* Wed Aug 26 2009 Andrew Overholt <overholt@redhat.com> 1.43-5
- Add maven POM

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.43-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.43-3
- Raise java requirement to >= 1.7 once again.

* Fri Jul 10 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.43-2
- Re-enable AOT bits thanks to Andrew Haley.

* Mon Apr 20 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.43-1
- Import Bouncy Castle 1.43.

* Sat Apr 18 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.42-3
- Don't build AOT bits. The package needs java1.6

* Thu Apr 09 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.42-2
- Add missing Requires: junit4

* Tue Mar 17 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.42-1
- Import Bouncy Castle 1.42.
- Update description.
- Add javadoc subpackage.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 11 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.41-2
- Fixed license tag (BSD -> MIT).
- Minor improvements in the SPEC file for better compatibility with the 
  Fedora Java Packaging Guidelines.
- Added "Provides: bcprov == %%{version}-%%{release}".

* Thu Oct  2 2008 Lillian Angel <langel@redhat.com> - 1.41-1
- Import Bouncy Castle 1.41.
- Resolves: rhbz#465203

* Thu May 15 2008 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.39-1
- Import Bouncy Castle 1.39.
- Set target to 1.5.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.38-2
- Autorebuild for GCC 4.3

* Thu Nov 29 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.38-1
- Import Bouncy Castle 1.38.
- Require junit4 for build.
- Require java-1.7.0-icedtea-devel for build.
- Wrap lines at 80 columns.
- Inline rebuild-security-providers in post and postun sections.
- Related: rhbz#260161

* Sat Mar 31 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.34-3
- Require java-1.5.0-gcj.

* Tue Dec 12 2006 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.34-2
- Install bcprov jar and unversioned symlink in %%{_javadir}.
- Install bcprov symlink in %%{_javadir}/gcj-endorsed.
- Change release numbering format to X.fc7.
- Include new bcprov files in files list.
- Import Bouncy Castle 1.34.
- Related: rhbz#218794

* Tue Jul 25 2006 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.33-3
- Bump release number.

* Mon Jul 10 2006 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.33-2
- Fix problems pointed out by reviewer.

* Fri Jul  7 2006 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.33-1
- First release.
