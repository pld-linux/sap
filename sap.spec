Summary:	A Polish-English-Polish dictionary
Summary(pl):	S³ownik polsko-angielski i angielsko-polski
Name:		sap
Version:	0.2
Release:	1
License:	GPL
Vendor:		Bohdan R. Rau <ethanak@bigfoot.com>
Group:		Applications/Dictionaries
Group(de):	Applikationen/Wörterbücher
Group(pl):	Aplikacje/S³owniki
Source0:	http://www.terravista.pt/Mussulo/1345/sap/%{name}-%{version}.tgz
Patch0:		%{name}-path.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polish English / English Polish dictionary.

%description -l pl
S³ownik polsko-angielski i angielsko-polski.

%prep
%setup -q
%patch0 -p1

%build
cd src
%{__cc} %{rpmcflags} -o sap alt_unistd.c charfilter.c sap.c \
	-DDICTIONARIES_DIRECTORY=\"%{_datadir}/%{name}/\" \
	-DGLOBAL_SAPRC_FULLPATH=\"%{_sysconfdir}/saprc\"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_datadir}/%{name}}

> $RPM_BUILD_ROOT%{_sysconfdir}/saprc
install src/sap $RPM_BUILD_ROOT%{_bindir}
install	lib/dvp_{1,2}.dic $RPM_BUILD_ROOT%{_datadir}/%{name}

gzip -9nf README saprc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/saprc
%attr(755,root,root) %{_bindir}/sap
%{_datadir}/%{name}
