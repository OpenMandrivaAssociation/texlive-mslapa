%global tl_name mslapa
%global tl_revision 76790

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Michael Landys APA citation style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mslapa
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mslapa.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mslapa.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX and BibTeX style files for a respectably close approximation to
APA (American Psychological Association) citation and reference style.

