# Lecture notes

A LaTeX handout of lecture notes plus the Python code that generates its
figures. The repo is synced to an Overleaf project via Overleaf's GitHub
integration, and is a fork of https://github.com/maurovm/thesis_template
(the `oxengthesis` class, built on memoir).

Several people may work on this, some editing directly in Overleaf and some
through git with coding agents. Treat Overleaf as a second, equal source of
edits (see "Collaborating" below).

## Layout

- `lecture_notes.tex`: main file (the Overleaf main document). It holds the metadata, class options and the `\include` list of lectures.
- `lectures/lecture_NN.tex`: one chapter per lecture. `lectures/references.bib` holds the bibliography.
- `frontmatter/`: the title page, plus optional `abstract.tex`, `acknowledgements.tex` and `glossary.tex`. The class only includes a page if its file exists.
- `code/`: a uv project (`lecture_figures` package). Each figure is a module in `code/src/lecture_figures/figures/` with a `make()` function. Shared styling lives in `style.py`.
- `figures/generated/`: PDF output of `code/`. **Commit these files**, because Overleaf cannot run Python.
- `figures/`: hand-made images, plus the upstream sample images.
- Everything else in the root (`oxengthesis.cls`, `sample_dphil_thesis.tex`, `chap_*.tex`, ...) is upstream's template and sample content. It is not part of the notes, but is kept so that upstream merges stay clean.

## Common tasks

- **Add a lecture:** create `lectures/lecture_NN.tex` starting with `\chapter{...}\label{chap:lecture_NN}`, then add `\include{lectures/lecture_NN}` to `lecture_notes.tex`.
- **Add a figure from code:**
  1. Add `code/src/lecture_figures/figures/<name>.py` with a `make()` that uses `style.figure()` and `style.save(fig, "<name>")`, using `example_signal.py` as a template.
  2. Run `uv run make-figures <name>`.
  3. Include the figure with `\includegraphics[width=\linewidth]{generated/<name>}` and label it `fig:<name>`.
  4. Commit both the script and the PDF.
- **Add a reference:** add a BibTeX entry to `lectures/references.bib` and cite it with `\cite{key}`.

## Typography

- The document font is Latin Modern Roman, set via `font=` in the `\documentclass` options. The class default (Carlito) is overridden there. Maths uses Latin Modern Math (the class default).
- Figures use matplotlib's bundled `cmr10` (Computer Modern) so they match the text. If the document font changes, update `apply_style()` in `code/src/lecture_figures/style.py` to match and regenerate all figures.
- Other class options (`chapterstyle=`, `headingcolour=`, `11pt`/`12pt`, margins, and memoir options such as `article`) are documented in upstream's `README.md`, under "Package options".

## Keeping in sync with upstream

`upstream` is the remote for maurovm/thesis_template. Do **not** edit, move or
delete upstream files (`oxengthesis.cls`, `sample_dphil_thesis.tex`, `chap_*.tex`,
`appendix_*.tex`, `titlepage-*.tex`, the root front matter `.tex` files, `README.md`,
`.gitignore`, `compile_document.sh`, `figures/*.png`). Customise through
class options and macro overrides in `lecture_notes.tex`, or through files in
`frontmatter/`, instead. To pull upstream changes:

```bash
git fetch upstream && git merge upstream/master
```

## Commands

- Regenerate all figures: `cd code && uv run make-figures`. To regenerate only some, pass their names, e.g. `uv run make-figures example_signal`.
- Build the PDF locally: run `latexmk` in the repo root. The output `lecture_notes.pdf` is gitignored.
- Clean the LaTeX aux files: `latexmk -c`.

The class only compiles with **LuaLaTeX**; XeLaTeX and tectonic fail on its
`microtype` settings. If LuaLaTeX isn't installed locally (it comes with
MacTeX or TeX Live), you can't verify the build there. Say so, and leave
the check to an Overleaf recompile after syncing rather than assuming it
compiles.

## Collaborating and the Overleaf sync

Overleaf only syncs with the `master` branch, and syncing is manual in both
directions:

- Local → Overleaf: commit and push to `master`, then in Overleaf use Menu → GitHub → Pull changes.
- Overleaf → local: in Overleaf, use Menu → GitHub → Push changes, then run `git pull`.

Rules for agents and collaborators:

- **Before starting work, run `git pull`.** If someone may have edited in Overleaf since the last sync, ask them to push from Overleaf first. Edits that are unsynced on both sides lead to merge conflicts.
- Keep commits focused, e.g. one lecture or one figure each, so they are easy to review and to merge with Overleaf edits.
- Larger changes from collaborators can go on a branch with a pull request. They only reach Overleaf once merged into `master`.
- Don't commit build output (`*.aux`, `*.log`, `lecture_notes.pdf`). The root `.gitignore` handles this.
- Don't push or merge into `master` without the repo owner's OK.

Overleaf settings: Compiler = LuaLaTeX, Main document = `lecture_notes.tex`.

## Conventions

- Size figures with `style.figure()`, which matches the text width (16 cm), and include them at `width=\linewidth`. Use `style.COLOURS` in their fixed order.
- Label lectures `chap:lecture_NN`, and label figures `fig:<module_name>` to match the generating script.
