#!/usr/bin/python3
"""
Module for XML serialization and deserialization of a dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML and saves it to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the output XML file.
    """
    # Kök elementi yaradırıq: <data>
    root = ET.Element("data")

    # Lüğətin hər bir elementini kökə alt element (child) kimi əlavə edirik
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # XML-də məlumatlar sətir (string) olmalıdır

    # XML ağacını yaradırıq və fayla yazırıq
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Reads XML data from a file and returns a deserialized Python dictionary.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict: The reconstructed dictionary.
    """
    try:
        # XML faylını parse edirik (təhlil edirik)
        tree = ET.parse(filename)
        root = tree.getroot()

        # Elementləri yenidən lüğətə yığırıq
        reconstructed_dict = {}
        for child in root:
            reconstructed_dict[child.tag] = child.text

        return reconstructed_dict
    except FileNotFoundError:
        return None
    except Exception:
        return None
