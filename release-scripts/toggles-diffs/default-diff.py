"""
Generates a report of what defaults have changed for existing flags

Usage:
1. Generate or download the previous release's doc build (`make xml` in the edx-platform/docs directory)
   * Note: You will need a new virtualenv with that release's correct Python version & requirements (`make requirements`) installed
   * Note: This may be available already from the previous release's release notes writer, saving the pain of setting up a legacy environment.
2. Rename the output `_build/xml` directory to `release-name-xml` (eg, `teak-xml`)
3. Do steps 1 & 2 in a new virtualenv for the current release (so you'll have a new directory, `ulmo-xml`)
4. Move the two `release-name-xml` folders to a new directory where this script lives
5. Run the following commands in this directory:
   * git diff --no-index teak-xml/xml/references/settings.xml ulmo-xml/xml/references/settings.xml > settings-diff.txt
   * git diff --no-index teak-xml/xml/references/featuretoggles.xml ulmo-xml/xml/references/featuretoggles.xml > featuretoggles-diff.txt
6. Run the following commands:
   * python3 default-diff.py settings-diff.txt
   * python3 default-diff.py featuretoggles-diff.txt

The output will be generated in ddoutput-settings-diff.txt and ddoutput-featuretoggles-diff.txt, formatted for RST.
"dd" stands for the name of this script, as opposed to "settings-flags-diff.py" script
"""

import sys
import re


# Get the file path from the command line argument
file_path = sys.argv[1]
output_file_path = "ddoutput-" + file_path

# Read the file
with open(file_path, 'r') as file:
   lines = file.readlines()

# Initialize output list
result_lines = []

# Variables to store the current state
current_section = None
previous_default_value = None
new_default_value = None


# Determine the type of file (settings or feature toggles)
is_feature_toggle = any('<section ids="featuretoggle-' in line for line in lines)
is_setting = any('<section ids="setting-' in line for line in lines)

# var for HTML that starts a new section stanza
section_start = "<section"

# Process each line
for line in lines:
       if section_start in line:
           # Reset state at the start of a new section
           current_section = None
           previous_default_value = None
           new_default_value = None

       added_removed = line.startswith("+") or line.startswith("-")
       # Check if it is the start of a section and not a new or deleted toggle/setting, we're only looking for
       # existing toggles/settings that have changed default values
       if not added_removed:   
           if is_feature_toggle:
               # Should match either pattern
               # +        <section ids="featuretoggle-ENABLE_CODEJAIL_DARKLAUNCH">
               # +        <section ids="featuretoggle-FEATURES['ENABLE_BLAKE2B_HASHING']">
               # -        <section ids="featuretoggle-order_history.redirect_to_microfrontend"> 
               section_match = re.search(r'<section ids="featuretoggle-(.*)">', line)

           # Otherwise it is a setting
           elif is_setting:
               section_match = re.search(r'<section ids="setting-([A-Z_]+)">', line)

        #    else:
        #        # Reset state and move on
        #        current_section = None
        #        previous_default_value = None
        #        new_default_value = None
        #        continue

       # If we found a section, we grab the name of the section
       # Save as current_section for the next iteration of the loop
       if section_match:
           current_section = section_match.group(1)

       else:
           # Check if it is a line within a section, determined by previous loop
           if current_section:
               # Extract the default value from this line
               default_match = re.search(r'Default: <literal>(.*)</literal>', line)

               # If we found a default on a removed line, save it as the previous default
               if default_match and line.startswith("-"):
                   previous_default_value = default_match.group(1)
                   continue

               # If we found a default on an added line, save it as the new default
               if default_match and line.startswith("+"):
                   new_default_value = default_match.group(1)
              
               # If we find a changed default value, create an output line
               if previous_default_value and new_default_value:
                   print(f"Writing line for {current_section}")
                   output_line = f"* {current_section}: Changed default value! Previous: {previous_default_value}; Now: {new_default_value}\n\n"
                   result_lines.append(output_line)
                   # Reset state here, otherwise it will duplicate this line for the rest of the section
                   current_section = None
                   previous_default_value = None
                   new_default_value = None




# Write the transformed lines back to the file
with open(output_file_path, 'w') as file:
   if result_lines == []:
      file.writelines("No changed default values\n")
   else:   
      file.writelines(result_lines)

print(f"Wrote output to {output_file_path}")