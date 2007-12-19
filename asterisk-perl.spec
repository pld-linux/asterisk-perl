#
# TODO:
# - License, name perl-Asterisk?
#
%include	/usr/lib/rpm/macros.perl
Summary:	Asterisk PBX Perl Modules
Summary(pl.UTF-8):	Moduły Perla do centralki (PBX-a) Asterisk
Name:		asterisk-perl
Version:	0.10
Release:	0.1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Development/Languages/Perl
Source0:	http://asterisk.gnuinter.net/files/%{name}-%{version}.tar.gz
# Source0-md5:	27fd83d417c556e83cfe7f5dcb40aba0
URL:		http://asterisk.gnuinter.net/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
asterisk-perl is a collection of Perl modules to be used with the
Asterisk PBX.

%description -l pl.UTF-8
asterisk-perl jest zbiorem modułów Perla używanych z pakietem Asterisk
PBX.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/%{name}/.packlist

rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/auto/asterisk-perl/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{_mandir}/man3/*
%{perl_vendorlib}/Asterisk
%{perl_vendorlib}/Asterisk.pm
