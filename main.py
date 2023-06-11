import dlt

from notion import notion_databases


def load_databases() -> None:
    """Loads all databases from a Notion workspace which have been shared with
    an integration.
    """
    pipeline = dlt.pipeline(
        pipeline_name="notion",
        destination='bigquery',
        dataset_name="notion_data",
    )

    data = notion_databases()

    info = pipeline.run(data)
    print(info)
    return "data loaded successfully"

def mainpipelinenotion(request):
    return load_databases()
    
