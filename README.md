# preparation

The preparation project for algorithms and system design.

## Prerequisites

- Python >= 3.13
- [uv](https://docs.astral.sh/uv/)

## Setup

1.  **Install dependencies:**

    ```bash
    uv sync
    ```

2.  **Install Jupyter Kernel:**

    To use this virtual environment in Jupyter Notebooks, you need to register it as a kernel:

    ```bash
    uv run python -m ipykernel install --user --name=preparation --display-name "Python (preparation)"
    ```

3. **Run Jupyter Notebook:**

    To run the notebook using the internal kernel, run this

    ```bash
    uv run jupyter notebook
    ```