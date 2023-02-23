#!/bin/sh

version=$(grep '^Version:' bouncycastle.spec | sed -e 's/^Version:\W*//')

for bc in bcprov bcpkix bcpg bcmail bctls bcutil ; do
  rm -f $bc-*.pom
  wget https://repo1.maven.org/maven2/org/bouncycastle/$bc-jdk15on/$version/$bc-jdk15on-$version.pom
done
