#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-Caller
Version  : 2.06
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Devel-Caller-2.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Devel-Caller-2.06.tar.gz
Summary  : 'meatier versions of C<caller>'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Devel-Caller-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(PadWalker)

%description
No detailed description available

%package dev
Summary: dev components for the perl-Devel-Caller package.
Group: Development
Provides: perl-Devel-Caller-devel = %{version}-%{release}
Requires: perl-Devel-Caller = %{version}-%{release}

%description dev
dev components for the perl-Devel-Caller package.


%package perl
Summary: perl components for the perl-Devel-Caller package.
Group: Default
Requires: perl-Devel-Caller = %{version}-%{release}

%description perl
perl components for the perl-Devel-Caller package.


%prep
%setup -q -n Devel-Caller-2.06
cd %{_builddir}/Devel-Caller-2.06

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::Caller.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/Devel/Caller.pm
/usr/lib/perl5/vendor_perl/5.30.1/x86_64-linux-thread-multi/auto/Devel/Caller/Caller.so
