Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

Name:           plexus-resources
Version:        1.1.0
Release:        9%{?dist}
Summary:        Plexus Resource Manager
License:        MIT
URL:            https://github.com/codehaus-plexus/plexus-resources
BuildArch:      noarch

Source0:        https://github.com/codehaus-plexus/plexus-resources/archive/plexus-resources-%{version}.tar.gz

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.codehaus.plexus:plexus-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
%endif

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
API documentation for %{name}.

%prep
%setup -q -n plexus-resources-plexus-resources-%{version}

%build
%mvn_file  : plexus/resources
%mvn_build -f

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.1.0-9
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.0-6
- Bootstrap build
- Non-bootstrap build

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.1.0-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.0-2
- Mass rebuild for javapackages-tools 201902

* Tue Aug 20 2019 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- Update to version 1.1.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.26.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Marian Koncek <mkoncek@redhat.com> - 1.1.0-1
- Update to upstream version 1.1.0

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.24.a7
- Mass rebuild for javapackages-tools 201901

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.25.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.24.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.23.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.22.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.21.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.20.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.19.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.18.a7
- Cleanup spec file

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.17.a7
- Update upstream URL

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.16.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.15.a7
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.14.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 08 2013 Michal Srb <msrb@redhat.com> - 1.0-0.13.a7
- Remove unnecessary BR on maven-doxia and maven-doxia-sitetools

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-0.12.a7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 1.0-0.11.a7
- Build with xmvn

* Thu Nov 22 2012 Jaromir Capik <jcapik@redhat.com> - 1.0-0.10.a7
- Migration to plexus-containers-container-default

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.9.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.7.a7
- Rebuild for java 1.6.0 downgrade

* Wed Jul 27 2011 Jaromir Capik <jcapik@redhat.com> - 1.0-0.6.a7
- Removal of plexus-maven-plugin dependency (not needed)
- Minor spec file changes according to the latest guidelines

* Sun Jun 12 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0-0.5.a7
- Build with maven 3.x

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 25 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-0.3.a7
- Update to alpha 7.
- Apply patch to fix rhbz#621714.
- Use global instead of define.
- Drop ant build - broken after update.

* Wed Aug 26 2009 Andrew Overholt <overholt@redhat.com> 1.0-0.2.a4
- Fix release and defattr
- Make -javadoc description better

* Tue Aug 25 2009 Andrew Overholt <overholt@redhat.com> 1.0-0.1.a4.5
- Remove gcj support
- Fix license tag
- Improve source build instructions
- Remove "excalibur-" prefix from two BRs

* Thu Mar 20 2009 Yong Yang <yyang@redhat.com> 0:1.0-0.1.a4.4
- Build with maven2-2.0.8 built in non-bootstrap mode
- Add some missing BRs

* Thu Mar 20 2009 Yong Yang <yyang@redhat.com> 0:1.0-0.1.a10.3
- Build with maven2 2.0.8

* Tue Jan 20 2009 Yong Yang <yyang@redhat.com> 0:1.0-0.1.a4.2jpp.1
- Import from dbhole's maven 2.0.8 packages
- Merge with JPP-5

* Fri Sep 21 2007 Deepak Bhole <dbhole@redhat.com> 0:1.0-0.1.a4.2jpp.3
- ExcludeArch ppc64

* Tue Mar 20 2007 Deepak Bhole <dbhole@redhat.com> 0:1.0-0.1.a4.2jpp.2
- Enable gcj

* Tue Feb 20 2007 Tania Bento <tbento@redhat.com> 0:1.0-0.1.a4.2jpp.1
- Fixed %%Release.
- Fixed %%BuildRoot.
- Removed %%Vendor.
- Removed %%Distribution.
- Edited instructions on how to generate the source drops.
- Removed %%post and %%postun sections for javadoc.
- Added gcj support.

* Tue Oct 17 2006 Deepak Bhole <dbhole@redhat.com> 1.0-0.a4.2jpp
- Update for maven2 9jpp

* Mon Jun 12 2006 Deepak Bhole <dbhole@redhat.com> - 0:1.0-0.a4.1jpp
- Initial build
