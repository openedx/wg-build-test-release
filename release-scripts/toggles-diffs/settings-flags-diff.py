"""
Generates the new and removed featuretoggles & settings for this release, compared to the last release,
formatted for RST. New featuretoggles & settings will also list their default values.

Usage:
1. Generate or download the previous release's doc build (`make xml` in the edx-platform/docs directory)
   * Note: You will need a new virtualenv with that release's correct Python version & requirements (`make requirements`) installed
   * Note: This may be available already from the previous release's release notes writer, saving the pain of setting up a legacy environment.
2. Rename the output _build/xml directory to `release-name-xml` (eg, `teak-xml`)
3. Do steps 1 & 2 in a new virtualenv for the current release (so you'll have a new directory, `ulmo-xml`)
4. Move the two `release-name-xml` folders to a new directory where this script lives
5. Run the following commands in this directory (old release first, then new release):
   * git diff --no-index teak-xml/xml/references/settings.xml ulmo-xml/xml/references/settings.xml > settings-diff.txt
   * git diff --no-index teak-xml/xml/references/featuretoggles.xml ulmo-xml/xml/references/featuretoggles.xml > featuretoggles-diff.txt
6. Run the following commands:
   * python3 settings-flags-diff.py settings-diff.txt
   * python3 settings-flags-diff.py featuretoggles-diff.txt

The output will be generated in sfdoutput-settings-diff.txt and sfdoutput-featuretoggles-diff.txt, formatted for RST.
"sfd" stands for the name of this script, as opposed to "default-diff.py" script
"""

import sys
import re


# Get the file path from the command line argument
file_path = sys.argv[1]
output_file_path = "sfdoutput-" + file_path

# Read the file
with open(file_path, 'r') as file:
   lines = file.readlines()

# Determine the type of file (settings or feature toggles)
is_feature_toggle = any('<section ids="featuretoggle-' in line for line in lines)

# Initialize lists to store added and removed lines
# Add headings for RST output
if is_feature_toggle:
    added_lines = ["Added Feature Toggles\n", "*********************\n"]
    removed_lines = ["\nRemoved Feature Toggles\n", "*************************"]
else:
    added_lines = ["Added Settings\n", "*********************\n"]
    removed_lines = ["\nRemoved Settings\n", "*************************\n"]

# Variables to store the current state
current_section = None
current_list = None
default_value = None


# Process each line
for line in lines:
   # Check if the line starts with + or -
   if line.startswith('+') or line.startswith('-'):
       # Check if it is the start of a section
       if is_feature_toggle:
           # Should match either pattern
           # +        <section ids="featuretoggle-ENABLE_CODEJAIL_DARKLAUNCH">
           # +        <section ids="featuretoggle-FEATURES['ENABLE_BLAKE2B_HASHING']">
           # -        <section ids="featuretoggle-order_history.redirect_to_microfrontend"> 
           section_match = re.search(r'<section ids="featuretoggle-(.*)">', line)

       # Otherwise it is a setting
       else:
           section_match = re.search(r'<section ids="setting-([A-Z_]+)">', line)

       # If we found a section, we grab the name of the section and determine if it was added or deleted
       # Save as current_section for the next iteration of the loop
       if section_match:
           current_section = section_match.group(1)
           current_list = added_lines if line.startswith('+') else removed_lines
           # Add a blank line before this entry for RST purposes
           current_list.append("\n")

       else:
           # Check if it is a line within a section, determined by previous loop
           if current_section:
               # Extract the location of the setting or feature toggle and the hash
               location_match = re.search(r'<reference refuri="https://github.com/openedx/edx-platform/blob/([a-f0-9]+)/(.*?)#L(\d+)">', line)
               # Extract the default value of this flag or setting
               default_match = re.search(r'Default: <literal>(.*)</literal>', line)
               # Extract the flag/setting description
               description_match = re.search(r'description.*">(.*)', line)

               # If we find the location in this line, create an output line
               if location_match:
                   hash_value = location_match.group(1)
                   location = location_match.group(2)
                   line_number = location_match.group(3)
                   output_line = f"* {line[0]}{current_section}: [{location} (line {line_number})](https://github.com/openedx/edx-platform/blob/{hash_value}/{location}#L{line_number})\n"
                   # the Default value is found before the Source line
                   if default_value:
                       output_line += f"   * Default value = {default_value}\n"
                   current_list.append(output_line)

               # If we found the default value in this line, create another entry for added lines about what the default value is
               # Save for the next loop since Default is defined before Source
               if default_match:
                   if line.startswith("+"):
                      default_value = default_match.group(1)

               # Add the description, if it exists
               if description_match:
                   description = description_match.group(1)
                   # Sometimes description is more than one line, indicate that it's truncated
                   if "</paragraph>" not in line:
                       description = description + " [output truncated, see link for full description]"
                   else:
                       # Remove </paragraph>
                       description = description[:-12]

                   output_line = f"   * Description: {description}\n"
                   current_list.append(output_line)



   else:
       # If the line does not start with + or -, reset the current state
       current_section = None
       current_list = None
       default_value = None


# Combine the lists in the desired order
result_lines = added_lines + removed_lines


# Write the transformed lines back to the file
with open(output_file_path, 'w') as file:
   file.writelines(result_lines)

print(f"Wrote output to {output_file_path}")