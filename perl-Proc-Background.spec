%define upstream_name    Proc-Background
%define upstream_version 1.10

Name:		perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Generic interface to Unix and Win32 background process management
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/B/BZ/BZAJAC/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(App::Cache)
BuildRequires: perl(Class::Accessor::Chained)
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
BuildArch: noarch

%description
This is a generic interface for placing processes in the background on both 
Unix and Win32 platforms. This module lets you start, kill, wait on, 
retrieve exit values, and see if background processes still exist.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

