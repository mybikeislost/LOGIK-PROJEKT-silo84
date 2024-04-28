#!/bin/bash

# -------------------------------------------------------------------------- #

# filename: "function_29-create_archive_script.sh"

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section defines the primary functions for the script.
# ========================================================================== #

# Function to create archive script
create_archive_script() {
    local src_flame_archive_script="presets/templates/archive_template"
    local tgt_flame_archive_script="$tgt_flame_archives_dir/$name.sh"

    # Copy the default archive text to a new archiving shell script
    cp "$src_flame_archive_script" "$tgt_flame_archive_script"

    # Add execution permissions to new archiving shell script
    chmod +x "$tgt_flame_archive_script"

    # Set the search and replace strings
    local search_replace=(
        "ArchiveScriptName:$name.sh"
        "ArchiveScriptProjekt:$name"
        "ScriptCreationDate:$NOW"
        "LogikProjektClient:$client"
        "LogikProjektCampaign:$campaign"
        "LogikProjektName:$nickname"
        "FlameSoftwareVersion:$max_sanitized_sw_ver"
        "FlameWorkstationName:$workstation_name"
    )

    # Use sed to replace the strings in the shell script
    if [ "$operating_system" == "Linux" ]; then
        for pair in "${search_replace[@]}"; do
            IFS=':' read -r search replace <<< "$pair"
            sed -i "s|$search|$replace|g" "$tgt_flame_archive_script"
        done
    elif [ "$operating_system" == "macOS" ]; then
        for pair in "${search_replace[@]}"; do
            IFS=':' read -r search replace <<< "$pair"
            sed -i '' "s|$search|$replace|g" "$tgt_flame_archive_script"
        done
    else
        echo "Unsupported operating system."
        return 1
    fi

    echo -e "  logik projekt flame archive script created:\n"
    echo -e "  $(basename "$tgt_flame_archive_script")"
    echo -e "\n$separator\n"

}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Check if the script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    create_archive_script
fi

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #