#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Config
%define		pnam	General
Summary:	Config::General - generic config module
Summary(pl.UTF-8):   Config::General - ogólny moduł konfiguracji
Name:		perl-Config-General
Version:	2.31
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5d51723f6fb36cf943934b80c261d680
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module opens a config file and parses it's contents for you. The
method new requires one parameter which needs to be a filename. The
method getall returns a hash which contains all options and it's
associated values of your config file.

%description -l pl.UTF-8
Ten moduł otwiera plik konfiguracyjny i analizuje jego zawartość.
Metoda new wymaga jednego parametru, którym musi być nazwa pliku.
Metoda getall zwraca hasza zawierającego wszystkie opcje i związane
z nimi wartości z pliku konfiguracyjnego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog example.cfg
%{perl_vendorlib}/Config/*.pm
%{perl_vendorlib}/Config/General
%{_mandir}/man3/*
