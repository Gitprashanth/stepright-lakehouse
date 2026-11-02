"""
Shared utilities for stepright ingestion pipeline
"""

from pyspark.sql import SparkSession

def get_catalog() -> str:
    """
    Returns the target catalog for this pipeline run. 

    Reads the 'stepright.catalog' key from the pipeline's configuration field
    Defaults to 'dev' so the pipelie still works during interactive developlement, before any 
    configuration value has been set
    """

    spark = SparkSession.getActiveSession()
    return spark.conf.get("stepright.catalog", "dev")

def landing_path(subfolder: str) -> str:
    """
    Builds a path into ithis project's landing volume for a given source subfolder.
    """
    return f"/Volumes/{get_catalog()}/stepright/landing/{subfolder}"




















