%define upstream_name    Proc-Background
%define upstream_version 1.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Generic interface to Unix and Win32 background process management
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/B/BZ/BZAJAC/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(App::Cache)
BuildRequires:	perl(Class::Accessor::Chained)
BuildArch:	noarch

%description
This is a generic interface for placing processes in the background on both 
Unix and Win32 platforms. This module lets you start, kill, wait on, 
retrieve exit values, and see if background processes still exist.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*



%changelog
* Mon Jul 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.0
+ Revision: 392715
- update to 1.10
- using %%perl_convert_version
- fixed license field

* Fri Jul 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-1mdv2010.0
+ Revision: 391952
- update to new version 1.09

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.08-6mdv2009.0
+ Revision: 241846
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-4mdv2008.0
+ Revision: 86818
- rebuild


* Thu Jul 20 2006 Michael Scherer <misc@mandriva.org> 1.08-3mdv2007.0
- Rebuild

* Tue Dec 27 2005 Michael Scherer <misc@mandriva.org> 1.08-2mdk
- Do not ship empty dir

* Fri Sep 23 2005 Michael Scherer <misc@mandriva.org> 1.08-1mdk
- First mandriva package

