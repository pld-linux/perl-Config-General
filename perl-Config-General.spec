#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Config
%define		pnam	General
Summary:	Config::General - Generic Config Module
Summary(pl):	Config::General - ogólny modu³ konfiguracji
Name:		perl-Config-General
Version:	2.21
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	52861e3035c8f4fb063f0d8d45429c02
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module opens a config file and parses it's contents for you. The
method new requires one parameter which needs to be a filename. The
method getall returns a hash which contains all options and it's
associated values of your config file.

%description -l pl
Ten modu³ otwiera plik konfiguracyjny i analizuje jego zawarto¶æ.
Metoda new wymaga jednego parametru, którym musi byæ nazwa pliku.
Metoda getall zwraca hasza zawieraj±cego wszystkie opcje i zwi±zane
z nimi warto¶ci z pliku konfiguracyjnego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%{perl_vendorlib}/Config/General.pm
%{perl_vendorlib}/Config/General
%{_mandir}/man3/*
