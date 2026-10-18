# Lecture notes

A LaTeX handout of lecture notes plus the Python code that generates its
figures. The repo is synced to an Overleaf project via Overleaf's GitHub
integration, and is a fork of https://github.com/maurovm/thesis_template.

## Layout

- `lecture_notes.tex`: main file (the Overleaf main document). It holds the metadata, class options and the `\include` list of lectures.
- `lectures/lecture_NN.tex`: one chapter per lecture. `lectures/references.bib` holds the bibliography.
- `frontmatter/`: the title page, plus optional `abstract.tex`, `acknowledgements.tex` and `glossary.tex`. The class only includes a page if its file exists.
- `code/`: a uv project (`lecture_figures` package). Each figure is a module in `code/src/lecture_figures/figures/` with a `make()` function. Shared styling lives in `style.py`.
- `figures/generated/`: PDF output of `code/`. **Commit these files**, because Overleaf cannot run Python.
- `figures/`: hand-made images, plus the upstream sample images.

## Keeping in sync with upstream

`upstream` is the remote for maurovm/thesis_template. Do **not** edit, move or
delete upstream files (`oxengthesis.cls`, `sample_dphil_thesis.tex`, `chap_*.tex`,
`appendix_*.tex`, `titlepage-*.tex`, the root front matter `.tex` files, `README.md`,
`.gitignore`, `compile_document.sh`, `figures/*.png`). Customise through
class options and macro overrides in `lecture_notes.tex` instead. To pull
upstream changes:

```bash
git fetch upstream && git merge upstream/master
```

## Commands

- Regenerate all figures: `cd code && uv run make-figures`. To regenerate only some, pass their names, e.g. `uv run make-figures example_signal`.
- Build the PDF locally: `latexmk` in the repo root. This needs LuaLaTeX (MacTeX). The output `lecture_notes.pdf` is gitignored.
- Clean the LaTeX aux files: `latexmk -c`.

## Overleaf sync workflow

Sync is manual on both sides, so avoid editing the same file in Overleaf and
locally between syncs.

- Local → Overleaf: commit and push to `master`, then in Overleaf use Menu → GitHub → Pull changes.
- Overleaf → local: in Overleaf, use Menu → GitHub → Push changes, then run `git pull` here.

Overleaf settings: Compiler = LuaLaTeX, Main document = `lecture_notes.tex`.

## Conventions

- Size figures with `style.figure()`, which matches the text width (16 cm), and include them at `width=\linewidth`. Use `style.COLOURS` in their fixed order.
- Label lectures `chap:lecture_NN`, and label figures `fig:<module_name>` to match the generating script.
