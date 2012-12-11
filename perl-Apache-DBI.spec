%define upstream_name    Apache-DBI
%define upstream_version 1.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Initiate a persistent database connection
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Apache/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBD::mysql)

BuildArch:	noarch

%description
This module initiates a persistent database connection.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Apache
%{_mandir}/*/*


%changelog
* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 635489
- update to new version 1.10

* Fri Nov 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.90.0-1mdv2011.0
+ Revision: 596515
- update to new version 1.09

* Fri Feb 05 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.80.0-1mdv2011.0
+ Revision: 501140
- update to 1.08

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.70.0-1mdv2010.0
+ Revision: 402964
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.07-2mdv2009.0
+ Revision: 268366
- rebuild early 2009.0 package (before pixel changes)

* Sat May 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdv2009.0
+ Revision: 208350
- update to new version 1.07

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.06-3mdv2008.1
+ Revision: 136657
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 19 2007 Oden Eriksson <oeriksson@mandriva.com> 1.06-3mdv2008.0
+ Revision: 66862
- rebuild

* Mon Apr 23 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1.06-1mdv2008.0
+ Revision: 17436
- New version


* Thu Nov 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2007.0
+ Revision: 86553
- new version

* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.03-1mdv2007.1
+ Revision: 73191
- import perl-Apache-DBI-1.03-1mdv2007.0

* Sat Aug 26 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2007.0
- New version 1.03

* Sat Aug 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2007.0
- New version 1.02

* Wed Jun 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2007.0
- New release 1.01
- HTTP source URL

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.9901-2mdk
- Fix SPEC Using perl Policies
    - Source URL
    - BuildRequires

* Thu Dec 15 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.9901-1mdk
- new version
- spec cleanup
- rpmbuildupdate aware
- better URL
- reenable tests

* Sat Jul 16 2005 Oden Eriksson <oeriksson@mandriva.com> 0.98-1mdk
- 0.98

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.94-2mdk
- fix buildrequires in a backward compatible way

* Tue Jun 01 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.94-1mdk
- 0.94
- cosmetics
- drop test for now

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.92-2mdk
- fixed dir ownership (distlint)

* Mon Dec 08 2003 Guillaume Rousse <guillomovitch@mandrake.org> 0.92-1mdk
- first mdk release

