# revision 17514
# category Package
# catalog-ctan /macros/latex/contrib/mslapa
# catalog-date 2010-03-20 19:23:31 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-mslapa
Version:	20100320
Release:	5
Summary:	Michael Landy's APA citation style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mslapa
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mslapa.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mslapa.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX and BibTeX style files for a respectably close
approximation to APA (American Psychological Association)
citation and reference style.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100320-2
+ Revision: 754180
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100320-1
+ Revision: 719076
- texlive-mslapa
- texlive-mslapa
- texlive-mslapa
- texlive-mslapa

