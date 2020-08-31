"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class InputDocument:
    """
            InputDocument = {path: path of input data,
            type: type of input data file(txt, json, ...),
            separator: }
    """
    path: str
    type: any
    separator = '\n'


@dataclass
class Types:
    """
        Types
    """
    txt_type = 'txt'


@dataclass
class Document:
    """
            Document = {text: list of strings separated by a specified separator,
                        type: type of document(txt, json, ...)}
    """
    text: List[str]
    type: any


@dataclass
class OutPutDocument:
    """
            OutPutDocument = {}
    """
    output_value: List[str]
    operation: str
    package: str


class ReaderAndWriter(ABC):
    """
            ReaderAndWriter interface
    """
    def __init__(self):
        pass

    @abstractmethod
    def read_data(self, data, batch_size) -> Document:
        """
        Args:
            data: An object of InputDocument
        Returns:
            Document: An object of Document
        """

    @abstractmethod
    def write_data(self, result_data):
        """
        Args:
            result_data: An object of InputDocument
        Returns:
            Document: An object of Document
        """
    @abstractmethod
    def get_file_size(self, path):
        """
        Args:
            path:
        Returns:
        """
