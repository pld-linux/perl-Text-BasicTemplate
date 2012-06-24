%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	BasicTemplate
Summary:	Text-BasicTemplate perl module
Summary(pl):	Modu� perla Text-BasicTemplate
Name:		perl-Text-BasicTemplate
Version:	2.005
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-BasicTemplate - simple text/HTML/generic template parsing module.

%description -l pl
Modu� perla Text-BasicTemplate.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
