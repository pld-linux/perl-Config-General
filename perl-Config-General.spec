%include	/usr/lib/rpm/macros.perl
%define		pdir	Config
%define		pnam	General
Summary:	Config::General perl module
Summary(pl):	Modu³ perla Config::General
Name:		perl-Config-General
Version:	1.32
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::General perl module.

%description -l pl
Modu³ perla Config::General.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changelog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{perl_sitelib}/Config
%{perl_sitelib}/Config/General.pm
%{_mandir}/man3/*
