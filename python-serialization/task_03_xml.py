#!/usr/bin/python3
"""Serialize and deserialize with XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
        Serialize a dictionary to XML and save to a file
        - dictionary: The Python dictionary to serialize
        - filename: The XML file to save to
    """
    root = ET.Element('data')
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
        Deserialize XML data from a file to a dictionary
        - filename: The XML file to read from
        Returns: A Python dictionary with the deserialized data
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    
    return dictionary
