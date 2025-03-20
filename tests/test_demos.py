import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def test_execute_plotting_demo():
    """
    Test that executes the plotting-demo notebook and saves the executed notebook to /docs/.
    """
    # Setup paths
    notebook_path = os.path.join("notebooks", "plotting-demo.ipynb")
    output_dir = "docs"
    output_path = os.path.join(output_dir, "plotting-demo.ipynb")

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Load the notebook
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook = nbformat.read(f, as_version=4)

    # Execute the notebook
    execute_preprocessor = ExecutePreprocessor(timeout=600, kernel_name="python3")
    execute_preprocessor.preprocess(
        notebook, {"metadata": {"path": os.path.dirname(notebook_path)}}
    )

    # Save the executed notebook
    with open(output_path, "w", encoding="utf-8") as f:
        nbformat.write(notebook, f)

    # Assert the file exists (this is what pytest will use to determine test success)
    assert os.path.exists(output_path), f"Output file {output_path} was not created"
