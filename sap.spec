Summary:	An English Polish Dictionary
Summary(pl):	S³ownik Angielsko Polski i Polsko Angielski
Name:		sap
Version:	0.1b
Release:	1
Copyright:	Unknown
Group:		Applications/Dictionaries
Group(pl):	Aplikacje/S³owniki
Vendor:		Bohdan R. Rau <ethanak@bigfoot.com>
Source0:	http://ethanak.sih.pl/%{name}-%{version}.tar.gz
Patch0:		%{name}-path.patch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
English Polish / Polish English Dictionary.

%description -l pl
S³ownik angielsko-polski i polsko-angielski.

%prep
%setup -q -c
%patch0 -p1

%build
gcc "%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}" -o sap sap.c \
	-DDATADIR=\"%{_datadir}\" -DSYSCONFDIR=\"%{_sysconfdir}\"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_sysconfdir}}

install sap $RPM_BUILD_ROOT%{_bindir}
install	lib/sap/dvp_{1,2}.dic $RPM_BUILD_ROOT%{_datadir}/sap/
install .saprc $RPM_BUILD_ROOT%{_sysconfdir}/saprc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.doc
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/saprc
%attr(755,root,root) %{_bindir}/sap
%{_datadir}/%{name}
