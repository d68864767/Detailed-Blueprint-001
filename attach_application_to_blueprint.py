```python
import os

def attach_application_to_blueprint():
    # Define the file paths
    blueprint_file = 'create_blueprint.kicad_pcb'
    application_file = 'prepare_patent_application.txt'

    # Check if the files exist
    if not os.path.exists(blueprint_file):
        print(f"Blueprint file '{blueprint_file}' not found.")
        return
    if not os.path.exists(application_file):
        print(f"Application file '{application_file}' not found.")
        return

    # Read the contents of the files
    with open(blueprint_file, 'r') as file:
        blueprint_contents = file.read()
    with open(application_file, 'r') as file:
        application_contents = file.read()

    # Combine the contents
    combined_contents = f"{application_contents}\n\n{blueprint_contents}"

    # Write the combined contents to a new file
    with open('patent_application_with_blueprint.txt', 'w') as file:
        file.write(combined_contents)

    print("Successfully attached the patent application to the blueprint.")

if __name__ == "__main__":
    attach_application_to_blueprint()
```
