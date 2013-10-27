#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Unicode
%define		pnam	EastAsianWidth
%include	/usr/lib/rpm/macros.perl
Summary:	Unicode::EastAsianWidth - East Asian Width properties
Summary(pl.UTF-8):	Unicode::EastAsianWidth - właściwości szerokości znaków wschodnioazjatyckich
Name:		perl-Unicode-EastAsianWidth
Version:	1.33
Release:	1
License:	unrestricted
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Unicode/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c33367b020995ff4fdd20e2b3cdae6be
URL:		http://search.cpan.org/dist/Unicode-EastAsianWidth/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.59
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provide user-defined Unicode properties that deal with
width status of East Asian characters, as specified in
<http://www.unicode.org/unicode/reports/tr11/>.

%description -l pl.UTF-8
Ten moduł udostępnia zdefiniowane przez użytkownika właściwości
Unicode dotyczące stanu szerokości znaków wschodnioazjatyckich,
zgodnie ze specyfikacją
<http://www.unicode.org/unicode/reports/tr11/>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Unicode/EastAsianWidth.pm
%{_mandir}/man3/Unicode::EastAsianWidth.3pm*
