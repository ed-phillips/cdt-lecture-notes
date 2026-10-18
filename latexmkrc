# latexmk configuration, used both locally and by Overleaf.
#
# Locally, run `latexmk` in the repository root to build lecture_notes.pdf.
# On Overleaf, also set Menu > Compiler to LuaLaTeX and
# Menu > Main document to lecture_notes.tex.

# The class needs fontspec and unicode-math, so compile with LuaLaTeX
$pdf_mode = 4;

@default_files = ('lecture_notes.tex');

# Run makeglossaries automatically (only matters once frontmatter/glossary.tex exists)
add_cus_dep('glo', 'gls', 0, 'run_makeglossaries');
add_cus_dep('acn', 'acr', 0, 'run_makeglossaries');
add_cus_dep('glo-abr', 'gls-abr', 0, 'run_makeglossaries');

sub run_makeglossaries {
    my ($base_name, $path) = fileparse($_[0]);
    pushd $path;
    my $return = system "makeglossaries", $base_name;
    popd;
    return $return;
}

push @generated_exts, 'glo', 'gls', 'glg', 'acn', 'acr', 'alg', 'glo-abr', 'gls-abr', 'glg-abr', 'ist';
