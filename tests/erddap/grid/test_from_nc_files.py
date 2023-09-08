from pathlib import Path

from dataset_catalog.erddap import erddap_datasets
from dataset_catalog.erddap.dataset.grid.from_nc_files import GridFromNcFiles

from_nc_files_path = Path(__file__).parent / "../examples/grid/from_nc_files.xml"


def test_load_nc_files():
    # datasets_xml = erddap_datasets.ErddapDatasets.from_xml(from_nc_files_path.read_bytes())
    dataset = GridFromNcFiles.from_xml(from_nc_files_path.read_bytes())

    print(f"source={from_nc_files_path.read_text()}")
    print(f"parsed={dataset}")
    print(f"rendered={dataset.to_xml(pretty_print=True).decode('utf-8')}")

    assert dataset.dataset_id == "WW3_GulfOfMaine_latest"
    assert dataset.type == "EDDGridFromNcFiles"
    assert dataset.active == True

    found_att_names = {att.name for att in dataset.add_attributes}
    some_known_att_names = {"cdm_data_type", "Conventions", "infoUrl"}
    assert found_att_names.issuperset(some_known_att_names)

    found_att_values = {att.value for att in dataset.add_attributes}
    some_known_att_values = {"Grid", "http://www.neracoos.org"}
    assert found_att_values.issuperset(some_known_att_values)

    assert {var.source_name for var in dataset.axis_variables} == {"time", "lat", "lon"}
    assert {var.destination_name for var in dataset.axis_variables} == {
        "time",
        "latitude",
        "longitude",
    }

    assert {var.source_name for var in dataset.data_variables} == {"hs", "swp", "dir"}
    assert {var.destination_name for var in dataset.data_variables} == {
        "hs",
        "swp",
        "dir",
    }

    data_var = dataset.data_variables[2]

    assert data_var.source_name == "dir"
    assert data_var.add_attributes[3].name == "standard_name"
    assert data_var.add_attributes[3].value == "sea_surface_wave_to_direction"


def test_load_nc_files_union():
    datasets_xml = erddap_datasets.ErddapDatasets.from_xml(
        f"<erddapDatasets>{from_nc_files_path.read_text()}</erddapDatasets>",
    )

    dataset = datasets_xml.datasets[0]

    print(f"source={from_nc_files_path.read_text()}")
    print(f"parsed={dataset}")
    print(f"rendered={dataset.to_xml(pretty_print=True).decode('utf-8')}")

    assert dataset.dataset_id == "WW3_GulfOfMaine_latest"
    assert dataset.type == "EDDGridFromNcFiles"
    assert dataset.active == True

    assert {var.source_name for var in dataset.axis_variables} == {"time", "lat", "lon"}
    assert {var.destination_name for var in dataset.axis_variables} == {
        "time",
        "latitude",
        "longitude",
    }

    assert {var.source_name for var in dataset.data_variables} == {"hs", "swp", "dir"}
    assert {var.destination_name for var in dataset.data_variables} == {
        "hs",
        "swp",
        "dir",
    }

    data_var = dataset.data_variables[2]
    print(data_var)

    assert data_var.source_name == "dir"
    assert data_var.add_attributes[3].name == "standard_name"
    assert data_var.add_attributes[3].value == "sea_surface_wave_to_direction"
