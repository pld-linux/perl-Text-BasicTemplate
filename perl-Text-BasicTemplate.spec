#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	BasicTemplate
Summary:	Text::BasicTemplate perl module
Summary(pl):	Modu³ perla Text::BasicTemplate
Name:		perl-Text-BasicTemplate
Version:	2.006.1
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::BasicTemplate - simple text/HTML/generic template parsing module.

%description -l pl
Modu³ perla Text::BasicTemplate - prosty modu³ do analizowania wzorców
tekstowych, HTML i ogólnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Text/BasicTemplate.pm
# empty autosplit.ix
#%dir %{perl_sitelib}/auto/Text/BasicTemplate
#%%{perl_sitelib}/auto/Text/BasicTemplate/autosplit.ix
%{_mandir}/man3/*
