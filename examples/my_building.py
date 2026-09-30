"""
Building definition (BUI) for pyBuildingEnergy / ISO 52016-1.
Copied from examples/new_building.py - edit this file to describe YOUR building.
See the notes in run_demand.py for what the main fields mean.
"""

BUI = {
    "building": {
        "name": "Archetype_ITA_SFH_2010",
        "azimuth_relative_to_true_north": 0,
        "latitude": 41.9,
        "longitude": 12.5,
        "exposed_perimeter": 40,
        "height": 6,
        "wall_thickness": 0.35,
        "n_floors": 2,
        "building_type_class": "Residential_apartment",
        "adj_zones_present": False,
        "number_adj_zone": 0,
        "net_floor_area": 120,
        "construction_class": "class_i",
        "construction_year": "2010-today",
        "country": "Italy"
    },
    "adjacent_zones": [
        {
            "name": "adj_1",
            "orientation_zone": {
                "azimuth": 0.0
            },
            "area_facade_elements": [
                20,
                60,
                30,
                30,
                50,
                50
            ],
            "typology_elements": [
                "OP",
                "OP",
                "OP",
                "OP",
                "GR",
                "OP"
            ],
            "transmittance_U_elements": [
                0.8196721311475411,
                0.8196721311475411,
                0.8196721311475411,
                0.8196721311475411,
                0.5156683855612851,
                1.162633192818565
            ],
            "orientation_elements": [
                "NV",
                "SV",
                "EV",
                "WV",
                "HOR",
                "HOR"
            ],
            "volume": 300.0,
            "building_type_class": "Residential_apartment",
            "a_use": 50.0
        },
        {
            "name": "adj_2",
            "orientation_zone": {
                "azimuth": 180.0
            },
            "area_facade_elements": [
                20,
                60,
                30,
                30,
                50,
                50
            ],
            "typology_elements": [
                "OP",
                "OP",
                "OP",
                "OP",
                "GR",
                "OP"
            ],
            "transmittance_U_elements": [
                0.8196721311475411,
                0.8196721311475411,
                0.8196721311475411,
                0.8196721311475411,
                0.5156683855612851,
                1.162633192818565
            ],
            "orientation_elements": [
                "NV",
                "SV",
                "EV",
                "WV",
                "HOR",
                "HOR"
            ],
            "volume": 300.0,
            "building_type_class": "Residential_apartment",
            "a_use": 50.0
        }
    ],
    "building_surface": [
        {
            "name": "Roof surface",
            "type": "opaque",
            "area": 130.0,
            "sky_view_factor": 1.0,
            "u_value": 2.2,
            "solar_absorptance": 0.4,
            "thermal_capacity": 741500.0,
            "orientation": {
                "azimuth": 0.0,
                "tilt": 0.0
            },
            "name_adj_zone": None,
            "height": 10.0,
            "length": 13.0
        },
        {
            "name": "Opaque north surface",
            "type": "opaque",
            "area": 30.0,
            "sky_view_factor": 0.5,
            "u_value": 1.4,
            "solar_absorptance": 0.4,
            "thermal_capacity": 1416240.0,
            "orientation": {
                "azimuth": 0.0,
                "tilt": 90.0
            },
            "name_adj_zone": "adj_1",
            "height": 10.0,
            "length": 3.0
        },
        {
            "name": "Opaque south surface",
            "type": "opaque",
            "area": 30.0,
            "sky_view_factor": 0.5,
            "u_value": 1.4,
            "solar_absorptance": 0.4,
            "thermal_capacity": 1416240.0,
            "orientation": {
                "azimuth": 180.0,
                "tilt": 90.0
            },
            "name_adj_zone": "adj_2",
            "height": 10.0,
            "length": 3.0
        },
        {
            "name": "Opaque east surface",
            "type": "opaque",
            "area": 30.0,
            "sky_view_factor": 0.5,
            "u_value": 1.2,
            "solar_absorptance": 0.6,
            "thermal_capacity": 1416240.0,
            "orientation": {
                "azimuth": 90.0,
                "tilt": 90.0
            },
            "name_adj_zone": None,
            "height": 10.0,
            "length": 3.0
        },
        {
            "name": "Opaque west surface",
            "type": "opaque",
            "area": 30.0,
            "sky_view_factor": 0.5,
            "u_value": 1.2,
            "solar_absorptance": 0.7,
            "thermal_capacity": 1416240.0,
            "orientation": {
                "azimuth": 270.0,
                "tilt": 90.0
            },
            "name_adj_zone": None,
            "height": 10.0,
            "length": 3.0
        },
        {
            "name": "Slab to ground",
            "type": "opaque",
            "area": 100.0,
            "sky_view_factor": 0.5,
            "u_value": 1.6,
            "solar_absorptance": 0.6,
            "thermal_capacity": 405801.0,
            "orientation": {
                "azimuth": 0.0,
                "tilt": 0.0
            },
            "name_adj_zone": None,
            "height": 10.0,
            "length": 10.0
        },
        {
            "name": "Transparent east surface",
            "type": "transparent",
            "area": 3.0,
            "sky_view_factor": 0.5,
            "u_value": 5.0,
            "solar_absorptance": 0.5,
            "thermal_capacity": 0.0,
            "orientation": {
                "azimuth": 90.0,
                "tilt": 90.0
            },
            "name_adj_zone": None,
            "height": 2.0,
            # "length": 1.0,
            "g_value": 0.726,
            "width": 1.0,
            "parapet": 1.1,
            "shading": False,
            "shading_type": "horizontal_overhang",
            "width_or_distance_of_shading_elements": 0.5,
            "overhang_properties": {
                "width_of_horizontal_overhangs": 1.0
            }
        },
        {
            "name": "Transparent west surface",
            "type": "transparent",
            "area": 5.0,
            "sky_view_factor": 0.5,
            "u_value": 5.0,
            "solar_absorptance": 0.5,
            "thermal_capacity": 0.0,
            "orientation": {
                "azimuth": 270.0,
                "tilt": 90.0
            },
            "name_adj_zone": None,
            "height": 2.0,
            # "length": 1.0,
            "g_value": 0.726,
            "width": 1.0,
            "parapet": 1.1,
            "shading": False,
            "shading_type": "horizontal_overhang",
            "width_or_distance_of_shading_elements": 0.5,
            "overhang_properties": {
                "width_of_horizontal_overhangs": 1.0
            }
        }
    ],
    "units": {
        "area": "m\u00b2",
        "u_value": "W/m\u00b2K",
        "thermal_capacity": "J/kgK",
        "azimuth": "degrees (0=N, 90=E, 180=S, 270=W)",
        "tilt": "degrees (0=horizontal, 90=vertical)",
        "internal_gain": "W/m\u00b2",
        "internal_gain_profile": "Normalized to 0-1",
        "HVAC_profile": "0: off, 1: on"
    },
    "building_parameters": {
        "temperature_setpoints": {
            "heating_setpoint": 20.0,
            "heating_setback": 17.0,
            "cooling_setpoint": 26.0,
            "cooling_setback": 30.0,
            "units": "\u00b0C"
        },
        "system_capacities": {
            "heating_capacity": 10000000.0,
            "cooling_capacity": 12000000.0,
            "units": "W"
        },
        "ventilation": {
            "ventilation_type": "occupancy",
            "flow_rate_per_person": 0.3,
            "units": "l/(s m2)",
            # Keep a numeric fallback because ventilation.py always casts this field to float().
            "custom_heat_transfer_coefficient_ventilation": 0.0,
            "info": "ventilation type could be: 1) Occupancy 2) occupancy 3)custom. If custum the value of custom_heat_transfer_coefficient_ventilation is used"
        },
        "internal_gains": [
            {
                "name": "occupants",
                "full_load": 4.2,
                "weekday": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.5,
                    0.5,
                    0.5,
                    0.1,
                    0.1,
                    0.1,
                    0.1,
                    0.2,
                    0.2,
                    0.2,
                    0.5,
                    0.5,
                    0.5,
                    0.8,
                    0.8,
                    0.8,
                    1.0,
                    1.0
                ],
                "weekend": [
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.5,
                    0.5,
                    0.5,
                    0.1,
                    0.1,
                    0.1,
                    0.1,
                    0.2,
                    0.2,
                    0.2,
                    0.5,
                    0.5,
                    0.5,
                    0.8,
                    0.8,
                    0.8,
                    1.0,
                    1.0
                ]
            },
            {
                "name": "appliances",
                "full_load": 3.0,
                "weekday": [
                    0.5,
                    0.5,
                    0.5,
                    0.5,
                    0.5,
                    0.5,
                    0.5,
                    0.7,
                    0.7,
                    0.5,
                    0.5,
                    0.6,
                    0.6,
                    0.6,
                    0.6,
                    0.5,
                    0.5,
                    0.7,
                    0.7,
                    0.8,
                    0.8,
                    0.8,
                    0.6,
                    0.6
                ],
                "weekend": [
                    0.5,
                    0.5,
                    0.5,
                    0.5,
                    0.5,
                    0.5,
                    0.5,
                    0.7,
                    0.7,
                    0.5,
                    0.5,
                    0.6,
                    0.6,
                    0.6,
                    0.6,
                    0.5,
                    0.5,
                    0.7,
                    0.7,
                    0.8,
                    0.8,
                    0.8,
                    0.6,
                    0.6
                ]
            },
            {
                "name": "lighting",
                "full_load": 3.0,
                "weekday": [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.15,
                    0.15,
                    0.15,
                    0.15,
                    0.05,
                    0.05,
                    0.05,
                    0.05,
                    0.05,
                    0.05,
                    0.2,
                    0.2,
                    0.2,
                    0.2,
                    0.2,
                    0.2,
                    0.15,
                    0.15
                ],
                "weekend": [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.15,
                    0.15,
                    0.15,
                    0.15,
                    0.05,
                    0.05,
                    0.05,
                    0.05,
                    0.05,
                    0.05,
                    0.2,
                    0.2,
                    0.2,
                    0.2,
                    0.2,
                    0.2,
                    0.15,
                    0.15
                ]
            }
        ],
        "construction": {
            "wall_thickness": 0.35,
            "thermal_bridge_heat_W_K": 2.0,
            "units": "m (for thickness), W/K (for total thermal-bridge coefficient)"
        },
        "climate_parameters": {
            "coldest_month": 1,
            "units": "1-12 (January-December)"
        },
        "heating_profile": {
            "weekday": [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                0.0
            ],
            "weekend": [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                0.0
            ]
        },
        "cooling_profile": {
            "weekday": [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                0.0
            ],
            "weekend": [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                0.0,
                0.0,
                0.0
            ]
        },
        "ventilation_profile": {
            "weekday": [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                0.0
            ],
            "weekend": [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                1.0,
                0.0
            ]
        }
    }
}
