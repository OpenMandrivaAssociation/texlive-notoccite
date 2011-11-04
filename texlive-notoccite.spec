# revision 18129
# category Package
# catalog-ctan /macros/latex/contrib/notoccite
# catalog-date 2010-05-11 12:36:30 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-notoccite
Version:	20100511
Release:	1
Summary:	Prevent trouble from citations in table of contents, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/notoccite
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notoccite.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notoccite.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
If you have \cite commands in \section-like commands, or in
\caption, the citation will also appear in the table of
contents, or list of whatever. If you are also using an unsrt-
like bibliography style, these citations will come at the very
start of the bibliography, which is confusing. This package
suppresses the effect.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/notoccite/notoccite.sty
%doc %{_texmfdistdir}/doc/latex/notoccite/notoccite.pdf
%doc %{_texmfdistdir}/doc/latex/notoccite/notoccite.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
