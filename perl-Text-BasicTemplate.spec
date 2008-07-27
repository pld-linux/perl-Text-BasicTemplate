#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	BasicTemplate
Summary:	Text::BasicTemplate perl module
Summary(pl.UTF-8):	Moduł perla Text::BasicTemplate
Name:		perl-Text-BasicTemplate
Version:	2.006.1
Release:	5
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c849a595e8908ace13e2b9fc7f819036
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::BasicTemplate - simple text/HTML/generic template parsing module.

%description -l pl.UTF-8
Moduł perla Text::BasicTemplate - prosty moduł do analizowania wzorców
tekstowych, HTML i ogólnych.

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
%doc Changes README
%{perl_vendorlib}/Text/BasicTemplate.pm
# empty autosplit.ix
#%dir %{perl_vendorlib}/auto/Text/BasicTemplate
#%%{perl_vendorlib}/auto/Text/BasicTemplate/autosplit.ix
%{_mandir}/man3/*
