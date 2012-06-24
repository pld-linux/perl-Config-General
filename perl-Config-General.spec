%include	/usr/lib/rpm/macros.perl
%define		pdir	Config
%define		pnam	General
Summary:	Config::General Perl module
Summary(cs):	Modul Config::General pro Perl
Summary(da):	Perlmodul Config::General
Summary(de):	Config::General Perl Modul
Summary(es):	M�dulo de Perl Config::General
Summary(fr):	Module Perl Config::General
Summary(it):	Modulo di Perl Config::General
Summary(ja):	Config::General Perl �⥸�塼��
Summary(ko):	Config::General �� ����
Summary(no):	Perlmodul Config::General
Summary(pl):	Modu� Perla Config::General
Summary(pt):	M�dulo de Perl Config::General
Summary(pt_BR):	M�dulo Perl Config::General
Summary(ru):	������ ��� Perl Config::General
Summary(sv):	Config::General Perlmodul
Summary(uk):	������ ��� Perl Config::General
Summary(zh_CN):	Config::General Perl ģ��
Name:		perl-Config-General
Version:	1.36
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::General perl module.

%description -l cs
Modul Config::General pro Perl.

%description -l da
Perlmodul Config::General.

%description -l de
Config::General Perl Modul.

%description -l es
M�dulo de Perl Config::General.

%description -l fr
Module Perl Config::General.

%description -l it
Modulo di Perl Config::General.

%description -l ja
Config::General Perl �⥸�塼��

%description -l ko
Config::General �� ����.

%description -l no
Perlmodul Config::General.

%description -l pl
Modu� perla Config::General.

%description -l pt
M�dulo de Perl Config::General.

%description -l pt_BR
M�dulo Perl Config::General.

%description -l ru
������ ��� Perl Config::General.

%description -l sv
Config::General Perlmodul.

%description -l uk
������ ��� Perl Config::General.

%description -l zh_CN
Config::General Perl ģ��

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%{perl_sitelib}/Config/General.pm
%{perl_sitelib}/Config/General
%{_mandir}/man3/*
