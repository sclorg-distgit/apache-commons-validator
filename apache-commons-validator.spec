%global pkg_name apache-commons-validator
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global base_name       validator
%global short_name      commons-%{base_name}

Name:             %{?scl_prefix}%{pkg_name}
Version:          1.4.0
Release:          8.11%{?dist}
Summary:          Apache Commons Validator
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:        noarch

BuildRequires:    %{?scl_prefix_java_common}javapackages-tools
BuildRequires:    maven30-apache-commons-parent >= 26-7
BuildRequires:    %{?scl_prefix_java_common}apache-commons-beanutils
BuildRequires:    maven30-apache-commons-digester
BuildRequires:    %{?scl_prefix_java_common}apache-commons-logging
BuildRequires:    %{?scl_prefix_java_common}maven-local
BuildRequires:    %{?scl_prefix_java_common}junit


%description
A common issue when receiving data either electronically or from user input is
verifying the integrity of the data. This work is repetitive and becomes even
more complicated when different sets of validation rules need to be applied to
the same set of data based on locale for example. Error messages may also vary
by locale. This package attempts to address some of these issues and speed
development and maintenance of validation rules.

%package javadoc
Summary:          Javadoc for %{pkg_name}


%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n %{short_name}-%{version}-src
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' RELEASE-NOTES.txt
sed -i 's/\r//' NOTICE.txt

# Compatibility links
%mvn_file :commons-validator %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.4.0-8.11
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.4.0-8.10
- Mass rebuild 2015-01-13

* Mon Jan 12 2015 Michael Simacek <msimacek@redhat.com> - 1.4.0-8.9
- Rebuild to regenerate requires from java-common

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.4.0-8.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-8.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-8.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-8.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-8.4
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-8.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-8.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-8.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.4.0-8
- Mass rebuild 2013-12-27

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-7
- Add BuildRequires on apache-commons-parent >= 26-7

* Thu Aug 22 2013 Michal Srb <msrb@redhat.com> - 1.4.0-6
- Migrate away from mvn-rpmbuild (Resolves: #997476)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-5
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4.0-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Nov 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-2
- Install NOTICE file with javadoc package

* Fri Oct 19 2012 Chris Spike <spike@fedoraproject.org> 1.4.0-1
- Updated to 1.4.0
- Switched build tool from ant to maven
- Updated to latest java packaging guidelines
- Dropped oro BR/R

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 18 2012 Stanislav Ochotnicky <sochotnicky@redhat.com>- 1.3.1-8
- Fix tests after junit update

* Sat Jan 14 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.3.1-7
- Tweak source encoding to fix build with Java 1.7.
- Drop versioned jars and javadoc dir.
- Drop no longer needed javadoc Obsoletes.
- Crosslink with local JDK API docs.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 22 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3.1-5
- Change oro to jakarta-oro in BR/R

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 20 2010 Chris Spike <chris.spike@arcor.de> 1.3.1-3
- Moved junit tests to check section

* Sat Oct 2 2010 Chris Spike <chris.spike@arcor.de> 1.3.1-2
- Rename and rebase from jakarta-commons-validator
