%include	/usr/lib/rpm/macros.perl
Summary:	Text-BasicTemplate perl module
Summary(pl):	Modu³ perla Text-BasicTemplate
Name:		perl-Text-BasicTemplate
Version:	0.9.8
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-BasicTemplate-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/BasicTemplate
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Text/BasicTemplate.pm
%{perl_sitelib}/auto/Text/BasicTemplate
%{perl_sitearch}/auto/Text/BasicTemplate

%{_mandir}/man3/*
