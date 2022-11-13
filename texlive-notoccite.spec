Name:		texlive-notoccite
Version:	18129
Release:	1
Summary:	Prevent trouble from citations in table of contents, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/notoccite
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notoccite.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notoccite.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
If you have \cite commands in \section-like commands, or in
\caption, the citation will also appear in the table of
contents, or list of whatever. If you are also using an unsrt-
like bibliography style, these citations will come at the very
start of the bibliography, which is confusing. This package
suppresses the effect.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/notoccite/notoccite.sty
%doc %{_texmfdistdir}/doc/latex/notoccite/notoccite.pdf
%doc %{_texmfdistdir}/doc/latex/notoccite/notoccite.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
