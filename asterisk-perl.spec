#TODO - prefix in build section and files
%include	/usr/lib/rpm/macros.perl
Summary:	Asterisk PBX Perl Modules
Summary(pl):	Modu³y Perl-a do Asterisk PBX.
Name:		asterisk-perl
Version:	0.08
Release:	0.1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://asterisk.gnuinter.net/files/%{name}-%{version}.tar.gz
# Source0-md5:	73a47caaff8cafbf78053692f408ceb6
URL:		http://asterisk.gnuinter.net/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
asterisk-perl is a collection of perl modules to be used with the
Asterisk PBX.

%description -l pl
asterisk-perl jest zbiorem modu³ów perl-a u¿ywanych z Asterisk PBX.

%prep
%setup -q

%build
%{__perl} Makefile.PL 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
#??????%%{_libdir}/perl5/5.8.0/%{arch}-pld-linux-thread-multi/auto/asterisk-perl/.packlist
#%{_datadir}/perl5/Asterisk*
#%{_datadir}/perl5/Asterisk/*
#%{_mandir}/man3/Asterisk*
