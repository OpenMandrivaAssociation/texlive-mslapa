Name:		texlive-mslapa
Version:	20180303
Release:	1
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
%{_texmfdistdir}/bibtex/bst/mslapa
%{_texmfdistdir}/tex/latex/mslapa
%doc %{_texmfdistdir}/doc/latex/mslapa

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
