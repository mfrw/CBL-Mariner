Vendor:         Microsoft Corporation
Distribution:   Mariner
%global version_id parent
%global upstream_name client_java

Name:          prometheus-simpleclient-java
Version:       0.12.0
Release:       4%{?dist}
Summary:       Prometheus JVM Client

License:       ASL 2.0 and CC0
URL:           https://github.com/prometheus/client_java/

Source0:       https://github.com/prometheus/client_java/archive/%{version_id}-%{version}.tar.gz
# OpenTelemetry isn't in Fedora
Patch1:        remove_opentelemetry_tracer.patch

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(junit:junit)

%description
Prometheus instrumentation library for JVM applications.

%prep
%setup -q -n %{upstream_name}-%{version_id}-%{version}

# Remove included jar files
find . -name \*.jar -print0 | xargs -0 rm

# Only build the following artefacts as these are actually dependencies
# of prometheus_jmxexporter
# 
# io.prometheus:simpleclient
# io.prometheus:simpleclient_hotspot
# io.prometheus:simpleclient_httpserver
# io.prometheus:simpleclient_common
for m in simpleclient_caffeine \
         simpleclient_dropwizard \
         simpleclient_graphite_bridge \
         simpleclient_hibernate \
         simpleclient_guava \
         simpleclient_log4j \
         simpleclient_log4j2 \
         simpleclient_logback \
         simpleclient_pushgateway \
         simpleclient_servlet \
         simpleclient_spring_web \
         simpleclient_spring_boot \
         simpleclient_jetty \
         simpleclient_jetty_jdk8 \
         simpleclient_vertx \
         simpleclient_bom \
         integration_tests \
         simpleclient_servlet_common \
         simpleclient_servlet_jakarta \
         benchmarks; do
%pom_disable_module $m
done
# Only build simpleclient_tracer_common as it's being used by an Examplar class
%pom_disable_module simpleclient_tracer_otel_agent simpleclient_tracer
%pom_disable_module simpleclient_tracer_otel simpleclient_tracer

# Remove test dependencies for hotspot
%pom_remove_dep io.prometheus:simpleclient_servlet simpleclient_hotspot
%pom_remove_dep org.mockito:mockito-core simpleclient_hotspot
%pom_remove_dep org.eclipse.jetty:jetty-servlet simpleclient_hotspot
# Remove test dependencies for httpserver
%pom_remove_dep org.assertj:assertj-core simpleclient_httpserver
%pom_remove_dep javax.xml.bind:jaxb-api simpleclient_httpserver

# Remove tests which wouldn't compile with removed deps (like mockito)
for i in $(find simpleclient_hotspot/src/test/java/io/prometheus/client/hotspot -name \*.java); do
  if ! echo $i | grep -q -E 'VersionInfoExportsTest\.java'; then
    rm $i
  fi
done
rm -rf simpleclient_httpserver/src/test/java

# remove OpenTelemetry stuff, which we don't support
%patch1 -p2
%pom_remove_dep io.prometheus:simpleclient_tracer_otel simpleclient
%pom_remove_dep io.prometheus:simpleclient_tracer_otel_agent simpleclient
%pom_add_dep io.prometheus:simpleclient_tracer_common:%{version} simpleclient

# Change compiler source/target version to JDK 8 level
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" "1.8" pom.xml
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" "1.8" pom.xml


%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc NOTICE

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.12.0-4
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Severin Gehwolf <sgehwolf@redhat.com> - 0.12.0-2
- Bump source/target Java compiler level to JDK 8 for JDK 17
  compatibility.

* Thu Sep 02 2021 Severin Gehwolf <sgehwolf@redhat.com> - 0.12.0-1
- Update to latest upstream 0.12.0 release.
- Doesn't include support for OpenTelemetry tracing.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Severin Gehwolf <sgehwolf@redhat.com> - 0.6.0-2
- Enable some tests during build.

* Mon Aug 12 2019 Severin Gehwolf <sgehwolf@redhat.com> - 0.6.0-1
- Initial package.

