# revision 17514
# category Package
# catalog-ctan /macros/latex/contrib/mslapa
# catalog-date 2010-03-20 19:23:31 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-mslapa
Version:	20100320
Release:	1
Summary:	Michael Landy's APA citation style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mslapa
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mslapa.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mslapa.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
LaTeX and BibTeX style files for a respectably close
approximation to APA (American Psychological Association)
citation and reference style.

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
%{_texmfdistdir}/bibtex/bst/mslapa/mslapa.bst
%{_texmfdistdir}/tex/latex/mslapa/mslapa.sty
%doc %{_texmfdistdir}/doc/latex/mslapa/README
%doc %{_texmfdistdir}/doc/latex/mslapa/bibfile.bib
%doc %{_texmfdistdir}/doc/latex/mslapa/examp.tex
%doc %{_texmfdistdir}/doc/latex/mslapa/mslapa.pdf
%doc %{_texmfdistdir}/doc/latex/mslapa/mslapa.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
