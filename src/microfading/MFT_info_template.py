beam_FWHM = {
    '1': 590,
    '2': 610,
    '3': 730,
    '4': 560,
    '5': 580,
    '6': 460
}



device_info = ["[DEVICE INFO]",
        "device",
        "measurement_mode",
        "zoom",
        "iris",
        "geometry",
        "distance_ill_mm",
        "distance_coll_mm",
        "fiber_fading",
        "fiber_ill",
        "fiber_coll",
        "lamp_fading",
        "lamp_ill",
        "filter_fading",
        "filter_ill",
        "white_ref",
]

analysis_info = [
    "[ANALYSIS INFO]",
        "meas_id",
        "group",
        "group_description",
        "background",
        "specular_component",
        "integration_time_ms",
        "average",
        "duration_min",
        "interval_sec",
        "measurements_N",
        "illuminant",
        "observer",
]

beam_info = [
    "[BEAM INFO]",
        "beam_photo",
        "resolution_micron/pixel",
        "FWHM_micron",
        "current_mA",
        "power_mW",
        "luminuous_flux_lm",
        "irradiance_W/m**2",        
        "illuminance_Mlx",
]





template = {
    "parameter": [
        "[SINGLE MICRO-FADING ANALYSIS]",
        "author",
        "date_time",
        "comment",
        "[PROJECT DATA]",
        "laboratorium",
        "project_id",
        "project_leader",        
        "start_date",
        "end_date",                
        "[OBJECT DATA]",
        "institution",
        "object_id",
        "object_category",
        "object_type",
        "object_technique",
        "object_title",
        "object_name",
        "object_creator",
        "object_date",
        "object_support",
        "color",
        "colorants",
        "colorants_name",
        "binding",
        "ratio",        
        "thickness_microns",
        "status",
        "[DEVICE DATA]",
        "device",
        "measurement_mode",
        "zoom",
        "iris",
        "geometry",
        "distance_ill_mm",
        "distance_coll_mm",
        "fiber_fading",
        "fiber_ill",
        "fiber_coll",
        "lamp_fading",
        "lamp_ill",
        "filter_fading",
        "filter_ill",
        "white_ref",
        "[ANALYSIS DATA]",
        "meas_id",
        "group",
        "group_description",
        "background",
        "specular_component",
        "integration_time_ms",
        "average",
        "duration_min",
        "interval_sec",
        "measurements_N",
        "illuminant",
        "observer",
        "[BEAM DATA]",
        "beam_photo",
        "resolution_micron/pixel",
        "FWHM_micron",
        "current_mA",
        "power_mW",
        "irradiance_W/m**2",
        "luminuous_flux_lm",
        "illuminance_Mlx",
        "[RESULTS]",
        "totalDose_He_MJ/m**2",
        "totalDose_Hv_Mlxh",
        "fittedEqHe_dE00",
        "fittedEqHv_dE00",
        "fittedRate_dE00_at_2Mlxh",
        "fittedRate_dE00_at_20MJ/m**2",        
        "dE00_at_300klxh",
        "dE00_at_3MJ/m**2",        
        "dEab_final",
        "dE00_final",
        "dR_VIS_final",
        "Hv_at_1dE00",
        "BWSE",
    ]
}
