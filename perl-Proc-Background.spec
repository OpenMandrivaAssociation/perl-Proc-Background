%define realname   Proc-Background

Name:		perl-%{realname}
Version:    1.09
Release:    %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Generic interface to Unix and Win32 background process management
Source0:    http://search.cpan.org/CPAN/authors/id/B/BZ/BZAJAC/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel perl-App-Cache perl-Class-Accessor-Chained 
BuildArch:      noarch

%description
This is a generic interface for placing processes in the background on both 
Unix and Win32 platforms. This module lets you start, kill, wait on, 
retrieve exit values, and see if background processes still exist.


%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*

