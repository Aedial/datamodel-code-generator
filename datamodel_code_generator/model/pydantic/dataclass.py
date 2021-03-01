from pathlib import Path
from typing import Any, DefaultDict, List, Optional

from datamodel_code_generator.imports import Import
from datamodel_code_generator.model import DataModel, DataModelFieldBase
from datamodel_code_generator.reference import Reference
from datamodel_code_generator.types import DataType


class DataClass(DataModel):
    TEMPLATE_FILE_PATH = 'pydantic/dataclass.jinja2'

    def __init__(
        self,
        name: str,
        fields: List[DataModelFieldBase],
        reference: Reference,
        decorators: Optional[List[str]] = None,
        base_classes: Optional[List[Reference]] = None,
        custom_base_class: Optional[str] = None,
        custom_template_dir: Optional[Path] = None,
        extra_template_data: Optional[DefaultDict[str, Any]] = None,
        auto_import: bool = True,
        path: Optional[Path] = None,
        description: Optional[str] = None,
    ):

        super().__init__(
            name,
            fields,
            reference,
            decorators,
            base_classes,
            custom_base_class=custom_base_class,
            custom_template_dir=custom_template_dir,
            extra_template_data=extra_template_data,
            auto_import=auto_import,
            path=path,
            description=description,
        )
        self.imports.append(Import.from_full_path('pydantic.dataclasses.dataclass'))
