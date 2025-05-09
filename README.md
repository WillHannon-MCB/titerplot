# `Titerplot`

Author: [Will Hannon](https://willhannon.com/)

Plotting viral titers from experiments with a factorial/combinatorial design with [Altair](https://altair-viz.github.io/).

## Install

```bash
# Requires Python > 3.12
pip install titerplot
```

## Use

The primary function of this library is `plot_titers`, which can be imported directly from the package:

```python
from titerplot import plot_titers

# Example usage
plot_titers(
    data,
    titer_col="Titer",
    condition_cols=["Condition_A", "Condition_B", "Condition_C", "Condition_D"],
    facet_col="Facet",
    color_col="Virus"
)
```

For a complete demonstration of the library's capabilities, check out the [plotting demo notebook](docs/plotting-demo.ipynb). For an example of the ideal data format, check out the [dummy_data](data/dummy_titers.csv). 

## Develop

This project uses [Poetry](https://python-poetry.org/) for dependency management and packaging.

### Setup development environment

```bash
# Clone the repository
git clone git@github.com:WillHannon-MCB/titerplot.git
cd titerplot

# Install dependencies with Poetry
poetry install

# Activate the virtual environment
poetry shell
```

### Run tests

Pytest runs the demo notebooks and saves the rendered notebooks to `/docs/`.

```bash
# Run pytest
pytest
```

### Project structure

```
.
├── data/               # Sample data files
├── docs/               # Rendered Demo notebooks
├── notebooks/          # Development notebooks
├── src/                # Source code
│   └── titerplot/      # Main package
├── tests/              # Test files
├── pyproject.toml      # Package configuration
└── poetry.lock         # Locked dependencies
```

## Publish

`titerplot` is published on [PyPI](https://pypi.org/) so that it can be installed with `pip`. A [worflow](.github/workflows/publish.yml) run by Github Actions publishes to PyPI when the tag is updated:

```bash
git tag -a v0.1.0 -m "First release version"
git push origin v0.1.0 
```

Ensure that you've updated the [`CHANGELOG`](CHANGELOG) with specific changes and [pyproject.toml](pyproject.toml) with the same version as the tag. For now, this is handled manually.
