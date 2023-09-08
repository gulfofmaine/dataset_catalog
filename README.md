## dataset_catalog

Load and generate ERDDAP datasets.xml catalogs with
[pydantic-xml](https://pydantic-xml.readthedocs.io/en/latest/index.html),
and use those configs to load Xarray datasets and Pandas dataframes.

Additionally we should be able to use Xarray datasets and Pandas dataframes
to template out a config.

In the future it may support other catalog types like THREDDS...

```py
from dataset_catalog.erddap.dataset import Attribute, AxisVariable, DataVariable
from dataset_catalog.erddap.dataset.grid.from_nc_files import GridFromNcFiles

dataset = GridFromNcFiles(
    dataset_id="WaveWatch3",
    file_dir=Path("/datastore/models/WW3"),
    file_name_regex="GulfOfMaine\\.nc",
    add_attributes=[
        Attribute(name="cdm_data_type", value="Grid"),
        Attribute(name='Conventions', value='COARDS, CF-1.6'),
        Attribute(name='infoUrl', value='http://www.neracoos.org'),
    ],
    axis_variables=[
        AxisVariable(
            source_name='time',
            destination_name='time',
            add_attributes=[
                Attribute(name='ioos_category', value='Time'),
                Attribute(name='long_name', value='Time'),
                Attribute(name='standard_name', value='time')
            ]
        ),
        AxisVariable(
            source_name='lat',
            destination_name='latitude',
            add_attributes=[
                Attribute(name='ioos_category', value='Location'),
                Attribute(name='long_name', value='Latitude'),
                Attribute(name='standard_name', value='latitude')
            ]
        ),
        AxisVariable(
            source_name='lon',
            destination_name='longitude',
            add_attributes=[
                Attribute(name='ioos_category', value='Location'),
                Attribute(name='long_name', value='Longitude'),
                Attribute(name='standard_name', value='longitude')
            ]
        )
    ],
    data_variables=[
        DataVariable(source_name='hs', destination_name='hs', add_attributes=[
            Attribute(name="ioos_category", value="Surface Waves")
        ])
    ]
)

print(dataset.to_xml(pretty_print=True))
```

```xml
<dataset type="EDDGridFromNcFiles" datasetID="WaveWatch3" active="true">
    <fileDir>/datastore/models/WW3/</fileDir>
    <fileNameRegex>GulfOfMaine\.nc</fileNameRegex>
    <addAttributes>
        <att name="cdm_data_type">Grid</att>
        <att name="Conventions">COARDS, CF-1.6</att>
        <att name="infoUrl">http://www.neracoos.org</att>
    </addAttributes>
    <axisVariable>
        <sourceName>time</sourceName>
        <destinationName>time</destinationName>
        <addAttributes>
            <att name="ioos_category">Time</att>
            <att name="long_name">Time</att>
            <att name="standard_name">time</att>
        </addAttributes>
    </axisVariable>
    <axisVariable>
        <sourceName>lat</sourceName>
        <destinationName>latitude</destinationName>
        <addAttributes>
            <att name="ioos_category">Location</att>
            <att name="long_name">Latitude</att>
            <att name="standard_name">latitude</att>
        </addAttributes>
    </axisVariable>
    <axisVariable>
        <sourceName>lon</sourceName>
        <destinationName>longitude</destinationName>
        <addAttributes>
            <att name="ioos_category">Location</att>
            <att name="long_name">Longitude</att>
            <att name="standard_name">longitude</att>
        </addAttributes>
    </axisVariable>
    <dataVariable>
        <sourceName>hs</sourceName>
        <destinationName>hs</destinationName>
        <addAttributes>
            <att name="ioos_category">Surface Waves</att>
        </addAttributes>
    </dataVariable>
</dataset>
```
