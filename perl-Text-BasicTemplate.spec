%include	/usr/lib/rpm/macros.perl
Summary:	Text-BasicTemplate perl module
Summary(pl):	Modu³ perla Text-BasicTemplate
Name:		perl-Text-BasicTemplate
Version:	2.005
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-BasicTemplate-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-BasicTemplate - simple text/HTML/generic template parsing module.

%description -l pl
Modu³ perla Text-BasicTemplate.

%prep
%setup -q -n Text-BasicTemplate-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Text/BasicTemplate.pm
%{perl_sitelib}/auto/Text/BasicTemplate
%{_mandir}/man3/*
